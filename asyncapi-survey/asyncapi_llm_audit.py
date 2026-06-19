#!/usr/bin/env python3
"""
Full LLM re-pass over EVERY repo with readable text (not just the uncategorized
residual), to *audit* the rule-based classifier — build a confusion matrix and a
reviewable disagreement set (a gold-set seed). It does NOT change any bucket;
disagreements are emitted for human review, because the LLM has its own error
modes (notably over-calling `tangential` on terse descriptions).

Shares the cache with asyncapi_llm_classify.py (raw/llm-classification.json), so
repos already classified by the augmentation pass are reused, not re-billed.

Usage:   asyncapi_llm_audit.py <survey-out-dir>
Inputs:  <out>/raw/repo-classification.json, repo-metadata.json, readmes/
Outputs: <out>/raw/llm-classification.json            (extended cache)
         <out>/raw/llm-audit-disagreements.json        (rule != llm, for review)
         <out>/asyncapi-llm-audit.md                   (confusion matrix + disagreements)
Requires: `claude` CLI authenticated.
"""
from __future__ import annotations

import json
import os
import sys
import threading
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asyncapi_llm_classify import build_prompt, call_claude, clean_lead, topics_of  # noqa: E402

BATCH = 16
WORKERS = 4
RULE_BUCKETS = ["product", "tooling/library", "demo/fixture", "spec/docs"]
LLM_COLS = ["product", "tooling/library", "demo/fixture", "spec/docs",
            "tangential", "uncategorized"]


def main() -> int:
    out = Path(sys.argv[1]).resolve()
    raw = out / "raw"
    cls = json.loads((raw / "repo-classification.json").read_text())
    meta = json.loads((raw / "repo-metadata.json").read_text())
    rdir = raw / "readmes"
    cache_path = raw / "llm-classification.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    def lead(full):
        p = rdir / (full.replace("/", "__") + ".txt")
        return clean_lead(p.read_text(encoding="utf-8", errors="replace")) if p.exists() else ""

    # every repo with readable text, regardless of current bucket
    todo = []
    for full, rec in cls.items():
        if full in cache:
            continue
        m = meta.get(full, {})
        desc = (m.get("description") or "").strip()
        ld = lead(full)
        if not desc and len(ld) < 40:
            continue
        todo.append((full, desc, topics_of(m), ld))

    sys.stderr.write(
        f"repos={len(cls)}  cached={len(cache)}  to-classify={len(todo)} "
        f"in {(len(todo)+BATCH-1)//BATCH} batches (BATCH={BATCH}, WORKERS={WORKERS})\n")

    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    lock = threading.Lock()
    done = 0

    def work(batch):
        verdicts = call_claude(build_prompt([(n, d, t, l) for n, d, t, l in batch]))
        by = {v.get("repo"): v for v in verdicts if isinstance(v, dict)}
        got = {}
        for full, *_ in batch:
            v = by.get(full) or {}
            if not v:
                for vr, vv in by.items():
                    if vr and (vr.endswith("/" + full.split("/")[-1]) or full.endswith(str(vr))):
                        v = vv
                        break
            got[full] = {"bucket": v.get("bucket", "uncategorized"),
                         "confidence": v.get("confidence", 0.0),
                         "reason": (v.get("reason") or "")[:120]}
        return got

    if batches:
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futs = {ex.submit(work, b): b for b in batches}
            for fut in as_completed(futs):
                with lock:
                    cache.update(fut.result())
                    cache_path.write_text(json.dumps(cache, indent=2, sort_keys=True))
                    done += 1
                    sys.stderr.write(f"  batch {done}/{len(batches)}; cache={len(cache)}\n")

    # ---- confusion matrix + disagreements (rule vs llm) ----
    matrix = defaultdict(Counter)
    dis = []
    for full, rec in cls.items():
        rb = rec.get("_bucket")
        v = cache.get(full)
        if not v:
            continue
        lb = v["bucket"]
        matrix[rb][lb] += 1
        if rb in RULE_BUCKETS and lb != rb and lb in LLM_COLS:
            try:
                conf = float(v.get("confidence") or 0)
            except (TypeError, ValueError):
                conf = 0.0
            m = meta.get(full, {})
            dis.append({
                "repo": full, "stars": m.get("stargazerCount", 0),
                "rule": rb, "llm": lb, "confidence": conf,
                "reason": v.get("reason", ""),
                "text": ((m.get("description") or "").strip() or lead(full))[:140],
            })
    dis.sort(key=lambda d: (d["rule"], -d["confidence"]))
    (raw / "llm-audit-disagreements.json").write_text(json.dumps(dis, indent=2))

    # agreement on the SUT buckets the rules assigned confidently
    agree = sum(matrix[b][b] for b in RULE_BUCKETS)
    tot = sum(sum(matrix[b].values()) for b in RULE_BUCKETS)

    md = ["# LLM audit of the rule-based classifier\n",
          "Full LLM re-pass (`claude --model sonnet`) over every repo with readable "
          "text, compared to the rule-based bucket. **No buckets were changed** — "
          "disagreements are listed for review.\n",
          f"\nAgreement on rule-assigned SUT buckets (product/tooling/demo/spec): "
          f"**{agree}/{tot} = {100*agree/tot:.0f}%**\n",
          "\n## Confusion matrix (rows = rule bucket, cols = LLM verdict)\n",
          "| rule \\\\ llm | " + " | ".join(LLM_COLS) + " | total |",
          "|---" * (len(LLM_COLS) + 2) + "|"]
    for rb in RULE_BUCKETS + ["catalog", "tangential", "uncategorized"]:
        row = matrix.get(rb, Counter())
        cells = " | ".join(str(row.get(c, 0)) for c in LLM_COLS)
        md.append(f"| {rb} | {cells} | {sum(row.values())} |")
    md.append(f"\n## Disagreements for review ({len(dis)})\n")
    md.append("Sorted by rule bucket, then LLM confidence. High-confidence rows are "
              "the likeliest rule errors.\n")
    cur = None
    for d in dis:
        if d["rule"] != cur:
            cur = d["rule"]
            md.append(f"\n### rule = {cur} ({sum(1 for x in dis if x['rule']==cur)})\n")
        md.append(f"- **{d['repo']}** ({d['stars']}★) → llm=**{d['llm']}** "
                  f"(c={d['confidence']}) — {d['reason']}\n  `{d['text']}`")
    (out / "asyncapi-llm-audit.md").write_text("\n".join(md))

    sys.stderr.write(
        f"\nSUT agreement: {agree}/{tot} = {100*agree/tot:.0f}%\n"
        f"disagreements: {len(dis)}\n"
        f"by rule bucket: {dict(Counter(d['rule'] for d in dis))}\n"
        f"-> {out/'asyncapi-llm-audit.md'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
