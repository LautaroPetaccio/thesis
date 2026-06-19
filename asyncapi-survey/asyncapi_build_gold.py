#!/usr/bin/env python3
"""
Build the GOLD classification = the deterministic rule output, with the LLM pass
layered on in two ways:

  1. residual recovery  — uncategorized repos the LLM resolved (confidence >= RES_TH)
  2. high-conf correction — repos the rules put in a SUT bucket but the LLM disagrees
                            with at confidence >= COR_TH (the systematic rule errors
                            surfaced by asyncapi_llm_audit.py)

Disagreements BELOW COR_TH are NOT applied — they are listed in the report's
"flagged for review" section, because at lower confidence the LLM's own error
modes (notably over-calling `tangential`) are no longer clearly outweighed.

Each repo carries provenance: _source (rule | llm-recovered | llm-corrected),
_rule_bucket, _confidence, _reason — so every deviation from the rules is auditable.

Usage:   asyncapi_build_gold.py <survey-out-dir>
Inputs:  <out>/raw/repo-classification.json, llm-classification.json, repo-metadata.json, readmes/
Outputs: <out>/raw/repo-classification-gold.json
         <out>/asyncapi-classification-gold.md
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

RES_TH = 0.60   # accept an LLM bucket for an uncategorized repo
COR_TH = 0.78   # override a confident rule bucket above this LLM confidence. Set
#                 from a manual walk of the 0.78-0.84 band (~90% LLM-correct, 0 clear
#                 LLM errors); disagreements below 0.78 stay flagged for review.
SUT = ["product", "tooling/library", "demo/fixture", "spec/docs"]
ACCEPT = SUT + ["tangential"]
ORDER = ["product", "tooling/library", "demo/fixture", "spec/docs",
         "catalog", "tangential", "uncategorized"]


def main() -> int:
    out = Path(sys.argv[1]).resolve()
    raw = out / "raw"
    cls = json.loads((raw / "repo-classification.json").read_text())
    llm = json.loads((raw / "llm-classification.json").read_text())
    meta = json.loads((raw / "repo-metadata.json").read_text())

    def conf(v):
        try:
            return float(v.get("confidence") or 0)
        except (TypeError, ValueError):
            return 0.0

    gold = {}
    recovered = corrected = 0
    cor_dir = Counter()
    flagged = []  # sub-threshold SUT disagreements, kept as rule
    for n, r in cls.items():
        rb = r["_bucket"]
        g = {"_bucket": rb, "_source": "rule", "_rule_bucket": rb,
             "stargazerCount": meta.get(n, {}).get("stargazerCount", 0)}
        v = llm.get(n)
        if v:
            lb, c = v["bucket"], conf(v)
            if rb == "uncategorized" and lb in ACCEPT and c >= RES_TH:
                g.update(_bucket=lb, _source="llm-recovered", _confidence=c,
                         _reason=v.get("reason", ""))
                recovered += 1
            elif rb in SUT and lb != rb and lb in ACCEPT:
                if c >= COR_TH:
                    g.update(_bucket=lb, _source="llm-corrected", _confidence=c,
                             _reason=v.get("reason", ""))
                    corrected += 1
                    cor_dir[(rb, lb)] += 1
                else:
                    flagged.append((n, rb, lb, c, v.get("reason", "")))
        gold[n] = g
    (raw / "repo-classification-gold.json").write_text(json.dumps(gold, indent=2, sort_keys=True))

    rdist = Counter(r["_bucket"] for r in cls.values())
    gdist = Counter(g["_bucket"] for g in gold.values())

    md = ["# AsyncAPI repos — GOLD classification (rules + audited LLM pass)\n",
          f"Deterministic rule output with the LLM pass layered on: uncategorized "
          f"recovered at confidence ≥ {RES_TH}, and confident rule buckets overridden "
          f"only where the LLM disagrees at confidence ≥ {COR_TH}. Lower-confidence "
          f"disagreements are listed at the end for manual review, not applied.\n",
          "\n## Distribution: rules → gold\n",
          "| bucket | rules | gold | Δ |", "|---|--:|--:|--:|"]
    for b in ORDER:
        d = gdist.get(b, 0) - rdist.get(b, 0)
        md.append(f"| {b} | {rdist.get(b,0)} | {gdist.get(b,0)} | {d:+d} |")
    md.append(f"\n**{recovered}** uncategorized recovered · **{corrected}** confident "
              f"rule buckets corrected · **{len(flagged)}** lower-confidence "
              f"disagreements flagged (kept as rule).\n")
    md.append("\n## High-confidence corrections applied (rule → llm)\n")
    for (a, b), c in cor_dir.most_common():
        md.append(f"- {a} → **{b}**: {c}")
    md.append("\n## Corrected repos (auditable)\n")
    cors = sorted([(n, g) for n, g in gold.items() if g["_source"] == "llm-corrected"],
                  key=lambda x: (x[1]["_rule_bucket"], -x[1].get("stargazerCount", 0)))
    for n, g in cors:
        md.append(f"- **{n}** ({g.get('stargazerCount',0)}★) {g['_rule_bucket']} → "
                  f"**{g['_bucket']}** (c={g.get('_confidence')}) — {g.get('_reason','')}")
    md.append(f"\n## ⚠ Flagged for review — LLM disagrees but below {COR_TH} "
              f"(kept as rule) ({len(flagged)})\n")
    for n, rb, lb, c, rs in sorted(flagged, key=lambda x: (x[1], -x[3])):
        md.append(f"- **{n}** — rule={rb}, llm={lb} (c={c}) — {rs}")
    (out / "asyncapi-classification-gold.md").write_text("\n".join(md))

    sys.stderr.write(
        f"recovered={recovered}  corrected={corrected}  flagged={len(flagged)}\n"
        f"rules: {dict(rdist)}\ngold : {dict(gdist)}\n"
        f"-> repo-classification-gold.json, asyncapi-classification-gold.md\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
