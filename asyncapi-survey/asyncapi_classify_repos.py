#!/usr/bin/env python3
"""
Classify the AsyncAPI 3.x repositories surfaced by the survey into:
  product          — a deployable service/application that is described by AsyncAPI
  tooling/library  — operates ON AsyncAPI/specs (codegen, parser, CLI, SDK, framework, plugin)
  demo/fixture     — sample / tutorial / template / benchmark / test-fixture
  spec/docs        — specifications, standards, docs sites, schema collections
  catalog          — EXCLUDED: apis.json API-profile catalogs (e.g. api-evangelist)
  tangential       — EXCLUDED: AI coding-skill / agent repos matching AsyncAPI only incidentally
  uncategorized    — insufficient signal (review or escalate to an LLM pass)

NO hand-maintained allowlist. Each repo is *scored* from observable signals and
assigned the highest-scoring bucket; the decision and its evidence are recorded
per repo (`_bucket`, `_scores`, `_reason`) so every call is auditable and the
method reproduces for new repos.

Signals and weights:
  GitHub topics             +3   most decisive — maintainer-curated. Matched by
                                 SUBSTRING against ordered fragment groups, so
                                 compound topics ("documentation-generator",
                                 "sdk-generator") resolve to the right bucket
                                 (first group wins).
  description keywords      +2
  repo-name keywords        +1..2
  AsyncAPI usage (paths)    +1   spec at repo root/docs ⇒ product nudge;
                                 spec(s) only under test/fixture dirs ⇒ tooling/demo nudge
  docs-only language        +1   (HTML/MDX/Markdown/none/…) ⇒ spec/docs
  homepage present          +1   ⇒ product

Stars are NOT used to bucket (only to order the report). Ties break
demo > spec/docs > tooling > product (conservative about calling something a
real product). Top score below MIN_SCORE ⇒ uncategorized.

Input:
  <out>/raw/repo-metadata.json        (must include repositoryTopics + homepageUrl)
  <out>/raw/asyncapi-3-*.json         (to map repo -> spec file paths)
  <out>/raw/<slug>.unique-repos.tsv   (feature flags for the report)
Output:
  <out>/raw/repo-classification.json
  <out>/asyncapi-classification.md
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

# --- signal vocabularies -------------------------------------------------
# Topics are matched by SUBSTRING against these ordered groups (first match
# wins), so "documentation-generator" -> tooling (via "generator"),
# "schema-registry" -> product (via "registry"), "json-schema" -> spec/docs.
TOPIC_FRAGMENTS = [
    ("demo/fixture", ("sample", "demo", "example", "tutorial", "workshop",
        "hackathon", "boilerplate", "template", "starter", "playground",
        "benchmark", "fixture", "showcase", "getting-started", "course", "kata")),
    ("tooling/library", ("generator", "codegen", "code-generation", "parser",
        "validator", "linter", "lint", "bundler", "transpiler", "compiler",
        "sdk", "cli", "plugin", "library", "framework", "devtool", "scaffold",
        "toolkit", "converter", "renderer", "preview", "editor")),
    ("product", ("microservice", "backend", "gateway", "api-management",
        "broker", "messaging", "platform", "saas", "self-hosted", "kubernetes",
        "registry", "webapp", "web-app", "application", "iot", "event-driven",
        "server", "daemon", "orchestrat", "mocking", "mock-server")),
    ("spec/docs", ("specification", "standard", "schema", "documentation",
        "docs", "guidelines", "rfc", "openapi-spec", "asyncapi-spec",
        "architecture-as-code")),
]

TOOL_DESC = re.compile(
    r"(?i)(\b(code ?generator|codegen|code generation|generator|parser|validator|"
    r"linter|bundler|transpiler|compiler|cli|plugin|library|sdks?|spec renderer|"
    r"renderer|toolkit|framework|scaffold|command[- ]line|designer|editor|preview|"
    r"converter)\b"
    r"|\bgenerate[sd]?\s+(?:\w+\s+){0,2}(?:documentation|docs|code|models?|types?|clients?|sdks?|stubs?)\b"
    r"|\bmock(?:ing)?\s+(?:tool|library|framework|server)\b)")
PRODUCT_DESC = re.compile(
    r"(?i)\b(platform|micro[- ]?services?|back[- ]?end|gateway|api management|"
    r"marketplace|self-hosted|message broker|broker|registry|firmware|daemon|"
    r"orchestrat\w*|\bserver\b)\b")
# Weaker product cues (+1): generic enough to over-fire on demos/SDKs, so they
# only nudge product and never outweigh a demo/tooling signal on their own.
PRODUCT_DESC_WEAK = re.compile(
    r"(?i)\b(application|engine|service|bot|dashboard|portal|web ?app|website)\b")
DEMO_DESC = re.compile(
    r"(?i)\b(sample|demo|demonstrat\w*|example|tutorial|exercise|workshop|playground|"
    r"template|boilerplate|hackathon|hands-on|learn(ing)?|practice|study|"
    r"reference (implementation|platform|app|service)|showcase|getting started|"
    r"proof[- ]of[- ]concept|poc|benchmark|experimental|test service|test fixture|"
    r"testfachdienst|school project|university|"
    r"coursework|semester|academic|class project|final project|lab activity|"
    r"laborator\w*|curso|ejemplos?|exemplos?|beispiele?|курс)\b")
# Unambiguous demo markers that should OUTWEIGH product/tooling signals (+3, topic-
# tier), not just nudge (+2). These are the systematic misses the LLM audit found:
# book/talk companion code, explicit demo/repro projects. Chosen for >=89% precision
# against the LLM labels, so they rarely fire on a real product or tool.
DEMO_STRONG = re.compile(
    r"(?i)(published by (packt|apress|bpb|o'?reilly|manning|no starch|wiley|leanpub|pearson)"
    r"|companion (code|repo|repository|source|project)|book companion"
    r"|conference talk|\bmeetup\b|presentation (for|at)\b|\bslides\b"
    r"|demo project|example project|sample project|showcas\w*"
    r"|reproduction (case|repo|repository)|bug repro|minimal repro"
    r"|learning (project|purpose)|\bstudy\b)")
SPEC_DESC = re.compile(
    r"(?i)\b(specification|standard|api guidelines|message definitions|"
    r"schema versions?|documentation (site|website|for)|docs (site|for|website)|"
    r"public website|open protocol|protocol specification|wire format)\b")

DEMO_NAME = re.compile(
    r"(?i)\b(sample|samples|demo|demos|example|examples|tutorial|workshop|"
    r"hackathon|labs?|playground|template|templates|starter|boilerplate|scaffold|"
    r"fixtures?|poc|kata)\b")
TOOL_NAME = re.compile(r"(?i)\b(cli|sdk|generator|codegen|parser|validator|linter|bundler|plugin|studio|editor)\b")
SPEC_NAME = re.compile(r"(?i)\b(spec|specs|specification|standards?|docs|documentation|website|guidelines)\b")

DOCS_LANGS = {None, "HTML", "MDX", "Markdown", "CSS", "TeX", "Jupyter Notebook", "reStructuredText"}

FIXTURE_PATH = re.compile(r"(?i)(^|/)(tests?|__tests__|fixtures?|examples?|samples?|testdata|test-resources|e2e|mocks?|demo|demos)(/|$)")
ROOT_DOCS_PATH = re.compile(r"(?i)(^[^/]+\.(ya?ml|json)$)|(^(docs?|api|asyncapi|contracts?|schemas?|spec)/)")

# apis.json API-profile catalogs (e.g. the api-evangelist project) and AI
# coding-skill / agent repos that match AsyncAPI only incidentally are routed to
# dedicated EXCLUDED buckets, not scored as SUTs.
CATALOG_TOPICS = {"apis-json", "naftiko"}
CATALOG_OWNERS = {"api-evangelist"}
TANGENTIAL_TOPICS = {"claude-code", "claude-skills", "claude-skill", "claude-plugin",
                     "ai-skills", "agent-skills", "ai-agent-skills", "agentic",
                     "agent-economy", "agent-coordination"}
# Same pollution, but expressed in the README/description rather than as a topic.
# Applied ONLY as a last resort to repos that would otherwise be uncategorized,
# so it can never pull an already-classified repo out of its bucket.
TANGENTIAL_TEXT = re.compile(
    r"(?i)(claude[- ]code|claude[- ]skills?|claude plugin|\bai[- ]skills?\b|"
    r"agent[- ]skills?|agentic|cursor rules|cursorrules|\baiflow\b|"
    r"skill (registry|marketplace|store)|coding agent)")
# A high-precision subset (~100% AI-skill pollution by the LLM labels), promoted to
# an EARLY route so it excludes even repos that would otherwise score a SUT bucket —
# unlike TANGENTIAL_TEXT, whose fuzzier terms run only on the uncategorized residual.
TANGENTIAL_STRONG = re.compile(
    r"(?i)(skills? for (claude|cursor|ai)\b|\bagent[- ]skills?\b|"
    r"\bclaude[- ]skills?\b|cursorrules)")

# Codegen templates consumed by the AsyncAPI Generator (html-template, java-template,
# *-client-template, …) read as "template"=boilerplate=demo, but they are reusable
# code-generation tooling. Detected via the topic pair {template,generator} or a
# description that pairs "template" with "generator/generates" — checked against the
# DESCRIPTION only (a README mention of "generator" misfires on real demos).
CODEGEN_TEMPLATE = re.compile(
    r"(?i)\btemplate\b[^.]{0,60}\b(generator|generates?|scaffold\w*)\b|"
    r"\b(generator|generation)\b[^.]{0,60}\btemplate\b")

MIN_SCORE = 2  # one clear signal (a topic, or a description/README keyword) classifies
# Tiebreak when buckets score equally. Derived from the pairwise calls:
# tooling>spec (doc generators), tooling>demo (generator templates),
# demo>product (example apps), product>spec (e.g. EventCatalog).
TIEBREAK = ["tooling/library", "demo/fixture", "product", "spec/docs"]
BUCKETS = ["product", "tooling/library", "demo/fixture", "spec/docs"]


def get_topics(info: dict) -> set:
    nodes = ((info.get("repositoryTopics") or {}).get("nodes")) or []
    return {n["topic"]["name"].lower() for n in nodes if n and n.get("topic")}


# Code-context tokens that legitimize a bare "generator" topic as tooling, so
# "code-generator"/"sdk-generator" count but "lyrics-generator" (a feature) does not.
_CODE_CTX = ("code", "codegen", "sdk", "api", "schema", "model", "doc", "spec",
             "type", "client", "openapi", "asyncapi", "proto", "json", "yaml",
             "boilerplate", "scaffold")


def topic_bucket(topic: str):
    """First fragment group whose substring appears in the topic, else None.
    A bare 'generator' fragment only implies tooling in a code context."""
    for bucket, frags in TOPIC_FRAGMENTS:
        for f in frags:
            if f not in topic:
                continue
            if f == "generator" and topic != "generator" and not any(cx in topic for cx in _CODE_CTX):
                continue
            return bucket
    return None


def load_spec_paths(raw_dir: Path) -> dict:
    """repo full_name -> set of AsyncAPI spec file paths, from the version-query
    result JSONs (each a stream of concatenated GitHub API page objects)."""
    paths: dict = {}
    dec = json.JSONDecoder()
    # Version-query result JSONs present in this out-dir: 3.x (asyncapi-3-*) and/or
    # 2.x (asyncapi-2-*). Globbing keeps the 3.x behavior identical (those six files)
    # while letting a 2.x out-dir staged with asyncapi-2-*.json be classified the same way.
    for fp in sorted(raw_dir.glob("asyncapi-3-*.json")) + sorted(raw_dir.glob("asyncapi-2-*.json")):
        if not fp.exists():
            continue
        text = fp.read_text(encoding="utf-8", errors="replace")
        i, n = 0, len(text)
        while i < n:
            while i < n and text[i].isspace():
                i += 1
            if i >= n:
                break
            try:
                obj, i = dec.raw_decode(text, i)
            except json.JSONDecodeError:
                break
            for it in (obj.get("items") or []):
                repo = (it.get("repository") or {}).get("full_name")
                p = it.get("path")
                if repo and p:
                    paths.setdefault(repo, set()).add(p)
    return paths


_MD_IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_HTML = re.compile(r"<[^>]+>")


def clean_readme_lead(text: str, n: int = 500) -> str:
    """Strip badges/images/HTML/markdown punctuation and return the leading
    ~n chars — the part that states what the repo is, with least noise."""
    if not text:
        return ""
    text = _MD_IMG.sub(" ", text)
    text = _HTML.sub(" ", text)
    text = _MD_LINK.sub(r"\1", text)
    text = re.sub(r"[#*_`>|=~-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()[:n]


def classify(name: str, info: dict, spec_paths: dict, readme: str = ""):
    """Score the repo against every bucket and return (bucket, scores, reason)."""
    topics = get_topics(info)
    owner = name.split("/", 1)[0].lower()
    if owner in CATALOG_OWNERS or (topics & CATALOG_TOPICS):
        return "catalog", {}, ["apis.json API-profile catalog (excluded)"]
    if topics & TANGENTIAL_TOPICS:
        return "tangential", {}, ["AI coding-skill / agent repo (excluded): "
                                  + ",".join(sorted(topics & TANGENTIAL_TOPICS))]
    if TANGENTIAL_STRONG.search((info.get("description") or "") + " " + readme[:600]):
        return "tangential", {}, ["AI coding-skill repo (excluded): strong text marker"]
    desc = info.get("description") or ""
    repo_part = name.split("/")[-1]
    lang = (info.get("primaryLanguage") or {}).get("name")
    home = info.get("homepageUrl")
    paths = spec_paths.get(name, set())

    tl = {t.lower() for t in topics}
    is_tpl_name = "template" in repo_part.lower()
    if (("template" in tl and "generator" in tl)
            or CODEGEN_TEMPLATE.search(desc)
            or (is_tpl_name and CODEGEN_TEMPLATE.search(readme[:800]))):
        return "tooling/library", {}, ["AsyncAPI Generator codegen-template (tooling, not demo)"]

    scores = {b: 0 for b in BUCKETS}
    why: list = []

    def add(bucket: str, pts: int, label: str):
        scores[bucket] += pts
        why.append(f"{label} (+{pts} {bucket})")

    # topics (substring/fragment match) — strongest signal
    topic_hits: dict = {}
    for t in topics:
        b = topic_bucket(t)
        if b:
            topic_hits.setdefault(b, []).append(t)
    for b, ts in topic_hits.items():
        add(b, 3, "topic=" + ",".join(sorted(ts)))

    # Description + README lead as ONE capped text signal per bucket. The README
    # is a fallback for repos with no GitHub description; both are noisier than
    # topics, so a text match (+2) is weaker than a topic (+3) and never
    # double-counts (desc and readme matching the same bucket still yield +2).
    text = (desc + " \n " + clean_readme_lead(readme)).strip()
    if text:
        if TOOL_DESC.search(text):
            add("tooling/library", 2, "text~tool")
        if PRODUCT_DESC.search(text):
            add("product", 2, "text~product")
        elif PRODUCT_DESC_WEAK.search(text):
            add("product", 1, "text~product(weak)")
        if DEMO_STRONG.search(text):
            add("demo/fixture", 3, "text~demo-strong")
        elif DEMO_DESC.search(text):
            add("demo/fixture", 2, "text~demo")
        if SPEC_DESC.search(text):
            add("spec/docs", 2, "text~spec")

    if DEMO_NAME.search(repo_part):
        add("demo/fixture", 2, "name~demo")
    if TOOL_NAME.search(repo_part):
        add("tooling/library", 1, "name~tool")
    if SPEC_NAME.search(repo_part):
        add("spec/docs", 1, "name~spec")

    if paths:
        if all(FIXTURE_PATH.search(p) for p in paths):
            add("tooling/library", 1, "spec-only-in-fixtures")
            add("demo/fixture", 1, "spec-only-in-fixtures")
        if any(ROOT_DOCS_PATH.search(p) for p in paths):
            add("product", 1, "spec-at-root/docs")

    if lang in DOCS_LANGS:
        add("spec/docs", 1, f"lang={lang}")

    topval = max(scores.values())
    if topval < MIN_SCORE:
        if TANGENTIAL_TEXT.search(text):
            return "tangential", scores, why + ["AI coding-skill/agent markers in text (excluded)"]
        return "uncategorized", scores, why
    contenders = [b for b in BUCKETS if scores[b] == topval]
    if len(contenders) > 1:
        for b in TIEBREAK:
            if b in contenders:
                return b, scores, why
    return max(scores, key=lambda b: scores[b]), scores, why


def load_feature_flags(raw_dir: Path) -> dict:
    flags: dict = {}
    for tsv in raw_dir.glob("*.unique-repos.tsv"):
        if "combined" in tsv.name:
            continue
        slug = tsv.name.removesuffix(".unique-repos.tsv")
        with tsv.open() as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line:
                    continue
                full = line.split("\t", 1)[0]
                flags.setdefault(full, set()).add(slug)
    return flags


def render_feature_badges(flags: set) -> str:
    badges: list = []
    if "reply-clause" in flags:
        badges.append("reply")
    if "kafka-bindings" in flags:
        badges.append("kafka")
    if "mqtt-bindings" in flags:
        badges.append("mqtt")
    if "amqp-bindings" in flags:
        badges.append("amqp")
    if "channel-parameters" in flags:
        badges.append("channel-params")
    return " · ".join(badges) if badges else "—"


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__.lstrip())
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    raw_dir = out_dir / "raw"
    metadata_path = raw_dir / "repo-metadata.json"
    if not metadata_path.exists():
        sys.stderr.write(f"error: {metadata_path} not found — run asyncapi_repo_metadata.py first\n")
        return 2

    metadata = json.loads(metadata_path.read_text())
    feature_flags = load_feature_flags(raw_dir)
    spec_paths = load_spec_paths(raw_dir)
    readme_dir = raw_dir / "readmes"
    readmes = {}
    for name in metadata:
        fp = readme_dir / (name.replace("/", "__") + ".txt")
        if fp.exists():
            readmes[name] = fp.read_text(encoding="utf-8", errors="replace")

    buckets: dict = {}
    counts: Counter = Counter()
    archived = 0
    classified: dict = {}
    for name, info in metadata.items():
        bucket, scores, why = classify(name, info, spec_paths, readmes.get(name, ""))
        counts[bucket] += 1
        if info.get("isArchived"):
            archived += 1
        buckets.setdefault(bucket, []).append((info.get("stargazerCount", 0), name, info, why))
        classified[name] = {**info, "_bucket": bucket, "_scores": scores, "_reason": why}

    for bucket in buckets:
        buckets[bucket].sort(key=lambda row: (-row[0], row[1].lower()))

    (raw_dir / "repo-classification.json").write_text(json.dumps(classified, indent=2, sort_keys=True))

    total = sum(counts.values())
    bucket_order = ["product", "tooling/library", "demo/fixture", "spec/docs",
                    "catalog", "tangential", "uncategorized"]
    lines: list = []
    lines.append("# AsyncAPI 3.x repository classification")
    lines.append("")
    lines.append("Seedless, signal-scored classification of every unique repository surfaced by "
                 "`asyncapi_adoption_survey.sh` for AsyncAPI 3.x. Each repo is assigned the "
                 "highest-scoring bucket from GitHub topics, description, name, how it uses "
                 "AsyncAPI (spec file locations), language, and homepage. See the module "
                 "docstring for weights; `_scores`/`_reason` in `repo-classification.json` "
                 "record the evidence per repo.")
    lines.append("")
    lines.append(f"_{archived} of {total} repos are archived (recorded as `isArchived`, not a bucket)._")
    lines.append("")
    lines.append("## Bucket counts")
    lines.append("")
    lines.append("| Bucket | Count | % of total |")
    lines.append("|---|---:|---:|")
    for bucket in bucket_order:
        c = counts.get(bucket, 0)
        pct = 100 * c / total if total else 0
        lines.append(f"| `{bucket}` | {c} | {pct:.1f} % |")
    lines.append(f"| **total** | **{total}** | 100 % |")
    lines.append("")

    for bucket in bucket_order:
        rows = buckets.get(bucket, [])
        if not rows:
            continue
        lines.append(f"## {bucket} ({len(rows)})")
        lines.append("")
        lines.append("| ★ | Repo | Features | Why | Description |")
        lines.append("|---:|---|---|---|---|")
        for stars, name, info, why in rows:
            badges = render_feature_badges(feature_flags.get(name, set()))
            desc = (info.get("description") or "").replace("|", "\\|")
            if len(desc) > 70:
                desc = desc[:67] + "..."
            reason = "; ".join(why).replace("|", "\\|")
            if len(reason) > 60:
                reason = reason[:57] + "..."
            lines.append(f"| {stars} | [{name}](https://github.com/{name}) | {badges} | {reason} | {desc} |")
        lines.append("")

    (out_dir / "asyncapi-classification.md").write_text("\n".join(lines))

    sys.stderr.write("Classified %d repos: " % total
                     + ", ".join(f"{b}={counts.get(b, 0)}" for b in bucket_order) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
