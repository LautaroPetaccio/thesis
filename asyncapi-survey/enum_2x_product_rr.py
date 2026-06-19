#!/usr/bin/env python3
#
# Enumerate 2.x **product** repos on Kafka/AMQP that plausibly implement a
# request/reply (reply/response) pattern *in code* but DON'T declare it in the
# AsyncAPI schema — i.e. no `correlationId` object, yet the service is
# bidirectional (has both publish & subscribe ops), or has a duplex channel, or
# request/reply-suggestive naming. These are the candidates to code-read.
#
# Reuses asyncapi_correlation_2x.analyze_doc for correlationId/duplex/naming, the
# 2.x gold classification (out-2x) for the product filter + stars, and
# repo-metadata for description/language/fork flags. Read-only; no network.
#
import glob
import json
import os
import sys
from collections import defaultdict

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asyncapi_correlation_2x import analyze_doc, is_2x, iter_json_objects  # noqa: E402

SURVEY = "/Users/lpetaccio/tesis/asyncapi-survey"
CACHE = os.path.join(SURVEY, "asyncapi-survey-out", "raw", "specs-2x")
OUT2X_RAW = os.path.join(SURVEY, "asyncapi-survey-out-2x", "raw")
GOLD = os.path.join(OUT2X_RAW, "repo-classification-gold.json")
META = os.path.join(OUT2X_RAW, "repo-metadata.json")
VERSION_JSONS = [f"asyncapi-2-{m}.json" for m in range(7)]

# Every AMQP/Kafka repo already code-read across both prior batches (so we don't re-read).
ALREADY_READ = {
    "ldynia/learning-api-styles", "caiquedebrito/logistics-platform", "joass1/ESD-Ticket-booking",
    "vincenzocorso/car-sharing", "kaje94/slek-link", "ClearEyesFullHearts/mft",
    "gsperim/account-engine-lab", "cibanezb95STG/quoteAssessmentCIB", "JLanders96/abw-processor",
    "ibm-cloud-architecture/vaccine-freezer-mgr", "n-bolanos/FastEventManager", "Brico87/event-gateway",
    "LingshijunRenzy/ICS-guard-next", "rvasqz86/manufacturing-mes-streaming-aggregate",
    "nesaa-a/SPDD-EventSystem", "David-DAM/spring-boot-async-template-ultimate",
    "arih1299/solacedemo-kafkasummitapac2021", "bcwilsondotcom/nx-monorepo-template",
    "aimerzarashi/ts-cqrs-es-v1", "nandorsilva/asyncapi-demo",
    "Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i", "ldynia/rabbitmq",
    "baldimir/kie-backend", "tayyabfayyaz/hakathon_2",
}

gold = json.load(open(GOLD, encoding="utf-8"))
meta = json.load(open(META, encoding="utf-8")) if os.path.exists(META) else {}


def bidirectional(doc):
    """2.x service both sends and receives: a publish op AND a subscribe op anywhere."""
    has_pub = has_sub = False
    ch = doc.get("channels")
    if isinstance(ch, dict):
        for c in ch.values():
            if isinstance(c, dict):
                has_pub = has_pub or "publish" in c
                has_sub = has_sub or "subscribe" in c
    return has_pub and has_sub


# sha -> set(repos), sha -> ext
sha_repos = defaultdict(set)
sha_ext = {}
for fn in VERSION_JSONS:
    p = os.path.join(OUT2X_RAW, fn)
    if not os.path.exists(p):
        continue
    for obj in iter_json_objects(open(p, encoding="utf-8", errors="replace").read()):
        for it in (obj.get("items") or []):
            sha = it.get("sha")
            repo = (it.get("repository") or {}).get("full_name")
            path = it.get("path")
            if not (sha and repo):
                continue
            sha_repos[sha].add(repo)
            if sha not in sha_ext and path:
                sha_ext[sha] = path.rsplit(".", 1)[-1].lower() if "." in path else "yaml"

repo_info = defaultdict(lambda: {"protocols": set(), "corr": False, "duplex": False,
                                 "naming": False, "bidir": False, "n_specs": 0})
missing_cache = 0
for sha, repos in sha_repos.items():
    prod = [r for r in repos if gold.get(r, {}).get("_bucket") == "product"]
    if not prod:
        continue
    ext = sha_ext.get(sha, "yaml")
    cf = os.path.join(CACHE, f"{sha}.{ext}")
    if not os.path.exists(cf):
        alt = glob.glob(os.path.join(CACHE, f"{sha}.*"))
        if not alt:
            missing_cache += 1
            continue
        cf = alt[0]
    try:
        doc = yaml.safe_load(open(cf, encoding="utf-8", errors="replace"))
    except Exception:
        continue
    if not isinstance(doc, dict) or not is_2x(doc):
        continue
    try:
        r = analyze_doc(doc)
    except Exception:
        continue
    protos = set(r["protocols"])
    bidir = bidirectional(doc)
    for repo in prod:
        ri = repo_info[repo]
        ri["protocols"] |= protos
        ri["corr"] = ri["corr"] or r["has_correlationId"]
        ri["duplex"] = ri["duplex"] or r["duplex_channel"]
        ri["naming"] = ri["naming"] or r["reqreply_naming"]
        ri["bidir"] = ri["bidir"] or bidir
        ri["n_specs"] += 1

cands = []
for repo, ri in repo_info.items():
    if not ({"kafka", "amqp"} & ri["protocols"]):
        continue
    if ri["corr"]:
        continue
    if not (ri["bidir"] or ri["duplex"] or ri["naming"]):
        continue
    stars = int(gold.get(repo, {}).get("stargazerCount", 0) or 0)
    cands.append((repo, ri, stars))

# strongest signal first (naming > duplex > bidir), then stars
def rank(t):
    _, ri, stars = t
    sig = (2 if ri["naming"] else 0) + (1 if ri["duplex"] else 0)
    return (-sig, -stars, t[0])


cands.sort(key=rank)
print("# 2.x PRODUCT repos on Kafka/AMQP — NO declared correlationId — with an in-code R/R signal")
print(f"# candidates: {len(cands)}   (product repos missing from cache: {missing_cache})")
print("# signal: naming = req/reply-ish names; duplex = pub+sub same channel; bidir = pub & sub ops exist")
print("# [READ] = already code-read in a prior batch;  fork/arch flagged\n")
unread = []
for repo, ri, stars in cands:
    read = repo in ALREADY_READ
    if not read:
        unread.append((repo, ri, stars))
    tag = "[READ]" if read else "      "
    sig = ",".join(s for s, v in [("naming", ri["naming"]), ("duplex", ri["duplex"]),
                                   ("bidir", ri["bidir"])] if v)
    proto = "+".join(sorted({"kafka", "amqp"} & ri["protocols"]))
    md = meta.get(repo) if isinstance(meta, dict) else None
    flags = ""
    desc = ""
    if isinstance(md, dict):
        if md.get("isFork"):
            flags += "FORK "
        if md.get("isArchived"):
            flags += "ARCH "
        lang = (md.get("primaryLanguage") or {}).get("name") or ""
        desc = f"[{lang}] " + (md.get("description") or "")[:90]
    print(f"{tag} {stars:>4}* {proto:11} {sig:18} {flags}{repo}\n           {desc}")

print(f"\n# UNREAD product candidates: {len(unread)}")
print("# unread repo list (for dispatch):")
for repo, ri, stars in unread:
    print(repo)
