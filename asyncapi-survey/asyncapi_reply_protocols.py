#!/usr/bin/env python3
#
# AsyncAPI 3.x request-reply protocol analysis.
#
# Goal: across ALL real-world AsyncAPI 3.x specs found by the survey
# (asyncapi_adoption_survey.sh), determine which messaging protocols
# (kafka, mqtt, amqp, ...) are used by operations that implement the
# request-reply pattern where the SUT is the responder, i.e. operations
# with `action: receive` AND a `reply` (the reply may target the same
# channel as the request, a different channel, or just an address).
#
# Unlike the shell survey (which only does GitHub code-search text
# matching), this script actually FETCHES and PARSES the specs, so the
# reply pattern and its protocols are detected structurally.
#
# Corpus: the union of the 3.x version-query result sets the survey
# captured (yaml + yml + json, 3.0.0 + 3.1.0), deduplicated by blob sha.
#
# Protocol attribution:
#   - reply-scoped (headline): protocol(s) of the channels the reply
#     operation touches (request channel + reply channel) -> their
#     servers' `protocol` and/or their `bindings` keys.
#   - document-level (context): any protocol declared anywhere in a spec
#     that has at least one receive+reply operation.
#
# Requires: gh CLI (authenticated), PyYAML.
# Usage:   asyncapi_reply_protocols.py [out-dir]   (default ./asyncapi-survey-out)
#
from __future__ import annotations

import base64
import csv
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import yaml

OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(), "asyncapi-survey-out")
RAW = os.path.join(OUT_DIR, "raw")
CACHE = os.path.join(RAW, "specs-3x")

# The 3.x version-query result files produced by asyncapi_adoption_survey.sh.
VERSION_JSONS = [
    "asyncapi-3-0.json", "asyncapi-3-1.json",
    "asyncapi-3-0-yml.json", "asyncapi-3-1-yml.json",
    "asyncapi-3-0-json.json", "asyncapi-3-1-json.json",
]

# AsyncAPI 3.0 binding keys == protocol identifiers (server protocols use the
# same names plus TLS variants, normalized below).
KNOWN_PROTOCOLS = {
    "amqp", "amqp1", "anypointmq", "googlepubsub", "http", "ibmmq", "jms",
    "kafka", "mercure", "mqtt", "mqtt5", "nats", "pulsar", "redis", "sns",
    "solace", "sqs", "stomp", "ws", "wss",
}
# Collapse TLS/secure server-protocol variants onto their base protocol.
# ws/wss kept distinct to match the survey's taxonomy.
PROTO_NORMALIZE = {
    "kafka-secure": "kafka", "secure-mqtt": "mqtt", "mqtts": "mqtt",
    "amqps": "amqp", "https": "http", "stomps": "stomp",
}


def norm_proto(p):
    if not isinstance(p, str):
        return None
    p = p.strip().lower()
    return PROTO_NORMALIZE.get(p, p)


def as_dict(x):
    """Real-world specs are messy: a field that should be a map is sometimes a
    list or scalar. Treat anything non-dict as empty."""
    return x if isinstance(x, dict) else {}


# ---------------------------------------------------------------------------
# Corpus loading
# ---------------------------------------------------------------------------
def iter_json_objects(text):
    """Yield each top-level JSON object from a file that concatenates several
    of them (the survey appends one API response per page/size-bucket)."""
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
    """Return sha -> {ext, repo, path, git_url, repos:set, locations:set}.
    Dedupe by blob sha (identical content); keep every (repo,path) it appears
    at so we can report per-repo / per-location."""
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
                           "git_url": git_url, "repos": set(), "locations": set()}
                    corpus[sha] = rec
                rec["repos"].add(repo)
                rec["locations"].add((repo, p))
    return corpus


# ---------------------------------------------------------------------------
# Fetching (gh api blob -> base64 -> cached file)
# ---------------------------------------------------------------------------
def fetch_blob(git_url):
    """Return decoded bytes for a git blob, or raise on persistent failure."""
    backoff = 5
    for attempt in range(5):
        proc = subprocess.run(
            ["gh", "api", git_url, "--jq", ".content"],
            capture_output=True, text=True, timeout=90,
        )
        if proc.returncode == 0:
            b64 = proc.stdout.strip()
            return base64.b64decode(b64) if b64 else b""
        err = (proc.stderr or "").lower()
        if any(s in err for s in ("rate limit", "secondary", "abuse", "403", "was submitted too quickly")):
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
            continue
        # Non-retryable (404, empty repo, removed file, etc.)
        raise RuntimeError(proc.stderr.strip()[:200] or "gh api failed")
    raise RuntimeError("gave up after retries (rate limited)")


def cache_file(sha, ext):
    return os.path.join(CACHE, "%s.%s" % (sha, ext))


def fetch_all(corpus):
    os.makedirs(CACHE, exist_ok=True)
    todo = [(sha, rec) for sha, rec in corpus.items()
            if not (os.path.exists(cache_file(sha, rec["ext"]))
                    and os.path.getsize(cache_file(sha, rec["ext"])) > 0)]
    print("  %d unique blobs; %d already cached, %d to fetch"
          % (len(corpus), len(corpus) - len(todo), len(todo)))
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
        print("  %d blobs failed to fetch (e.g. deleted/renamed since survey)" % len(failed),
              file=sys.stderr)
    return failed


# ---------------------------------------------------------------------------
# Parsing & reply-pattern detection
# ---------------------------------------------------------------------------
def load_yaml(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return yaml.safe_load(fh)


def is_3x(doc):
    v = doc.get("asyncapi") if isinstance(doc, dict) else None
    return isinstance(v, str) and (v.startswith("3.0") or v.startswith("3.1"))


def ref_name(obj):
    """For a {'$ref': '#/x/y/Name'} mapping return ('Name', is_internal)."""
    if isinstance(obj, dict) and "$ref" in obj:
        ref = obj["$ref"]
        if isinstance(ref, str) and ref.startswith("#/"):
            return ref.split("/")[-1], True
        return None, False  # external ref
    return None, None


def resolve_channel(doc, channel_field):
    """Return the channel object for an operation/reply `channel` field
    (either a $ref into #/channels or an inline object). None if external/absent."""
    if not isinstance(channel_field, dict):
        return None
    name, internal = ref_name(channel_field)
    if internal is True:
        return as_dict(doc.get("channels")).get(name)
    if internal is False:
        return None  # external ref -> unresolvable here
    return channel_field  # inline channel object


def binding_keys(obj):
    if isinstance(obj, dict):
        b = obj.get("bindings")
        if isinstance(b, dict):
            return {k.lower() for k in b.keys()}
    return set()


def server_protocols(doc):
    out = {}
    for name, srv in as_dict(doc.get("servers")).items():
        if isinstance(srv, dict):
            out[name] = norm_proto(srv.get("protocol"))
    return out


def channel_protocols(doc, ch, all_server_protos):
    """Protocols implied by a channel: its pinned servers' protocols (or all
    servers if none pinned) plus binding keys on the channel and its inline
    messages. Returns (protocols:set, via_all_servers:bool)."""
    protos = set()
    via_all = False
    if not isinstance(ch, dict):
        return protos, via_all
    servers = ch.get("servers")
    if isinstance(servers, list) and servers:
        for s in servers:
            nm, internal = ref_name(s)
            if internal is True:
                p = norm_proto(as_dict(as_dict(doc.get("servers")).get(nm)).get("protocol"))
                if p:
                    protos.add(p)
    else:
        # No server pinning -> channel is available on all servers.
        protos.update(p for p in all_server_protos.values() if p)
        via_all = True
    protos |= binding_keys(ch)
    msgs = ch.get("messages")
    if isinstance(msgs, dict):
        for m in msgs.values():
            protos |= binding_keys(m)
    return protos, via_all


def doc_level_protocols(doc):
    """All protocols declared anywhere in the document."""
    protos = set(p for p in server_protocols(doc).values() if p)

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
    return {norm_proto(p) for p in protos if norm_proto(p) in KNOWN_PROTOCOLS}


def analyze_doc(doc):
    """Return list of receive+reply operation records for a 3.x doc."""
    records = []
    ops = doc.get("operations")
    if not isinstance(ops, dict):
        return records
    all_srv = server_protocols(doc)
    doc_protos = doc_level_protocols(doc)
    for op_id, op in ops.items():
        if not isinstance(op, dict):
            continue
        if op.get("action") != "receive":
            continue
        if "reply" not in op or op.get("reply") is None:
            continue
        reply = op.get("reply")
        req_ch = resolve_channel(doc, op.get("channel"))
        rep_ch = resolve_channel(doc, reply.get("channel")) if isinstance(reply, dict) else None
        reply_addr = reply.get("address") if isinstance(reply, dict) else None

        raw = set()
        via_all = False
        for ch in (req_ch, rep_ch):
            if ch is not None:
                cp, va = channel_protocols(doc, ch, all_srv)
                raw |= cp
                via_all = via_all or va
        raw |= binding_keys(op)
        if isinstance(reply, dict):
            raw |= binding_keys(reply)
        protos = {p for p in (norm_proto(x) for x in raw) if p in KNOWN_PROTOCOLS}
        if not protos:
            # Channels tied no protocol (missing/external $ref, or a channel that
            # pins no server). Fall back to the document's server protocol(s):
            # the operation still runs on those servers. Truly transport-agnostic
            # specs (no servers, no bindings) remain undetermined.
            fallback = {p for p in all_srv.values() if p in KNOWN_PROTOCOLS}
            if fallback:
                protos = fallback
                via_all = True

        def ch_label(field):
            if isinstance(field, dict) and "$ref" in field:
                return field["$ref"]
            if isinstance(field, dict):
                return "(inline)"
            return None

        records.append({
            "opId": op_id,
            "requestChannel": ch_label(op.get("channel")),
            "replyChannel": ch_label(reply.get("channel")) if isinstance(reply, dict) else None,
            "replyAddress": reply_addr,
            "sameChannel": (ch_label(op.get("channel")) is not None
                            and ch_label(op.get("channel")) == (ch_label(reply.get("channel")) if isinstance(reply, dict) else None)),
            "replyScopedProtocols": sorted(protos),
            "viaAllServers": via_all,
            "docLevelProtocols": sorted(doc_protos),
        })
    return records


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Loading corpus from %s ..." % RAW)
    corpus = load_corpus()
    if not corpus:
        print("error: no corpus items found; run asyncapi_adoption_survey.sh first", file=sys.stderr)
        sys.exit(1)
    by_ext = defaultdict(int)
    for rec in corpus.values():
        by_ext[rec["ext"]] += 1
    print("  unique blobs by sha: %d  (by ext: %s)  across %d repos"
          % (len(corpus), dict(by_ext),
             len({r for rec in corpus.values() for r in rec["repos"]})))

    print("Fetching specs (cached under %s) ..." % CACHE)
    failed = fetch_all(corpus)

    print("Parsing & detecting receive+reply ...")
    funnel = defaultdict(int)
    funnel["unique_blobs"] = len(corpus)
    funnel["fetch_failed"] = len(failed)

    # protocol -> sets, for headline (reply-scoped) and doc-level (context)
    hl_specs = defaultdict(set)   # proto -> set(sha)
    hl_repos = defaultdict(set)   # proto -> set(repo)
    hl_ops = defaultdict(int)     # proto -> op count
    dl_specs = defaultdict(set)
    dl_repos = defaultdict(set)
    undetermined_ops = 0
    op_rows = []                  # for CSV / appendix
    reply_specs = []              # per-spec appendix

    for sha, rec in corpus.items():
        if sha in failed:
            continue
        cf = cache_file(sha, rec["ext"])
        if not os.path.exists(cf):
            funnel["fetch_failed"] += 1
            continue
        try:
            doc = load_yaml(cf)
        except Exception:  # noqa: BLE001
            funnel["parse_failed"] += 1
            continue
        if not isinstance(doc, dict):
            funnel["parse_failed"] += 1
            continue
        if not is_3x(doc):
            funnel["non_3x"] += 1
            continue
        funnel["parsed_3x"] += 1
        if not isinstance(doc.get("operations"), dict):
            funnel["no_operations"] += 1
            continue
        try:
            recs = analyze_doc(doc)
        except Exception:  # noqa: BLE001 — one malformed spec must not abort the run
            funnel["analyze_failed"] += 1
            continue
        if not recs:
            continue
        funnel["specs_with_receive_reply"] += 1
        version = doc.get("asyncapi")
        repos = sorted(rec["repos"])
        doc_protos = recs[0]["docLevelProtocols"]
        spec_entry = {"sha": sha, "ext": rec["ext"], "repo": rec["repo"],
                      "path": rec["path"], "version": version, "repos": repos,
                      "n_locations": len(rec["locations"]),
                      "docLevelProtocols": doc_protos, "ops": []}
        for r in recs:
            funnel["receive_reply_ops"] += 1
            rp = r["replyScopedProtocols"]
            if rp:
                for p in rp:
                    hl_ops[p] += 1
                    hl_specs[p].add(sha)
                    hl_repos[p].update(repos)
            else:
                undetermined_ops += 1
            for p in doc_protos:
                dl_specs[p].add(sha)
                dl_repos[p].update(repos)
            spec_entry["ops"].append(r)
            op_rows.append({
                "repo": rec["repo"], "path": rec["path"], "sha": sha,
                "version": version, "opId": r["opId"],
                "requestChannel": r["requestChannel"] or "",
                "replyChannel": r["replyChannel"] or "",
                "replyAddress": r["replyAddress"] or "",
                "sameChannel": r["sameChannel"],
                "replyScopedProtocols": "|".join(r["replyScopedProtocols"]) or "undetermined",
                "viaAllServers": r["viaAllServers"],
                "docLevelProtocols": "|".join(doc_protos),
            })
        reply_specs.append(spec_entry)

    # ---- write JSON ----
    headline = sorted(
        ({"protocol": p, "ops": hl_ops[p], "specs": len(hl_specs[p]),
          "repos": len(hl_repos[p])} for p in hl_specs),
        key=lambda d: (-d["specs"], -d["ops"], d["protocol"]),
    )
    doclevel = sorted(
        ({"protocol": p, "specs": len(dl_specs[p]), "repos": len(dl_repos[p])}
         for p in dl_specs),
        key=lambda d: (-d["specs"], d["protocol"]),
    )
    result = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "definition": "operations with action:receive AND a reply (request channel may equal reply channel)",
        "funnel": dict(funnel),
        "by_extension": dict(by_ext),
        "headline_reply_scoped": headline,
        "undetermined_ops": undetermined_ops,
        "document_level": doclevel,
        "specs": reply_specs,
    }
    with open(os.path.join(OUT_DIR, "reply-protocols.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- write CSV ----
    with open(os.path.join(OUT_DIR, "reply-protocols.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "repo", "path", "sha", "version", "opId", "requestChannel",
            "replyChannel", "replyAddress", "sameChannel",
            "replyScopedProtocols", "viaAllServers", "docLevelProtocols"])
        w.writeheader()
        for row in op_rows:
            w.writerow(row)

    # ---- write Markdown ----
    write_markdown(os.path.join(OUT_DIR, "reply-protocols.md"),
                   result, headline, doclevel, undetermined_ops, funnel, by_ext, reply_specs)

    # ---- console summary ----
    print("\n==== AsyncAPI 3.x receive+reply protocol summary ====")
    print("unique 3.x blobs: %d | parsed 3.x: %d | specs with receive+reply: %d | ops: %d"
          % (funnel["unique_blobs"], funnel["parsed_3x"],
             funnel["specs_with_receive_reply"], funnel["receive_reply_ops"]))
    print("\nProtocol (reply-scoped)   ops  specs  repos")
    for d in headline:
        print("  %-22s %4d  %4d  %4d" % (d["protocol"], d["ops"], d["specs"], d["repos"]))
    if undetermined_ops:
        print("  %-22s %4d   (no protocol resolvable from channels/bindings)" % ("undetermined", undetermined_ops))
    print("\nOutputs: reply-protocols.{md,csv,json} under %s" % OUT_DIR)


def write_markdown(path, result, headline, doclevel, undetermined_ops, funnel, by_ext, reply_specs):
    L = []
    L.append("# AsyncAPI 3.x request-reply protocols\n")
    L.append("_Generated %s by `asyncapi_reply_protocols.py`._\n" % result["generated"])
    L.append("**Question.** For AsyncAPI 3.x specs, which messaging protocols are used by "
             "operations implementing the request-reply pattern where the SUT is the responder "
             "— i.e. operations with `action: receive` **and** a `reply` (the reply may target the "
             "same channel as the request, a different channel, or an address).\n")
    L.append("**Method.** The full 3.x corpus (yaml+yml+json, 3.0.0+3.1.0) enumerated by "
             "`asyncapi_adoption_survey.sh` was fetched and parsed. Reply operations were detected "
             "structurally; protocols were attributed **reply-scoped** (the channels the operation "
             "touches → their servers' `protocol` and/or `bindings`) for the headline, and "
             "**document-level** (any protocol declared in the spec) for context.\n")

    L.append("## Coverage funnel\n")
    L.append("| Stage | Count |")
    L.append("|-------|------:|")
    L.append("| Unique 3.x blobs (by sha) | %d |" % funnel.get("unique_blobs", 0))
    L.append("| &nbsp;&nbsp;by extension | %s |" % ", ".join("%s=%d" % (k, v) for k, v in sorted(by_ext.items())))
    L.append("| Fetch failed (deleted/renamed since survey) | %d |" % funnel.get("fetch_failed", 0))
    L.append("| Parse failed | %d |" % funnel.get("parse_failed", 0))
    L.append("| Not AsyncAPI 3.x (text-match false positives) | %d |" % funnel.get("non_3x", 0))
    L.append("| Parsed AsyncAPI 3.x | %d |" % funnel.get("parsed_3x", 0))
    L.append("| &nbsp;&nbsp;with no `operations` map | %d |" % funnel.get("no_operations", 0))
    L.append("| **Specs with ≥1 `receive`+`reply` op** | **%d** |" % funnel.get("specs_with_receive_reply", 0))
    L.append("| Total `receive`+`reply` operations | %d |\n" % funnel.get("receive_reply_ops", 0))

    L.append("## Headline — protocols of receive+reply operations (reply-scoped)\n")
    L.append("Counted from the protocol of the request and reply channels each operation uses. "
             "An operation using multiple protocols contributes to each.\n")
    L.append("| Protocol | receive+reply ops | specs | repos |")
    L.append("|----------|------------------:|------:|------:|")
    for d in headline:
        L.append("| `%s` | %d | %d | %d |" % (d["protocol"], d["ops"], d["specs"], d["repos"]))
    if undetermined_ops:
        L.append("| _undetermined_ | %d | | |" % undetermined_ops)
    L.append("")
    L.append("_`undetermined` = the spec declares no server `protocol` and no protocol `bindings` the "
             "operation can reach — i.e. a transport-agnostic spec (common in examples/fixtures/tooling). "
             "Where channels don't pin a server, the document's server protocol is used (flagged `viaAllServers`)._\n")

    L.append("## Document-level protocols (context)\n")
    L.append("Any protocol declared anywhere in a spec that has ≥1 receive+reply operation.\n")
    L.append("| Protocol | specs | repos |")
    L.append("|----------|------:|------:|")
    for d in doclevel:
        L.append("| `%s` | %d | %d |" % (d["protocol"], d["specs"], d["repos"]))
    L.append("")

    L.append("## Caveats\n")
    L.append("- Corpus seeded by the survey's `asyncapi: 3.0.0/3.1.0` GitHub code-search "
             "(yaml from the May snapshot; yml/json freshly enumerated) — a mild temporal mix. "
             "Parsing removes text-match false positives but cannot recover files GitHub never enumerated.\n")
    L.append("- Deduped by blob `sha` (identical content counted once); `repos` counts every repo "
             "containing that blob (forks inflate repo counts; `specs` does not).\n")
    L.append("- Only internal `#/...` `$ref`s are resolved; operations whose channels are external "
             "refs with no inline bindings fall into `undetermined`.\n")

    L.append("## Appendix — specs with receive+reply operations\n")
    for s in sorted(reply_specs, key=lambda x: (x["repo"], x["path"])):
        L.append("- [`%s`](https://github.com/%s) `%s` (asyncapi %s%s)"
                 % (s["repo"], s["repo"], s["path"], s["version"],
                    ", +%d more repo(s)" % (len(s["repos"]) - 1) if len(s["repos"]) > 1 else ""))
        for op in s["ops"]:
            prot = ", ".join(op["replyScopedProtocols"]) or "undetermined"
            same = " (same channel)" if op["sameChannel"] else ""
            L.append("    - `%s`: req=%s reply=%s%s → **%s**"
                     % (op["opId"], op["requestChannel"], op["replyChannel"] or op["replyAddress"] or "?", same, prot))
    L.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    main()
