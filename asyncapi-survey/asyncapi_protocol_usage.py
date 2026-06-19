#!/usr/bin/env python3
#
# Protocol usage across the FULL AsyncAPI corpus (NOT just request/reply).
#
# The reply-scoped tables (reply-protocols.md / correlation-2x.md) only count the
# rare request/reply slice. This counterpart parses EVERY cached spec in
# specs-3x/ and specs-2x/ and tallies the **document-level** protocols (each
# spec's servers' `protocol` + any protocol `bindings` keys), per version — i.e.
# which transports AsyncAPI users actually declare at all. Repo counts attribute
# a spec's protocols to every repo that contains that blob (via the version-query
# JSONs), deduped by sha for the spec count.
#
# Output: <out>/protocol-usage.{md,json} + a console table.
# Requires: PyYAML. Reuses the cached specs already fetched by the reply/2x scripts.
#
from __future__ import annotations

import glob
import json
import os
import sys
from collections import defaultdict

import yaml

OUT = sys.argv[1] if len(sys.argv) > 1 else "/Users/lpetaccio/tesis/asyncapi-survey/asyncapi-survey-out"
RAW = os.path.join(OUT, "raw")

KNOWN_PROTOCOLS = {
    "amqp", "amqp1", "anypointmq", "googlepubsub", "http", "ibmmq", "jms",
    "kafka", "mercure", "mqtt", "mqtt5", "nats", "pulsar", "redis", "sns",
    "solace", "sqs", "stomp", "ws", "wss",
}
PROTO_NORMALIZE = {
    "kafka-secure": "kafka", "secure-mqtt": "mqtt", "mqtts": "mqtt",
    "amqps": "amqp", "https": "http", "stomps": "stomp",
}


def norm(p):
    if not isinstance(p, str):
        return None
    return PROTO_NORMALIZE.get(p.strip().lower(), p.strip().lower())


def doc_protocols(doc):
    """All protocols declared anywhere: servers[].protocol + every `bindings` key."""
    protos = set()
    servers = doc.get("servers")
    if isinstance(servers, dict):
        for s in servers.values():
            if isinstance(s, dict):
                p = norm(s.get("protocol"))
                if p:
                    protos.add(p)

    def walk(node):
        if isinstance(node, dict):
            b = node.get("bindings")
            if isinstance(b, dict):
                protos.update(k.lower() for k in b.keys())
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(doc)
    return {p for p in (norm(x) for x in protos) if p in KNOWN_PROTOCOLS}


def iter_json_objects(text):
    dec = json.JSONDecoder()
    i, n = 0, len(text)
    while i < n:
        while i < n and text[i].isspace():
            i += 1
        if i >= n:
            break
        try:
            obj, end = dec.raw_decode(text, i)
        except json.JSONDecodeError:
            break
        yield obj
        i = end


def sha_to_repos(version_globs):
    m = defaultdict(set)
    for g in version_globs:
        for path in glob.glob(os.path.join(RAW, g)):
            for obj in iter_json_objects(open(path, encoding="utf-8", errors="replace").read()):
                for it in (obj.get("items") or []):
                    sha = it.get("sha")
                    repo = (it.get("repository") or {}).get("full_name")
                    if sha and repo:
                        m[sha].add(repo)
    return m


def tally(specs_dir, version_globs, prefix):
    s2r = sha_to_repos(version_globs)
    spec_of = defaultdict(set)   # proto -> set(sha)
    repo_of = defaultdict(set)   # proto -> set(repo)
    parsed = with_proto = 0
    all_repos = set()
    for f in glob.glob(os.path.join(RAW, specs_dir, "*")):
        sha = os.path.basename(f).rsplit(".", 1)[0]
        try:
            doc = yaml.safe_load(open(f, encoding="utf-8", errors="replace"))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        v = doc.get("asyncapi")
        if not (isinstance(v, str) and v.startswith(prefix)):
            continue
        parsed += 1
        repos = s2r.get(sha, set())
        all_repos |= repos
        protos = doc_protocols(doc)
        if protos:
            with_proto += 1
        for p in protos:
            spec_of[p].add(sha)
            repo_of[p].update(repos)
    return {
        "parsed": parsed, "with_protocol": with_proto,
        "repos_total": len(all_repos),
        "by_proto": {p: {"specs": len(spec_of[p]), "repos": len(repo_of[p])} for p in spec_of},
    }


def main():
    g3 = tally("specs-3x", ["asyncapi-3-*.json"], "3.")
    g2 = tally("specs-2x", ["asyncapi-2-*.json"], "2.")

    protos = sorted(set(g3["by_proto"]) | set(g2["by_proto"]),
                    key=lambda p: -(g3["by_proto"].get(p, {}).get("specs", 0)
                                    + g2["by_proto"].get(p, {}).get("specs", 0)))

    result = {"3x": g3, "2x": g2, "protocols": protos}
    with open(os.path.join(OUT, "protocol-usage.json"), "w") as fh:
        json.dump(result, fh, indent=2)

    def cell(g, p):
        d = g["by_proto"].get(p)
        return f"{d['specs']} / {d['repos']}" if d else "—"

    L = ["# AsyncAPI protocol usage — full corpus (document-level)\n",
         "Protocols declared anywhere in each spec (servers' `protocol` + binding keys), across the "
         "WHOLE corpus — not just the request/reply slice. `specs / repos` per version.\n",
         f"- 3.x: {g3['parsed']} parsed specs, {g3['with_protocol']} declare a protocol "
         f"({g3['repos_total']} repos).",
         f"- 2.x: {g2['parsed']} parsed specs, {g2['with_protocol']} declare a protocol "
         f"({g2['repos_total']} repos).\n",
         "| Protocol | 3.x (specs / repos) | 2.x (specs / repos) |",
         "| -------- | ------------------: | ------------------: |"]
    for p in protos:
        L.append(f"| {p} | {cell(g3, p)} | {cell(g2, p)} |")
    md = "\n".join(L)
    with open(os.path.join(OUT, "protocol-usage.md"), "w") as fh:
        fh.write(md + "\n")

    print(md)
    print(f"\n(3.x: {g3['with_protocol']}/{g3['parsed']} specs declare a protocol; "
          f"2.x: {g2['with_protocol']}/{g2['parsed']})")
    print(f"\nOutputs: protocol-usage.{{md,json}} under {OUT}")


if __name__ == "__main__":
    main()
