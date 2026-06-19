# Are the request/reply corpus repos usable as SUTs?

A concrete, per-repo read of every AsyncAPI 3.x repository in the survey that declares a
`receive`+`reply` operation, judged against one bar:

> **Is this a real, runnable service that consumes a request message and emits a *correlated* reply
> over a broker/socket — something we could containerize and drive as a black box (publish a
> request, observe the reply)?**

This is the evaluation question for the thesis: do we have real-world SUTs, or must we rely on the
synthetic NCS SUTs (NCS over Kafka/AMQP/MQTT/WebSocket)?

## Method

The survey's reply-pattern set is **81 repos**. Of these, 42 are **tooling/library** (30) or
**spec/docs** (12) — by definition not runnable services, only contracts or tools — so they were
dispositioned at category level. The **39 candidates** (13 products + 23 demo/fixture + 3
uncategorized) were each read concretely: the cached README and AsyncAPI spec
(`asyncapi-survey/asyncapi-survey-out/raw/{readmes,specs-3x}/`) plus a live check of the GitHub repo
for **actual request/reply handler code** (a spec file in a repo does *not* imply a matching
implementation), docker/compose, license, language, correlation mechanism, and external dependencies.

## Headline

| Outcome | Count (of 81) | Meaning |
| --- | ---: | --- |
| **Usable with minimal effort** | **2** | real R/R service, clean-ish standup, permissive license |
| **Usable with real work** | **~17** | real R/R code, but needs containerizing / dep-stubbing / correlation fixes / a license |
| **Not usable as a SUT** | **~62** | tools, specs, fixtures, docs-only, no implementation, broadcast-not-reply, wrong transport, or hard SaaS deps |

The corpus is **SUT-poor for this thesis.** Almost nothing sits in the "small, clean, runnable,
well-specified, permissively-licensed" sweet spot. The real services are **bimodal**: tiny
hobby/student repos (0–3★) where the AsyncAPI file is aspirational, or large platforms (EVerest,
Netcracker) that are genuine but heavy to stand up. This is exactly the gap the
synthetic NCS SUTs fill.

## Verification (re-check)

These verdicts were re-checked independently of the first pass: (1) a deterministic scan of the
cached specs re-derived every repo's transport, reply operations, and correlation declarations (no
web, no agent — so it cannot drift); (2) adversarial readers re-opened the highest-stakes repos on
GitHub and **quoted the actual handler code**. **Every verdict held** — both USABLE repos were
confirmed from source (`enterprise-sample`'s `PlaceOrderKafkaHandler.kt` echoes the `correlationId`
header; `voiceblender`'s `/v1/vsi` handler echoes `request_id`), and the four NOT-USABLE
spot-checks (Taxi, ollert-backend, vequate, CRM) were confirmed with **no false negatives**.

The re-check corrected several supporting facts (folded into the tables here), the most important
being **correlation**. Contrary to an earlier claim, *no* shortlist service except the Specmatic
samples / `stueble` / `CRM` declares a formal AsyncAPI `correlationId.location`; the usable services
correlate via a header/payload **field the responder echoes in code**. That is itself a finding: a
black-box tool keying off the contract's `correlationId.location` (as in `proposal.md` §"Transports
and correlation") would *not* find correlation in most real services and would fall back to reading
header schemas or heuristics — reinforcing that caveat. Smaller fixes: `CRM` *does* implement a
correlated `requestId` reply (disqualified by a hard live-Salesforce dependency + no license, not by
being fire-and-forget); `Taxi` carries an Apache-2.0 license but is still source-less; and
`e_commerce` standup is heavier than first stated (external RabbitMQ network + MariaDB + Liquibase +
a secrets file).

## The viable shortlist (real services worth using)

Prioritised by licensing + standup effort. Transport/lang/license/correlation are as-implemented
(not as the spec claims — see "spec drift" below).

| Repo | Transport | Lang | License | Correlation (as built) | Effort to use as SUT |
| --- | --- | --- | --- | --- | --- |
| **VoiceBlender/voiceblender** | WebSocket | Go | MIT | `request_id` echoed (convention, no AsyncAPI `correlationId`) | **Low** — Dockerized; drive `/v1/vsi` commands, assert `*.result` by `request_id`; avoid SIP/cloud commands |
| **specmatic/enterprise-sample** | Kafka | Kotlin | MIT | `correlationId` Kafka-header field, **echoed in code** (no formal `correlationId.location` in spec) | **Low** — `docker compose up` Kafka+service; drive `orders.place.cmd`→`orders.place.reply` |
| **specmatic/specmatic-arazzo-…-sample** | Kafka | Python | **none** | `requestId` header, declared + echoed | Low–moderate — turnkey compose (Kafka+PG); **add a license** |
| **metalalive/e_commerce** (order svc) | AMQP | Rust | MIT | AMQP `correlation_id` property echoed; reply-to = `replyTo` header | Moderate–high — needs **external** RabbitMQ network + MariaDB + Liquibase migrations + a `secrets.json` |
| **gematik/zeta-testfachdienst** | STOMP/WS | Java | **Apache-2.0** | STOMP `@SendToUser` session routing (no declared id) | Moderate — write a STOMP client; spec correlation is weak/generated |
| **EVerest/EVerest** | MQTT | C++ | **Apache-2.0** | `replyTo` header, **declared + implemented** | **High** — needs the full EVerest manager+MQTT+config + ready-beacon handshake |
| **eclipse-uprotocol/symphony-target-example-rust** | MQTT5 (uProtocol) | Rust | Apache-2.0 | uProtocol `UAttributes` (req-id) | Moderate–high — must embed a uProtocol-over-MQTT client to frame requests |

The two closest to plug-and-play are **voiceblender** and **enterprise-sample**. Correction from the
re-check: *neither* declares a formal AsyncAPI `correlationId.location` — both correlate via a field
the responder echoes in code (voiceblender a `request_id` payload field; enterprise-sample a
`correlationId` Kafka-header field). The repos that *do* declare a formal `correlationId.location`
are `stueble`, `CRM`, and the Specmatic samples (`arazzo-sample`, `kafka-sample-asyncapi3`,
`aws-lambda`, `labs`) — none of which is among the most usable services. For a real-world evaluation
set, the best licensed mix spanning transports is **enterprise-sample (Kafka) + e_commerce (AMQP) +
EVerest or symphony (MQTT) + voiceblender or zeta (WS/STOMP)** — all MIT/Apache-2.0.

## What would make a repo usable (the recurring fixes)

Across the candidates, the same blockers recur. The "changes to make them usable" generalise to:

1. **Containerize / isolate** the one R/R service: trim multi-service `docker-compose` to the
   service + its broker; replace cloud infra (GCP Pub/Sub, MSK-on-LocalStack, k3d/AKS) with a local
   broker container.
2. **Stub the hard external dependency** that gates any reply: live SIGAA (sigaa-socket-api),
   Salesforce (CRM), a downstream REST "System A" (mq-rest-sync-adapter), Firebase
   (nurtura-backend), a paid LocalStack token (aws-lambda-…). Without this, only error/auth paths
   are observable.
3. **Fix or declare correlation** so a black-box oracle can match replies:
   - broadcast → unicast-correlated reply (ollert-backend, stardew/web, nurtura-backend);
   - **un-hardcode** a correlation id (specmatic-kafka-sample-asyncapi3 literally replies with
     `orderCorrelationId="12345"` — correlation is *declared but broken*);
   - promote an ad-hoc payload field (`request_id`, `reqId`) to a declared AsyncAPI `correlationId`.
4. **Add a license** — many real candidates ship none (stueble, vequate, nurtura is *UNLICENSED*,
   several specmatic samples, chanx), which blocks reuse in a thesis artifact.
5. **Supply the reply side** where the repo is only the *requester* — znsio/specmatic-async-order-api
   publishes the request and consumes the reply, but the responder is a Specmatic **mock**, not code.
6. **Write a transport adapter** for non-plain framings: uProtocol `UAttributes`, Zilla
   `zilla:correlation-id` headers, STOMP, NATS request/reply.
7. **Reconcile spec↔code drift** (below) before trusting the contract.

## Spec drift found (contract ≠ implementation)

The concrete read surfaced cases where the AsyncAPI file does not match the code — a problem-domain
finding in itself (and a caution for any purely contract-driven tool):

- **BackendFans83/Taxi** — spec is **gRPC**, README says RabbitMQ, and there is **no source at all**.
- **Jack-the-Pro101/vequate** — spec says **Redis**, code uses **Google Cloud Pub/Sub**.
- **codemonstersteam/mq-rest-sync-adapter** — spec says **AMQP**, code uses **IBM MQ (JMS)**.
- Several repos carry a **borrowed sample spec** as a fixture: the canonical AsyncAPI **Kraken
  WebSocket** sample (CodeBeast357/webosapi-asyncapi, Shurtu-gal/action-test-bed) and the
  **adeo-kafka-request-reply** example (see `proposal.md`).
- Catalog metadata itself drifted: `sillygod/scaffold` is **Go** (not Python); the Den-Team uService
  is **Rust** (not Python); `sigaa-socket-api` is **GPL-3.0** though its spec says MIT.

## Correlation, as actually implemented (by transport)

Reading the request/reply code of real services (rather than their AsyncAPI docs) shows that whether a
reply can be correlated to its request — the precondition for any black-box oracle — is decided by the
implementation, and differs sharply by transport. (`proposal.md` carries the repo-name-free,
descriptive version of this.)

- **AMQP — native, when the responder echoes.** `metalalive/e_commerce` (Rust order service) reads the
  inbound AMQP `correlation-id` + `reply-to` properties and echoes them — the canonical RabbitMQ RPC
  convention; a tool can pair replies knowing only "it's RabbitMQ", no doc needed. By contrast the
  official `asyncapi/dotnet-rabbitmq-template` *sets* native `CorrelationId`/`ReplyTo` on publish but
  **never echoes them and never sends a reply** — scaffolding, not a working RPC responder.
- **Kafka — per-implementation header, sometimes broken.** Three real services, three different
  homemade header names, none using Spring's `kafka_correlationId` default: `specmatic/enterprise-sample`
  echoes a custom `correlationId` header (works); `aklivity/todo-service` echoes `zilla:correlation-id`
  (Zilla convention, works); but `specmatic/specmatic-kafka-sample-asyncapi3` declares `orderCorrelationId`
  in its spec while the code **hardcodes `"12345"`** and never echoes the inbound id — so all replies
  collide and correlation is impossible despite a "correct" contract.
- **MQTT — hand-rolled; docs declare headers the wire cannot carry.** `OI4/oi4-oec-service` runs MQTT
  **3.1.1** and correlates via payload `MessageId`↔`ReplyTo`, yet its AsyncAPI doc declares
  `$message.header#/correlationId` — impossible on a header-less 3.1.1 wire. `EVerest` negotiates MQTT
  **5.0** (its client even has Correlation Data / Response Topic helpers) but the request/reply path
  **ignores them**, using a per-UUID reply **topic** plus a `replyTo` field inside the JSON payload.

The throughline: the AsyncAPI `correlationId` is a hint to verify, not a guarantee — correlation works
with no declaration (e_commerce), fails despite one (kafka-sample), and is mis-declared against the
wire (OI4). The only reliable check is empirical: stamp an id on the request and see whether the reply
carries it back.

## Beyond the 39: AMQP/Kafka services that correlate in code without declaring it

A service can correlate a reply to its request without ever declaring a `correlationId` — via native
AMQP properties, a Kafka header, or a payload field. To find SUTs we'd otherwise miss, we searched the
**AMQP/Kafka** repos of both corpora for a request/reply hint in the spec (a reply op in 3.x;
request/reply-suggestive names or a duplex `publish`+`subscribe` channel in 2.x) but **no** declared
`correlationId` — and code-read every candidate this surfaces across both corpora: **139 in all**
(enumerated by `asyncapi-survey/enum_2x_rr_all.py`) — the complete 2.x **product + demo/fixture** set on
Kafka/AMQP (73), the **uncategorized + tooling + spec/docs** buckets (66, overwhelmingly AsyncAPI tools
and doc collections rather than services), plus the early cross-corpus reads. The 3.x reply-construct
repos turn out to be exactly the corpus-suitability candidates already assessed above, so they add no
new gaps. Most were one-way event streaming (no reply); **11 are genuine correlated request/reply**
(every one correlates by a payload field, a native AMQP property, or an app header — never the AsyncAPI
keyword):

| Repo | Transport | Correlation (as built) | Verdict |
| --- | --- | --- | --- |
| `ldynia/learning-api-styles` (RabbitMQ-RPC teaching example, `src/rabbitmq/6.RequestResponse`) | AMQP | **native** `correlation-id` + `reply-to`, echoed (MIT) | USABLE (compose; TLS on by default → `TLS_ENABLE=0`) |
| `ldynia/rabbitmq` (RabbitMQ "tutorial six" RPC, `6.RPC/`) | AMQP | **native** `correlation_id` + `reply_to`, echoed | USABLE-WITH-CHANGES (TLS default → `TLS_ENABLE=false`; request body is a bare integer, not the spec's JSON) |
| `caiquedebrito/logistics-platform` (tracking↔route-opt) | AMQP | **payload** field `correlationId`/`deliveryId`, echoed | USABLE (Dockerized; HTTP trigger → reply on `q.tracking.route_updates`) |
| `joass1/ESD-Ticket-booking` (waitlist↔seat) | AMQP | **payload** field `waitlist_entry_id`, echoed | USABLE (Dockerized; publish `seat.reserve.request` → `…confirmed`/`failed`) |
| `vincenzocorso/car-sharing` (CQRS saga) | Kafka | **header** `correlation_id` (= request `message_id`), echoed | USABLE-WITH-CHANGES (heavy: Debezium+Kafka+Temporal; and it _documents_ the header) |
| `sepa79/PocketHive` (load/behaviour-simulation platform — **a real product**; control plane) | AMQP | **payload** field `correlationId` (`ControlSignal`→`CommandOutcome`, echoed) | USABLE-WITH-CHANGES (build multi-module Maven; run RabbitMQ + a worker; the data-plane pipeline is one-way and would mislead) |
| `Alex009/architecture-sprint-3` (smart-home microservices; OTUS course) | Kafka | **payload** field `deviceId`, echoed (register/command → success/failed) | USABLE (docker-compose; the most product-grade of the demos — JWT/Kong/InfluxDB) |
| `ChunPingWang/saga-kafka` (SAGA orchestrator↔participant) | Kafka | **payload** field `orderId`, echoed (+ a carried-but-unused `correlationId`) | USABLE (3-service saga; spec declares `correlationId` only as a header _property_, not the keyword) |
| `tsurdilo/async-demo` (banking txn→account-info) | Kafka | **payload** field `transactionId`, echoed | USABLE-WITH-CHANGES (spec topic suffix `.02` vs code `.03`; drive the Spring `banking-service`, not the Temporal `wf-demo`) |
| `fmvilas/workshop-ride-app` (AsyncAPI-founder ride-hailing workshop) | Kafka | **payload** field `rideId`, echoed (`ride-accepted`→`ride-assigned`) | USABLE-WITH-CHANGES (decouple from Slack/Netlify/CloudKafka; drive Kafka directly) |
| `AceTheCreator/simple-commerce` (microservice e-commerce demo over RabbitMQ/Glee) | AMQP | **native** `correlationId` header **+** echoed payload `reqId`; gateway blocks on a matching listener | USABLE-WITH-CHANGES (RabbitMQ + a Mongo per service; boot several services; hardcoded URLs; has compose) |

NOT correlated request/reply (one-way streaming / no reply): `kaje94/slek-link`,
`ClearEyesFullHearts/mft`, `gsperim/account-engine-lab`, `cibanezb95STG/quoteAssessmentCIB` (Azure
Service Bus, one-way — and it _does_ declare a correlationId), `JLanders96/abw-processor` (Cloudflare
Queues; replies are HTTP), `ibm-cloud-architecture/vaccine-freezer-mgr`, `n-bolanos/FastEventManager`,
`Brico87/event-gateway`. A second pass over the remaining weaker-signal 2.x candidates (duplex
`publish`+`subscribe` channel only) added **11 more one-way finds**, no new R/R:
`LingshijunRenzy/ICS-guard-next`, `rvasqz86/manufacturing-mes-streaming-aggregate` (Kafka Streams),
`nesaa-a/SPDD-EventSystem`, `David-DAM/spring-boot-async-template-ultimate` (request-named event to a
different topic, random key), `arih1299/solacedemo-kafkasummitapac2021` (timer-driven suppliers +
fire-and-forget transform), `bcwilsondotcom/nx-monorepo-template` (no broker code — HTTP/Lambda +
contract-only), `aimerzarashi/ts-cqrs-es-v1` (one-way CQRS via Debezium CDC), `nandorsilva/asyncapi-demo`
(log-only consumer on the same topic), `Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i` (GitOps
manifests + an MQ send-then-receive smoke test, no `JMSReplyTo`/`JMSCorrelationID`), `baldimir/kie-backend`
(Kogito one-way CloudEvents; the duplex channel is two independent workflows), `tayyabfayyaz/hakathon_2`
(forward-only event choreography).

A third pass widened the net to **every 2.x product repo** on Kafka/AMQP that is bidirectional (a
publish op _and_ a subscribe op) but declares no `correlationId` (20 candidates; 12 unread, read here —
enumerated by `asyncapi-survey/enum_2x_product_rr.py`). It produced the search's **only product-grade
find**, `sepa79/PocketHive` (above), plus one real-but-unusable product:
`Netcracker/qubership-integration-platform` (Qubership iPaaS) — its engine echoes a configurable
correlation id (Kafka header or body field) in the service-call element (`CorrelationIdPropagationProcessor`
→ `CorrelationIdSetter`), but request/reply is authored per integration chain rather than intrinsic, the
stack is heavy (Consul+Kafka+Postgres+engine+catalog+UI), and its AsyncAPI files are spec **importer
fixtures** describing third-party systems, not its own messaging. The other 10 were one-way or not real
products: `funny-bunny-corp/payment-executor` (event choreography, HTTP to the PSP),
`naomesh/naomesh-onion-orchestrator` + `naomesh/naomesh-web-api` (fire-and-forget despite `@RabbitRPC`
names; AMQP props discarded — research demo), `Netcracker/qubership-integration-runtime-catalog`
(archived control-plane half, no messaging runtime), `SebastianBorchardt1984/incubator-kie-kogito-runtimes`
(Kogito fork = the same one-way CloudEvents as `baldimir/kie-backend`), `EvenToNight/EvenToNight`
(university capstone), `999iQ/networking` (Kafka-producer toy, no consumer), `XerxesDGreat/tt-notif-service`
(IBM codegen, subscribe-A→publish-unrelated-B), `karlosdaniel451/message-chat` (NATS pub/sub chat),
`raulgonzalezdev/eda-backend-plus` (feed-forward streaming/alerting).

A fourth pass swept **all remaining 2.x demo/fixture repos** on Kafka/AMQP (37 unread of the 73; the
strongest _naming_-signal tier was already exhausted). It produced the four Kafka payload-field finds in
the table plus four instructive special cases: **`aklivity/zilla-demos`** — real, product-grade
request/reply (it echoes a `zilla:correlation-id` Kafka header; sibling demos use AsyncAPI **3.0** native
`reply`/`correlationIds`) but **declared in the schema** (via the `x-reply-to`/header extension or 3.0
`reply`) — the lone counter-example of contract-surfaced correlation; **`HenderOrlando/booklyapp`** — a
fully-coded, undeclared correlated _requester_ (payload `correlationId`/`requestId`+`replyTo` over
Kafka+RabbitMQ) whose **responder half is unimplemented** (PARTIAL/UWC — add the missing consumer);
**`WebFuzzing/Dataset`** (EvoMaster's own benchmark) which contains one genuine correlated Kafka R/R
(`familie-tilbake`→`familie-ba-sak`, echoed record-key UUID, **no AsyncAPI at all**) but spans two SUTs
and is gated behind Spring profiles; and **`somosphi/ts-seed-jest`** — weak (find-user→publish reply tied
only by an echoed `id`; its committed spec is the stock Streetlights MQTT sample, unrelated to the code).
The remaining ~25 were one-way or not runnable services: `jhoncastro28/saga-choreography`,
the Dapr trio `kurtrisley/DemoEventDrivenService` + `kurtrisley/EventDrivenServices` +
`paulCormierProgressive/EventDrivenServices` (latter two identical subsets), `funny-bunny-corp/ledger` +
`payment-service` (choreography, like their `payment-executor` sibling), `robev2252060/2247107_MAP`,
`pfarkya/asyncApi_AccountManagerEDA`, `mariacolab/einzelhandel`, `gregoriocarranza/APPS-II-Core-Backend`
(inert `correlationId` field), `yoshioterada/Spec-Driven-Dev` (Azure Service Bus tracing-only),
`alexandramartinez/asyncapis-accounts-email` (MuleSoft fan-out), `nandorsilva/arc-dados` (producer-only),
`Labdata-FIA/Engenharia-Dados` (tracing forward), `baldimir/kie-frontend` (Apache KIE Tools editor
monorepo), both SpecMesh demos (spec-only / stub `main`), `GUR-ok/otus-microservice-architecture`
(charts/specs only), and the AsyncAPI example/tutorial/codegen collections (`bump-sh/examples`,
`meteatamel/asyncapi-basics`, `enisspahi/async-api-example`, `mzegarras/asyncapi-labs`,
`coiouhkc/asyncapi-generator-examples`, `ueisele/showcase-asyncapi-api`, `edwmurph/api-docs`,
`atharvagadkari05/template_EDA_API`, `ZiyamSanthosh/AsyncApiAmf`, `ninkovski/bootcamp-back-util-api-contracts`,
`invivo-digital-factory/openapi-compiler-ts`).

A fifth pass extended the net beyond the service buckets to the corpus's **uncategorized** (the classifier
couldn't label them, so genuinely unknown), **tooling/library**, **tangential**, and **spec/docs** repos on
Kafka/AMQP with an in-code request/reply signal and no `correlationId` (66 candidates). The uncategorized
bucket yielded the table's one new find, **`AceTheCreator/simple-commerce`** (AMQP RPC: native
`correlationId` header + echoed `reqId` payload, undeclared). It also surfaced strong **negative evidence on
real products**: two production **PagoPA** (Italian government) IDPay services — `pagopa/idpay-reward-calculator`
(reply keyed by `userId`; payload `correlationId` is an upstream passthrough, never a messaging correlator)
and `pagopa/idpay-onboarding-workflow` (sends its request to a _different_ service over Azure Service Bus,
matches outcomes by a Mongo lookup) — both genuine products, both **one-way choreography**.
`aklivity/todo-service` (the standalone Zilla todo) correlates via a `zilla:correlation-id` header but
**declares it** (AsyncAPI 3.0 `reply`), reinforcing the Zilla counter-example rather than adding a find. The
other uncategorized app candidates were NO (`leopcaraballo/RLApp-V2` MassTransit event-sourcing/projections,
`Archi-Lab-FAE/fae-team-2-service` two one-way flows, `BakangMonei/PolyGlot-Demo-Examples` docs + producer-only,
`parmendes/MessageBrokerExample` doc-gen with publish commented out, `rakeshmani35/springboot-openAPI`
HTTP-only). The ~50 tooling/spec repos triaged out by definition — AsyncAPI _tools_ (validators, parsers,
generators, templates, `microcks`/`mokapi`/`apidom` mockers, CLI plugins, doc portals, API consoles), not
services that implement a contract. This covers every Kafka/AMQP service with an in-code request/reply _signal_.

A sixth pass closed the last gap — the **62 Kafka/AMQP services whose AsyncAPI is purely one-directional**
(no reply op, no duplex channel, no request/reply naming) and declares no `correlationId`, i.e. the schema
gives zero hint but the _code_ might still correlate (enumerated by `enum_2x_rr_all.py` with `SIGNAL=nohint`).
It produced **no new clean find** — a one-way spec almost always means one-way code. The only near-misses
were **forward-saga choreography** services that echo a business id across stages: `lok-hit/CarRentalApp`
(reply echoes `reservationId`, but the payment leg is unwired — stub publishers), `mnabli94/ecommerce-microservices`
(`orderId`), `zdmooc/TradeOps-GenAI-Integration` (`correlation_id` payload field, downstream),
`ChiragSethi-1153/RMHA` (`order_id`), `Lynda1423/gestion-vehicules` (`vehiculeId` as key + field) — each a
forward event chain, not a reply tied to a single request, so none meets the bar. The rest were one-way
producers, producer-only ingest (`adevinta/vulcan-api`, `Metsuk1/bybitParser`, `dataGriff/Outbox.events`,
`znsio/scheduler-demo`), mislabeled REST apps, or spec/template/tooling/docs. This **fully exhausts the 2.x
Kafka/AMQP corpus** for the undeclared-correlation hunt — **201 candidate services** read across all buckets
(139 with an in-code request/reply signal + 62 without), the usable count holding at **11**; the only repos
left undriven are those that _declare_ a `correlationId` (a different, in-contract case) and the payload-only
transports (MQTT/WS).

Takeaways: (1) usable correlated-R/R SUTs are **more plentiful than the contract-based survey implied** —
**11** across both corpora once you read code, versus the ~2 usable-as-is among the 81 _declared_ 3.x reply
repos — but they are **almost all demos / course projects / workshops**; among real **products** only one is
usable (`PocketHive`), while the others examined (a too-heavy iPaaS, two PagoPA government services) correlate
one-way or are not clean SUTs, so real _products_ that hide R/R in code remain **vanishingly rare**. (2) **None correlate via the AsyncAPI
`correlationId` keyword** (a payload field, a native AMQP property, or an app header in every case), so
they are invisible to a contract-driven tool and surface only by reading the code — and the one repo that
_does_ surface correlation in its contract (`zilla-demos`, via a header extension / AsyncAPI 3.0 native
`reply`) is the exception that proves the rule. (3) Net: the contract is an unreliable _positive_ guide —
services correlate without declaring it (the 11), and many _declared_ replies are tooling/fixtures — so a
black-box tool must learn whether and how a service correlates by reading the implementation, not the
schema; its one reliable signal is the _negative_, since a purely one-directional spec did, in 62/62 cases,
mean one-way code.

## Payload-only transports: WebSocket & MQTT

The same code-read, repointed to the **payload-only** transports — WebSocket (no protocol-level
correlation slot; everything in the payload) and MQTT (3.1.1 payload/topic-only; 5.0 adds Correlation
Data + Response Topic). The enumerator surfaced **177 product/demo candidates** with an in-code
request/reply signal (`enum_2x_rr_all.py` with `PROTOCOLS=ws,wss,mqtt,mqtt5`); we read a curated
high-value ~48 first (naming-tier, JSON-RPC/ledger-bridge products, MQTT IoT/robotics, device-control,
turn-based games), then swept **all 126 remaining** — so **every one of the 177 candidates has now been
read** (`Navvyaa/ChatBE` was tree-only/unconfirmed). The full bulk is detailed in _The chat/streaming
bulk_ below.

Two structural facts shape the result. First, **WebSocket is bidirectional by nature**, so the
duplex/bidir signal is near-universal (126 of 177) and tells you almost nothing — most WS services are
streaming / pub-sub / broadcast (chat fan-out, game-state push, telemetry, quote streams), which is
**not** request/reply. Second, the genuine request/reply over WS is the **JSON-RPC shape**: the client
sends a request bearing an `id`, the server echoes that `id` on the response over the same socket.

Where that shape appears it is real and, strikingly, often **product-grade** — a far richer seam of
usable SUTs than Kafka/AMQP yielded:

| Repo | Transport | Correlation (as built) | Declared? | Verdict |
| --- | --- | --- | --- | --- |
| `CardanoSolutions/ogmios` (JSON-RPC bridge to a Cardano node — **real product**, 327★) | WS | payload `id` (JSON-RPC 2.0), echoed | as a **property** (`id` "mirrored back"), not `correlationId` | USABLE (clean oracle; needs a cardano-node behind it) |
| `Sofie-Automation/sofie-core` (TV-studio automation — **real product**, 341★) | WS | payload `reqid`, echoed (ping→pong, subscribe→status) | **yes**, as a property ("client-originated id reflected in response") | USABLE-WITH-CHANGES (needs Sofie/Mongo backend; ping/subscribe testable alone) |
| `jniebuhr/gaggimate` (Gaggia espresso smart control — **real product**, 834★) | WS | payload `rid` (`req:`→`res:`), echoed | **yes**, as a property | USABLE-WITH-CHANGES (ESP32 firmware; needs device/sim) |
| `kubescape/synchronizer` (k8s object sync — **real product**) | WS | payload `msgId` (getObject→putObject), echoed | **yes**, as a property | USABLE-WITH-CHANGES (point at a fake/kind cluster) |
| `RidgeRun/ridgerun-immersive-teleoperation` (robot teleop — **real commercial product**) | Socket.IO/WS | payload `uuid` (command→response), echoed | **yes**, as a property | USABLE-WITH-CHANGES (degrades gracefully without ROS2; RPC-ack style) |
| `kidoneself/DockPilot` (Docker-management UI — demo) | WS | payload `taskId` (command→progress/complete), echoed | **yes**, as a property | USABLE-WITH-CHANGES (needs a Docker daemon) |
| `phalanxduel/phalanxduel` (turn-based duel game — **product-grade**; Fastify WS + Postgres + matchmaking) | WS | `ReliableChannel`: client `msgId` echoed as `ackedMsgId` in an `ack` (+ `replyTo` on `pong`) | **yes**, as a property (`ackedMsgId`, documented) | USABLE-WITH-CHANGES (needs Postgres; ships a test socket helper) |
| `adalbertocajueiro/edscorbot-c-cpp` (robot-arm simulator — research) | MQTT 3.1.1 | echoed `client` identity + `signal` pairing; move→reply on a **different** topic | **no** | USABLE-WITH-CHANGES (hardcoded broker IP; correlation by identity, not per-request id) |
| `HexRohit/cardano` (stale ogmios fork) | WS | JSON-WSP `mirror`→`reflection`, echoed | as a property | USABLE-WITH-CHANGES (obsolete protocol; prefer ogmios) |
| `MariamElsoufyx/IMMERSA-Voice-Chat-API` (AI voice chat — demo) | WS | per-chunk `chunk_index` echoed in an `ack` (borderline) | as a property | USABLE-WITH-CHANGES (acks testable without LLM keys; ordinal, not a GUID) |

PARTIAL: `energywebfoundation/ddhub-client-gateway` (echoes a `transactionId`, but it's an idempotency key
on a relay) and `EthanSheehan/Grid-Sentinel` (real request/response pairs, but correlation is by WS
connection — no id carried). NOT request/reply (representative of the bulk): the JSON-RPC-_looking_ but
actually server-streaming/broadcast products — `cardano-scaling/hydra` (WS broadcast; its Request/Response
pairs are HTTP), `digital-asset/canton` + `canton-network/splice` (1-request→N-response server streams),
`wso2/product-microgateway` (transparent WS proxy), `bitrockteam/kafka-dvs-api` (subscription-controlled
broadcast); the IoT telemetry buses (`absmach/magistrala`, `IlijaIvanovic78/F1DataStream`,
`guilhermerodrigues680/globo-terrestre-iot`); device one-way streamers (`christian-photo/ninaAPI`,
`bang-olufsen/beoremote-halo`); and the chat/game broadcasters (`hmecruz/chat-service`, `joshwambere/Galileo`,
`Ikay14/Suxch`, `TeleGrammy/backend`, `yelaco/ludofy`, `blagoySimandov/takgo`, `Verdenroz/finance-query`,
`victorrentea/training-assistant`, plus the turn-based games `KamilMarszalek/checkers-online`, `TP-O/werewolf`,
`masechkacat/tic-tac-toe-server`, `chess-vn/slchess`, `BillyBolton/menace`, `montionugera/atlas-world-svc`,
`ciel334288/ghoulies` — authoritative game state broadcast to all players) — each fans messages out or
pushes state with no per-request id echoed.

### The chat/streaming bulk (the remaining 126 candidates)

Sweeping all 126 remaining WS/MQTT candidates confirmed the structural read — the overwhelming majority are
**broadcast / pub-sub / state-push** (room chat, game-state fan-out, collaborative editing, IoT telemetry,
quote/price streams) or are spec-only / templates / client libraries / dashboards. But the **payload-id echo
pattern recurs far more often than expected**: a sizeable minority implement a genuine correlated
request→reply by echoing a client-supplied id in a directed reply. New genuine finds (id echoed in code,
none via the `correlationId` keyword):

| Repo | Transport | Correlation (as built) | Verdict |
| --- | --- | --- | --- |
| `vdm-systems/swifty-server` (messaging relay — **product**) | WS | payload `msgid` echoed in `delivery_status`/`ack_received`/`topic_sent` | USABLE-WITH-CHANGES (JWT via `/register`; Redis optional) |
| `litmuschaos/m-agent` (CNCF Litmus chaos machine-agent — **product**) | WS | payload `reqid` echoed (e.g. `ACTION_SUCCESSFUL`) | USABLE-WITH-CHANGES (JWT; sandbox — it stresses CPU/kills procs) |
| `lxbme/E-ee` (E2E-encrypted chat — product-grade) | WS | payload `client_msg_id` echoed in `ack_required` | USABLE (docker-compose; assert on the ack — payloads are encrypted) |
| `leynos/bournemouth` (LLM graph-chat) | WS | payload `transaction_id` echoed on every stream fragment | USABLE-WITH-CHANGES (stub OpenRouter) |
| `rahul-10-byte/multi-video-conferencing-app` (mediasoup SFU signaling) | WS | payload `requestId` echoed on direct responses/acks | USABLE-WITH-CHANGES (JWT + mediasoup) |
| `germanProgq/crypto-hackathon` (sealed-bid auction) | WS | payload `requestId`: `place_bid`→`bid_result` | USABLE-WITH-CHANGES (auth + Mongo/Redis) |
| `anonymousc/ft_transcendance-42` (friends-service chat) | WS | payload `tempId`→`message_ack` (opt-in) | USABLE-WITH-CHANGES (DB/auth fixtures) |
| `ewanvidal/SimuMarty` (Marty robot 3D simulator) | WS | payload `requestId`→`commandAck` | USABLE (standalone Python — cleanest black-box of the batch) |
| `dgnsrekt/gexbot-faker-api` (GEX market-data faker) | WS | payload `ackId` echoed in `Ack` (control plane only; data is streamed) | USABLE (deterministic ack echo) |
| `hasathcharu/ballerina-websockets-test` (Ballerina WS tooling) | WS | payload `id` echoed; `Chat` is `simple-rpc` (declared via `x-dispatcherStreamId`) | USABLE (needs Ballerina toolchain) |
| `d1m1tur/PGJ-2026` (game-jam lobby) | WS | payload `requestId`→`RoomJoinAck`/`LobbyList` | USABLE-WITH-CHANGES (toy) |
| `kyleczhang/cits5506-iot-parkreserve-group29` (parking reservation) | **MQTT** | command→event ack correlated by `reservation_id`/`event_id` (backend↔Raspberry Pi) | USABLE-WITH-CHANGES (two deployables + broker; well-tested) |
| `carlosquintino/realtime-iot-decisioning` (agri closed-loop on Magistrala) | **MQTT** | observation↔command correlated by SenML timestamp `t` | USABLE-WITH-CHANGES (stub the LLM; run Magistrala) |

Plus three **`jniebuhr/gaggimate` forks** carrying the identical `rid` echo (`dulerabbit/GaggiBre`,
`Velkromod/gaggimate-feature-gearpump`, `…-Modded-MPC`).

Near-misses / out of scope: `henrykey/kone-elevator` + `faraz7321/robot-elevator-middleware` correlate by
`requestId` but only as **clients** of KONE's external cloud (the responder isn't in the repo) — not usable.
`mattbishop/asyncapi-hotels` deliberately models CQRS `commandId`/`causationId`/`correlationId` **headers**
but ships no implementation. Several have directed replies correlated only by **socket / event-name / a
shared domain id, with no per-request id echoed** (`zimoch84/HaggisProject` — the cleanest req/resp _design_,
but no id; `music10/server`, `imaksb/quizy`, `kasrasabertehrani/mancala`, `one-2-one/task-manager`,
`jpxcz/websocket_template_nodejs`) — these fail the bar. `caochun/tollgate` is a genuine correlated reply
but over **AMQP**, out of this transport's scope. Everything else (the large remainder) is broadcast / pub-sub
/ telemetry / streaming, spec-only, template/codegen, client-library, or dashboard.

Two findings stand out. (1) **The payload-only transports are by far the richest seam of correlated-R/R
SUTs** in the whole corpus — reading every candidate turns up **more than two dozen** genuine correlated
request/reply services over WS/MQTT (≈10 product-grade: ogmios, sofie-core, gaggimate, kubescape/synchronizer,
RidgeRun, phalanxduel, swifty-server, m-agent, `lxbme/E-ee`, …) versus the lone usable product (PocketHive)
across all of Kafka/AMQP. The scarcity was a Kafka/AMQP phenomenon: over WebSocket, JSON-RPC / payload-id
correlation is a natural, common pattern, so request/reply is plentiful — just never spelled with the schema
keyword. (2) **Yet not one uses the AsyncAPI `correlationId` keyword.** The contrast with Kafka/AMQP is instructive: there correlation
was usually hidden in the code; here it is usually **documented in the spec — but as an ordinary payload
property (`id`/`reqid`/`msgID`/`taskId`/`uuid`), never via the formal `correlationId` construct**. Either
way a black-box tool that keys off `correlationId` finds nothing; it must take the id from the message
payload schema (when documented) or the code (when not).

**The no-hint pass (one-directional WS/MQTT specs).** For completeness we also swept the **71 WS/MQTT
services whose AsyncAPI is purely one-directional** (no reply op, no duplex, no bidirectional ops) and
declares no `correlationId` — the schema gives zero hint, so the question is whether the code correlates
anyway (`enum_2x_rr_all.py SIGNAL=nohint`). As with Kafka/AMQP, the answer is **almost always no**: these
are one-way sensor telemetry, server-push notifications, streaming feeds, REST-request/WS-push splits, or
spec-only / tooling / doc repos. Only two edge cases correlate in code, and each sits at the survey's
boundary: **`btc-vision/opnet-node`** (an OP_NET Bitcoin smart-contract node — **real product**) runs a
genuine per-request reply echoing a 4-byte **binary `requestId`**, but over a custom protobuf/opcode wire
with no AsyncAPI document describing it; and **`officialdavidtaylor/leftover-label-printer`** (MQTT)
correlates `PrintJobCommand`→`PrintJobOutcome` by an echoed `jobId`, but its spec actually declares
**both** channels (the one-directional heuristic mis-bucketed it on 2.x's ambiguous `publish`/`subscribe`
verbs). `netbill/auth-svc` is a PARTIAL — its WS QR-login is correlated by a QR token, but the confirming
request comes over REST and the spec shows only the one-directional half. The takeaway holds across
**both** transport families: a purely one-directional AsyncAPI spec is a **reliable negative** — it
almost always means one-way code (and, notably, neither edge-case find uses the `correlationId` keyword
either).

## Per-repo verdicts (all passes)

A consolidated, at-a-glance index of **every individually code-read repository** across all passes — the
39 3.x `receive`+`reply` candidates, the 2.x (and cross-corpus) Kafka/AMQP code-reads, and the
WebSocket/MQTT code-reads. The thematic tables earlier in this file carry the correlation mechanics and
full evidence; this section is the flat lookup. Verdict key: **USABLE** (real correlated R/R, clean-ish
standup) · **USABLE-WITH-CHANGES** (real R/R code, needs containerizing / dep-stubbing / correlation or
licence fixes) · **PARTIAL** (R/R only half-implemented) · **NOT-USABLE** (one-way/broadcast, no
implementation, tooling/spec/docs, wrong transport, or hard external deps). Counts across everything
read: roughly **12 USABLE + ~48 USABLE-WITH-CHANGES + ~9 PARTIAL** (the rest NOT-USABLE) — but only
~10 are product-grade; the great majority are demos, course projects, or workshops.

### 3.x `receive`+`reply` candidates — usable with minimal effort (2)
| Repo | Class | Why |
| --- | --- | --- |
| VoiceBlender/voiceblender | product | Go WS VSI; spec generated from code; Dockerized; `request_id` correlation; core needs no DB |
| specmatic/enterprise-sample | demo | Kotlin Kafka R/R; echoes a `correlationId` Kafka-header field in code (no formal `correlationId.location`); MIT; `docker compose up` |

### 3.x `receive`+`reply` candidates — usable with real work (~17)
| Repo | Class | Transport | Blocker → change needed |
| --- | --- | --- | --- |
| EVerest/EVerest | product | MQTT | heavy EVerest-specific stack; run one `*_API` module + MQTT + config |
| gematik/zeta-testfachdienst | product | STOMP/WS | write a STOMP client; correlation is `@SendToUser` session routing (no declared id); Apache-2.0 |
| gopal45656/everest-core-release | product | MQTT | EVerest copy — prefer canonical upstream |
| dduartee/sigaa-socket-api | product | WS (Socket.IO) | needs live SIGAA → stub the scraper layer; GPL-3.0 |
| wohnheim/stueble | product | WS (MessagePack) | Nix-only build, Postgres+keys+email → containerize+stub; **no license** |
| aklivity/todo-service | uncategorized | Kafka | real `zilla:correlation-id` R/R; drive raw Kafka or add Zilla; **non-OSI license** |
| metalalive/e_commerce | demo | AMQP | external RabbitMQ network + MariaDB + Liquibase + `secrets.json`; AMQP `correlation_id` echoed; MIT |
| specmatic/specmatic-arazzo-…-sample | demo | Kafka | turnkey compose; **add license** |
| specmatic/specmatic-kafka-avro-sample | demo | Kafka+Avro | needs Schema Registry; correlation via key; **no license** |
| specmatic/specmatic-kafka-sample-asyncapi3 | demo | Kafka | **un-hardcode** correlation id (`"12345"`); **no license** |
| specmatic/specmatic-async-sample | demo | AMQP/MQTT | pin a transport; verify correlation echo; **no license** |
| znsio/specmatic-async-order-api-kotlin | demo | Kafka | it's the *requester* — supply a real responder (reply side is a mock); MIT |
| eclipse-uprotocol/symphony-target-example-rust | demo | MQTT5/uProtocol | build a uProtocol client to frame requests; Apache-2.0 |
| Eclipse-SDV-Hackathon-…/Den-Team | demo | MQTT5/uProtocol | same Rust uService embedded; uProtocol client needed |
| CodingFlow/rating-service-dotnet | demo | NATS | k8s-coupled → local compose (NATS+PG+Redis); **no license** |
| ambihome-gmbh/asyncapi | demo | MQTT | experimental/toy; add a service entrypoint + explicit correlation; MIT |
| sillygod/scaffold | demo | WS | cookiecutter template; instantiate + fix TODO'd dispatch; MIT |
| huynguyengl99/chanx-fastapi-tutorial | demo | WS | real FastAPI WS R/R; **no license**; WS transport |
| specmatic/aws-lambda-kafka-with-localstack | demo | Kafka | lift handler out of Lambda/LocalStack (paid token); **no license** |

### 3.x `receive`+`reply` candidates — not usable (of the 39)
| Repo | Class | Why not |
| --- | --- | --- |
| Netcracker/qubership-integration-platform | product | spec is an unrelated parser fixture; K8s/Consul/PG |
| Netcracker/qubership-integration-runtime-catalog | product | archived; same fixture; no R/R impl |
| acidtango/ollert-backend | product | broadcasts events, not a correlated reply; no license; dormant |
| BackendFans83/Taxi | product | docs-only, **zero source** (has Apache-2.0, but nothing to run); spec is gRPC |
| Jack-the-Pro101/vequate | product | GCP Pub/Sub (not Redis); no correlation; no license |
| stardew-valley-dedicated-server/web | product | WS relay/broadcast, not R/R; placeholder spec |
| davidtgillard/fits | product | library only; RPC server "planned"/elsewhere |
| adreno255/nurtura-backend | product | ack-by-event-name (no correlation); Firebase-gated; UNLICENSED |
| CodeBeast357/webosapi-asyncapi | uncategorized | spec-only; copied Kraken sample |
| Shurtu-gal/action-test-bed | uncategorized | CI fixture; Kraken sample |
| aklivity/zilla-demos | demo | reply is Zilla broker config, not a service (real consumer is `aklivity/todo-service`) |
| specmatic/studio-demo | demo | mock/docs only; no service code |
| Integration-Project-2026-Groep-2/CRM | demo | **real correlated `requestId` reply in code**, but gated by a hard live-Salesforce dependency (receiver won't start without SF login) + no license |
| codemonstersteam/mq-rest-sync-adapter | demo | IBM MQ (not AMQP); needs external REST; teaching snapshot |
| specmatic/specmatic-studio-playwright-ts-tests | demo | Playwright UI tests; no service |
| specmatic/labs | demo | spec + Specmatic virtualization; no app code |
| Forsakringskassan/template-asyncapi | demo | empty Gradle template |
| zuevrs/yanote | demo | coverage-analysis tool; the "specs" are its test fixtures |

### Beyond the 39 — 2.x Kafka/AMQP code-reads
The six passes above code-read **201 candidate services** on Kafka/AMQP across both corpora (see _Beyond
the 39_). Genuine finds, partials, and the named negatives:

**Usable / usable-with-changes (genuine correlated R/R, none via the `correlationId` keyword):**
| Repo | Transport | Verdict | Correlation / note |
| --- | --- | --- | --- |
| `ldynia/learning-api-styles` | AMQP | USABLE | native `correlation-id`/`reply-to` RPC; MIT; compose (TLS off) |
| `caiquedebrito/logistics-platform` | AMQP | USABLE | payload `correlationId`/`deliveryId` echoed; Dockerized |
| `joass1/ESD-Ticket-booking` | AMQP | USABLE | payload `waitlist_entry_id` echoed; Dockerized |
| `Alex009/architecture-sprint-3` | Kafka | USABLE | payload `deviceId` echoed; docker-compose; most product-grade demo |
| `ChunPingWang/saga-kafka` | Kafka | USABLE | payload `orderId` echoed; 3-service saga |
| `ldynia/rabbitmq` | AMQP | USABLE-WITH-CHANGES | native `correlation_id`/`reply_to` (tutorial-six RPC); TLS default; bare-int body |
| `vincenzocorso/car-sharing` | Kafka | USABLE-WITH-CHANGES | header `correlation_id` echoed; heavy (Debezium/Kafka/Temporal) |
| `sepa79/PocketHive` | AMQP | USABLE-WITH-CHANGES | payload `correlationId` (control plane); **the only product-grade Kafka/AMQP find**; multi-module build |
| `tsurdilo/async-demo` | Kafka | USABLE-WITH-CHANGES | payload `transactionId` echoed; spec/code topic drift; drive Spring `banking-service` |
| `fmvilas/workshop-ride-app` | Kafka | USABLE-WITH-CHANGES | payload `rideId` echoed; decouple from Slack/Netlify/CloudKafka |
| `AceTheCreator/simple-commerce` | AMQP | USABLE-WITH-CHANGES | native `correlationId` header + `reqId` payload; multi-service standup |

**Partial:**
| Repo | Transport | Note |
| --- | --- | --- |
| `HenderOrlando/booklyapp` | Kafka+AMQP | fully-coded correlated *requester*; responder half unimplemented |
| `WebFuzzing/Dataset` | Kafka | one real R/R (`familie-tilbake`→`familie-ba-sak`, record-key UUID) across **two** SUTs; profile-gated; no AsyncAPI |
| `somosphi/ts-seed-jest` | AMQP | find-user→publish reply tied only by an echoed `id`; committed spec is the stock Streetlights sample |

**Real products examined — not usable:**
| Repo | Transport | Why not |
| --- | --- | --- |
| `Netcracker/qubership-integration-platform` | Kafka/AMQP | iPaaS; correlation authored per integration chain, not intrinsic; AsyncAPI files are importer fixtures; heavy (Consul/Kafka/PG/UI) |
| `pagopa/idpay-reward-calculator` | Kafka | gov product; one-way; reply keyed by `userId`; payload `correlationId` is an upstream passthrough |
| `pagopa/idpay-onboarding-workflow` | Kafka+ASB | gov product; one-way; request to a *different* service over Service Bus; Mongo-lookup matching |

**Not usable — one-way / not-a-service (grouped; every named negative):**
| Reason | Repos |
| --- | --- |
| One-way event streaming / choreography / producer-only | `kaje94/slek-link`, `ClearEyesFullHearts/mft`, `gsperim/account-engine-lab`, `cibanezb95STG/quoteAssessmentCIB` (Azure SB; *declares* a correlationId), `JLanders96/abw-processor` (Cloudflare Queues; HTTP replies), `ibm-cloud-architecture/vaccine-freezer-mgr`, `n-bolanos/FastEventManager`, `Brico87/event-gateway`, `LingshijunRenzy/ICS-guard-next`, `rvasqz86/manufacturing-mes-streaming-aggregate`, `nesaa-a/SPDD-EventSystem`, `David-DAM/spring-boot-async-template-ultimate`, `arih1299/solacedemo-kafkasummitapac2021`, `aimerzarashi/ts-cqrs-es-v1`, `nandorsilva/asyncapi-demo`, `baldimir/kie-backend`, `tayyabfayyaz/hakathon_2`, `funny-bunny-corp/payment-executor`, `funny-bunny-corp/ledger`, `funny-bunny-corp/payment-service`, `naomesh/naomesh-onion-orchestrator`, `naomesh/naomesh-web-api`, `EvenToNight/EvenToNight`, `999iQ/networking`, `XerxesDGreat/tt-notif-service`, `karlosdaniel451/message-chat`, `raulgonzalezdev/eda-backend-plus`, `jhoncastro28/saga-choreography`, `robev2252060/2247107_MAP`, `pfarkya/asyncApi_AccountManagerEDA`, `mariacolab/einzelhandel`, `gregoriocarranza/APPS-II-Core-Backend`, `yoshioterada/Spec-Driven-Dev`, `alexandramartinez/asyncapis-accounts-email`, `nandorsilva/arc-dados`, `Labdata-FIA/Engenharia-Dados`, `adevinta/vulcan-api`, `Metsuk1/bybitParser`, `dataGriff/Outbox.events`, `znsio/scheduler-demo` |
| Forward-saga choreography — echoes a business id across stages, but no reply tied to one request (no-hint near-misses) | `lok-hit/CarRentalApp`, `mnabli94/ecommerce-microservices`, `zdmooc/TradeOps-GenAI-Integration`, `ChiragSethi-1153/RMHA`, `Lynda1423/gestion-vehicules` |
| Not a runnable service (no broker code / fork / GitOps / Dapr / template) | `bcwilsondotcom/nx-monorepo-template`, `Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i`, `Netcracker/qubership-integration-runtime-catalog`, `SebastianBorchardt1984/incubator-kie-kogito-runtimes`, `baldimir/kie-frontend`, `kurtrisley/DemoEventDrivenService`, `kurtrisley/EventDrivenServices`, `paulCormierProgressive/EventDrivenServices`, `specmesh/getting-started-apachekafka`, `specmesh/helloworld-demo`, `GUR-ok/otus-microservice-architecture`, `leopcaraballo/RLApp-V2`, `Archi-Lab-FAE/fae-team-2-service`, `BakangMonei/PolyGlot-Demo-Examples`, `parmendes/MessageBrokerExample`, `rakeshmani35/springboot-openAPI` |
| AsyncAPI examples / tutorials / codegen collections (not services) | `bump-sh/examples`, `meteatamel/asyncapi-basics`, `enisspahi/async-api-example`, `mzegarras/asyncapi-labs`, `coiouhkc/asyncapi-generator-examples`, `ueisele/showcase-asyncapi-api`, `edwmurph/api-docs`, `atharvagadkari05/template_EDA_API`, `ZiyamSanthosh/AsyncApiAmf`, `ninkovski/bootcamp-back-util-api-contracts`, `invivo-digital-factory/openapi-compiler-ts` |

(`aklivity/zilla-demos`: declared `zilla:correlation-id` R/R, but the reply is Zilla broker config — the real consumer is `aklivity/todo-service`, listed under the 3.x candidates above.)

### Payload-only transports — WebSocket & MQTT code-reads
177 signal candidates + 71 no-hint, **all read** (see _Payload-only transports_). WebSocket is
bidirectional by nature, so most are streaming/broadcast; genuine request/reply uses a JSON-RPC-style
echoed payload id. This is the **richest seam of correlated-R/R SUTs in the corpus** (~10 product-grade).

**Usable / usable-with-changes (genuine correlated R/R; id documented as a payload property, never as `correlationId`):**
| Repo | Transport | Verdict | Correlation / note |
| --- | --- | --- | --- |
| `CardanoSolutions/ogmios` | WS | USABLE | JSON-RPC `id` echoed; **real product** (327★); needs a cardano-node behind it |
| `ewanvidal/SimuMarty` | WS | USABLE | payload `requestId`→`commandAck`; standalone Python — cleanest black-box |
| `lxbme/E-ee` | WS | USABLE | payload `client_msg_id`→`ack_required`; E2E chat; docker-compose |
| `dgnsrekt/gexbot-faker-api` | WS | USABLE | payload `ackId` echoed (control plane); deterministic |
| `hasathcharu/ballerina-websockets-test` | WS | USABLE | payload `id` echoed; `simple-rpc`; needs Ballerina toolchain |
| `Sofie-Automation/sofie-core` | WS | USABLE-WITH-CHANGES | payload `reqid` echoed; **real product** (341★); needs Sofie/Mongo |
| `jniebuhr/gaggimate` | WS | USABLE-WITH-CHANGES | payload `rid` echoed; **real product** (834★); ESP32 firmware |
| `kubescape/synchronizer` | WS | USABLE-WITH-CHANGES | payload `msgId` echoed; **real product**; point at a fake/kind cluster |
| `RidgeRun/ridgerun-immersive-teleoperation` | Socket.IO/WS | USABLE-WITH-CHANGES | payload `uuid` echoed; **real commercial product**; degrades w/o ROS2 |
| `phalanxduel/phalanxduel` | WS | USABLE-WITH-CHANGES | `ReliableChannel` `msgId`→`ackedMsgId`; product-grade game; needs Postgres |
| `vdm-systems/swifty-server` | WS | USABLE-WITH-CHANGES | payload `msgid` echoed; messaging-relay **product**; JWT+Redis |
| `litmuschaos/m-agent` | WS | USABLE-WITH-CHANGES | payload `reqid` echoed; **CNCF product**; sandbox (it stresses CPU) |
| `leynos/bournemouth` | WS | USABLE-WITH-CHANGES | payload `transaction_id` echoed per fragment; LLM chat; stub OpenRouter |
| `rahul-10-byte/multi-video-conferencing-app` | WS | USABLE-WITH-CHANGES | payload `requestId` echoed; mediasoup; JWT |
| `germanProgq/crypto-hackathon` | WS | USABLE-WITH-CHANGES | payload `requestId`: place_bid→bid_result; auth+Mongo/Redis |
| `anonymousc/ft_transcendance-42` | WS | USABLE-WITH-CHANGES | payload `tempId`→`message_ack`; DB/auth fixtures |
| `d1m1tur/PGJ-2026` | WS | USABLE-WITH-CHANGES | payload `requestId`→`RoomJoinAck`/`LobbyList`; toy |
| `kidoneself/DockPilot` | WS | USABLE-WITH-CHANGES | payload `taskId` echoed; needs a Docker daemon |
| `MariamElsoufyx/IMMERSA-Voice-Chat-API` | WS | USABLE-WITH-CHANGES | per-chunk `chunk_index` ack (borderline) |
| `HexRohit/cardano` | WS | USABLE-WITH-CHANGES | JSON-WSP `mirror`→`reflection`; stale ogmios fork |
| `adalbertocajueiro/edscorbot-c-cpp` | MQTT 3.1.1 | USABLE-WITH-CHANGES | echoed `client` identity + signal; robot-arm sim; hardcoded broker IP |
| `kyleczhang/cits5506-iot-parkreserve-group29` | MQTT | USABLE-WITH-CHANGES | command→event ack by `reservation_id`/`event_id`; two deployables |
| `carlosquintino/realtime-iot-decisioning` | MQTT | USABLE-WITH-CHANGES | observation↔command by SenML `t`; on Magistrala; stub the LLM |
| `officialdavidtaylor/leftover-label-printer` | MQTT | USABLE-WITH-CHANGES | `PrintJobCommand`→`PrintJobOutcome` echoed `jobId`; needs broker + agent |
| `btc-vision/opnet-node` | WS | USABLE-WITH-CHANGES | binary `requestId` echoed; **real product**; custom protobuf/opcode wire (no AsyncAPI) |
| `dulerabbit/GaggiBre`, `Velkromod/gaggimate-feature-gearpump`, `…-Modded-MPC` | WS | USABLE-WITH-CHANGES | `gaggimate` forks; identical `rid` echo |

**Partial / out of scope:**
| Repo | Note |
| --- | --- |
| `energywebfoundation/ddhub-client-gateway` | echoes a `transactionId`, but it's an idempotency key on a relay |
| `EthanSheehan/Grid-Sentinel` | real request/response pairs, but correlated by WS connection — no id carried |
| `netbill/auth-svc` | WS QR-login correlated by a QR token, but the confirm is REST; spec one-directional |
| `henrykey/kone-elevator`, `faraz7321/robot-elevator-middleware` | correlate by `requestId` but only as **clients** of KONE's external cloud |
| `caochun/tollgate` | genuine correlated reply, but over **AMQP** (out of this transport's scope) |
| `mattbishop/asyncapi-hotels` | deliberately models CQRS correlation headers, but ships no implementation |

**Not usable — streaming / broadcast / not-a-service (grouped; named negatives):**
| Reason | Repos |
| --- | --- |
| JSON-RPC-looking but server-streaming / proxy products | `cardano-scaling/hydra` (pairs are HTTP), `digital-asset/canton`, `canton-network/splice`, `wso2/product-microgateway` (WS proxy), `bitrockteam/kafka-dvs-api` |
| IoT telemetry / device one-way streamers | `absmach/magistrala`, `IlijaIvanovic78/F1DataStream`, `guilhermerodrigues680/globo-terrestre-iot`, `christian-photo/ninaAPI`, `bang-olufsen/beoremote-halo` |
| Chat / game / collab broadcasters (fan-out, no per-request id) | `hmecruz/chat-service`, `joshwambere/Galileo`, `Ikay14/Suxch`, `TeleGrammy/backend`, `yelaco/ludofy`, `blagoySimandov/takgo`, `Verdenroz/finance-query`, `victorrentea/training-assistant`, `KamilMarszalek/checkers-online`, `TP-O/werewolf`, `masechkacat/tic-tac-toe-server`, `chess-vn/slchess`, `BillyBolton/menace`, `montionugera/atlas-world-svc`, `ciel334288/ghoulies` |
| Directed reply but correlated only by socket / event-name (no per-request id) | `zimoch84/HaggisProject`, `music10/server`, `imaksb/quizy`, `kasrasabertehrani/mancala`, `one-2-one/task-manager`, `jpxcz/websocket_template_nodejs` |

The remaining WS/MQTT bulk (~120 of the 177) and the 71 no-hint repos are overwhelmingly
broadcast/streaming/telemetry, spec-only, templates, or tooling; they are named individually in _The
chat/streaming bulk_ and _The no-hint pass_ above and are not re-listed here.

## The 42 tools and specs (category disposition)

**Tooling/library (30)** — generators (`asyncapi/generator`, `lerenn/asyncapi-codegen`,
`the-codegen-project/cli`, `asyncapi/jasyncapi`, `dghilardi/asyncapiv3`), validators/parsers
(`WaleedAshraf/asyncapi-validator`, `insspb/asyncapi3`, `G-USI/asyncapi-python`), CLIs/IDEs
(`Redocly/redocly-cli`, `specmatic/specmatic`, `asyncapi/studio`), mocking/testing tools
(`microcks/microcks`), and WS frameworks (`huynguyengl99/chanx`, `RobinTail/zod-sockets`). **Not
SUTs**: their reply-pattern specs are test fixtures or generated examples, not a running product
service. Usable only as **contract inputs**. (Framework repos like `chanx`/`zod-sockets` can
*generate* a runnable WS service, but that is a synthetic example, not a real-world SUT — and we
already have synthetic SUTs.)

**Spec/docs (12)** — the repo *is* a spec or docs set: `asyncapi/spec`, `asyncapi/website`,
`OAI/Arazzo-Specification`, `specmatic/*-contracts`, `simliai/docs`, `coinpaprika/coinpaprika-docs`,
etc. **Not SUTs**; usable only as **reference contracts** (and several host the adeo-kafka example).

## Bottom line for the thesis

- The synthetic **NCS SUTs remain the evaluation backbone** — controlled, clean declared
  correlation, all four transports, redistributable. The corpus does not provide a comparable set.
- For **external validity**, lift 2–3 real services from the shortlist, prioritising licensing and
  transport spread: **specmatic/enterprise-sample** (Kafka, MIT, declared correlation),
  **metalalive/e_commerce** (AMQP, MIT), and **voiceblender** (WS, MIT) or **EVerest** (MQTT,
  Apache-2.0) — each requiring the standard "containerize + stub deps + confirm correlation" work
  above.
- The read also produced **problem-domain evidence** worth citing: most reply-pattern repos are not
  runnable services; correlation is frequently broadcast/ad-hoc/hardcoded/broker-specific rather
  than a clean declared `correlationId`; and contracts drift from implementations (transport
  mismatches, borrowed sample specs). These reinforce the gaps catalogued in `proposal-problems.md`.
