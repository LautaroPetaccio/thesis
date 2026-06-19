#!/usr/bin/env python3
#
# AsyncAPI 2.x correlation-id analysis.
#
# Goal: AsyncAPI 2.x has NO first-class `reply:` construct (that arrives in 3.0).
# The only native way to pair a reply with its request in 2.x is the
# **Correlation ID Object** — a `correlationId` on a message whose `location`
# is a runtime expression (`$message.header#/...` or `$message.payload#/...`).
# This script measures, across the real-world AsyncAPI 2.x corpus enumerated by
# `asyncapi_adoption_survey.sh`, how often that mechanism is actually used, where
# the id lives (header vs payload), over which transports, and how often it
# co-occurs with a request/reply *convention* (since 2.x can only express
# request/reply by convention).
#
# It is the 2.x counterpart of `asyncapi_reply_protocols.py` (3.x receive+reply):
# same corpus-loading / blob-fetching machinery, different structural detector.
#
# Requires: gh CLI (authenticated), PyYAML.
# Usage:   asyncapi_correlation_2x.py [out-dir]      (default ./asyncapi-survey-out)
#          LIMIT=200 asyncapi_correlation_2x.py      (cap blobs — quick validation)
#
from __future__ import annotations

import base64
import csv
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import yaml

OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(), "asyncapi-survey-out")
RAW = os.path.join(OUT_DIR, "raw")
CACHE = os.path.join(RAW, "specs-2x")
LIMIT = int(os.environ.get("LIMIT", "0"))  # 0 = no cap

# 2.x version-query result files produced by asyncapi_adoption_survey.sh
# (the survey enumerated 2.0 .. 2.6, .yaml only).
VERSION_JSONS = [f"asyncapi-2-{m}.json" for m in range(0, 7)]

KNOWN_PROTOCOLS = {
    "amqp", "amqp1", "anypointmq", "googlepubsub", "http", "ibmmq", "jms",
    "kafka", "mercure", "mqtt", "mqtt5", "nats", "pulsar", "redis", "sns",
    "solace", "sqs", "stomp", "ws", "wss",
}
PROTO_NORMALIZE = {
    "kafka-secure": "kafka", "secure-mqtt": "mqtt", "mqtts": "mqtt",
    "amqps": "amqp", "https": "http", "wss": "wss", "stomps": "stomp",
}

# Request/reply *convention* heuristics (2.x has no formal reply).
REQ_RE = re.compile(r"(request|/req\b|\.req\b|_req\b|\brpc\b|command|\bcmd\b|query|invoke)", re.I)
REP_RE = re.compile(r"(reply|response|/res\b|\.res\b|_res\b|reply[-_]?to|result|\back\b)", re.I)


def norm_proto(p):
    if not isinstance(p, str):
        return None
    return PROTO_NORMALIZE.get(p.strip().lower(), p.strip().lower())


def as_dict(x):
    return x if isinstance(x, dict) else {}


# ---------------------------------------------------------------------------
# Corpus loading + fetching (identical machinery to the 3.x script)
# ---------------------------------------------------------------------------
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


def load_corpus():
    corpus = {}
    for fname in VERSION_JSONS:
        path = os.path.join(RAW, fname)
        if not os.path.exists(path):
            print("  warning: missing %s (skipping)" % fname, file=sys.stderr)
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for obj in iter_json_objects(text):
            for it in (obj.get("items") or []):
                sha = it.get("sha")
                repo = (it.get("repository") or {}).get("full_name")
                p = it.get("path")
                git_url = it.get("git_url")
                if not (sha and repo and p and git_url):
                    continue
                ext = p.rsplit(".", 1)[-1].lower() if "." in p else "yaml"
                rec = corpus.get(sha)
                if rec is None:
                    rec = {"ext": ext, "repo": repo, "path": p,
                           "git_url": git_url, "repos": set()}
                    corpus[sha] = rec
                rec["repos"].add(repo)
    return corpus


def fetch_blob(git_url):
    backoff = 5
    for _ in range(5):
        proc = subprocess.run(["gh", "api", git_url, "--jq", ".content"],
                              capture_output=True, text=True, timeout=90)
        if proc.returncode == 0:
            b64 = proc.stdout.strip()
            return base64.b64decode(b64) if b64 else b""
        err = (proc.stderr or "").lower()
        if any(s in err for s in ("rate limit", "secondary", "abuse", "403", "too quickly")):
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
            continue
        raise RuntimeError(proc.stderr.strip()[:200] or "gh api failed")
    raise RuntimeError("gave up after retries (rate limited)")


def cache_file(sha, ext):
    return os.path.join(CACHE, "%s.%s" % (sha, ext))


def fetch_all(corpus):
    os.makedirs(CACHE, exist_ok=True)
    todo = [(sha, rec) for sha, rec in corpus.items()
            if not (os.path.exists(cache_file(sha, rec["ext"]))
                    and os.path.getsize(cache_file(sha, rec["ext"])) > 0)]
    print("  %d unique blobs; %d cached, %d to fetch" % (len(corpus), len(corpus) - len(todo), len(todo)))
    failed = {}
    done = 0

    def work(item):
        sha, rec = item
        data = fetch_blob(rec["git_url"])
        with open(cache_file(sha, rec["ext"]), "wb") as fh:
            fh.write(data)
        return sha

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(work, it): it for it in todo}
        for fut in as_completed(futs):
            sha, rec = futs[fut]
            try:
                fut.result()
            except Exception as e:  # noqa: BLE001
                failed[sha] = str(e)
            done += 1
            if done % 250 == 0:
                print("    fetched %d/%d (%d failed)" % (done, len(todo), len(failed)))
    if failed:
        print("  %d blobs failed (deleted/renamed since survey)" % len(failed), file=sys.stderr)
    return failed


# ---------------------------------------------------------------------------
# 2.x correlation-id detection
# ---------------------------------------------------------------------------
def load_yaml(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return yaml.safe_load(fh)


def is_2x(doc):
    v = doc.get("asyncapi") if isinstance(doc, dict) else None
    return isinstance(v, str) and v.startswith("2.")


def resolve_internal(doc, ref):
    """Resolve an internal '#/a/b/c' JSON-pointer ref; None if external/missing."""
    if not (isinstance(ref, str) and ref.startswith("#/")):
        return None
    node = doc
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return None
    return node


def corr_location(doc, cid):
    """Given a `correlationId` value (inline obj or $ref), return its location str."""
    if not isinstance(cid, dict):
        return None
    if "$ref" in cid:
        tgt = resolve_internal(doc, cid["$ref"])
        return tgt.get("location") if isinstance(tgt, dict) and isinstance(tgt.get("location"), str) else None
    return cid.get("location") if isinstance(cid.get("location"), str) else None


def message_correlations(doc, msg, depth=0):
    """All correlationId locations declared by a 2.x message object, following
    $ref (message + correlationId), oneOf, and message traits."""
    locs = []
    if not isinstance(msg, dict) or depth > 6:
        return locs
    if "$ref" in msg:
        tgt = resolve_internal(doc, msg["$ref"])
        return message_correlations(doc, tgt, depth + 1) if isinstance(tgt, dict) else locs
    if isinstance(msg.get("oneOf"), list):
        for m in msg["oneOf"]:
            locs += message_correlations(doc, m, depth + 1)
    loc = corr_location(doc, msg.get("correlationId"))
    if loc:
        locs.append(loc)
    for tr in (msg.get("traits") or []):
        t = resolve_internal(doc, tr["$ref"]) if isinstance(tr, dict) and "$ref" in tr else tr
        if isinstance(t, dict):
            loc = corr_location(doc, t.get("correlationId"))
            if loc:
                locs.append(loc)
    return locs


def classify_location(loc):
    """('header'|'payload'|'other', field) from a runtime expression."""
    m = re.match(r"\$message\.(header|payload)#?/?(.*)$", loc.strip())
    if m:
        return m.group(1), (m.group(2) or "(root)")
    return "other", loc.strip()


def server_protocols(doc):
    out = set()
    for srv in as_dict(doc.get("servers")).values():
        p = norm_proto(srv.get("protocol")) if isinstance(srv, dict) else None
        if p:
            out.add(p)
    return out


def doc_protocols(doc):
    protos = set(server_protocols(doc))

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
    return {p for p in (norm_proto(x) for x in protos) if p in KNOWN_PROTOCOLS}


def analyze_doc(doc):
    """Return a per-spec correlation/request-reply record for a 2.x doc."""
    channels = as_dict(doc.get("channels"))
    comps = as_dict(doc.get("components"))

    locations = []          # all correlationId location strings found
    # 1) messages on channel operations
    for ch in channels.values():
        if not isinstance(ch, dict):
            continue
        for verb in ("publish", "subscribe"):
            op = ch.get(verb)
            if isinstance(op, dict) and "message" in op:
                locations += message_correlations(doc, op.get("message"))
    # 2) reusable component messages + messageTraits
    for m in as_dict(comps.get("messages")).values():
        locations += message_correlations(doc, m)
    for t in as_dict(comps.get("messageTraits")).values():
        loc = corr_location(doc, t.get("correlationId")) if isinstance(t, dict) else None
        if loc:
            locations.append(loc)
    # 3) declared-but-maybe-unbound correlationIds in components
    declared_corr_ids = list(as_dict(comps.get("correlationIds")).values())
    for c in declared_corr_ids:
        if isinstance(c, dict) and isinstance(c.get("location"), str):
            locations.append(c["location"])

    has_corr = bool(locations)
    classes = Counter()
    fields = Counter()
    for loc in locations:
        kind, field = classify_location(loc)
        classes[kind] += 1
        fields[field] += 1

    # request/reply convention signals
    names = []
    duplex = False
    for cname, ch in channels.items():
        names.append(str(cname))
        if isinstance(ch, dict):
            if "publish" in ch and "subscribe" in ch:
                duplex = True
            for verb in ("publish", "subscribe"):
                op = ch.get(verb)
                if isinstance(op, dict) and isinstance(op.get("operationId"), str):
                    names.append(op["operationId"])
    blob = " \n".join(names)
    has_req = bool(REQ_RE.search(blob))
    has_rep = bool(REP_RE.search(blob))
    reqreply_naming = has_req and has_rep

    return {
        "has_correlationId": has_corr,
        "n_locations": len(locations),
        "n_declared_correlationIds": len(declared_corr_ids),
        "location_classes": dict(classes),
        "fields": dict(fields),
        "locations": sorted(set(locations)),
        "protocols": sorted(doc_protocols(doc)),
        "duplex_channel": duplex,
        "reqreply_naming": reqreply_naming,
        "n_channels": len(channels),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Loading 2.x corpus from %s ..." % RAW)
    corpus = load_corpus()
    if not corpus:
        print("error: no 2.x corpus items; run asyncapi_adoption_survey.sh first", file=sys.stderr)
        sys.exit(1)
    if LIMIT:
        corpus = dict(list(corpus.items())[:LIMIT])
        print("  LIMIT=%d -> processing %d blobs" % (LIMIT, len(corpus)))
    print("  %d unique blobs across %d repos"
          % (len(corpus), len({r for rec in corpus.values() for r in rec["repos"]})))

    print("Fetching specs (cached under %s) ..." % CACHE)
    failed = fetch_all(corpus)

    print("Parsing & detecting correlationId ...")
    funnel = defaultdict(int)
    funnel["unique_blobs"] = len(corpus)
    funnel["fetch_failed"] = len(failed)

    corr_specs = defaultdict(set)        # location-class -> set(sha)
    corr_repos = defaultdict(set)
    field_counter = Counter()
    proto_specs = defaultdict(set)       # protocol -> set(sha) among correlationId specs
    proto_repos = defaultdict(set)
    rows = []                            # per correlationId-spec CSV/appendix
    repos_with_corr = set()
    n_corr_and_reqreply = 0
    n_reqreply_total = 0
    n_duplex_total = 0

    for sha, rec in corpus.items():
        cf = cache_file(sha, rec["ext"])
        if sha in failed or not os.path.exists(cf):
            continue
        try:
            doc = load_yaml(cf)
        except Exception:  # noqa: BLE001
            funnel["parse_failed"] += 1
            continue
        if not isinstance(doc, dict):
            funnel["parse_failed"] += 1
            continue
        if not is_2x(doc):
            funnel["non_2x"] += 1
            continue
        funnel["parsed_2x"] += 1
        try:
            r = analyze_doc(doc)
        except Exception:  # noqa: BLE001
            funnel["analyze_failed"] += 1
            continue

        if r["reqreply_naming"]:
            n_reqreply_total += 1
        if r["duplex_channel"]:
            n_duplex_total += 1
        if not r["has_correlationId"]:
            continue

        funnel["specs_with_correlationId"] += 1
        repos = sorted(rec["repos"])
        repos_with_corr.update(repos)
        for kind in r["location_classes"]:
            corr_specs[kind].add(sha)
            corr_repos[kind].update(repos)
        for field, c in r["fields"].items():
            field_counter[field] += c
        for p in r["protocols"]:
            proto_specs[p].add(sha)
            proto_repos[p].update(repos)
        if r["reqreply_naming"] or r["duplex_channel"]:
            n_corr_and_reqreply += 1
        rows.append({"repo": rec["repo"], "path": rec["path"], "sha": sha,
                     "version": doc.get("asyncapi"),
                     "n_correlationIds": r["n_locations"],
                     "locations": "|".join(r["locations"]),
                     "location_classes": "|".join("%s:%d" % kv for kv in r["location_classes"].items()),
                     "protocols": "|".join(r["protocols"]) or "undetermined",
                     "duplex_channel": r["duplex_channel"],
                     "reqreply_naming": r["reqreply_naming"]})

    result = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "definition": "AsyncAPI 2.x messages declaring a correlationId (location runtime expression), "
                      "the 2.x mechanism for pairing a reply with its request",
        "funnel": dict(funnel),
        "correlationId": {
            "specs": funnel.get("specs_with_correlationId", 0),
            "repos": len(repos_with_corr),
            "by_location": {k: {"specs": len(corr_specs[k]), "repos": len(corr_repos[k])} for k in corr_specs},
            "top_fields": field_counter.most_common(20),
            "by_protocol": sorted(({"protocol": p, "specs": len(proto_specs[p]), "repos": len(proto_repos[p])}
                                   for p in proto_specs), key=lambda d: (-d["specs"], d["protocol"])),
        },
        "request_reply_context": {
            "parsed_2x": funnel.get("parsed_2x", 0),
            "specs_with_reqreply_naming": n_reqreply_total,
            "specs_with_duplex_channel": n_duplex_total,
            "correlationId_specs_with_reqreply_signal": n_corr_and_reqreply,
        },
        "specs": rows,
    }
    with open(os.path.join(OUT_DIR, "correlation-2x.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    with open(os.path.join(OUT_DIR, "correlation-2x.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["repo", "path", "sha", "version", "n_correlationIds",
                                           "locations", "location_classes", "protocols",
                                           "duplex_channel", "reqreply_naming"])
        w.writeheader()
        for row in sorted(rows, key=lambda r: (r["repo"], r["path"])):
            w.writerow(row)

    write_markdown(os.path.join(OUT_DIR, "correlation-2x.md"), result)

    f = funnel
    print("\n==== AsyncAPI 2.x correlationId summary ====")
    print("unique 2.x blobs: %d | parsed 2.x: %d | specs with correlationId: %d (repos: %d)"
          % (f["unique_blobs"], f.get("parsed_2x", 0), f.get("specs_with_correlationId", 0), len(repos_with_corr)))
    print("by location:", {k: len(corr_specs[k]) for k in corr_specs})
    print("top fields:", field_counter.most_common(8))
    print("by protocol:", [(d["protocol"], d["specs"]) for d in result["correlationId"]["by_protocol"]])
    print("of correlationId specs, %d also show a request/reply naming or duplex-channel signal" % n_corr_and_reqreply)
    print("\nOutputs: correlation-2x.{md,csv,json} under %s" % OUT_DIR)


def write_markdown(path, res):
    c = res["correlationId"]
    rr = res["request_reply_context"]
    f = res["funnel"]
    L = []
    L.append("# AsyncAPI 2.x correlation ids\n")
    L.append("_Generated %s by `asyncapi_correlation_2x.py`._\n" % res["generated"])
    L.append("**Question.** AsyncAPI 2.x has no first-class `reply:` construct; the native way to pair "
             "a reply with its request is the **Correlation ID Object** (a message `correlationId` whose "
             "`location` is a runtime expression). How often does the real-world 2.x corpus actually use it, "
             "where does the id live, and over which transports?\n")
    L.append("## Coverage funnel\n")
    L.append("| Stage | Count |\n|-------|------:|")
    L.append("| Unique 2.x blobs (by sha) | %d |" % f.get("unique_blobs", 0))
    L.append("| Fetch failed | %d |" % f.get("fetch_failed", 0))
    L.append("| Parse failed | %d |" % f.get("parse_failed", 0))
    L.append("| Not AsyncAPI 2.x | %d |" % f.get("non_2x", 0))
    L.append("| Parsed AsyncAPI 2.x | %d |" % f.get("parsed_2x", 0))
    L.append("| **Specs with ≥1 `correlationId`** | **%d** |\n" % f.get("specs_with_correlationId", 0))

    L.append("## Correlation ids\n")
    L.append("**%d specs across %d repos** declare a `correlationId` "
             "(%.1f%% of parsed 2.x specs).\n"
             % (c["specs"], c["repos"], 100.0 * c["specs"] / max(1, f.get("parsed_2x", 1))))
    L.append("### Where the id lives\n| Location | specs | repos |\n|----------|------:|------:|")
    for k, v in sorted(c["by_location"].items(), key=lambda kv: -kv[1]["specs"]):
        L.append("| `%s` | %d | %d |" % (k, v["specs"], v["repos"]))
    L.append("\n### Field the id maps to (top)\n| Field | occurrences |\n|-------|------:|")
    for field, n in c["top_fields"]:
        L.append("| `%s` | %d |" % (field, n))
    L.append("\n### Transport of correlationId specs\n| Protocol | specs | repos |\n|----------|------:|------:|")
    for d in c["by_protocol"]:
        L.append("| `%s` | %d | %d |" % (d["protocol"], d["specs"], d["repos"]))
    if not c["by_protocol"]:
        L.append("| _undetermined_ | | |")

    L.append("\n## Request/reply context\n")
    L.append("2.x cannot declare a reply, so request/reply is only a *convention*. Of **%d** parsed 2.x "
             "specs, **%d** use request/reply-suggestive channel/operation names and **%d** have a "
             "duplex channel (both `publish` and `subscribe`). Of the **%d** specs that declare a "
             "`correlationId`, **%d** also show one of those request/reply signals — i.e. the id is "
             "plausibly used to pair a reply with its request, not just to tag a one-way event.\n"
             % (rr["parsed_2x"], rr["specs_with_reqreply_naming"], rr["specs_with_duplex_channel"],
                c["specs"], rr["correlationId_specs_with_reqreply_signal"]))

    L.append("## Caveats\n")
    L.append("- Corpus = the survey's `asyncapi: 2.0..2.6` GitHub code-search (`.yaml` only — 2.x `.yml`/"
             "`.json` were not separately enumerated), deduped by blob sha.\n")
    L.append("- `correlationId` presence is detected structurally (message `correlationId`, `$ref` to "
             "`components/correlationIds`, `oneOf`, and message `traits`); request/reply is a *naming* "
             "heuristic, not a structural reply (2.x has none).\n")
    L.append("\n## Appendix — 2.x specs declaring a correlationId\n")
    for row in sorted(res["specs"], key=lambda r: (r["repo"], r["path"])):
        L.append("- [`%s`](https://github.com/%s) `%s` — %s — loc: `%s`%s"
                 % (row["repo"], row["repo"], row["path"], row["protocols"],
                    row["location_classes"], "  ·  req/reply-ish" if row["reqreply_naming"] or row["duplex_channel"] else ""))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    main()
