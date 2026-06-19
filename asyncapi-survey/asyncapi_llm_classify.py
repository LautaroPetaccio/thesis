#!/usr/bin/env python3
"""
LLM classification pass for the repos the rule-based classifier left
*uncategorized* — the ones whose README describes the repo's *domain/function*
rather than its *type*, which keyword rules structurally cannot read (see
asyncapi_classify_repos.py).

It does NOT touch the deterministic artifact. It layers an *augmented*
classification on top: for each repo the rules left uncategorized **and** that
has readable text, it asks Claude (via the `claude` CLI in print mode — reuses
the user's Claude Code auth, no API key needed) which bucket it belongs to, and
accepts the answer only when confidence >= THRESHOLD. Everything else stays
exactly as the rules left it.

Resumable + cached: each repo's LLM verdict is cached in
raw/llm-classification.json; re-running only calls the model for repos not yet
cached. Deterministic merge given the cache.

Usage:   asyncapi_llm_classify.py <survey-out-dir>
Inputs:  <out>/raw/repo-classification.json   (rule-based result; picks uncategorized)
         <out>/raw/repo-metadata.json          (description + topics)
         <out>/raw/readmes/<owner>__<name>.txt  (README lead)
Outputs: <out>/raw/llm-classification.json            (raw LLM verdicts, cached)
         <out>/raw/repo-classification-augmented.json (rules + accepted LLM verdicts)
         <out>/asyncapi-classification-augmented.md   (readable, by bucket)
Requires: `claude` CLI authenticated.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BATCH = 12            # repos per LLM call (amortizes per-session cache cost)
WORKERS = 3           # concurrent claude -p sessions (gentle on rate limits)
MODEL = "sonnet"      # CLI alias; good + cheap for classification, reproducible
THRESHOLD = 0.60      # accept an LLM bucket only at/above this confidence
LEAD = 380            # README chars handed to the model per repo
REAL = ["product", "tooling/library", "demo/fixture", "spec/docs", "tangential"]

INSTRUCTION = """You are classifying GitHub repositories that each contain an AsyncAPI specification, for an academic survey of how AsyncAPI 3.x is used in the wild.

Assign each repository to EXACTLY ONE bucket:
- product — a real, deployable application or service that uses AsyncAPI to describe its own event-driven API (backend, microservice, gateway, message broker, platform, bot, dashboard, IoT/firmware, trading/matching engine, etc.).
- tooling/library — software whose purpose is to work with AsyncAPI or messaging: generators, parsers, validators, linters, CLIs, SDKs, code generators, documentation renderers, mocking tools, client libraries, frameworks.
- demo/fixture — exists to teach or demonstrate, not for production: examples, samples, tutorials, workshops, templates/boilerplate, course or school projects, book companion code, proofs-of-concept, test fixtures.
- spec/docs — the repository's main content is a specification, schema set, event/message catalog, API guidelines, or a documentation site — not runnable software.
- tangential — not a genuine AsyncAPI user: AI coding-agent / "skills" repos, API directories/catalogs, or repos that only mention AsyncAPI incidentally.
- uncategorized — genuinely impossible to tell from the information given.

Judge what the repository IS, not which technologies it mentions. Use "uncategorized" only when the text truly does not say.

Return ONLY a JSON array (no prose, no markdown fences), one object per repo, in the same order:
[{"repo":"owner/name","bucket":"<bucket>","confidence":<float 0-1>,"reason":"<max 12 words>"}]

Repositories:
"""


def clean_lead(text: str, n: int = LEAD) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#*_`>|=~\-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()[:n]


def topics_of(meta: dict) -> list:
    nodes = (meta.get("repositoryTopics") or {}).get("nodes") or []
    return [n["topic"]["name"] for n in nodes if n.get("topic")]


def build_prompt(batch: list) -> str:
    lines = [INSTRUCTION]
    for full, desc, topics, lead in batch:
        lines.append(f"### {full}")
        if topics:
            lines.append("topics: " + ", ".join(topics))
        lines.append("description: " + (desc or "(none)"))
        lines.append("readme: " + (lead or "(none)"))
        lines.append("")
    return "\n".join(lines)


def call_claude(prompt: str) -> list:
    """One claude -p call; returns parsed list of verdicts (or [] on failure)."""
    proc = subprocess.run(
        ["claude", "-p", "--model", MODEL, "--output-format", "json", prompt],
        capture_output=True, text=True, timeout=300,
    )
    try:
        env = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return []
    if env.get("is_error"):
        return []
    result = env.get("result", "")
    s = result.strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-z]*\n?", "", s)
        s = re.sub(r"\n?```$", "", s).strip()
    i, j = s.find("["), s.rfind("]")
    if i < 0 or j < 0:
        return []
    try:
        arr = json.loads(s[i:j + 1])
        return arr if isinstance(arr, list) else []
    except json.JSONDecodeError:
        return []


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__.lstrip())
        return 2
    if not shutil.which("claude"):
        sys.stderr.write("error: `claude` CLI not found on PATH\n")
        return 2
    out = Path(sys.argv[1]).resolve()
    raw = out / "raw"
    cls = json.loads((raw / "repo-classification.json").read_text())
    meta = json.loads((raw / "repo-metadata.json").read_text())
    rdir = raw / "readmes"
    cache_path = raw / "llm-classification.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    # Select the readable uncategorized residual.
    todo = []
    for full, rec in cls.items():
        if rec.get("_bucket") != "uncategorized" or full in cache:
            continue
        m = meta.get(full, {})
        desc = (m.get("description") or "").strip()
        rf = rdir / (full.replace("/", "__") + ".txt")
        lead = clean_lead(rf.read_text(encoding="utf-8", errors="replace")) if rf.exists() else ""
        if not desc and len(lead) < 40:
            continue  # no readable text — true floor, leave for code inspection
        todo.append((full, desc, topics_of(m), lead))

    total_unc = sum(1 for r in cls.values() if r.get("_bucket") == "uncategorized")
    sys.stderr.write(
        f"uncategorized={total_unc}  cached={len(cache)}  to-classify={len(todo)} "
        f"in {(len(todo)+BATCH-1)//BATCH} batches\n")

    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    lock = threading.Lock()
    done = 0

    def work(batch):
        verdicts = call_claude(build_prompt(batch))
        by_repo = {v.get("repo"): v for v in verdicts if isinstance(v, dict)}
        got = {}
        names = [b[0] for b in batch]
        for full in names:
            v = by_repo.get(full) or {}
            # Fuzzy fallback: model sometimes returns name-only or reorders.
            if not v:
                for vr, vv in by_repo.items():
                    if vr and (vr.endswith("/" + full.split("/")[-1]) or full.endswith(str(vr))):
                        v = vv
                        break
            got[full] = {
                "bucket": v.get("bucket", "uncategorized"),
                "confidence": v.get("confidence", 0.0),
                "reason": (v.get("reason") or "")[:120],
            }
        return got

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(work, b): b for b in batches}
        for fut in as_completed(futs):
            got = fut.result()
            with lock:
                cache.update(got)
                cache_path.write_text(json.dumps(cache, indent=2, sort_keys=True))
                done += 1
                sys.stderr.write(f"  batch {done}/{len(batches)} done; cache={len(cache)}\n")

    # ---- merge: rules + accepted LLM verdicts -> augmented classification ----
    aug = {k: dict(v) for k, v in cls.items()}
    accepted = recov_by_bucket = 0
    from collections import Counter
    recov = Counter()
    llm_dist = Counter()
    for full, rec in aug.items():
        if rec.get("_bucket") != "uncategorized":
            continue
        v = cache.get(full)
        if not v:
            continue
        llm_dist[v["bucket"]] += 1
        try:
            conf = float(v.get("confidence") or 0)
        except (TypeError, ValueError):
            conf = 0.0
        if v["bucket"] in REAL and conf >= THRESHOLD:
            rec["_bucket"] = v["bucket"]
            rec["_source"] = "llm"
            rec["_llm_confidence"] = conf
            rec["_llm_reason"] = v.get("reason", "")
            accepted += 1
            recov[v["bucket"]] += 1
    (raw / "repo-classification-augmented.json").write_text(
        json.dumps(aug, indent=2, sort_keys=True))

    # ---- readable markdown of the augmented buckets ----
    order = ["product", "tooling/library", "demo/fixture", "spec/docs",
             "catalog", "tangential", "uncategorized"]
    groups = {b: [] for b in order}
    for full, rec in aug.items():
        groups.setdefault(rec["_bucket"], []).append((full, rec))
    md = ["# AsyncAPI repos — augmented classification (rules + LLM pass)\n",
          f"Rule-based buckets, with the readable uncategorized residual resolved by an "
          f"LLM pass (`claude --model {MODEL}`, accepted at confidence ≥ {THRESHOLD}).\n"]
    fin = Counter(rec["_bucket"] for rec in aug.values())
    md.append("| bucket | count |\n|---|--:|")
    for b in order:
        md.append(f"| {b} | {fin.get(b,0)} |")
    md.append("")
    for b in order:
        rows = sorted(groups.get(b, []), key=lambda r: -r[1].get("stargazerCount", 0))
        md.append(f"\n## {b} ({len(rows)})\n")
        for full, rec in rows:
            tag = ""
            if rec.get("_source") == "llm":
                tag = f"  _(llm {rec.get('_llm_confidence')}: {rec.get('_llm_reason')})_"
            md.append(f"- **{full}** — {rec.get('stargazerCount',0)}★{tag}")
    (out / "asyncapi-classification-augmented.md").write_text("\n".join(md))

    sys.stderr.write(
        f"\nLLM verdict distribution (readable residual): {dict(llm_dist)}\n"
        f"accepted (conf>={THRESHOLD}) -> recovered {accepted}: {dict(recov)}\n"
        f"augmented uncategorized: {fin.get('uncategorized',0)} "
        f"(was {total_unc})\nfinal distribution: {dict(fin)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
