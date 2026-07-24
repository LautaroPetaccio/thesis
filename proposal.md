# Testing AsyncAPI Services in EvoMaster: Black-Box and White-Box

This proposal asks whether EvoMaster, an automated test generator, can test **AsyncAPI** services — in
two modes that resolve the same difficulty from opposite ends. A message published into an async service
is consumed and processed **later**, off the request thread. **Black-box** can observe only what the
service sends _back_, which confines it to the rare **request/reply** subset; **white-box** adds
instrumentation, so it can test an operation by its **coverage** rather than a reply — unlocking the
**fire-and-forget** majority, at the price of a new question black-box never faces: _when has the SUT
finished processing the message?_

The document runs problem-first, then one approach per mode:

- **The problem** — why asynchronous messaging breaks REST's request/response assumptions (for
  black-box, no self-labelling response; for white-box, no synchronous moment to collect coverage);
  which interactions are observable at all; how often they occur in the wild (a corpus survey — rarely,
  and mostly in tooling); how the four dominant transports carry correlation; and whether the real
  services are usable as SUTs — read once for black-box (the 81 request/reply repositories) and once
  for white-box (the 92 JVM products).
- **The black-box approach**, scoped to **Kafka and AMQP over AsyncAPI 3.x** — reuse EvoMaster's
  black-box engine by making the **reply message a synthesized status code**, drive every transport
  through a **user-supplied driver** (the extension point EvoMaster already uses for non-HTTP
  protocols) that keeps the core protocol-agnostic, and ground it in controlled SUTs.
- **The white-box approach**, covering **AsyncAPI 3.x and 2.x** — reuse MIO, the Driver and the
  instrumentation, model a consume operation as an async action, and solve **completion detection**.

The companion `corpus-suitability.md` holds the full per-repository evidence behind the survey.

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

## Differences from REST-based testing

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

### White-box: when to collect coverage

The two differences above frame the black-box difficulty. White-box testing has its own. In REST
white-box testing, EvoMaster runs the instrumented SUT behind a **Driver** and drives it with HTTP. The
call is **synchronous**: the handler executes _during_ the call, the instrumentation records the lines,
branches and **branch distances** it took, and MIO climbs that gradient toward uncovered code. The HTTP
response is almost incidental — **code coverage is the objective**, and it is available the instant the
call returns.

Async messaging removes that instant. When EvoMaster publishes a message, the SUT's consumer runs
**later, on a broker- or listener-driven thread**, after the publish call has already returned. There
is no synchronous point at which "the SUT has finished this message," so the core does not know when to
snapshot coverage and evaluate the individual:

|                            | REST (white-box)           | Async messaging (white-box)                                                          |
| -------------------------- | -------------------------- | ------------------------------------------------------------------------------------ |
| Trigger → processing       | same thread, same call     | publish returns; consumer runs later, another thread                                 |
| When is coverage complete? | when the HTTP call returns | **unknown** — no synchronous signal                                                  |
| What ends the test         | the response               | must be **detected** (instrumentation inactivity, a completion signal, or a timeout) |

So the central white-box-async problem is not _what to assert_ (coverage answers that) but **when to
collect it**: attributing a test's coverage requires knowing that the async processing it triggered has
finished.

That cost buys a decisive gain. Black-box can only reach operations that reply, because the reply is its
only observable signal — and the survey below shows that subset is small, with products overwhelmingly
using Kafka/AMQP for **fire-and-forget** streaming, outside it. White-box needs no reply: if publishing a
message drives the consumer's code, the branch-distance gradient over that code **is** the signal,
whether or not anything is sent back. So the fire-and-forget majority — the bulk of real async
operations — moves **into scope**; the only thing standing between EvoMaster and testing them is the
completion problem above. For a request/reply operation, white-box gets **both**: the coverage gradient
_and_ the reply, so the black-box reply oracle still applies as an extra check. White-box therefore
strictly dominates black-box in _what_ it can test — at the cost of instrumentation and solving
completion (a driver is needed in both modes, since async has no universal wire; white-box just asks
more of it).

The secondary white-box difficulties:

- **Non-determinism / timing.** Completion is inherently racy; the same message may finish at different
  times across runs, so the mechanism that decides "done" must tolerate that without flaking.
- **Attribution under concurrency.** With several messages in flight on shared consumers, the coverage
  a run produces must be attributed to the message that caused it — or the tool falls back to
  **single-flight** execution (one outstanding message at a time).
- **The standing white-box requirements.** The SUT must be **instrumentable** — in EvoMaster's case, a
  **JVM** application — and reachable through a Driver. That requirement, more than anything, bounds how
  much of the AsyncAPI world this approach can address, which the white-box read of **Are the real
  services usable as SUTs?** measures.

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
| demo / fixture — examples, tutorials, student/book code |       261 |       322 |
| tool / library — generators, parsers, SDKs, validators  |       183 |       198 |
| spec / docs — the repo _is_ a spec / schema set / docs  |        97 |        85 |
| _tangential_ (excluded — incidental / AI-agent matches) |        56 |        92 |
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

| Repository kind |  repos | examples (with reply transport)                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | -----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| tool / library  |     30 | [`asyncapi/generator`](https://github.com/asyncapi/generator), [`microcks`](https://github.com/microcks/microcks), [`specmatic`](https://github.com/specmatic/specmatic), [`zod-sockets`](https://github.com/RobinTail/zod-sockets)                                                                                                                                                  |
| demo / fixture  |     23 | [`aklivity/zilla-demos`](https://github.com/aklivity/zilla-demos), the Kraken-WebSocket and ping-pong examples                                                                                                                                                                                                                                                                       |
| **product**     | **13** | [`EVerest`](https://github.com/EVerest/EVerest) (MQTT), [`voiceblender`](https://github.com/VoiceBlender/voiceblender), Netcracker qubership integration platform, [`ollert-backend`](https://github.com/acidtango/ollert-backend) / [`sigaa-socket-api`](https://github.com/dduartee/sigaa-socket-api) (WebSocket), [`vequate`](https://github.com/Jack-the-Pro101/vequate) (Redis) |
| spec / docs     |     12 | [`asyncapi/spec`](https://github.com/asyncapi/spec), [`OAI/Arazzo-Specification`](https://github.com/OAI/Arazzo-Specification)                                                                                                                                                                                                                                                       |
| uncategorized   |      3 | —                                                                                                                                                                                                                                                                                                                                                                                    |

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
3.x MQTT specs record it in the server's `protocolVersion` (the one field where a protocol version is
stated), and similarly in 2.x — so a tool must assume **3.1.1** and find correlation
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

The corpus is read twice against the runnable-SUT bar — once per mode, since each mode needs different
things from a repository: black-box a correlated request/reply it can drive from outside, white-box an
instrumentable JVM consumer.

### Through the black-box lens: the 81 reply repositories

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
known.

### Through the white-box lens: the 92 JVM products

White-box testing needs two things at once: a **JVM** service EvoMaster can instrument
(Java / Kotlin / Scala / Groovy), and an **AsyncAPI** document telling it which consume operations to
drive. The reachable population is the intersection — JVM services expressed in AsyncAPI — so we sliced
the corpus surveyed above by each repository's primary language (from the survey's
`repo-metadata.json`, cross-tabulated with the gold `product` classification):

|                            | 3.x corpus                     | 2.x corpus          |
| -------------------------- | ------------------------------ | ------------------- |
| classified repositories    | 984                            | 1,103               |
| — of which JVM (all kinds) | 148                            | 148                 |
| — **of which products**    | **55** (Java 33, Kotlin 21, …) | **43** (Java 35, …) |

JVM is a **top-tier** language for AsyncAPI products — Java is the third or fourth most common and
Kotlin adds a substantial tail — so a JVM-instrumenting tool has a real reachable population: **92
distinct JVM AsyncAPI products** across the two versions (55 + 43, with 6 in both).

But "JVM product with an AsyncAPI file" is a ceiling, not a runnable-SUT count. So we ran the deeper pass
this slice previously deferred, reading **all 92** repositories one by one — fetching each file tree and
source archive to grep for a real message **consumer** (`@KafkaListener`, `@SqsListener`,
`@RabbitListener`, `@Incoming`, `@MessageMapping`, Paho `messageArrived`, Ktor / Spring WS handlers, …)
and opening the AsyncAPI document to see whether it maps to that consumer — and graded each against the
white-box bar: _a runnable JVM service, with an instrumentable consume listener, described by an AsyncAPI
doc, whose transport we can stand up_:

| Of the 92 JVM products      | repos |
| --------------------------- | ----: |
| drivable with modest effort | **8** |
| drivable with real work     |    51 |
| not usable as a SUT         |    33 |

The tiers mirror the black-box read's (licensing again not a factor); only the bar changes. **Modest
effort** additionally demands an instrumentable consume listener that the AsyncAPI doc actually maps to,
over a transport we can stand up locally (a Testcontainers broker, or localstack for SNS/SQS). **Real
work** adds the white-box blockers: a streaming (Kafka Streams) or bespoke consume path to adapt, or
consume-side spec drift to reconcile by reading the listener. **Not usable** adds the white-box
disqualifiers: no async consumer at all (producer-only, or spec-only) or a bespoke non-standard
transport EvoMaster cannot instrument-and-drive.

The reachability gain white-box promised is real: **70 of the 92 carry an instrumentable consumer** —
against black-box, where only a _reply_ counted and the previous section found ~2 usable as-is and ~17
with work of the 81 request/reply repositories. Driving by coverage rather than by reply widens the
surface to **every consume operation**, fire-and-forget included.

**The binding constraint shifts, though — from "is there a reply" to "does the contract describe the
consume side," and usually it does not.** Only **24** of the 92 ship an AsyncAPI doc that maps cleanly to
the listener; in **35** the service genuinely consumes but the document describes only what it
_publishes_ (`action: send`), 15 are aspirational (a spec with no matching listener), 10 have a real
consumer but no AsyncAPI file, and 8 neither. This is the white-box echo of black-box's contract-drift
finding. One thing softens it here that did not hold for black-box: a white-box tool can **recover the
consume channel from the listener itself** — `@KafkaListener(topics=…)`, `@SqsListener("queue")` name it
in code the Driver already sees — so drift is survivable, and the AsyncAPI doc's irreducible value
narrows to supplying the **message schema** for payload generation rather than channel discovery.

The **8 modest-effort candidates** span every transport in scope — Kafka, AMQP, MQTT, WebSocket and
STOMP — and each ships an AsyncAPI doc that maps to its listener: [`kidoneself/DockPilot`](https://github.com/kidoneself/DockPilot)
(WebSocket), [`LingshijunRenzy/ICS-guard-next`](https://github.com/LingshijunRenzy/ICS-guard-next)
(Kafka), [`ODS-IS-UASL/safety-management`](https://github.com/ODS-IS-UASL/safety-management) (MQTT),
[`doemefu/very-cool-karaoke-server`](https://github.com/doemefu/very-cool-karaoke-server) (STOMP), the
two [`VALAWAI`](https://github.com/VALAWAI) components (AMQP, Quarkus `@Incoming`), and two more Kafka /
WebSocket services. Honestly, they skew small — student, hobby and research code, only DockPilot at all
product-like — the same lesson black-box reached: drivable real _products_ are rare. The largest
coherent seam is a different shape entirely: **17 near-identical Ministry-of-Justice HMPPS services**,
Kotlin Spring Boot consumers of domain events over AWS SNS/SQS (16 of the 17 land in "real work," gated
only by needing localstack and a publish-oriented spec) — a ready homogeneous cohort a single Driver
template could drive across all sixteen.

Two caveats bound this. The pass measures only the JVM fraction of repositories that **are** in
AsyncAPI; the far larger population of JVM messaging systems carrying **no** AsyncAPI document is, by
construction, invisible to it. And the per-repo verdicts come from automated tree/archive inspection, so
the modest-effort shortlist should be **hand-confirmed** before it anchors an evaluation.

Either way the corpus is read, controlled SUTs carry the evaluation. To make concrete what a test
against such a service must actually do, the next section writes one by hand.

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

|                             | Kafka                                | AMQP                                 | MQTT                                 | WebSocket                               |
| --------------------------- | ------------------------------------ | ------------------------------------ | ------------------------------------ | --------------------------------------- |
| addressing                  | topic `ncs.bessj.request` → `.reply` | queue `ncs.bessj.request` → `.reply` | topic `ncs/bessj/request` → `/reply` | single socket `/ncs`, `operation` field |
| correlation id              | record **header**                    | **`correlation-id` property**        | **payload** field                    | **payload** field                       |
| what the client connects to | a broker (`kafka:9092`)              | a broker (RabbitMQ)                  | a broker (Mosquitto)                 | the SUT itself (`ws://sut/ncs`)         |

That hand-written test is the target artifact: an AsyncAPI-aware EvoMaster must generate the input from
the message schema, stamp and match the id, await the reply, and assert the outcome — and **the only
thing that changes between the four transports is the plumbing**, which is exactly what the approach
that follows factors out.

## The black-box approach: classifying replies as the unit of coverage

Everything above characterizes the **problem**; this section sketches the **black-box approach** (the
white-box one follows it). The aim is to
reuse EvoMaster's existing black-box engine — its **SMARTS** algorithm (smart sampling, the black-box
default), which generates a request,
classifies the result, and keeps one test per newly-covered outcome, with **no instrumentation and no
search gradient** — and to give it a notion of "result" that asynchronous messaging can actually
supply. REST hands that engine an HTTP status code for free; async hands it nothing. So the whole
design reduces to one question: **what plays the role of the status code**, such that a decoupled
reply — arriving later, on another channel, possibly not at all — can be turned into the same kind of
discrete, assertable outcome. The short answer, developed below, is that **the reply message itself
becomes the unit of coverage**. The solution has four parts, defined in turn: a protocol-agnostic
**transport driver** (how EvoMaster reaches the SUT), a notion of **coverage** (what a generated suite
is measured against), the **individual** the search mutates (the representation the other parts hang on),
and the **generated test** itself (what comes out).

**Scope.** The black-box implementation targets **Kafka and AMQP, over AsyncAPI 3.x** — the combination
where a first-class `reply` exists and the correlation id rides in transport **metadata** (AMQP's native
`correlation-id` property, a Kafka header) that the tool can stamp and match without touching the
message body. MQTT 3.1.1 and WebSocket push the id into a **bespoke payload**, coupling the tool to each
service's hand-rolled message schema (the gradient of **The four transports and their correlation**), and
2.x has no reply construct at all — so those are **deferred**, not designed out: everything below is
written transport-agnostically, and the deferred cases re-enter as the per-SUT effort they demand.

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

### The transport driver

Triggering needs a live **transport client**, and async has no universal wire. EvoMaster's architecture
already fixes how to supply one. Every black-box mode it ships — REST, GraphQL — rides **HTTP**, so the
core points straight at a URL and needs nothing beside the running SUT. Its only non-HTTP problem,
**RPC**, has no URL to point at, and is therefore driven by a user-written **Driver**: a subclass of
`SutController` that the core talks to over an HTTP control protocol (`/controller/api/…`) and that holds
the client stub and performs the call — the core is emphatic that this cannot be skipped, throwing
_"NOT SUPPORT black-box for RPC yet"_ in `Main.kt`. AsyncAPI is the same shape: no universal wire, so
**a driver must hold the transport client and move the bytes**, with the core protocol-agnostic behind it.
The one way async is _easier_ than RPC is the schema: RPC has no contract, so EvoMaster reconstructs it by
**reflecting over the SUT's compiled interfaces** (`RPCEndpointsBuilder`), whereas the AsyncAPI document
already declares the operations and their JSON-Schema messages — parsed as data, like REST's OpenAPI, with
no reflection and no DTO classes on the classpath.

The driver is therefore **not a new abstraction but a `SutController` subclass** — the same base the REST
and RPC drivers extend — in one of the two standard flavours, which are **deployment choices, not testing
modes**:

- **`ExternalSutController`** — the SUT (and its broker) run as separate processes the driver starts and
  stops; instrumentation is still available (the driver injects the Java agent into the SUT's JVM and
  pulls coverage over a socket).
- **`EmbeddedSutController`** — the SUT runs inside the driver's own JVM, instrumented directly.

Black-box vs white-box is orthogonal to that choice: **black-box simply leaves instrumentation off**
(`isInstrumentationActivated()` returns false) and uses the driver for lifecycle and wire access only;
white-box turns it on (developed in **The white-box approach**). Either way the core never speaks a broker
protocol; it drives the SUT through the `SutController` control API, exactly as it drives its other
problem types.

**What the driver declares — `AsyncApiProblem`.** A `SutController` announces its kind through
`getProblemInfo()`, which returns a `ProblemInfo` — today `RestProblem`, `GraphQlProblem` or `RPCProblem`.
AsyncAPI adds one more, modelled on `RPCProblem` (which carries the interface class _and_ a live client
stub):

```
class AsyncApiProblem extends ProblemInfo:
    schema:  AsyncAPI document (URL or inline)     # operations, messages, servers, bindings
    client:  a transport client the driver holds   # Kafka producer + consumer, AMQP channel, …
```

The two fields play different roles. `schema` is the **portable, serialisable** part — the exact analogue
of `RestProblem`'s OpenAPI, conveyed the same way: the driver provides either a **URL** or the **inline
document**, and the core does the rest — it _fetches_ the document when given a URL (usually the SUT's own
served spec) or _parses_ it directly when given inline text, then reads it as data to learn the operations
and message JSON Schemas and build the input genes. The driver itself never parses the contract, and there
is no reflection step; the schema is the only part that crosses the control protocol to the core. `client` is a **live wire handle** — a Kafka producer/consumer, an AMQP channel — used
only on the driver side, inside `executeAsyncAction`, to publish and await; being an open connection it
never travels to the core. The contrast with RPC is instructive: `RPCProblem`'s client does _double
duty_ — its class is reflected for the schema **and** it is invoked to make the call — whereas
`AsyncApiProblem` keeps the two apart, `schema` describing the SUT and `client` only moving bytes.

Introducing it is a **new problem type, not just a subclass**: like the four before it (REST, GraphQL,
RPC, Web) it is added at a handful of hardcoded dispatch sites — a `ProblemType` enum value, a field on
`SutInfoDto`, a branch in the controller's `getProblemInfo` handling, and the problem→module wiring in
`Main.kt` — plus, for `executeAsyncAction`, a field on the action DTO. Additive and well-trodden, but
real plumbing across the controller, controller-api and core modules rather than a drop-in.

**The lifecycle methods, and how they behave.** The driver implements the same `SutController` methods as
any other driver; their async behaviour is:

- `startSut()` — start the SUT (black-box: and its broker), open `client`, **block until the SUT's
  consumer is subscribed and ready**, and return a base address.
- `resetStateOfSUT()` — restore a clean baseline between tests: drain reply queues/topics, reset consumer
  offsets, clear any seeded state.
- `stopSut()` — close `client`, stop the SUT (and broker).
- `getProblemInfo()` returns the `AsyncApiProblem`; `getPreferredOutputFormat()` gives the emitted-suite
  language — both unchanged in spirit from REST/RPC.

**How one action is executed — `executeAsyncAction`.** RPC adds exactly one method to the control
protocol that the core calls once per action, `executeRPCEndpoint(dto)`, which resolves the held client
and invokes the method reflectively (`method.invoke(client, params)`). AsyncAPI adds the direct analogue:

```
# on the driver (a SutController subclass); the core calls this once per action over the control API
executeAsyncAction(dto) -> AsyncReplyDto:
    cid   = dto.correlationId
    client.publish(dto.address, inject(cid, dto.body, dto.correlationLocation))   # header or payload
    reply = client.awaitReply(dto.replyAddress, match = cid, within = dto.window)
    return AsyncReplyDto(reply.headers, reply.body)          # handed back to the core to classify
```

The core builds `dto` from the individual (the payload genes, a freshly minted correlation id, the
request/reply addresses, the window), sends it over the existing control protocol, and classifies the returned reply — importing no
broker library. Only `publish` / `awaitReply` are protocol-specific, and they live **entirely inside the
driver**, a dumb pipe over `client`:

```
Kafka:  publish    → producer.send(topic=address, headers={correlationId: cid}, value=body)
        awaitReply → consumer.subscribe(replyTopic).poll(window)   matching header correlationId == cid
AMQP:   publish    → channel.basicPublish(address, props={correlationId: cid, replyTo: replyQueue}, body)
        awaitReply → channel.consume(replyQueue)                   matching property correlationId == cid
```

(MQTT 3.1.1 and WebSocket carry the id in the payload rather than a header/property, so the driver injects
and reads it there; `executeAsyncAction`'s shape is unchanged.) The four NCS messaging tests are, in
effect, four such drivers written by hand.

**Which protocol version the driver speaks** is only loosely fixed by the contract. AsyncAPI states it, if
at all, in the server's optional `protocolVersion` (free text like `"5.0"`, rarely set); the one firm
signal is the **binding choice** — the `amqp` binding _is_ AMQP 0-9-1, distinct from the separate `amqp1`
(1.0) binding, and `bindingVersion` names the AsyncAPI binding definition, not the protocol. So the driver
takes the version from the binding plus `protocolVersion` where present, and otherwise from a per-SUT
default (e.g. MQTT **3.1.1**). The same resolved version then steers **test generation**: the emitted
client code is written to match it, automatically (see **The generated test**).

**Who supplies that transport code — two scenarios to choose from.** The `publish` / `awaitReply` above
must be implemented somewhere on the driver side. There are two ways to provide it, and **neither couples
the core**:

- **Scenario A — a shipped, contract-driven transport module.** EvoMaster ships an optional `KafkaDriver`
  / `AmqpDriver` (a ready-made `SutController` base for the standard transport) that reads the AsyncAPI
  document and implements `startSut` and `executeAsyncAction` generically. The user writes almost nothing
  — a thin subclass pointing it at the SUT, plus the per-SUT bits the contract cannot give (a correlation
  field name where undeclared, auth). This is feasible _only because_ the AsyncAPI contract is portable
  and standard — the same reason RPC cannot ship a generic driver. The module depends on the Kafka / AMQP
  client library, but it is a **separate, optional artifact the core does not depend on**.
- **Scenario B — a user-written driver.** For a bespoke wire — a hand-rolled WebSocket protocol, a
  proprietary broker — the user implements the transport code in their own `SutController` subclass, with
  full control at the cost of more effort.

In both, the broker library lives on the driver side of the control protocol; the only difference is
whether **EvoMaster ships it (A)** or **the user writes it (B)**. The core is byte-for-byte identical
either way and imports nothing transport-specific — the decoupling holds regardless of which scenario a
given SUT uses.

**Black-box and white-box are one driver in two modes, not two drivers.** The split is not a different
class but which parts of the same `SutController` the core exercises:

- **Black-box** binds the driver as the core's `RemoteController` and drives actions through
  `executeAsyncAction`, but **never calls `getTestResults`** — there is no coverage to pull; the reply is
  the signal. EvoMaster already runs exactly this shape: its `bbExperiments` mode sets
  `usingRemoteController` and performs a black-box search against a live controller (used there only to
  reset the SUT between tests). Async black-box makes that path first-class, with the controller also
  doing the wire call.
- **White-box** is the _same driver_ with three switches thrown: `isInstrumentationActivated()` /
  `getPackagePrefixesToCover()` so the SUT is instrumented, the core's per-evaluation `getTestResults`
  pull, and a **completion hook** telling the core when the consumer has finished
  (**The white-box approach**).

This "two modes, one representation" split is not new — **REST already works this way**: black-box and
white-box share a single `RestCallAction` and a single `RestIndividual`, and `BlackBoxRestFitness` is
literally a _subclass_ of the white-box `RestFitness` with the coverage pull removed. The mode lives in
the fitness and the module wiring (`RestModule` vs `BlackBoxRestModule`), never in the action or the
individual — precisely the arrangement the async `AsyncMessageAction` / `AsyncApiIndividual` reuse.

The consequence unique to async: it makes **black-box require a driver at all** — the one place it
departs from REST/GraphQL, where black-box needs only a URL. With no universal wire, something must hold
the client, and that something is the `SutController`, exactly as for RPC.

How much of that driver the contract can fill — measured over every `ws` / `wss`, Kafka, AMQP and MQTT
spec in the corpus — splits cleanly:

| What it gives the client                                             | Schema-derivable? | Corpus (3.x, per repo)                                             |
| -------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------ |
| **Connection** — server URL + handshake                              | **yes**           | connectable 79–95%                                                 |
| **Encoding** — JSON / text / binary (`contentType` / `schemaFormat`) | **yes**           | JSON 87–96%                                                        |
| **Addressing + message shapes** → connect + typed send/receive       | **yes**           | **81–89% of repos**                                                |
| **Correlation / framing** → a full request/reply client              | **rarely**        | `correlationId` 4–11%; full client ≤ 8% (mostly samples), 2% on WS |

So the contract reliably auto-fills **connection, encoding and addressing on every transport**,
thinning the driver to its one irreducible job: the wire, plus the correlation hook the schema almost
never declares. Where that hook lives is the gradient from **The four transports and their correlation** — native for
AMQP (the driver need only honour `correlation-id` / `reply-to`), a header name for Kafka, a payload
field for MQTT / WebSocket — so the per-SUT effort _shrinks as the transport's native correlation
grows_, but the driver interface above it never changes.

**How the driver is resolved.** As with any EvoMaster controller, the driver is a `SutController` the user
registers with EvoMaster at launch (there is no auto-discovery) — their own subclass (Scenario B) or a thin subclass of a
shipped transport module (Scenario A). The user launches the driver process; the core **connects** to it
(host and port given at launch), learns from `getProblemInfo()` that the problem is an
`AsyncApiProblem`, asks it to start the SUT, and from then on drives one `executeAsyncAction` per sampled action for the
whole run — holding the single long-lived driver and never importing a broker library itself. That is the
_search-time_ picture; the **emitted suite** is different: like RPC's pure-test mode it is written against
a concrete transport client rather than this control protocol (see **The generated test**).

### Coverage

REST shows what to port. With no code coverage to optimise, SMARTS manufactures coverage
from the response: each **(endpoint, status-code)** pair it observes is a **binary coverage target**
(`GET /products → 200`, `→ 404`, `POST /products → 400` are three), and on top sit **automated
oracles** — an **HTTP 500**, or a body that **violates the declared schema** (where a response validator
is available), is flagged a _potential fault_.
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

A **2.x** service sits **beyond the initial black-box scope** (which targets 3.x — see **Scope** above),
but the unit generalises to it, and stating how matters: the white-box mode does cover 2.x, and the
handful of 2.x request/reply services should not need a second target model if black-box is later
extended. A 2.x service is reconstructed into the same unit **automatically** — from the contract plus
run-time probing, never by reading source. The consume side is mechanical: a channel's `publish` block
is, in 2.x's inverted vocabulary, the operation where _the application receives_ (others publish to it),
the equivalent of 3.0 `receive` (`subscribe` is the `send` side). The reply side has **no contract slot
at all**, so rather than pin it statically the tool **discovers it empirically at run time**: it
publishes a request with a stamped id and watches the channels the contract's `subscribe` blocks declare
— narrowed by a duplex or `*.request`/`*.reply` pairing where present, plus AMQP's native `reply-to` —
for a message echoing that id; whichever channel returns it is the reply channel, and the echo is the
correlation. This is the **same stamp-and-watch** used everywhere (see **Correlating automatically — and
why the contract can't be trusted**), extended only to _discover_ the reply channel 2.x cannot name. The
synthesized identity `(consume channel ↦ discovered reply channel)` then plays the role the 3.0
operation key does — with no human reading the repository. (The code-read in **Are the real services
usable as SUTs?** is a _survey_ activity for measuring the corpus, never part of the running tool.)

Its reach is bounded by the same thing as 3.0: the SUT must echo the id on a channel the tool can watch
— a declared `subscribe` channel, an AMQP `reply-to`, or a broker-wide scan as a last resort — and
where it correlates by business data instead, no black-box tool can pair it. That the model stays
**3.0-shaped** is deliberate: 2.x request/reply is vanishingly rare (3 products in the survey, its
`correlationId` mostly tracing), so the few testable services are reconstructed into the 3.0 shape
automatically rather than given a second, parallel target model.

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

| Axis                   | Observable values                                                                              | REST analogue               |
| ---------------------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **Reply variant**      | which declared `reply` message it validates as (`result`, `error`, …) / matches none           | status _class_ (2xx vs 4xx) |
| **Schema conformance** | reply payload conforms / violates the declared reply schema                                    | response-schema oracle      |
| **Application status** | an explicit code/flag inside the payload (a JSON-RPC `error.code`, a `status: ok\|error` enum) | the status code itself      |

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

| REST fault signal                | AsyncAPI analogue                                                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTP **500** server error        | a reply carrying a **server-fault code** (e.g. JSON-RPC `-32603`, a `status:"error"` with a server code); a SUT crash / connection drop mid-process |
| response **violates the schema** | a reply that matches **no declared reply message** (wrong type, missing required field, out-of-range)                                               |
| —                                | **correlation broken** — a reply arrives whose id is missing or does not match the one sent                                                         |
| —                                | **silent drop** — no reply to an operation whose contract _declares_ one (delivered, but silent past _W_)                                           |

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

### The individual

The parts above — driver, coverage — hang on the object the search actually holds, mutates and finally
serialises into a test: EvoMaster's **individual**. How an async one is shaped is where the
protocol-agnosticism is kept or lost, so it is worth stating explicitly.

EvoMaster gives **each protocol its own individual subclass and one main action type**, over a shared
spine: `Individual` → `EnterpriseIndividual` → `ApiWsIndividual` → `RestIndividual` / `GraphQLIndividual`
/ `RPCIndividual`. An individual is an ordered list of actions partitioned into **groups** —
initialization (SQL / Mongo / Redis seeding), a **main** group of the executable actions under test, and
cleanup — where each main action is wrapped in a group that can also carry its attached external-service
mocks. **RPC is the exact template for async**: its `RPCCallAction` holds an id, a list of input
parameters that _are_ the mutable genes, an **immutable response template**, and a **response filled at
execution** — and, tellingly, the genes it exposes to the search are only the input parameters, never the
response.

Async reuses that spine with **one `AsyncApiIndividual` for all four transports — not one per
transport.** This is the single most important representational decision, and it is the
protocol-agnosticism of **The transport driver** made concrete in the data model: the transport (Kafka
vs WebSocket vs …) appears **nowhere** in the individual. The individual is pure data — the operation,
the payload genes, the declared reply — and Kafka-vs-WebSocket is decided entirely
below the driver interface, in the driver and the fitness function. The same individual with the same genes runs over
any wire; only `send` / `receive` differ. Were the transport to leak into the representation, there would
be a `KafkaIndividual` and a `WebSocketIndividual` — exactly the coupling the approach rejects.

Its main action mirrors `RPCCallAction` almost one for one:

```
AsyncMessageAction:
    operationId        # the coverage unit: the 3.0 operation key,
                       #   or the synthesized 2.x (consume channel ↦ reply channel)
    inputParameters    # THE GENES: request payload built from the message JSON Schema
                       #   (same gene machinery as REST)
    correlationId      # a fresh nonce stamped at each execution — deliberately NOT a gene
    channel            # addressing, from the contract — immutable, NOT a gene
    replyTemplate      # the declared reply message set — immutable; the reply-variant axis
    reply              # filled at execution; read only by the classifier, never a gene

    seeGenes() = inputParameters.genes          # reply excluded, exactly as in RPC
```

Everything the coverage model needs is already here. `operationId` is the endpoint-analogue; the
correlation id is deliberately **not** a gene — searching over it could achieve nothing (the SUT only
echoes it) and pairing demands a value unique to each execution, so the core stamps a fresh nonce at
execution time and matches it on the reply, the way REST handles auth outside the genome; and the reply-variant
classification reads `reply` against `replyTemplate` **at fitness time**, so the search mutates only the
request while the reply drives the `(reply-variant × operation)` targets. Because it is an
`EnterpriseIndividual`, it inherits database seeding in the initialization groups with no async-specific
structure; per-action external-service mocking is the same shared machinery, though it is wired for REST
today, so a new problem type would need to wire it in rather than getting it for free. The individual
itself stays transport-agnostic; the emitted test, though, is written against a _concrete_ transport
client — so, unlike the search representation, its body does vary by transport.

### The life of an action

Driver, coverage and individual meet in the run-time lifecycle of a single action, which is EvoMaster's
**standard `Action` loop** — only two of its steps carry async-specific behaviour:

1. **Built from the contract, once.** At start-up the core parses the AsyncAPI document and, for each
   triggerable operation (a 3.0 `receive`, a 2.x consume block), creates one `AsyncMessageAction` template
   whose genes come from the message JSON Schema via the same builder REST uses.
2. **Sampled and randomised.** SMARTS places one or more such actions in an individual's MAIN group
   (optionally behind SQL-seeding init actions) and randomises the genes.
3. **Mutated.** The search perturbs only `seeGenes()` — the payload genes, boundary-fuzzed — leaving
   `operationId`, `channel` and `replyTemplate` fixed; the correlation id is stamped fresh per run.
4. **Executed — through the driver, never the wire.** The core serialises the genes to a DTO and calls
   `executeAsyncAction` over the control protocol; the driver publishes and awaits the correlated reply
   (**The transport driver**). The core imports no broker library.
5. **Scored.** The reply is classified into a `(reply-variant × operation)` target plus the fault oracles
   (**Coverage**), and the archive keeps one minimal test per newly-covered target.
6. **Emitted.** A retained action is serialised into concrete client code (next).

Only steps 4–5 are async-specific — and they are also the only steps that change in **white-box**: there
the driver reports _processing complete_ rather than a reply, and step 5 reads code coverage instead of
classifying a reply (see **The white-box approach**). Steps 1–3 and 6 are shared across both modes, exactly as
REST shares them across its black-box and white-box fitness. Execution is **single-flight** by default
(one message outstanding, so the reply is unambiguously the one we sent); concurrency is an optimisation
that leans on the correlation id to re-pair replies.

### The generated test

Here the driver is deliberately **left out of the output**. The emitted test is written against a
**concrete version of the transport — a real client — not the driver's control protocol.** This mirrors
EvoMaster's RPC test generation exactly: during the search the core drives the SUT through the driver,
but the test it _writes out_ (under `enablePureRPCTestGeneration`) fetches the **actual client stub** and
calls its real methods, rather than re-invoking the driver's generic `executeRPCEndpoint`. Async follows
suit — a generated Kafka test uses a real Kafka producer/consumer, a WebSocket test a real socket — so
the output is a standard client program a developer can read and run, with no dependency on the driver.
The driver (and its `executeAsyncAction`) governs the _search_; it is **not** what the suite runs against.

Concretely, the generated test is the hand-written shape from **What a request/reply test looks like**
with the genes and the expected variant filled in — for Kafka, `bessj_valid_over_kafka` with a real
producer/consumer:

```
test ncs_bessj__DoubleResult:                   # one test per covered (variant x operation)
    cid      = freshId()
    producer = connectKafkaProducer("kafka:9092")           # a concrete client, not Driver.send
    consumer = connectKafkaConsumer("kafka:9092", topic="ncs.bessj.reply")
    producer.publish(topic="ncs.bessj.request",
                     headers={ correlationId: cid }, body={ n:3, x:2.0 })   # genes -> body
    reply = consumer.pollUntil(match = r -> r.headers.correlationId == cid, within=W)
    assert reply.body.resultAsDouble is finite  # the DoubleResult variant
    assert not reply.body.has("error")

test ncs_bessj__Error:                          # the out-of-range outcome, n below minimum=3
    cid      = freshId()
    producer = connectKafkaProducer("kafka:9092")
    consumer = connectKafkaConsumer("kafka:9092", topic="ncs.bessj.reply")
    producer.publish(topic="ncs.bessj.request",
                     headers={ correlationId: cid }, body={ n:2, x:2.0 })   # boundary-fuzzed genes
    reply = consumer.pollUntil(match = r -> r.headers.correlationId == cid, within=W)
    assert reply.body.error.code == 400          # the Error variant
```

The addressing (`ncs.bessj.request` / `.reply`), the correlation location (a header here) and the message
shapes all come **straight from the AsyncAPI document** — the same values the core used to drive the SUT
during the run, now serialised into concrete client code. Only the **genes** and the asserted **variant**
differ between the two tests. Because the client is concrete, the body **does** vary by transport — the
WebSocket test is the `bessj_over_websocket` socket shape, AMQP the RabbitMQ-channel shape — which is
exactly the per-transport plumbing tabulated in **What a request/reply test looks like**:

|           | concrete client (pre-execution)   | id carried in             |
| --------- | --------------------------------- | ------------------------- |
| Kafka     | producer + reply-topic consumer   | header                    |
| AMQP      | channel + reply queue             | `correlation-id` property |
| MQTT      | client + reply-topic subscription | payload                   |
| WebSocket | one socket to `/ncs`              | payload                   |

The generator also writes the client code **to match the protocol version** the contract resolves to (per
the binding and `protocolVersion` above). This is where the version pays off: an **MQTT 5.0** test places
the id in Correlation Data with a Response Topic, an **MQTT 3.1.1** test hand-rolls it into the payload,
and an **AMQP 0-9-1** test uses the native `correlation-id` / `reply-to` properties — the generator emits
the version-correct calls automatically, falling back to the default only when the contract is silent.

Unlike a black-box REST test, the emitted suite is **not self-contained**: it depends on the **concrete
transport client** — the client library on the classpath and (for a bespoke wire, as with RPC's
`getRPCClient`) whatever hands it its connection — the concrete form of "a transport client must exist".

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

## The white-box approach: coverage as the signal, completion as the problem

### A consume operation is an async action

The engine is reused wholesale: EvoMaster's **white-box search — MIO with the branch-distance gradient**,
its **Driver** (`SutController`) that starts, instruments and resets the SUT, its database seeding, and
its external-service (WireMock) machinery — all stay (though the last is wired only for REST today, so a
new problem type must wire it in). Async adds one thing: a **new kind of action** — the
`AsyncMessageAction` of **The individual**, here possibly reply-less — and the lifecycle to run it.
Black-box and white-box thus **share the action and the individual**; only the fitness differs — the
same "two modes, one representation" split, with its REST precedent, described under **The transport
driver**.

For each `receive` operation (3.0) or consume block (2.x) in the AsyncAPI document, EvoMaster builds
the message payload exactly as the black-box side does — the genes of **The individual** — publishes it
to the SUT's channel, and then **waits for the SUT to finish processing it** before reading coverage.
With that wait in place, coverage over the consumer's code is the fitness, and MIO climbs it exactly as
for a REST endpoint. No reply is required, so fire-and-forget operations are first-class — and
correlation, the crux of the black-box approach, stops being central: nothing needs pairing for the
search to score a test.

### Solving "when did it end"

This is the crux. The signal can come from the SUT's own code, the effects
it leaves behind, the broker, or the clock — and the axis that matters is **how much each option must
know about the SUT**: its application framework (Spring / Micronaut / Quarkus / a plain client) and its
transport (Kafka / AMQP / MQTT / …). The right **default assumes nothing** and reuses instrumentation
EvoMaster already has; knowing the framework is an _optimization_ that buys precision, not a prerequisite.
Ordered most-agnostic first — precision rising as the tool is willing to know more:

1. **Instrumentation-probe inactivity — the default (agnostic to framework _and_ transport).** White-box
   already weaves bytecode probes into the SUT to compute coverage; as the consumer processes our message
   it executes instrumented code and those probes fire. So "done" is simply **the SUT's probe activity
   going quiet for a debounce interval** — a signal that knows nothing about Kafka or Spring, because it
   watches the SUT _execute code_, which is exactly what is already instrumented. It is always available
   and reuses the core mechanism. The costs are real but bounded: background threads (schedulers, health
   checks) add probe noise to filter out, and pinning quiet-time to _our_ message needs single-flight or
   thread tagging (below).
2. **A downstream side effect — also agnostic, and it doubles as an oracle.** Observed _below_ the
   messaging framework — at the JDBC and HTTP layers EvoMaster already intercepts — so it is independent
   of both framework and transport, and it tells us not just _when_ the handler finished but _what_ it
   did:
   - a **database write** surfacing in the per-action SQL snapshot the core already captures;
   - an **outbound message or external call**, intercepted by the external-service (WireMock) machinery
     (shared code, but wired for REST today — a new problem type must wire it in);
   - an **outbox / inbox / dedup row keyed by message id** — a near-perfect signal that is also
     **self-attributing under concurrency**, since the row carries _our_ id;
   - a **metric / counter delta** (a Micrometer processed-message counter) or, most brittle, a **terminal
     log line** correlated to our message.
     The limit is that a pure-compute handler with no observable effect gives nothing — so this sharpens or
     cross-checks probe inactivity rather than replacing it.
3. **Broker and transport-client signals — framework-agnostic, transport-specific.** These need one hook
   per _transport_, but none per framework, because every framework rides the same wire client:
   - **broker state** — a Kafka **committed offset / consumer lag** advancing past our record, or a
     RabbitMQ **queue depth** (ready + unacked) returning to baseline; observed off the broker, needing
     nothing from the SUT;
   - a **transport-client hook** — instrumenting the wire client itself (the Kafka `Consumer` commit, the
     RabbitMQ `Channel.basicAck`, the Paho MQTT callback) catches _every_ Spring / Micronaut / plain
     consumer built on that client with a single hook;
   - a **fence / sentinel** — publish a marker to the same partition/queue right after the test message;
     in-order delivery (a transport guarantee, not a framework feature) means that once the marker is
     observably handled — its offset commits, it is dead-lettered — our message is already done. Breaks
     under parallel consumers/partitions, and the marker still needs some observable, usually the offset
     commit above.
4. **The handler boundary — the precise option, when the framework _is_ known.** Knowing it is Spring
   Kafka, JMS, and so on buys the tightest, most attributable signal, hooked at the point that best
   matches the design — the obvious one is often too early:
   - the **listener method** entry/return (`@KafkaListener` / `@RabbitListener` / `@JmsListener`);
   - the **ack / commit** — `Acknowledgment.acknowledge()`, a Kafka offset commit, a RabbitMQ `basicAck`,
     or a `@Transactional` listener's commit — where the application declares it is done, later than the
     method return in hand-off designs;
   - the **terminal signal of a returned reactive type** (`CompletableFuture` / `Mono` / `Flux`), since a
     reactive handler returns an unresolved publisher immediately — "done" is its `onComplete` / `onError`;
   - the **whole task tree** — an **in-flight counter** that increments at handler entry and decrements at
     return, and follows the handler's hand-offs (instrumented `Thread.start` / `Executor.submit` /
     `CompletableFuture`) so background work our message spawns is awaited too, not just its top frame;
     the counter returning to zero is _done_.
     These need not weave user code either: register a **framework interceptor** (Spring Kafka
     `RecordInterceptor`, an AMQP advice) or subscribe to the SUT's existing **OpenTelemetry / Micrometer
     consume span** and wait for the span matched to our message to close. This family is the shape the
     `scheduletask` hooks are meant for — though, as the implementation section shows, only half-wired
     today (below).
5. **A timeout — the last resort, when nothing above fires.** A window _W_, the white-box analogue of
   black-box's observation window; a fixed _W_ is arbitrary, an **adaptive** one profiled from warm-up
   handler durations less so. Too short truncates coverage, too long slows every test, and slow-vs-stuck
   stays undecidable from outside.

**Which thread is ours, and following its hand-offs.** The precise options above need to know _which_
thread is processing _our_ message — and that is not known in advance: the broker dispatches onto a
listener thread we neither created nor hold. It is learned **at handler entry** — the instrumented
delivery method runs on the worker thread (`Thread.currentThread()` in the probe _is_ the worker,
whatever the framework picked), and reading back the **id we stamped** into the published message confirms
the invocation is ours. (It is the same id the black-box side uses, and it rides in the message even for
fire-and-forget, where there is no reply.) From that thread a task-local tag propagates through the
instrumented hand-offs, so the in-flight counter counts only work descended from our message. Where the
entry point cannot be hooked, **single-flight** makes this moot — with one message outstanding, any
consumer activity is necessarily ours.

**Coverage is transport-agnostic; only the hook is per-library.** Collecting coverage is _not_
transport-specific — the probes are woven into the SUT's own classes regardless of wire — so any
instrumentable JVM SUT is coverage-testable. Only the _precise_ completion hook is framework-specific, and
it targets the transport **library's** delivery method, an enumerable set: Spring Kafka / AMQP / JMS for
brokers, and for WebSocket `jakarta.websocket` `@OnMessage`, Java-WebSocket `onMessage`, Spring
`TextWebSocketHandler`, or Netty's frame handler. A "custom WebSocket" is almost always a bespoke message
format on one of these libraries, so it is still hookable. The genuinely hard case is a wire hand-rolled
on **raw sockets with no library boundary** (e.g. `free-note-service`, graded not-usable in the corpus
slice for exactly this reason): there the fallback ladder is **agnostic completion (probe inactivity /
side effect / timeout) → single-flight → a per-SUT entry-point hint** (the user names the handler
`class#method`, à la `getPackagePrefixesToCover`). Precision and parallelism are lost; testability is not.

Orthogonally, completion can be **forced rather than detected** by collapsing the asynchrony at test time:
drive the listener **synchronously** (invoke the handler directly, or run the container at concurrency = 1
and pump a single poll), or swap the broker for an **in-VM one that dispatches on the calling thread**.
Either turns "done" into a plain method return — the cleanest signal there is — but does not exercise the
production transport's real timing, trading fidelity for determinism rather than being strictly better.
**Single-flight** (one message outstanding) is the mild version: it keeps the real transport yet makes
probe inactivity unambiguous and every completion trivially attributable.

### Implementation: extending the scheduletask machinery

EvoMaster already has _partial_ scaffolding, built for a neighbouring problem. Its **`scheduletask`**
mechanism (`ScheduleTaskAction`, `ScheduleTaskExecutor`, `ScheduleTaskActionResult`) models **deferred
work** as an action, and the Driver exposes two hooks — `customizeScheduleTaskInvocation(...)` to
_trigger_ it and `isScheduleTaskCompleted(...)` to _report when it finished_ — the right shape for
"invoke async work, then know it is done." But it is scaffolding, not a finished mechanism, and closing
three gaps is the proposal's actual content:

- **The completion hook is inert.** `isScheduleTaskCompleted(...)` is _defined but never called_ by the
  framework today — the current flow invokes `customizeScheduleTaskInvocation` once and records its
  returned status immediately, with **no wait-for-completion loop**. The proposal must add that loop (or
  have the driver block/poll internally and return `COMPLETED`); this is where the completion mechanisms
  above plug in.
- **The path is RPC-bound.** Sampling is gated RPC-only (`probOfSamplingScheduleTask`) and invocation
  runs through `RPCFitness` and RPC-namespaced DTOs, so extending to AsyncAPI means a new sampler/fitness
  path or lifting this code out of the RPC package — not a flag flip.
- **`ScheduleTaskAction` is an init `EnvironmentAction`** (it does not count for fitness), so the consume
  operation is not literally a `ScheduleTaskAction` but a **new MAIN, coverage-bearing action** reusing
  the same trigger/completion hooks.

With those closed, the mapping onto existing machinery is:

| Piece                | Reused / extended                                                                                                                                             | What it does for a consume operation                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action + individual  | a **new MAIN consume action** in `EnterpriseIndividual` (modelled on `ScheduleTaskAction`'s lifecycle, but fitness-bearing — not an init `EnvironmentAction`) | one action per `receive`/consume operation, sampled and mutated by MIO                                                                                                                                                             |
| **Input generation** | REST's schema→gene builder                                                                                                                                    | build the message payload from the AsyncAPI message JSON Schema                                                                                                                                                                    |
| **Invocation**       | `customizeScheduleTaskInvocation` (Driver-side)                                                                                                               | the Driver publishes the message to the SUT's broker/channel — it holds the transport client, exactly as an RPC Driver holds the RPC stub                                                                                          |
| **Completion**       | `isScheduleTaskCompleted` hook + a **new wait-loop** that calls it                                                                                            | by default, detect completion agnostically — instrumentation-probe inactivity, a downstream write/emit, or broker/offset state — and, when the framework is known, sharpen it with a handler-boundary hook; timeout as last resort |
| **Fitness**          | standard branch-distance coverage                                                                                                                             | collected at completion; for request/reply operations, add the black-box reply oracle as an extra target                                                                                                                           |

Relative to RPC schedule tasks, the genuinely new pieces are: the trigger is a **broker publish** rather
than a direct method call; the operations and input schemas come from an **AsyncAPI document** rather than
RPC reflection; and — the real addition — the **wait-for-completion step**, which today's schedule-task
flow lacks. The target run lifecycle is sample → invoke → **wait for completion** → collect coverage →
MIO: the sample, collect and MIO stages reuse existing machinery, while the broker invoke and the wait are
what this proposal builds.

The open engineering items are correspondingly focused:

- **The agnostic completion default** — wiring instrumentation-probe inactivity and the side-effect
  signals (SQL snapshot, external-call interception) the core already produces, so completion works with
  no per-framework code; the optional per-**library** delivery hooks (Spring Kafka, Spring AMQP, JMS, and
  for WebSocket `jakarta.websocket` / Java-WebSocket / Spring `TextWebSocketHandler` / Netty) are the
  precision upgrade layered on top — an enumerable set, since coverage itself is already transport-
  agnostic — with a timeout, or a per-SUT entry-point hint for a raw-socket wire, as the final fallback.
- **Wiring completion and lifting it out of RPC** — the biggest lift: the `isScheduleTaskCompleted` hook
  is inert, so the wait-for-completion loop must be added, and the schedule-task path must gain an
  AsyncAPI sampler/fitness route (or be generalised out of the RPC package).
- **Attribution under concurrency** — identifying our worker thread **at handler entry** by the stamped
  id and tagging its hand-off lineage into an in-flight counter, or serialising to **single-flight** when
  the entry point cannot be hooked. The counter's thread/executor hooks are **new instrumentation** — no
  existing hook targets `Thread`/`Executor` — though EvoMaster's method-replacement framework and its
  DynamoDB `CompletableFuture` tracker are a close template.
- **Timeout tuning** — the completion timeout as a first-class, reported parameter, since (as in
  black-box) slow-vs-stuck is undecidable from outside the handler.

### What the generated white-box tests look like

One design question the coverage-driven search leaves open is the **output**: what does an emitted test
_assert_? Coverage cannot be the answer — it was the **search signal**, not a regression check; a test
that "asserts coverage" would be meaningless to a developer and brittle to any refactor. The emitted
test instead asserts on the **observable residue** of the processing that the completion mechanisms
already capture during the search. Ranked by how much of EvoMaster's existing assertion machinery each
one reuses:

1. **The publish completed without exception** — the existing try/catch + `fail(...)` emission,
   reusable as-is; the floor (a broker ack is not processing).
2. **A message the handler emitted onto another channel** — the strongest oracle: the test subscribes
   there, and the full REST/RPC payload machinery applies to that message (field matchers, list sizes,
   capped collections, volatile fields skipped) — in effect a "reply on another channel."
3. **The database rows the handler wrote** — read back and asserted RPC-style (typed, field-by-field
   equals, capped, unsafe values emitted commented-out); the comparison template exists, the
   **read-back is new machinery**.
4. **The external call the handler made** — WireMock stubs are already emitted into white-box suites
   but never verified; adding `verify(...)` is a one-line extension that turns the existing mock from
   stimulus into an oracle.
5. **Completion within the window** — the await doubles as an implicit assertion (timeout ⇒ fail),
   with the already-emitted per-test `@Timeout` as the hard ceiling; the await loop itself is new
   (nothing asynchronous has ever been emitted before).
6. **The SUT survived** — a health probe through the fixture's controller, generalising the existing
   `assertNotNull(baseUrlOfSut)` sanity idiom: it separates "crashed the consumer" from "processed
   quietly."

Where the operation *does* declare a reply, the black-box reply assertions ride along unchanged. And
three deliberate don'ts, each backed by an existing convention: no **absence** assertions (proving
silence is inherently flaky — a missing expected message is recorded as a comment, per the
flaky-to-comment rule); no **log or metric** assertions (no precedent, and the completion taxonomy
already calls the log line the most brittle signal); never **coverage** (run-time knowledge belongs in
comments, as REST's `// last executed statement` hint on 500s shows — an async test can annotate the
handler reached and the completion mechanism used the same way).

So a fire-and-forget test reads: publish the generated message with a concrete transport client (exactly
as in **The generated test** — the driver governs the search, not the output), await the completion
proxy (the observable side effect, or a bounded wait), then assert on the state the handler left behind.
At replay the SUT runs **uninstrumented** — but the suite is not driver-free: like every white-box suite
EvoMaster emits, it scaffolds on the driver (`SutHandler controller` in the fixture; `startSut()` before
the class, `resetStateOfSUT()` before each test — for async also draining reply topics and queues —
`stopSut()` after), while the **concrete transport client is only the wire**. That is exactly the split
the emitted REST suites already show: driver for lifecycle and state, client library for the calls.

The through-line of that menu: **assert-what-you-observed is EvoMaster's house style** — REST bakes the
response captured during the search into `.body("field", equalTo(…))` matchers, RPC generates typed
`assertEquals` scripts on the response object, and anything unstable across evaluations is demoted to a
"flaky" comment — and the async assertions inherit it wholesale: the values asserted are the ones the
search observed. (RPC also shows a second emission route — the driver itself generates the invocation
and assertion scripts, which the writer replays verbatim — an option for the transport-specific publish
code.) Netting it out, the genuinely new emission machinery is exactly **two pieces**: the
**subscribe/await plumbing** (items 2 and 5) and the **database read-back** (item 3 — emitted suites
today only _write_ DB state through the seeding DSL; a small driver-side query helper is needed to read
it back) — plus the one-line WireMock `verify` extension (item 4). Everything else reuses writers that
already exist.

Grounded in the same controlled NCS SUTs as the black-box approach, the evaluation would
then measure what black-box could not even attempt: coverage achieved on **fire-and-forget** consume
operations, over the JVM transports, with completion resolved by instrumentation. One evaluation asset
must be built first: the current NCS messaging SUTs are **request/reply throughout** (every operation
declares a reply), so the suite must gain **fire-and-forget variants** — consume-only operations with no
reply and an observable side effect (a database write, an emitted event) — before the headline
fire-and-forget measurement can run. Authoring those variants is an explicit deliverable of this
proposal, not an assumption.

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

| Signal                    | Weight | How it is read                                                                                                                                                                          |
| ------------------------- | -----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub topic              |     +3 | substring-matched against ordered fragment groups (demo → tool → product → spec, first group wins): `documentation-generator` → tool, `schema-registry` → product, `json-schema` → spec |
| description + README lead |     +2 | per-bucket keyword regexes (below); unambiguous demo markers score +3, weak product cues only +1                                                                                        |
| repository name           |   +1–2 | `*-sample` / `*-demo` → demo, `*-cli` / `*-sdk` → tool, `*-spec` → spec                                                                                                                 |
| spec-file location        |     +1 | specs only under `tests/` / `fixtures/` → tool + demo; a spec at repo root or `docs/` → product                                                                                         |
| docs-only language        |     +1 | HTML / MDX / Markdown / TeX … → spec/docs                                                                                                                                               |

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
