#!/usr/bin/env python3
#
# Generalization of enum_2x_product_rr.py to the full runnable-service set:
# enumerate 2.x repos on Kafka/AMQP that (a) are classified product OR demo,
# (b) declare NO `correlationId`, and (c) show an in-code request/reply signal,
# tiered by strength:  naming (req+reply-ish names) > duplex (pub+sub same
# channel) > bidir (a publish op and a subscribe op exist somewhere).
# Marks every repo already code-read in the three prior passes so we only grind
# new ground. Read-only; no network.
#
import glob
import json
import os
import re
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
# Buckets to enumerate; override with env BUCKETS="uncategorized,tooling/library,..."
BUCKETS = set(os.environ.get("BUCKETS", "product,demo/fixture").split(","))
# Transports to enumerate; override with env PROTOCOLS="ws,wss,mqtt,mqtt5"
PROTOCOLS = set(os.environ.get("PROTOCOLS", "kafka,amqp").split(","))

ALREADY_READ = {
    # batch 1
    "ldynia/learning-api-styles", "caiquedebrito/logistics-platform", "joass1/ESD-Ticket-booking",
    "vincenzocorso/car-sharing", "kaje94/slek-link", "ClearEyesFullHearts/mft",
    "gsperim/account-engine-lab", "cibanezb95STG/quoteAssessmentCIB", "JLanders96/abw-processor",
    "ibm-cloud-architecture/vaccine-freezer-mgr", "n-bolanos/FastEventManager", "Brico87/event-gateway",
    # batch 2 (weaker-signal duplex)
    "LingshijunRenzy/ICS-guard-next", "rvasqz86/manufacturing-mes-streaming-aggregate",
    "nesaa-a/SPDD-EventSystem", "David-DAM/spring-boot-async-template-ultimate",
    "arih1299/solacedemo-kafkasummitapac2021", "bcwilsondotcom/nx-monorepo-template",
    "aimerzarashi/ts-cqrs-es-v1", "nandorsilva/asyncapi-demo",
    "Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i", "ldynia/rabbitmq",
    "baldimir/kie-backend", "tayyabfayyaz/hakathon_2",
    # product pass
    "funny-bunny-corp/payment-executor", "naomesh/naomesh-onion-orchestrator",
    "naomesh/naomesh-web-api", "sepa79/PocketHive", "Netcracker/qubership-integration-platform",
    "Netcracker/qubership-integration-runtime-catalog",
    "SebastianBorchardt1984/incubator-kie-kogito-runtimes", "EvenToNight/EvenToNight",
    "999iQ/networking", "XerxesDGreat/tt-notif-service", "karlosdaniel451/message-chat",
    "raulgonzalezdev/eda-backend-plus",
    # demo/fixture sweep (37)
    "ChunPingWang/saga-kafka", "jhoncastro28/saga-choreography", "kurtrisley/DemoEventDrivenService",
    "kurtrisley/EventDrivenServices", "paulCormierProgressive/EventDrivenServices",
    "Alex009/architecture-sprint-3", "GUR-ok/otus-microservice-architecture", "HenderOrlando/booklyapp",
    "aklivity/zilla-demos", "pfarkya/asyncApi_AccountManagerEDA", "robev2252060/2247107_MAP",
    "funny-bunny-corp/ledger", "funny-bunny-corp/payment-service", "mariacolab/einzelhandel",
    "gregoriocarranza/APPS-II-Core-Backend", "bump-sh/examples", "meteatamel/asyncapi-basics",
    "enisspahi/async-api-example", "mzegarras/asyncapi-labs", "coiouhkc/asyncapi-generator-examples",
    "ueisele/showcase-asyncapi-api", "edwmurph/api-docs", "tsurdilo/async-demo",
    "fmvilas/workshop-ride-app", "yoshioterada/Spec-Driven-Dev", "somosphi/ts-seed-jest",
    "atharvagadkari05/template_EDA_API", "ZiyamSanthosh/AsyncApiAmf",
    "ninkovski/bootcamp-back-util-api-contracts", "invivo-digital-factory/openapi-compiler-ts",
    "alexandramartinez/asyncapis-accounts-email", "nandorsilva/arc-dados", "Labdata-FIA/Engenharia-Dados",
    "specmesh/getting-started-apachekafka", "specmesh/helloworld-demo", "baldimir/kie-frontend",
    "WebFuzzing/Dataset",
    # WS/MQTT sweep (40): JSON-RPC/ledger products
    "CardanoSolutions/ogmios", "cardano-scaling/hydra", "digital-asset/canton", "canton-network/splice",
    "wso2/product-microgateway", "bitrockteam/kafka-dvs-api", "varunaditya27/sentinel-orchestrator-network",
    "HexRohit/cardano",
    # MQTT
    "absmach/magistrala", "Okan-wqm/aquaculture_platform", "adalbertocajueiro/edscorbot-c-cpp",
    "IlijaIvanovic78/F1DataStream", "guilhermerodrigues680/globo-terrestre-iot",
    "RidgeRun/ridgerun-immersive-teleoperation", "EthanSheehan/Grid-Sentinel", "blagoySimandov/takgo",
    # device-control
    "christian-photo/ninaAPI", "jniebuhr/gaggimate", "bang-olufsen/beoremote-halo", "kidoneself/DockPilot",
    "Sofie-Automation/sofie-core", "kubescape/synchronizer", "energywebfoundation/ddhub-client-gateway",
    "yelaco/ludofy",
    # games
    "KamilMarszalek/checkers-online", "TP-O/werewolf", "masechkacat/tic-tac-toe-server", "chess-vn/slchess",
    "BillyBolton/menace", "montionugera/atlas-world-svc", "phalanxduel/phalanxduel", "ciel334288/ghoulies",
    # chat/streaming sample
    "hmecruz/chat-service", "joshwambere/Galileo", "Ikay14/Suxch", "Navvyaa/ChatBE", "TeleGrammy/backend",
    "MariamElsoufyx/IMMERSA-Voice-Chat-API", "victorrentea/training-assistant", "Verdenroz/finance-query",
}

gold = json.load(open(GOLD, encoding="utf-8"))
meta = json.load(open(META, encoding="utf-8")) if os.path.exists(META) else {}


def bidirectional(doc):
    has_pub = has_sub = False
    ch = doc.get("channels")
    if isinstance(ch, dict):
        for c in ch.values():
            if isinstance(c, dict):
                has_pub = has_pub or "publish" in c
                has_sub = has_sub or "subscribe" in c
    return has_pub and has_sub


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
for sha, repos in sha_repos.items():
    keep = [r for r in repos if gold.get(r, {}).get("_bucket") in BUCKETS]
    if not keep:
        continue
    ext = sha_ext.get(sha, "yaml")
    cf = os.path.join(CACHE, f"{sha}.{ext}")
    if not os.path.exists(cf):
        alt = glob.glob(os.path.join(CACHE, f"{sha}.*"))
        if not alt:
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
    for repo in keep:
        ri = repo_info[repo]
        ri["protocols"] |= protos
        ri["corr"] = ri["corr"] or r["has_correlationId"]
        ri["duplex"] = ri["duplex"] or r["duplex_channel"]
        ri["naming"] = ri["naming"] or r["reqreply_naming"]
        ri["bidir"] = ri["bidir"] or bidir
        ri["n_specs"] += 1


def tier(ri):
    if ri["naming"]:
        return "naming"
    if ri["duplex"]:
        return "duplex"
    return "bidir"


SIGNAL = os.environ.get("SIGNAL", "hint")  # "hint" = has R/R signal; "nohint" = one-directional spec
# repo name/description hint that the service might do request/reply despite a one-way spec
RR_DESC_RE = re.compile(
    r"(rpc|request[\s\-/]?(repl|res|response)|req[\s\-/]?res|repl(y|ies)\b|response|respond|"
    r"\bcommand\b|cqrs|\bsaga\b|\bquery\b|synchronous|round[\s\-]?trip|callback|rendezvous|ask[\s\-]?pattern)",
    re.I)


def desc_of(repo):
    md = meta.get(repo) if isinstance(meta, dict) else None
    if not isinstance(md, dict):
        return "", "", False, False, False
    lang = (md.get("primaryLanguage") or {}).get("name") or ""
    d = md.get("description") or ""
    rrkw = bool(RR_DESC_RE.search(d)) or bool(RR_DESC_RE.search(repo))
    return lang, d, bool(md.get("isFork")), bool(md.get("isArchived")), rrkw


cands = []
for repo, ri in repo_info.items():
    if not (PROTOCOLS & ri["protocols"]):
        continue
    if ri["corr"]:
        continue
    has_signal = ri["bidir"] or ri["duplex"] or ri["naming"]
    if SIGNAL == "nohint" and has_signal:
        continue
    if SIGNAL != "nohint" and not has_signal:
        continue
    bucket = gold.get(repo, {}).get("_bucket")
    stars = int(gold.get(repo, {}).get("stargazerCount", 0) or 0)
    cands.append((repo, ri, bucket, stars))

unread = [c for c in cands if c[0] not in ALREADY_READ]

if SIGNAL == "nohint":
    BUCKET_RANK = {"product": 0, "demo/fixture": 1, "uncategorized": 2}
    unread.sort(key=lambda t: (0 if desc_of(t[0])[4] else 1, BUCKET_RANK.get(t[2], 9), -t[3], t[0]))
    print(f"# 2.x {'/'.join(sorted(PROTOCOLS))} services with NO schema R/R hint (one-directional spec), "
          f"NO correlationId")
    print(f"# buckets={sorted(BUCKETS)}  total={len(cands)}  already-read={len(cands)-len(unread)}  "
          f"UNREAD={len(unread)}")
    print("# 'RR!' = repo name/description hints at request/reply (rpc/command/query/saga/sync/...)\n")
    for repo, ri, bucket, stars in unread:
        lang, d, fork, arch, rrkw = desc_of(repo)
        flags = ("RR! " if rrkw else "") + ("FORK " if fork else "") + ("ARCH " if arch else "")
        proto = "+".join(sorted(PROTOCOLS & ri["protocols"]))
        print(f"  {stars:>4}* {bucket:13} {proto:11} {flags}{repo}\n           [{lang}] {d[:85]}")
    print("\n# UNREAD list (for dispatch), R/R-keyword + product + stars first:")
    for repo, ri, bucket, stars in unread:
        print(repo)
else:
    TIER_RANK = {"naming": 0, "duplex": 1, "bidir": 2}
    BUCKET_RANK = {"product": 0, "demo/fixture": 1}
    unread.sort(key=lambda t: (TIER_RANK[tier(t[1])], BUCKET_RANK.get(t[2], 9), -t[3], t[0]))
    print(f"# 2.x repos on {'/'.join(sorted(PROTOCOLS))}, NO correlationId, WITH an in-code R/R signal")
    print(f"# total candidates: {len(cands)}   already-read: {len(cands)-len(unread)}   UNREAD: {len(unread)}")
    print("# tiers: naming > duplex > bidir\n")
    by_tier = defaultdict(list)
    for c in unread:
        by_tier[tier(c[1])].append(c)
    for tl in ("naming", "duplex", "bidir"):
        rows = by_tier[tl]
        print(f"### tier={tl}  ({len(rows)} unread)")
        for repo, ri, bucket, stars in rows:
            lang, d, fork, arch, _ = desc_of(repo)
            flags = ("FORK " if fork else "") + ("ARCH " if arch else "")
            proto = "+".join(sorted(PROTOCOLS & ri["protocols"]))
            print(f"  {stars:>4}* {bucket:13} {proto:11} {flags}{repo}\n           [{lang}] {d[:85]}")
        print()
    print("# UNREAD list (for dispatch), strongest-signal first:")
    for repo, ri, bucket, stars in unread:
        print(repo)
