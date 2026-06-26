# Black-Box Testing of AsyncAPI Services in EvoMaster

This proposal asks whether EvoMaster, an automated test generator, can test **AsyncAPI** services as a
black box. It proceeds in two parts. The **problem**: why asynchronous messaging breaks REST's
request/response assumptions, which interactions are observable at all (only **request/reply**), how
often that pattern occurs in the wild (a corpus survey — rarely, and mostly in tooling), how the four
dominant transports each carry the correlation a reply needs, and whether the real services that do it
are usable as systems under test (largely not). The **approach**: reuse EvoMaster's black-box engine by
making the **reply message a synthesized status code**, drive every transport through a thin,
protocol-agnostic boundary, and ground it in controlled SUTs. The companion `corpus-suitability.md`
holds the full per-repository evidence behind the survey.

## What is AsyncAPI

AsyncAPI is an open specification for describing **asynchronous, event-driven APIs** — the
counterpart of OpenAPI (formerly Swagger) for systems that communicate through message brokers and
event-streaming platforms instead of synchronous HTTP. An AsyncAPI document declares:

- **Channels** — the topics, queues, or routing keys where messages flow (e.g. `orders/created`).
- **Operations** — what the application does with a channel. In AsyncAPI 3.0 these are top-level and
  typed as `send` / `receive`, and a request can declare a paired `reply`.
- **Messages** — the structure of the data exchanged, defined with **JSON Schema**.
- **Servers** — broker connection details (URL, protocol, authentication).
- **Protocol bindings** — the transport that carries the messages (Kafka, MQTT, AMQP, WebSocket, …).

The relevant version distinction is **2.x vs 3.0**. AsyncAPI 2.x expresses operations as
`publish`/`subscribe` blocks _inside_ each channel and has no first-class reply concept — request/
reply is only expressible by convention (a request on one channel, a response on another, linked by
a `correlationId`). AsyncAPI **3.0** lifts operations to the top level and introduces a first-class
`reply:` field. Because that reply is what makes an interaction observable from the outside,
**AsyncAPI 3.0 is the version that matters for black-box testing**.

## Differences from REST-based black-box testing

### Asserting over responses

REST is **symmetric**: EvoMaster sends an HTTP request (the trigger), the system under test (SUT)
processes it synchronously, and an HTTP response (status code, body, headers) comes back in the same
cycle. The trigger and the feedback are one round-trip, so there is always something to assert on.

Asynchronous messaging is **decoupled**: a published message is consumed and processed later, and in
many designs there is **no response at all** — the broker only acknowledges _delivery_, not
_processing_. This produces a _fundamental asymmetry_ in what black-box testing can reach:

| AsyncAPI declaration | SUT role                              | EvoMaster's role                    | What we can test                                                           |
| -------------------- | ------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------- |
| `receive` (3.0)      | **Consumer** — reads from the channel | **Publisher** — sends test messages | **Directly** triggers the SUT's consumer code (a PUBLISH action)           |
| `send` (3.0)         | **Producer** — writes to the channel  | **Subscriber** — observes output    | **Observation only** — cannot trigger; can only assert on emitted messages |

| Aspect            | REST API                             | AsyncAPI                                                   |
| ----------------- | ------------------------------------ | ---------------------------------------------------------- |
| Request/response  | Synchronous — request, then response | Decoupled — broker ACKs delivery; a response may not exist |
| Timing            | SUT processes during the HTTP call   | SUT consumes and processes later                           |
| Observable signal | Status code, response body, headers  | Output messages on other channels; side effects            |

The signals available to assert on are therefore the externally observable ones: message _delivery_
(ok / fail), whether a reply _arrives_ at all, and — when one does — whether it _conforms to the
declared reply schema_ (field presence, enum membership, numeric boundaries, correlation match).

### Different asynchronous protocols

In REST and GraphQL the underlying wire protocol is **fixed**: it is always HTTP. AsyncAPI is not a
protocol — it is an **architectural concept** for asynchronous communication that can be realized
over many _incompatible_ transports: Kafka, MQTT, WebSocket, AMQP, or bespoke protocols layered on
plain sockets. Kafka's consumer-group offsets, MQTT's QoS levels, AMQP's exchange routing, and a
raw WebSocket frame have nothing in common at the API level.

The practical consequence is that **a transport client must exist for any generated test to run** —
either the tool or the developer using it has to provide the code that actually connects to the
broker and publishes/consumes. There is no single wire to target, the way REST always has HTTP.

## The observable subset: request/reply

The asymmetry above has a sharp consequence for what black-box testing can even attempt. A
_fire-and-forget_ consume operation gives the tester nothing to assert on — publishing into it is
"publishing into a void", indistinguishable from a message that was silently ignored. Only a
**request/reply** interaction carries a signal observable from the outside without instrumentation:
the reply is the AsyncAPI analogue of REST's response, and it is what lets a tester tell "the SUT
processed this" from "the SUT dropped this". In AsyncAPI 3.0 that pattern is an operation with
`action: receive` and a paired `reply:` (2.x has no first-class reply at all).

The natural question, then, is how often that observable pattern actually occurs in real AsyncAPI
specs, and over which transports. To find out, we surveyed the **public AsyncAPI corpus** on GitHub —
both major versions. Each version is measured by its own native signal: in **3.0**, the structural `receive`+`reply`; in **2.x**,
which has no reply construct, a message **`correlationId`**. Using GitHub code search we enumerated and
parsed every discoverable document (versions 2.0–2.6 and 3.0.0 / 3.1.0), attributed each hit's transport
from its servers and bindings, and classified every repository as **product**, **tool/library**,
**demo/fixture** or **spec/docs** by deterministic rules plus an LLM refinement pass. (Full method,
scripts and output are in the appendix and under `asyncapi-survey/`.)

**The corpus at scale.** The survey parsed **4,151 AsyncAPI 3.x specs** (across **984** repositories)
and **2,701 AsyncAPI 2.x specs** (of 3,189 candidates, across **1,108** repositories, 1,103 still
resolvable). Classified by
kind — a baseline for how AsyncAPI is used at all, before narrowing to request/reply:

| Repository kind                                         | 3.x repos | 2.x repos |
| ------------------------------------------------------- | --------: | --------: |
| product — real deployable apps / services               |       262 |       296 |
| demo / fixture — examples, tutorials, student/book code  |       261 |       322 |
| tool / library — generators, parsers, SDKs, validators   |       183 |       198 |
| spec / docs — the repo _is_ a spec / schema set / docs   |        97 |        85 |
| _tangential_ (excluded — incidental / AI-agent matches)  |        56 |        92 |
| _catalog_ (excluded — API directories)                  |        48 |         0 |
| _uncategorized_ (no readable metadata)                  |        77 |       110 |
| **total**                                               |   **984** | **1,103** |

**product** and **demo/fixture** are the two largest kinds in each version, so AsyncAPI overall is used
about as much for real services as for teaching and examples.

**Protocols across the whole corpus.** Of the specs that name a transport — **1,397 of 4,151 in 3.x**
and **1,627 of 2,701 in 2.x** (the rest are transport-agnostic) — four lead **both** versions:
**Kafka** (the most spec-dense), **WebSocket** (the most widely adopted by repository), **MQTT** and
**AMQP**; a long tail of single-digit-to-low-20s transports follows (NATS, Redis, SQS, Solace, Google
Pub/Sub, …; full list in the appendix). These four — detailed in **The four transports and their
correlation** below — are the ones worth pursuing.

| Protocol                 | 3.x (specs / repos) | 2.x (specs / repos) |
| ------------------------ | ------------------: | ------------------: |
| Kafka                    |           393 / 193 |           472 / 201 |
| WebSocket (`ws`)         |           229 / 203 |           459 / 250 |
| MQTT                     |           219 / 116 |           281 / 127 |
| AMQP                     |           173 / 107 |           228 / 106 |
| WebSocket-secure (`wss`) |           218 / 173 |           140 / 112 |
| HTTP                     |           179 / 110 |            145 / 81 |
| Amazon SQS               |             65 / 34 |              11 / 9 |
| Solace                   |              15 / 1 |             58 / 13 |
| IBM MQ                   |               9 / 9 |              44 / 7 |
| NATS                     |             42 / 29 |             31 / 27 |
| Amazon SNS               |             34 / 30 |              23 / 9 |
| Redis                    |             20 / 14 |             23 / 19 |

**The observable signal, by version.** Both versions land at almost the same rarity. In **3.x**,
**122 specs across 81 repositories** (~2.9% of parsed specs) declare at least one `receive`+`reply`
operation — **356 operations** in all. In **2.x**, **55 specs across 36 repositories** (2.0%) declare a
`correlationId`; but it almost always rides in a **header** (46 specs) on **one-way events**, pointing at
tracing/business keys (`transactionId`, `traceId`), and only **9 of the 55** show any request/reply
shape — so in 2.x the construct serves **distributed tracing, not reply-pairing**. The two are different
signals — 3.x structural reply operations vs 2.x correlation-id presence — so the per-transport counts
below are reported per version, not merged (`—` means none found):

| Protocol                 | 3.x `receive`+`reply` (ops / specs / repos) | 2.x `correlationId` (specs / repos) |
| ------------------------ | ------------------------------------------: | ----------------------------------: |
| Kafka                    |                                27 / 24 / 20 |                             19 / 18 |
| AMQP                     |                                  13 / 6 / 6 |                             23 / 18 |
| MQTT                     |                                 31 / 15 / 5 |                               7 / 7 |
| WebSocket (`ws`)         |                                 73 / 11 / 9 |                                   — |
| WebSocket-secure (`wss`) |                                  11 / 5 / 6 |                                   — |
| HTTP †                   |                                  18 / 9 / 6 |                               4 / 4 |
| Amazon SQS               |                                   8 / 6 / 4 |                                   — |
| Google Pub/Sub           |                                   4 / 2 / 2 |                                   — |
| STOMP                    |                                   3 / 1 / 1 |                                   — |
| NATS                     |                                           — |                               1 / 1 |
| Redis                    |                                   2 / 2 / 1 |                               1 / 1 |
| _undetermined_           |                                     186 ops |                                   — |

The header-carrying brokers — **Kafka, AMQP and MQTT** — dominate both, which is exactly where a
correlation id has somewhere to live. (Both columns are per-protocol breakdowns, not summands: the
**81 repositories** and **356 operations** are counted directly over distinct repos and operations. The
per-protocol counts both _overlap_ — one operation or repo can touch several protocols — and _omit_ the
**186** _undetermined_ operations, whose **transport-agnostic** specs declare no server or binding and so
appear in no row. So the operation counts run above 356, while the repository column falls short of 81.)

† The **HTTP** reply ops are synchronous request/response modeled with AsyncAPI's HTTP binding —
observably plain **REST**, already covered by EvoMaster's native HTTP mode, and all tooling or demo
fixtures, **no products**.

**Classifying the 81 reply repositories.** Counting how often the pattern occurs is not the same as
knowing _who_ writes it — a real service, or a mere example. So we ran the same classifier used for the
whole corpus above (the product / tool-library / demo-fixture / spec-docs scheme, deterministic rules
plus an LLM pass) over the 81 repositories that declare a `receive`+`reply` operation; the breakdown —
and the **13 products** it yields — is:

| Repository kind |  repos | examples (with reply transport)                                                                                                                   |
| --------------- | -----: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| tool / library  |     30 | [`asyncapi/generator`](https://github.com/asyncapi/generator), [`microcks`](https://github.com/microcks/microcks), [`specmatic`](https://github.com/specmatic/specmatic), [`zod-sockets`](https://github.com/RobinTail/zod-sockets)                                                                                      |
| demo / fixture  |     23 | [`aklivity/zilla-demos`](https://github.com/aklivity/zilla-demos), the Kraken-WebSocket and ping-pong examples                                                                               |
| **product**     | **13** | [`EVerest`](https://github.com/EVerest/EVerest) (MQTT), [`voiceblender`](https://github.com/VoiceBlender/voiceblender), Netcracker qubership integration platform, [`ollert-backend`](https://github.com/acidtango/ollert-backend) / [`sigaa-socket-api`](https://github.com/dduartee/sigaa-socket-api) (WebSocket), [`vequate`](https://github.com/Jack-the-Pro101/vequate) (Redis) |
| spec / docs     |     12 | [`asyncapi/spec`](https://github.com/asyncapi/spec), [`OAI/Arazzo-Specification`](https://github.com/OAI/Arazzo-Specification)                                                                                                       |
| uncategorized   |      3 | —                                                                                                                                                 |

The contrast with the full corpus is itself the finding: where 3.x splits evenly between products (262)
and demos (261), the request/reply _subset_ skews to **tooling test-fixtures and teaching examples**
(53 of 81 repos), with only **13 genuine products** — and the **2.x** subset converges (of **32 distinct
repositories**, only **3 are products**). Kafka leads the subset by repository, yet **none** of those
are products: they are vendored Spring-Kafka and Specmatic samples, because products use Kafka for
fire-and-forget streaming, outside this subset — the 13 products correlate over WebSocket, MQTT, AMQP and
Redis instead. So the observable construct is not just rare but thinly spread across mutually
incompatible transports and few real systems — itself a core difficulty of the problem. (Caveat: the
2.x enumeration is `.yaml`-only, so true prevalence may be marginally higher.)

## The four transports and their correlation

AsyncAPI is not a protocol — it is realized over whatever transport a service uses, and the survey
scattered request/reply across four mutually incompatible ones that share nothing at the API level:
Kafka's streaming log, AMQP's queues and exchanges, MQTT's minimal pub/sub, and WebSocket's broker-less
frames. A reply over any of them is only observable if the tester can tell _which_ request it answers —
the job of a **correlation id**: the requester stamps a unique value, the responder copies it onto the
reply, and the tester pairs the two. AsyncAPI 3.0 can declare _where_ that id lives, as a
**`correlationId.location`** runtime expression resolving to `$message.header#/<field>` or
`$message.payload#/<field>`; but whether it can be a header at all is decided by the transport:

| Transport  | Where the id can live                          | Native to the protocol?             | Reply destination                  |
| ---------- | ---------------------------------------------- | ----------------------------------- | ---------------------------------- |
| AMQP 0-9-1 | `correlation-id` **property**                  | **yes** — standard message property | `reply-to` property                |
| Kafka      | record **header** (e.g. `kafka_correlationId`) | no — opaque header, named by a lib  | reply-topic header (by convention) |
| MQTT 5.0   | **Correlation Data** (or a User Property)      | **yes** — added in v5               | **Response Topic** property        |
| MQTT 3.1.1 | inside the **payload**                         | n/a — no metadata exists            | encoded in the payload             |
| WebSocket  | inside the **payload**                         | n/a — custom app-level protocol     | encoded in the payload             |

Each transport, then, with its mechanics and where correlation can ride:

### Kafka

Apache [Kafka](https://kafka.apache.org/) is a distributed event-streaming platform: producers append
records to **topics** split into **partitions**; **consumer groups** read independently by committed
**offset**; a record is a key, a value, and — since v0.11 — a set of **headers**. Topic = channel maps
cleanly onto AsyncAPI. Correlation rides in a header, but **Kafka defines no meaning for it**: the names
(`kafka_correlationId`, `kafka_replyTopic`) and the echo-on-reply behaviour come from a client library
(Spring Kafka), not the protocol — which is why nearly every Kafka reply example in the corpus is a copy
of one Spring-Kafka sample. So correlation is **decidable only by reading the code**: the header name
varies per service, and even then the reply may fail to carry it back.

### AMQP

[AMQP 0-9-1](https://www.rabbitmq.com/) (most commonly RabbitMQ) routes messages through **exchanges**
into **queues** that consumers read, removing them once **acknowledged** (unlike Kafka's retained log).
Every message carries a standard envelope of **properties** — among them `correlation-id` and
`reply-to`. This makes it the most accommodating: the request/reply ("RPC") pattern of echoing
`correlation-id` and answering on `reply-to` is the canonical RabbitMQ convention, so a black-box tool
can pair replies knowing only that it is talking to RabbitMQ — **no contract `correlationId` required** —
provided the code does echo it, the one thing to verify by reading it.

### MQTT

[MQTT](https://mqtt.org/) is a lightweight publish/subscribe protocol for IoT and constrained networks:
clients publish to hierarchical **topics** (with `+`/`#` wildcards) at a chosen **QoS**, with no
partitions or consumer-group offsets. Its versions differ in the one capability that matters here:
**3.1.1** carries nothing beyond topic and payload, whereas **5.0** adds **Correlation Data** and a
**Response Topic** (effectively AMQP-like). But almost no one opts into 5.0 — only a handful of the 219
3.x MQTT specs declare it, and similarly in 2.x — so a tool must assume **3.1.1** and find correlation
hand-rolled **inside the payload** or as a per-request reply-**topic** convention. There is nothing
transport-level to rely on; read the payload or the topic scheme.

### WebSocket

A [WebSocket](https://datatracker.ietf.org/doc/html/rfc6455) (RFC 6455) is a single, long-lived, duplex
connection with no broker, no topics, and no message metadata — every service layers its **own**
application-level protocol on top. A reply on the same socket is the most natural request/reply shape,
which is why WebSocket is the **most common reply transport in the survey** — 73 of the 356 reply
operations, plus 11 over the secure `wss` variant. With no headers, the id always lives **in the
payload**, in a field each service invents; a tool can only follow the contract's declared
`correlationId.location` and trust the service to be internally consistent.

### Correlating automatically — and why the contract can't be trusted

Sending a correlated request is the easy half, and entirely on our end: the `correlationId.location`
(or a heuristic, when it is absent) tells the tool where to place a fresh id — a header/property where
the transport has one, or inside the payload where it does not. The **correlation itself is built by the
SUT, not by us**: a request and a reply become a matched pair only once the responder copies our id onto
the message it sends back, which is the service's own behaviour and outside black-box reach. A tool can
_detect_ a missing or non-matching id — itself an observable conformance failure — but cannot supply it.

And the contract is an unreliable guide. The `correlationId` keyword is **rarely declared** (2.0% of 2.x
specs; frequently absent even in 3.x) and, when present, may not match the code — specs even name a
`$message.header#/…` location the header-less MQTT 3.1.1 wire cannot carry, or a transport the code does
not use. Whether a service can be correlated black-box is therefore ultimately an **implementation
property, read from the repository, not the document**, and the only reliable check is **empirical**:
stamp an id and see whether the reply carries it back. The transports thus form a gradient — **AMQP**
fits black-box request/reply best (native, conventional, payload-agnostic), **Kafka** is nearly as
workable but leans on a framework convention, and **MQTT** and **WebSocket** push correlation into the
payload, coupling the tool to each message schema and, for WebSocket, to a bespoke per-service protocol.

## Are the real services usable as SUTs?

Finding the request/reply pattern in a repository is not the same as having a **runnable system under
test**. Reading the **81 3.x `receive`+`reply` repositories** one by one — _is this a real, runnable
service that consumes a request and emits a correlated reply over a broker/socket, that could be
containerized and driven as a black box?_ — the answer is sobering:

| Outcome                    | repos (of 81) |
| -------------------------- | ------------: |
| usable with minimal effort |         **2** |
| usable with real work      |           ~17 |
| not usable as a SUT        |           ~62 |

What the three tiers mean — how much stands between the repository and a black-box run, against that
bar:

- **usable with minimal effort** — runs essentially as-is (a container or a fat jar), its request/reply
  and correlation work out of the box, and the license is permissive: stand it up and point the tool at
  it.
- **usable with real work** — a genuine request/reply service, but not drivable until real setup is done
  — a heavy backend or stack to stand up, the correlation to recover by reading the code, an external
  dependency to stub, or a transport client to write.
- **not usable as a SUT** — cannot be driven as a controlled black box at all: not a runnable service,
  its spec has no matching implementation, it is one-way in practice, or it is gated by the recurring
  blockers below.

**42 of the 81 are tooling/library or spec/docs repos** — not runnable services at all. Among the 39
candidate services, **reading each one** shows almost none sit in the "small, clean, runnable,
well-specified, permissively-licensed" sweet spot; they are **bimodal** — tiny hobby, student or
course-project repos (0–3★, the AsyncAPI file aspirational rather than backed by a running service), or
large platforms (EVerest, the Netcracker integration platform) that are genuine but heavy to stand up. The same blockers recur, each a facet of the problem:

- **A spec in a repo is not an implementation** — many carry an AsyncAPI document as documentation or a
  test fixture with no matching service; the canonical example specs recur verbatim across unrelated
  repos.
- **Correlation is rarely contract-declared** — where a real reply exists, the service usually correlates
  by an ad-hoc payload field, a hardcoded id, or a broker/framework convention, not a declared
  `correlationId.location` (as **The four transports and their correlation** set out).
- **Contracts drift from implementations** — a spec claims a transport the code does not use (gRPC with
  no code, AMQP where the code uses IBM MQ), so the contract cannot be trusted at face value.
- **Hard external dependencies and licensing** — real candidates are frequently gated by live SaaS,
  Kubernetes stacks, or paid services, and a striking number ship **no license** at all.

Full per-repo verdicts are in `corpus-suitability.md`.

Reading the **implementations** — not just the contracts — both widens and sharpens the picture. Over
Kafka and AMQP a service can correlate in code while declaring nothing, so we read ~200 candidate
repositories directly; this surfaced roughly a dozen genuinely correlated request/reply services across
both versions, but almost all demos, course projects and workshops, with real **products vanishingly
rare** (Kafka and AMQP are overwhelmingly used fire-and-forget). The **payload-only transports tell the
opposite story**: over WebSocket the JSON-RPC shape — a request carries an `id` the server echoes on the
response over the same socket — is the **richest seam of product-grade correlated services in the
corpus**, roughly ten actively-maintained real products, because JSON-RPC-over-WebSocket makes request-id
correlation a natural pattern. Across every transport, though, one blind spot is constant: real services
correlate through a native property, a header, or a payload field — **essentially never through the
AsyncAPI `correlationId` keyword**. The contract's one dependable signal is the _negative_ (a purely
one-directional contract reliably predicts one-way code); for anything bidirectional, how a service
correlates must be learned from its behaviour, not its schema.

The practical consequence frames the rest of this proposal: **the public corpus does not supply ready
SUTs.** A corpus-grounded evaluation cannot simply harvest these repositories — it must adapt the handful
of genuine services and/or build **controlled SUTs** whose transports, correlation and licensing are
known. To make concrete what such a test must actually do, the next section shows one by hand.

## What a request/reply test looks like

Before the approach, it helps to see concretely what a black-box test for one of these services _is_ —
because that is what the tool must generate. Take a small request/reply service: the NCS numerical
functions (`triangle`, `bessj`, …) over each transport, the same operations and schemas throughout,
with a contract-honest reply — a success message (`IntResult` / `DoubleResult`) and, when the input is
out of range, an `Error` — bounds (`bessj` ∈ 3..1000, …) carried as `minimum` / `maximum`, and the
correlation id declared wherever the transport can carry it.

Written by hand, the test is the **same shape on every transport** — publish a request with a fresh
correlation id, await the reply, assert on it — and only the plumbing differs. Over WebSocket (the SUT
_is_ the server; the id rides in the payload):

```
test bessj_valid_over_websocket:
    cid    = freshId()
    socket = openWebSocket("ws://sut/ncs")              # no broker; SUT is the server
    send(socket, { operation:"bessj", correlationId:cid, n:3, x:2.0 })
    reply  = awaitFrame(socket, within=W)
    assert reply.correlationId  == cid                  # correlation
    assert reply.resultAsDouble is finite               # success (DoubleResult)
    assert not reply.has("error")

test bessj_outOfRange_over_websocket:
    cid    = freshId()
    socket = openWebSocket("ws://sut/ncs")
    send(socket, { operation:"bessj", correlationId:cid, n:2, x:2.0 })   # n < 3
    reply  = awaitFrame(socket, within=W)
    assert reply.correlationId == cid
    assert reply.error.code    == 400                   # Error variant
```

Over Kafka the identical payload is the _same test_, but the plumbing changes — a broker must be up,
each operation has its own request/reply topic, and the id rides in a **record header**:

```
test bessj_valid_over_kafka:
    cid      = freshId()
    producer = connectKafkaProducer("kafka:9092")       # broker already running; the SUT consumes it
    consumer = connectKafkaConsumer("kafka:9092", topic="ncs.bessj.reply")
    producer.publish(topic="ncs.bessj.request",
                     headers={ correlationId: cid }, body={ n:3, x:2.0 })
    reply = consumer.pollUntil(match = r -> r.headers.correlationId == cid, within=W)
    assert reply != null                                # a correlated reply arrived
    assert reply.body.resultAsDouble is finite
    assert not reply.body.has("error")
```

AMQP is the same again, against a RabbitMQ broker — but the id rides in the protocol's **native
`correlation-id` property** (with `reply-to` naming the reply queue), so it never touches the payload:

```
test bessj_valid_over_amqp:
    cid     = freshId()
    channel = connectRabbitMq("amqp://ncs@rabbit:5672")  # broker already running; the SUT consumes it
    channel.declareQueue("ncs.bessj.request"); channel.declareQueue("ncs.bessj.reply")
    channel.publish(queue="ncs.bessj.request",
                    properties={ correlationId: cid, replyTo: "ncs.bessj.reply" },
                    body={ n:3, x:2.0 })
    reply = channel.consumeUntil(queue="ncs.bessj.reply",
                                 match = m -> m.properties.correlationId == cid, within=W)
    assert reply != null                                 # a correlated reply arrived
    assert reply.body.resultAsDouble is finite
    assert not reply.body.has("error")
```

MQTT follows the WebSocket shape, with the id in the payload. So the same handful of steps is written
four times, differing only in addressing and where the id rides:

| | Kafka | AMQP | MQTT | WebSocket |
| --- | --- | --- | --- | --- |
| addressing | topic `ncs.bessj.request` → `.reply` | queue `ncs.bessj.request` → `.reply` | topic `ncs/bessj/request` → `/reply` | single socket `/ncs`, `operation` field |
| correlation id | record **header** | **`correlation-id` property** | **payload** field | **payload** field |
| what the client connects to | a broker (`kafka:9092`) | a broker (RabbitMQ) | a broker (Mosquitto) | the SUT itself (`ws://sut/ncs`) |

That hand-written test is the target artifact: an AsyncAPI-aware EvoMaster must generate the input from
the message schema, stamp and match the id, await the reply, and assert the outcome — and **the only
thing that changes between the four transports is the plumbing**, which is exactly what the approach
that follows factors out.

## The approach: classifying replies as the unit of coverage

Everything above characterizes the **problem**; this section sketches the **approach**. The aim is to
reuse EvoMaster's existing black-box engine — its **SMARTS** sampler, which generates a request,
classifies the result, and keeps one test per newly-covered outcome, with **no instrumentation and no
search gradient** — and to give it a notion of "result" that asynchronous messaging can actually
supply. REST hands that engine an HTTP status code for free; async hands it nothing. So the whole
design reduces to one question: **what plays the role of the status code**, such that a decoupled
reply — arriving later, on another channel, possibly not at all — can be turned into the same kind of
discrete, assertable outcome. The short answer, developed below, is that **the reply message itself
becomes the unit of coverage**. Three pieces make up the solution, defined in turn: a protocol-agnostic
**transport adapter** (how EvoMaster reaches the SUT), a notion of **coverage** (what a generated suite
is measured against), and the **generated test** itself (what comes out).

### What black-box testing can reach

Black-box testing can only exercise what it can both **trigger** and **observe** — which, as **The
observable subset: request/reply** established, is the `receive`+`reply` subset: operations the SUT
consumes and answers. On that surface the **input side is essentially the REST story**: for each such
operation EvoMaster is the publisher, building the request from the message's **JSON Schema** with the
same gene representation, mutation and boundary-fuzzing it uses for REST, and stamping a fresh
correlation id — generated per test, not searched over — where the contract (or a heuristic) says it
belongs. (Fire-and-forget `receive` and `send`-only operations fall outside this surface — nothing to
assert on, or nothing to trigger; messages a SUT emits on other channels are a weak secondary oracle,
left as a refinement.)

So **all the novelty is on the output side**: turning the async reply into the discrete result REST
reads off a status line — which is what the rest of this section develops.

### The transport adapter

Triggering needs a live **transport client**, and async has no universal wire. EvoMaster's own
architecture already shows how to handle that without coupling the tool to a protocol: every black-box
mode it has — REST, GraphQL — rides **HTTP**, so it needs no transport code at all; the _only_
non-HTTP protocol it supports, **RPC**, has **no black-box mode** (the core throws "NOT SUPPORT
black-box for RPC") and instead delegates the wire call to a user-written Driver. AsyncAPI is the
non-HTTP case — but, unlike RPC, it comes with a **portable contract**. That places it at a new point
on the spectrum and dictates the design: **EvoMaster's core stays protocol-agnostic, with every
transport library behind a thin boundary.**

- **The core** reads the AsyncAPI document _as data_, generates inputs from the message schemas, mints
  / injects / matches the correlation id (driven by `correlationId.location`), classifies the reply,
  and runs SMARTS. It imports **no** broker or socket library.
- **A transport boundary** — a small **SPI** (a _Service Provider Interface_: an interface the core
  defines and calls and a provider implements — the inverse of an API) that is a pure pipe:

```
interface Transport:                 # the whole protocol surface the core sees
    connect()
    send(address, headers, bytes)    # the core stamps the id into headers or bytes
    receive(address, within) -> (headers, bytes)
```

- **An adapter** on the far side implements that SPI with the actual Kafka / AMQP / MQTT / WebSocket
  client, and is the _only_ place a protocol dependency lives. It is supplied by the user, or shipped
  as an optional plugin the core does not depend on.

An adapter is a **dumb pipe**: all the smarts — serialising the request, placing and reading the
correlation id, matching and classifying the reply — stay in the core. The two extremes make that
concrete:

```
# Kafka adapter — a broker; the id rides in a header
class KafkaTransport implements Transport:
    connect():                 producer = KafkaProducer(spec.server.url)
                               consumer = KafkaConsumer(spec.server.url)
    send(addr, headers, body): producer.send(topic=addr, headers=headers, value=body)
    receive(addr, within):     r = consumer.subscribe(addr).poll(within); return (r.headers, r.value)

# WebSocket adapter — broker-less; one socket; the id rides in the payload
class WebSocketTransport implements Transport:
    connect():                 sock = openWebSocket(spec.server.url)     # ws://host/ncs
    send(addr, headers, body): sock.sendText(body)   # addr/headers unused: one socket, id already in body
    receive(addr, within):     return ({}, sock.awaitFrame(within))
```

The core hands them a body it has already serialised (per the contract's `contentType`), with a fresh
id placed in `headers` (Kafka) or inside `body` (WebSocket, per `correlationId.location`), then reads
the id back and classifies. The four NCS messaging tests are, in effect, these four adapters by hand.

**This adapter is not a Driver.** EvoMaster's Driver is a white-box controller that owns the SUT's
lifecycle, instruments it for code coverage, and is the source of the schema; in black-box mode no
Driver exists at all. The adapter does none of that — no lifecycle, no instrumentation, no schema, no
reset — it only moves bytes. It is the single wire-touching responsibility that black-box testing
always got _for free_ from HTTP, isolated and made pluggable now that the wire is no longer universal.

How much of that adapter the contract can fill — measured over every `ws` / `wss`, Kafka, AMQP and MQTT
spec in the corpus — splits cleanly:

| What it gives the client | Schema-derivable? | Corpus (3.x, per repo) |
| --- | --- | --- |
| **Connection** — server URL + handshake | **yes** | connectable 79–95% |
| **Encoding** — JSON / text / binary (`contentType` / `schemaFormat`) | **yes** | JSON 87–96% |
| **Addressing + message shapes** → connect + typed send/receive | **yes** | **81–89% of repos** |
| **Correlation / framing** → a full request/reply client | **rarely** | `correlationId` 4–11%; full client ≤ 8% (mostly samples), 2% on WS |

So the contract reliably auto-fills **connection, encoding and addressing on every transport**,
thinning the adapter to its one irreducible job: the wire, plus the correlation hook the schema almost
never declares. Where that hook lives is the gradient from **The four transports and their correlation** — native for
AMQP (the adapter need only honour `correlation-id` / `reply-to`), a header name for Kafka, a payload
field for MQTT / WebSocket — so the per-SUT effort _shrinks as the transport's native correlation
grows_, but the boundary above it never changes.

**How the adapter is initialised and consumed.** The core never constructs a protocol client directly.
It **resolves** the adapter from the server's protocol — a shipped plugin (`kafka` → KafkaTransport,
`ws` → WebSocketTransport, …, discovered the way the JVM loads any service provider) or, for a bespoke
wire, a user-supplied class — **initialises** it once at the start of a run from the server URL (plus a
small per-SUT profile where the contract is silent on a correlation field, address or auth) and calls
`connect()` to open the wire. From then on EvoMaster **consumes** it only through the SPI: for each
request action the search produces, the core calls `send(address, headers, body)` and then
`receive(replyAddress, within)`, holding one long-lived adapter and reusing it across the whole run —
never importing a broker or socket library itself. The emitted suite carries the same shape: the
adapter is built once in the test fixture and driven by `send` / `receive` in each test — the concrete
form of the dependency noted in **The generated test**, that the adapter must be present for the suite
to run.

### Coverage

REST shows what to port. With no code coverage to optimise, the SMARTS sampler manufactures coverage
from the response: each **(endpoint, status-code)** pair it observes is a **binary coverage target**
(`GET /products → 200`, `→ 404`, `POST /products → 400` are three), and on top sit **automated
oracles** — a `5xx`, or a body that **violates the declared schema**, is flagged a _potential fault_.
That single mechanism — enumerate the distinct outcomes per operation, keep a test for each, mark some
as faults — is what stands in for the white-box branch-distance gradient. Porting it to AsyncAPI means
defining the async equivalents of **`endpoint`**, **`status code`** and the **fault rules**: `endpoint`
becomes the **operation** we publish to, and `status code` — which async has no equivalent of — must be
**reconstructed from the reply**. We take those in turn, then assemble the criterion.

#### The unit: the operation, across versions

A top-level, named, `action`-typed **operation** is a construct only AsyncAPI **3.0** has; 2.x has
neither operations nor a `reply`. So the unit a coverage target is really built on is not the 3.0
keyword but the **request/reply interaction beneath it** — primitives _both_ versions express: a
**request channel + message** the tool drives, paired with a **reply channel + message** it observes.
AsyncAPI 3.0 merely _packages_ that interaction as a named `operations:` entry (an `action: receive`,
its channel and messages, and its `reply`), and that entry's key is the stable identity the
`(reply-variant × operation)` target hangs on. This is the clean case — and the one our authored 3.0
SUTs provide by construction.

A **2.x** service is reconstructed into the same unit. Its consume side is a channel's `publish` block
— in 2.x's inverted vocabulary, the operation where _the application receives_ (others publish to it),
the equivalent of 3.0 `receive` (`subscribe` is the `send` side). Its reply side has **no contract slot
at all**, so the reply channel is recovered the only way it can be — **empirically, from the
implementation** — the very code-read this proposal already leans on (the implementation read in
**Are the real services usable as SUTs?**). The synthesized identity `(channel, consume-block) ↦
recovered reply channel` then plays the role the 3.0 operation key does.

So the model is **3.0-shaped by design, not by oversight**: it follows the proposal's position that
AsyncAPI 3.0 is the version carrying the observable signal, that real 2.x request/reply is rare and its
`correlationId` mostly does tracing, and that 2.x candidates surface by code-reading rather than from
the contract. In practice the coverage target is defined on the 3.0 operation, and the few testable
2.x services are **lifted into that 3.0 shape** before testing — not given a second, parallel target
model.

#### The status analogue: the reply variant

An AsyncAPI 3.0 operation's `reply` declares the set of messages a reply may be — one message, or
several (`oneOf`): a **success** result, an **error** envelope, and so on. **Which of those declared
messages a given reply matches** is a schema-grounded, discrete label the contract itself enumerates —
and that is the natural status-code analogue. A `reply` with a _result_ message and an _error_ message
is, observationally, a two-valued "status"; the success/error split is the async echo of 2xx-vs-4xx.
The canonical real shape (the dominant request/reply form in the survey) is **JSON-RPC over
WebSocket**, where every reply is either `{…, result}` or `{…, error: {code, message}}` and `error.code`
is a _literal_ status-code analogue (`-32601` method-not-found, `-32603` internal-error, and so on).

That label is synthesized from a handful of independently observable axes of a single
publish-then-await interaction:

| Axis                              | Observable values                                                                                   | REST analogue                       |
| --------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Delivery**                      | broker accepted / rejected the publish                                                              | (transport-level; ~ connection error) |
| **Reply arrival** (within window _W_) | a correlated reply arrived / nothing arrived (timeout)                                          | a response always returns           |
| **Correlation**                   | id echoed and matches / mismatched / absent                                                         | none — async-only                   |
| **Reply variant**                 | which declared `reply` message it validates as (`result`, `error`, …) / matches none               | status _class_ (2xx vs 4xx)         |
| **Schema conformance**            | reply payload conforms / violates the declared reply schema                                         | response-schema oracle              |
| **Application status**            | an explicit code/flag inside the payload (a JSON-RPC `error.code`, a `status: ok\|error` enum)      | the status code itself              |

The **reply variant** (and any **application status** field it carries) is the strongest analogue,
because it is a _discrete enumeration the contract already declares_ — so the coverage target keys on
`(reply-variant × operation)`, the direct parallel to REST's `(status × endpoint)`, defined next.

#### The coverage criterion and the fault oracle

Coverage is defined over **targets**, created as outcomes are observed and reusing the very same archive
machinery as REST — only the _target strings_ change. There are two kinds.

**Coverage targets** — each distinct `(reply-variant × operation)` pair, plus the `no-reply` outcome;
binary, created on first observation. They drive diversity: the archive keeps one minimal test for each
distinct reply outcome the sampler produces per operation.

**Fault targets** — the outcomes that signal a defect:

| REST fault signal                | AsyncAPI analogue                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `5xx` server error               | a reply carrying a **server-fault code** (e.g. JSON-RPC `-32603`, a `status:"error"` with a server code); a SUT crash / connection drop mid-process |
| response **violates the schema** | a reply that matches **no declared reply message** (wrong type, missing required field, out-of-range)   |
| —                                | **correlation broken** — a reply arrives whose id is missing or does not match the one sent             |
| —                                | **silent drop** — no reply to an operation whose contract _declares_ one (delivered, but silent past _W_) |

A suite's coverage is the **set of distinct targets its tests cover**, and the search maximises that
set. One asymmetry with REST matters: a **well-formed error reply** — a conforming `error` message, a
declared client-error code — is **not** a fault but valid, declared behaviour and a coverage target,
exactly as a 400 is in REST; only _malformed_, _uncorrelated_, _absent-when-promised_ or _server-error_
replies are faults. The schema-conformance oracle ports directly (validate the reply payload against the
`reply` message schema); the **correlation** and **silent-drop** oracles are genuinely new, falling out
of the asynchronous semantics established earlier — and silent-drop is treated **cautiously** (a
configurable timeout, recorded but not hard-asserted), since a missing async reply may be slowness
rather than a defect. The criterion is thus the async analogue of REST's `(status × endpoint)` coverage
plus its fault oracle — though only as fine as the contract is rich (see **When coverage degenerates**).

#### When coverage degenerates

In a gradient-free search, the status code is the **entire diversity signal**: it multiplexes one
endpoint into several behaviour-correlated outcomes (200, 400, 404, 500 track different code paths), so
SMARTS keeps perturbing inputs only because each new status is a fresh target to cover.

The async analogue inherits that power **only when the contract actually declares more than one reply
variant**, and both the survey and the spec warn that it often does not. AsyncAPI lets a `reply` list
several messages, but provides **no field marking one as the error** (success/error is naming- or
payload-convention, never declared semantics), and real contracts frequently declare a **single**
reply message. When they do, `(reply-variant × operation)` collapses to **one coverage target per
operation** — "did a reply come back" — which a single seeded request already covers. At that point
the search has nothing left to optimise _within_ the operation: with no declared error variant to
chase, nothing rewards fuzzing inputs toward the validation or error path. This is strictly weaker than
REST, where even a one-behaviour endpoint still exposes the 400/500 partition for free.

The target is therefore only as discriminating as the contract is rich — and that gap has **no general
fix**. Granularity can be recovered by reading the reply more finely, but only one part of that
generalises:

- **What the reply _schema_ declares is fair game**, mechanically and without per-service code: every
  member of a multi-message `reply`, and every `enum` value or `oneOf` / `discriminator` branch
  declared _inside_ a reply message, is a discrete alternative the search can be set to chase. This
  widens the target set — but only ever to the granularity the contract itself chose to declare.
- **Going beyond the schema does not.** Splitting a single flat reply by recognising a bespoke `status`
  field, or by reading an undeclared JSON-RPC `error.code`, is **per-implementation envelope handling**
  — the very coupling to each service's hand-rolled protocol the approach otherwise tries to avoid.
  JSON-RPC is worth special-casing only because it is a widely-reused standard a tool can recognise
  once; that is an exception, not a method. So it is not a remedy but a **per-service heuristic**, whose
  reach is only ever whatever conventions the tool happens to recognise.

What remains is a genuine **limitation**: when a contract declares a single, flat reply with no
enumerated alternatives, the coverage signal stays coarse and no black-box technique recovers a finer
one — the discriminating behaviour simply is not observable from outside. Such an operation leans
entirely on the **fault oracle** (schema-mismatch, correlation, silent-drop), which fires regardless of
variant count, so it is _under-exercised_ rather than untestable. Two things follow for the evaluation.
Target **granularity is a per-SUT property to measure, not assume**. And because authored SUTs _can_ be
written contract-honest (success and error as distinct reply messages, or an enumerated status field)
while arbitrary third-party services cannot be assumed to be, results must be **reported separated by
contract richness** — the contract-honest and the degenerate cases are different experiments, and
conflating them would flatter the technique.

#### Where the classification signal comes from

The survey's blunt finding — the formal `correlationId` keyword is essentially unused, and contracts
drift from code — means the classifier cannot simply trust the document. It is therefore **layered**,
most-authoritative first:

1. **The contract**, where it is honest: the `reply` message set supplies the variant axis and the
   schema for the conformance axis; a declared `correlationId.location` supplies where to read the id.
2. **Recognized application envelopes**, where the contract is thin: the JSON-RPC `result`/`error`
   shape (and similar `status`/`code` conventions) supplies the variant and application-status axes
   even when the schema does not model them explicitly.
3. **Empirical probing**, for everything correlation-related: because echoing the id is the SUT's own
   behaviour and never guaranteed, the id is _stamped and watched for_, and "correlated vs not" is
   decided by what comes back — never assumed from the schema.

This layering is what lets a **single, transport-agnostic outcome model** sit on top of the four
incompatible transports: only _how the reply and its id are read off the wire_ differs per transport
(the gradient in **The four transports and their correlation**); _what an outcome means_ is uniform.

### The generated test

A generated test has two parts. **Pre-execution** (the fixture): assume the SUT and its broker are
already running — black-box owns no lifecycle — bind the transport **adapter** and open the connection.
**The body**: build the request from the genes, stamp a fresh id at the contract's location, `send`,
`receive` the correlated reply, assert the classified outcome. Because the body is written against the
`Transport` boundary, it is **identical across transports** — only the adapter bound in the fixture
differs:

```
fixture:
    transport = Adapter.for(spec.server)        # Kafka|AMQP|MQTT|WS — supplied / plugin
    transport.connect()                         # SUT + broker assumed up

test ncs_bessj__DoubleResult:                   # one test per covered (variant x operation)
    cid     = freshId()
    payload = generateFrom(spec.op("bessj").request)        # genes -> { n:3, x:2.0 }
    transport.send(addressOf("bessj"),
                   inject(cid, payload, spec.correlationLocation))   # header or body
    reply   = transport.receive(replyAddressOf("bessj"), match=cid, within=W)
    assert variantOf(reply) == "DoubleResult"   # classifier: which declared reply + schema
    assert correlationOf(reply) == cid

test ncs_bessj__Error:                          # the out-of-range outcome, n below minimum=3
    cid     = freshId()
    payload = generateFrom(spec.op("bessj").request)        # boundary-fuzzed -> { n:2 }
    transport.send(addressOf("bessj"), inject(cid, payload, spec.correlationLocation))
    reply   = transport.receive(replyAddressOf("bessj"), match=cid, within=W)
    assert variantOf(reply) == "Error"
    assert correlationOf(reply) == cid
```

`addressOf`, `replyAddressOf` and `correlationLocation` come straight from the AsyncAPI document;
switching transport is swapping `Adapter.for(...)` — the body never changes. The generator does not
write that adapter: `Adapter.for(spec.server)` is the run-time binding **serialised** — resolve the
adapter by the server's protocol, configure it from the server URL plus the per-SUT profile — using the
very values the core already used to drive the SUT during the run; the adapter implementation stays the
external dependency. The per-protocol fixture is the only delta:

| | fixture (pre-execution) | id carried in |
| --- | --- | --- |
| Kafka | producer + reply-topic consumer | header |
| AMQP | channel + reply queue | `correlation-id` property |
| MQTT | client + reply-topic subscription | payload |
| WebSocket | one socket to `/ncs` | payload |

Unlike a black-box REST test, the emitted suite is **not self-contained**: it carries a dependency on
the adapter, which must be present for the test to run — the concrete form of "a transport client must
exist".

### What async adds that REST gets for free

Three costs come with manufacturing a status code rather than being handed one, and each frames the
experimental work to follow:

- **The observation window.** "No reply" is only decidable relative to a timeout _W_: too short
  manufactures false silent-drops, too long makes every test slow, and slow-vs-dropped is inherently
  undecidable black-box. _W_ is a tuning parameter with no REST counterpart.
- **Shared channels and ordering.** Replies for different actions can interleave on one channel, arrive
  out of order, or be multiple; the correlation id is what untangles them, and where there is none the
  tool must fall back to **single-flight** execution (one outstanding request at a time) at a real
  throughput cost.
- **Non-determinism.** The same request may classify differently across runs (timing, broker state),
  so outcome targets and the generated assertions must tolerate benign variation rather than freeze a
  flaky reply.

These are the async-specific price of buying back the one thing REST supplies for nothing — a
synchronous, self-labelling response.

## Appendix: How repositories are classified

The corpus survey classifies each surveyed repository as a **product**, **tool/library**,
**demo/fixture** or **spec/docs** repo — plus two excluded classes, **catalog** (apis.json API
directories) and **tangential** (repos that merely mention AsyncAPI, e.g. AI-agent "skills"
collections), and **uncategorized** for repos with no readable metadata. Classification is
two-layered, and every result is reproducible from the scripts under `asyncapi-survey/`.

**1. Deterministic rules** (`asyncapi_classify_repos.py`). A **seedless** scorer — there is no
hand-curated list of known repositories; every repo is judged purely from its own observable signals —
working in three steps.

**Step 1 — shortcut rules** run before scoring and dispatch a few cases that keyword scoring reliably
gets wrong. Each fires on one narrow, high-precision signal — a topic, the repo owner, or a tightly
scoped text pattern — so it can never pull a genuine product, tool or demo out of the scorer:

- **AsyncAPI Generator template → tool.** Triggered by a `template`+`generator` **topic pair**, or a
  description/README that pairs the word "template" with "generator" / "generates" / "scaffold". These
  repos read as boilerplate to the keyword scorer but are reusable code-generation tooling.
- **AI coding-agent / "skills" repo → tangential** (excluded). Triggered by an agent **topic**
  (`claude-skills`, `ai-skills`, `agent-skills`, `agentic`, …) or a high-precision text marker such as
  "skills for Claude/Cursor" or "cursorrules" in the description/README.
- **apis.json API directory → catalog** (excluded). Triggered by the repo **owner** being a known
  catalog publisher (`api-evangelist`) or an `apis-json` **topic**.

Anything not matched falls through to the scoring below. (Tangential and catalog are the two excluded
classes — they are not scored as candidate services.)

**Step 2 — score the four buckets.** Every remaining repo accumulates points for each of product /
tooling-library / demo-fixture / spec-docs from the observable signals below; the highest-scoring bucket
wins:

| Signal                     | Weight | How it is read                                                                                                  |
| -------------------------- | -----: | --------------------------------------------------------------------------------------------------------------- |
| GitHub topic               |     +3 | substring-matched against ordered fragment groups (demo → tool → product → spec, first group wins): `documentation-generator` → tool, `schema-registry` → product, `json-schema` → spec |
| description + README lead  |     +2 | per-bucket keyword regexes (below); unambiguous demo markers score +3, weak product cues only +1                |
| repository name            |   +1–2 | `*-sample` / `*-demo` → demo, `*-cli` / `*-sdk` → tool, `*-spec` → spec                                          |
| spec-file location         |     +1 | specs only under `tests/` / `fixtures/` → tool + demo; a spec at repo root or `docs/` → product                 |
| docs-only language         |     +1 | HTML / MDX / Markdown / TeX … → spec/docs                                                                        |

**Step 3 — decide.** The top bucket wins if it clears **2 points** (one clear signal); ties break
**tool → demo → product → spec** (deliberately conservative about calling something a product); anything
below 2 points is left **uncategorized** for the LLM pass.

The keyword vocabularies (representative — the full regexes are in the script):

- **demo/fixture** — `sample`, `demo`, `example`, `tutorial`, `workshop`, `hackathon`, `boilerplate`,
  `template`, `starter`, `playground`, `benchmark`, `fixture`, `showcase`, `getting-started`, `course`,
  `kata`; learning/academic cues (`school` / `class` / `final project`, `university`, `coursework`,
  `semester`, `academic`, `lab`, and `curso` / `ejemplos` / `exemplos` / `beispiele`); and high-precision
  "strong" markers that outweigh other signals — book companions (`published by Packt/O'Reilly/Manning…`,
  `companion code`), talk material (`conference talk`, `meetup`, `slides`), `demo` / `example` /
  `sample project`, `reproduction` / `repro`, `learning project`.
- **tool/library** — `generator` / `codegen`, `parser`, `validator`, `linter`, `bundler`, `transpiler`,
  `compiler`, `sdk`, `cli`, `plugin`, `library`, `framework`, `scaffold`, `toolkit`, `converter`,
  `renderer`, `editor`; plus "generates documentation/code/models/clients/SDKs" and "mocking
  tool/library/server".
- **product** — `microservice`, `backend`, `gateway`, `api-management`, `broker`, `messaging`,
  `platform`, `saas`, `self-hosted`, `kubernetes`, `registry`, `iot`, `event-driven`, `server`, `daemon`,
  `orchestrat*`, `mock-server`; plus weaker cues that only **nudge** product (+1, so they never beat a
  demo or tool signal on their own): `application`, `engine`, `service`, `bot`, `dashboard`, `portal`,
  `web app`, `website`.
- **spec/docs** — `specification`, `standard`, `schema`, `documentation` / `docs`, `guidelines`, `rfc`,
  `protocol specification`, `wire format`.

**2. LLM refinement** (`asyncapi_llm_classify.py`, `asyncapi_llm_audit.py`, `asyncapi_build_gold.py`).
Every repository with a readable description or README is independently classified by Claude — run
through the `claude` CLI with the bucket definitions, cached so the pass is reproducible — and its
verdict is compared against the rules. The canonical **"gold" classification**
(`repo-classification-gold.json`) is the rule output with the model applied two ways: repos the
rules left _uncategorized_ are filled in when the model's confidence ≥ 0.60, and repos the rules
classified but the model contradicts are overridden when its confidence ≥ 0.78 (a threshold fixed by
manually reviewing that confidence band, where the model was ~90 % correct and the rules were the
ones in error). Every entry is tagged with its source (`rule` / `llm-recovered` / `llm-corrected`),
the confidence and a one-line rationale, so each deviation from the rules is auditable; lower-
confidence disagreements are left as the rules decided and listed for manual review. Combined
accuracy is roughly **90 %**; the residual is a small set of genuinely ambiguous repos plus the
repos that carry no descriptive metadata at all. The full rule-versus-LLM confusion matrix is in
`asyncapi-survey-out/asyncapi-llm-audit.md`.
