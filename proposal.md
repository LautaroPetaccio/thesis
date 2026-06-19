# Black-Box Testing of AsyncAPI Services in EvoMaster

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

The natural question for the problem domain, then, is how often that observable pattern actually
occurs in real AsyncAPI specs, and over which transports — which the next section surveys.

## Request/reply in the wild: a corpus survey

To characterize the problem domain, we surveyed the **public AsyncAPI corpus** on GitHub — both major
versions — for how common the observable request/reply pattern is and over which transports. The
version split drives how we measure it: AsyncAPI **3.0** has a first-class `reply`, so the pattern is
detected structurally; **2.x** has no reply construct, so its only native way to link a response to a
request is a message **`correlationId`** — we measure each version with its own native signal.

**Method.** We enumerated every AsyncAPI document discoverable through GitHub code search — versions
**2.0–2.6** and **3.0.0 / 3.1.0** (`.yaml`/`.yml`/`.json`, size-bucketed to beat the 1,000-result API
ceiling) — then fetched and parsed each one. In **3.x** we structurally detected operations with
`action: receive` **and** a `reply`; in **2.x** we detected the **Correlation ID Object** (a message
`correlationId` with a `location` runtime expression). For each hit we attributed the messaging
protocol from the channels' servers and bindings. **Both** corpora's repositories were then classified
as **product**, **tool/library**, **demo/fixture** or **spec/docs** by the same two-layer method
(deterministic rules + an LLM refinement pass; methodology in the appendix), so we could see _who_
writes these specs. Scripts and full output live under `asyncapi-survey/` (reply/correlation detection
in `asyncapi_reply_protocols.py` / `asyncapi_correlation_2x.py`; classification in
`asyncapi_classify_repos.py` + the LLM pass, run over each corpus).

**The corpus at scale.** The survey parsed **4,151 AsyncAPI 3.x specs** (across **984** repositories)
and **2,701 AsyncAPI 2.x specs** (of 3,189 candidates, across **1,108** repositories, 1,103 still
resolvable). Both corpora were classified by kind the same way — a baseline for how AsyncAPI is used
at all, before narrowing to request/reply:

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

Both versions look alike at this scale: **product** and **demo/fixture** are the two largest kinds in
each, so AsyncAPI overall is used about as much for real services as for teaching and examples. (The
2.x classification leans more on the LLM refinement layer than 3.x — the rules were tuned on 3.x — but
is built the same way; see the appendix.)

**Protocols across the whole corpus.** Which transports do these specs declare at all, before
narrowing to request/reply? Of the specs that name a transport — **1,397 of 4,151 in 3.x** and
**1,627 of 2,701 in 2.x** (the rest are transport-agnostic examples) — the document-level protocols
(servers + bindings) are:

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

A long tail follows in single digits to low-20s (Google Pub/Sub, AnypointMQ, JMS, Pulsar, STOMP,
explicit MQTT5, AMQP 1.0, Mercure; full list in `protocol-usage.md` under `asyncapi-survey/`,
reproducible via `asyncapi_protocol_usage.py`). The same four transports lead **both** versions —
**Kafka, WebSocket, MQTT and AMQP** (HTTP aside, the REST-degenerate case): Kafka leads by spec count
(and is the most spec-dense), WebSocket is the most widely adopted by repository, and together with
MQTT and AMQP they are the transports worth pursuing — the rest are a thin, fragmented tail led
distantly by NATS and Redis. These four are exactly the ones detailed in **The transports in play**
below. The request/reply subset is the thin slice within all this, which the rest of this section
drills into.

**The observable signal, by version.** The two versions land at almost the same rarity, each by its
own native signal. In **3.x**, **122 specs across 81 repositories** (~2.9% of the parsed 3.x specs)
declare at least one `receive`+`reply` operation — **356 operations** in total. In **2.x**, **55 specs
across 36 repositories** (2.0% of the parsed 2.x specs) declare a `correlationId`; it almost always
rides in a **header** (46 specs) rather than the **payload** (7; 2 are invalid), and — tellingly —
only **9 of the 55** also show any request/reply shape (request/reply-suggestive names, or a duplex
`publish`+`subscribe` channel). The rest attach the id to one-way events: the fields it points at are
mostly tracing/business keys (`transactionId` is the single most common, plus `traceId`, `businessId`),
so in 2.x the Correlation ID Object is used predominantly for **distributed tracing, not for pairing a
reply with its request**. These are two different lenses — structural reply vs correlation id — so the
counts below are reported per version, not merged.

**Protocols, both versions.** The table pairs each transport's 3.x reply-scoped count (the protocols
of the channels each `receive`+`reply` operation touches) with its 2.x `correlationId`-spec count. The
two columns are **different signals** — 3.x structural reply operations vs 2.x correlation-id presence
— so they are not comparable counts; `—` means none was found for that version.

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

The header-carrying brokers — **Kafka, AMQP and MQTT** — dominate in both versions, which is exactly
where a correlation id has somewhere to live; WebSocket, SQS, Google Pub/Sub and STOMP appear only as
3.x reply operations, and NATS only via a 2.x correlation id. The 3.x `repos` counts overlap (a repo
may use several protocols) — as do the operation counts, since one operation can touch more than one
protocol, so the column sums above the 356 total — and the 186 _undetermined_ 3.x operations come from
**transport-agnostic** specs that declare no server protocol or binding — common in the examples and fixtures where most of
these specs live (below).

† The **HTTP** reply ops are synchronous request/response modeled with AsyncAPI's HTTP binding (the
request channel is a URL path, the operation carries an `http.method`, and the reply is the HTTP
response on the same channel) — observably plain **REST**, already covered by EvoMaster's native HTTP
mode rather than needing any async transport machinery. All are tooling/library or demo fixtures —
mostly the canonical AsyncAPI ping/pong and HTTP-binding example specs vendored into converters/code
generators, plus one Socket.IO case and one mislabeled Streetlights-Kafka spec; **no products**.

**Who writes the reply-pattern specs** — those 81 repositories, classified:

| Repository kind |  repos | examples (with reply transport)                                                                                                                   |
| --------------- | -----: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| tool / library  |     30 | `asyncapi/generator`, `microcks`, `specmatic`, `zod-sockets`                                                                                      |
| demo / fixture  |     23 | `aklivity/zilla-demos`, the Kraken-WebSocket and ping-pong examples                                                                               |
| **product**     | **13** | `EVerest` (MQTT), `voiceblender`, Netcracker qubership integration platform, `ollert-backend` / `sigaa-socket-api` (WebSocket), `vequate` (Redis) |
| spec / docs     |     12 | `asyncapi/spec`, `OAI/Arazzo-Specification`                                                                                                       |
| uncategorized   |      3 | —                                                                                                                                                 |

The contrast with the full corpus is itself a finding: where AsyncAPI 3.x overall splits almost
evenly between products (262) and demos (261), the request/reply _subset_ skews differently — it
lives mostly in **tooling test-fixtures and teaching examples** (53 of 81 repos), with a smaller
core of **13 genuine products** — the repositories where the request/reply pattern actually occurs
(`voiceblender`, a real custom-WebSocket service, is among them). A second nuance: Kafka leads by
repository count, but all of those are non-products — tooling, spec and demo repos, the recurring one
being copies of a single widely-vendored example (`adeo-kafka-request-reply`) alongside a cluster of
Specmatic contract-testing samples — and **none** of the 13 products use Kafka for their reply
operations; the products use WebSocket, MQTT, AMQP and Redis. This is not because Kafka is rare in
practice, but because products overwhelmingly use it for fire-and-forget event streaming, which falls
outside the observable request/reply subset surveyed here. That spread of mutually incompatible transports,
thinly populated across so few real systems, is itself a core difficulty of the problem.

The 2.x picture converges on the same finding — and now that both corpora are classified the same way,
it can be said in the same terms. Of the **32 distinct repositories** behind those specs (the 36 above
counts a few forks that re-host the same spec), only **3 are products**; the rest are tooling/library
(13), demo/fixture (10), spec/docs (3), tangential (2) and one uncategorized — conformance test kits,
parser and comparison-tool fixtures, and the vendored
multi-protocol and adeo example specs. And, as noted above, most of those ids do tracing rather than
reply-matching. So across **both** versions the observable
request/reply construct — a 3.0 `reply`, or a 2.x `correlationId` — is rare and lives mostly in
test-fixtures and teaching examples rather than in real products: the same scarcity, seen through two
different lenses. (Caveat: the 2.x corpus enumerated here is `.yaml`-only, so true 2.x prevalence may
be marginally higher.)

## The transports in play

AsyncAPI is not itself a protocol — it is realized over whatever transport a service happens to use,
and the survey above shows the request/reply services scattered across several mutually incompatible
ones (WebSocket, MQTT, Kafka, AMQP, and a long tail of SQS / Google Pub/Sub / STOMP / Redis / HTTP).
Any black-box approach has to understand each of them, because they share nothing at the API level.
The four described below span that spectrum — from full-featured brokers (Kafka's streaming log,
AMQP's queues and exchanges), through MQTT's deliberately minimal pub/sub, to WebSocket's
broker-less, fully custom frames.

### Kafka

Apache [Kafka](https://kafka.apache.org/) is a distributed event-streaming platform. Producers
append records to **topics** that are split into **partitions** across the cluster; within a
partition records keep their order and are **retained** for a configured window, so the same record
can be read more than once. **Consumer groups** read independently, the broker tracking each group's
committed **offset** rather than deleting what has been consumed. A record is a key, a value, and —
since v0.11 — a set of **headers** (`(string, bytes)` pairs). The topic model maps cleanly onto
AsyncAPI channels (topic = channel), the most standardized end of the spectrum.

### AMQP

[AMQP 0-9-1](https://www.rabbitmq.com/) (most commonly RabbitMQ) is a traditional message broker
built around **exchanges** and **queues**: a producer publishes to an exchange, which routes the
message — by binding and routing key — into one or more queues that consumers read, with messages
typically removed once **acknowledged** (unlike Kafka's retained log). Beyond its body, every message
carries a structured envelope of standard **properties** defined by the protocol — among them
`correlation-id` and `reply-to`. It is the most feature-rich of the four for point-to-point exchange.

### MQTT

[MQTT](https://mqtt.org/) is a lightweight publish/subscribe protocol built for IoT and constrained
networks. Clients connect to a broker (such as [Eclipse Mosquitto](https://mosquitto.org/)) and
publish to hierarchical **topics** (with `+`/`#` wildcards) at a chosen **QoS** level (0
at-most-once, 1 at-least-once, 2 exactly-once). It is intentionally far simpler than Kafka — no
partitions, no consumer-group offsets. Its two live versions differ in one capability that matters
here: **3.1.1** messages carry nothing beyond the topic and payload, whereas **5.0** adds optional
`PUBLISH` properties — **User Properties** (string key/values), **Correlation Data**, and a
**Response Topic**.

### WebSocket

A [WebSocket](https://datatracker.ietf.org/doc/html/rfc6455) (RFC 6455) is a single, long-lived,
bidirectional connection, upgraded from an HTTP handshake, over which client and server exchange
**frames** (text or binary) freely in both directions. It is not a messaging system: there is no
broker, no topics or channels, no delivery guarantees, and no message metadata — just a duplex pipe,
on top of which every service layers its **own** application-level protocol. A reply on the same
socket is the most natural request/reply shape, which is why WebSocket is the **most common reply
transport in the survey** — 73 of the 356 reply operations, plus 11 more over the secure `wss`
variant.

## Transports and correlation

A reply is only observable if the tester can tell _which_ request it answers. That is the job of a
**correlation id**: the requester stamps a unique value on the request, the responder copies it onto
the reply, and the tester pairs the two. Because EvoMaster drives every transport as a black box,
correlation is the one mechanism it must perform identically everywhere — yet each transport offers a
different place to carry the id.

AsyncAPI 3.0 captures that place in a machine-readable way. A message can declare a
**`correlationId`** object whose `location` is a runtime expression pointing at where the id lives —
either `$message.header#/<field>` (in transport metadata) or `$message.payload#/<field>` (inside the
body). The same expression is attached to both the request and the reply message, so a tool that
reads it knows where to _write_ the id when sending and where to _read_ it when a reply arrives,
regardless of the wire format. Whether that expression can resolve to a header or only to the body,
however, is decided by the transport:

| Transport  | Where the id can live                          | Native to the protocol?             | Reply destination                  |
| ---------- | ---------------------------------------------- | ----------------------------------- | ---------------------------------- |
| AMQP 0-9-1 | `correlation-id` **property**                  | **yes** — standard message property | `reply-to` property                |
| Kafka      | record **header** (e.g. `kafka_correlationId`) | no — opaque header, named by a lib  | reply-topic header (by convention) |
| MQTT 5.0   | **Correlation Data** (or a User Property)      | **yes** — added in v5               | **Response Topic** property        |
| MQTT 3.1.1 | inside the **payload**                         | n/a — no metadata exists            | encoded in the payload             |
| WebSocket  | inside the **payload**                         | n/a — custom app-level protocol     | encoded in the payload             |

**AMQP** is the most accommodating. `correlation-id` and `reply-to` are first-class message
properties, and the request/reply ("RPC") pattern built on them is the canonical one in the RabbitMQ
documentation — a responder that echoes `correlation-id` and answers on `reply-to` is the norm, not
an invention. A black-box tool can set both on the request and read `correlation-id` back from the
reply without touching the payload at all.

**Kafka** also keeps the id out of the body, in a header, but that header has no protocol-defined
meaning: the names (`kafka_correlationId`, `kafka_replyTopic`) and the echo-on-reply behaviour come
from a client library (Spring Kafka), not from Kafka. Attaching the header is trivial; whether the
reply carries it back depends on the SUT following that same convention — which is why almost every
Kafka reply example in the corpus is a copy of one Spring-Kafka sample (`adeo-kafka-request-reply`).

**MQTT** splits on version. **5.0** has Correlation Data and a Response Topic — effectively AMQP-like
— but the survey shows almost no one opts in: of the **219 MQTT specs (116 repos)** in the 3.x corpus
only **10** (across 2 repos) carry an explicit 5.0 binding, the rest leaving the version unset (2.x is
the same story — 5 of 281). Since **3.1.1** is the de-facto default and carries **no metadata at all**,
a black-box tool cannot count on the v5 features and must place the id **inside the payload** — which is
what these MQTT contracts encode anyway.

**WebSocket** is the hardest. With no broker, no headers, and no standard protocol, the id always
lives **in the payload**, in a field whose name and shape each service invents. There is nothing
off-the-shelf to attach; a tool can only follow the `correlationId.location` the contract declares
(e.g. `$message.payload#/correlationId`) and trust the service to be internally consistent. The real
custom-WebSocket services in the survey hand-roll it their own way — `voiceblender`, for instance, echoes
a `request_id` field inside the payload.

For our purpose the transports therefore form a gradient: **AMQP** fits black-box request/reply best
(native, conventional, payload-agnostic); **Kafka** is nearly as workable but leans on a framework
convention; **MQTT** and **WebSocket** push correlation into the payload, coupling the tool to each
message schema and, for WebSocket, to a bespoke per-service protocol.

### Can the messages be correlated automatically?

Sending a correlated request is the easy half, and it is entirely on our end: the
`correlationId.location` expression tells the tool where the id belongs, so EvoMaster generates a
fresh value and places it — as a header/property where the transport has one (AMQP, Kafka, MQTT 5.0)
or inside the payload where it does not (MQTT 3.1.1, WebSocket). No SUT cooperation is needed to
_send_ it.

The correlation itself, though, is **built by the SUT, not by us**. A request and a reply only become
a matched pair once the responder copies our id onto the message it sends back; until it does, there
is nothing for the tool to pair. That step is the service's own behaviour and lies outside black-box
reach — we can set the id and watch for it, but we cannot make the service echo it. How reliably it
happens is a property of the SUT: with AMQP (and MQTT 5.0) echoing `correlation-id` is the documented
norm, with Kafka it follows only if the SUT uses the matching client library, and with MQTT 3.1.1 and
WebSocket it is whatever the service's hand-rolled protocol chose to do. The tool can _detect_ when
correlation was not built — a reply that arrives with a missing or non-matching id is itself an
observable conformance failure — but it cannot supply it.

Two consequences follow. The contract must actually declare `correlationId` for any of this to be
automatic; when it is omitted — common in this example-heavy corpus — there is no anchor, and the
tool falls back to heuristics (a lone id-shaped field, or single-flight / timing assumptions). And it
assumes the SUT correlates the way the contract implies: **one opaque id, echoed verbatim**. Services
that mint a new reply id, spread correlation across several fields, or key off business data still
correlate their messages — just not in a way a generic tool can follow without per-service handling.
In short: **we can always inject the id; whether the messages end up correlated is decided by the
SUT** — a black-box tool can require correlation (via the contract) and verify it (via the reply), but
the act of correlating is the service's to perform.

### Reading the implementation: which transports' correlation can a tool rely on?

Because the contract so rarely declares correlation (2.0% of 2.x specs above; and even in 3.x the
`correlationId.location` is frequently absent) — and is unreliable even when it does — whether a given
service can be correlated black-box is ultimately an **implementation** property, decided by reading
the repository, not the document. Reading real Kafka, AMQP and MQTT services shows three very different
situations (named per-repo evidence is in `corpus-suitability.md`):

- **AMQP — decidable, and usually yes.** Correlation rides in the protocol's native `correlation-id`
  and `reply-to` message properties, and the RabbitMQ "RPC" convention is canonical. The one thing to
  verify by reading the code is that the responder **echoes** the inbound `correlation-id` and answers
  on the inbound `reply-to`; when it does, a black-box tool can pair replies knowing only that it is
  talking to RabbitMQ — no `correlationId` in the document required.
- **Kafka — decidable only by reading the code.** Kafka has no native correlation; it is a
  per-implementation **header convention**. The header name varies from service to service (and is
  usually not the client library's default), so a tool cannot guess it — it must read the
  implementation — and even then correlation is **not guaranteed**, since an implementation may fail to
  echo the inbound id back onto the reply.
- **MQTT — read the payload or the topic scheme.** MQTT 3.1.1 (the de-facto corpus default) has no
  headers or properties at all, so correlation is hand-rolled, either as a field **inside the payload**
  or as a per-request reply-**topic** convention; even services that negotiate MQTT 5.0 often leave its
  native Correlation Data and Response Topic unused. There is nothing transport-level to rely on.

In every case the AsyncAPI `correlationId` is a **hint to verify, not a guarantee**: services correlate
correctly with no declaration at all, others declare one the code does not honour, and several MQTT
documents declare a `$message.header#/…` location the header-less 3.1.1 wire cannot carry. The only
reliable check is **empirical** — stamp an id on the request and see whether the reply carries it back.

## SUT usability of the corpus

Finding the request/reply pattern in a repository is not the same as having a **runnable system under
test**. The **81 3.x `receive`+`reply` repositories** above were read one by one against a single bar
— _is this a real, runnable service that consumes a request and emits a correlated reply over a
broker/socket, that could be containerized and driven as a black box?_ — and the answer is sobering.
(Full per-repo verdicts, independently re-checked from the cached specs and the live source, are in
`corpus-suitability.md`.) This per-repo assessment is **3.x-scoped**; because AsyncAPI 2.x has no
`reply` construct, its candidate services are instead surfaced by reading implementations directly
(see _Reading the code: AMQP/Kafka services without a declared correlation id_, below).

| Outcome                    | repos (of 81) |
| -------------------------- | ------------: |
| usable with minimal effort |         **2** |
| usable with real work      |           ~17 |
| not usable as a SUT        |           ~62 |

Of the 81, **42 are tooling/library or spec/docs repos** — by definition not runnable services, only
contracts or tools. Among the remaining 39 candidate services, almost none sit in the "small, clean,
runnable, well-specified, permissively-licensed" sweet spot; the real services are **bimodal** — tiny
hobby/student repos (0–3★) where the AsyncAPI file is aspirational, or large platforms (EVerest, the
Netcracker integration platform) that are genuine but heavy to stand up. The two
closest to plug-and-play are `voiceblender` (Go, WebSocket) and `specmatic/enterprise-sample` (Kotlin,
Kafka); a wider but workable set — `metalalive/e_commerce` (AMQP), `EVerest` (MQTT),
`gematik/zeta-testfachdienst` (STOMP) — each needs real work first.

The same blockers recur, and each is itself a facet of the problem:

- **A spec in a repo is not an implementation.** Many repositories carry an AsyncAPI document as
  documentation, an aspiration, or a **test fixture** with no matching service — the canonical Kraken
  WebSocket and adeo-Kafka example specs recur verbatim across unrelated repos.
- **Correlation is rarely contract-declared.** Where a real reply exists, the service usually
  correlates by broadcasting, an ad-hoc payload field, a hardcoded id, or a broker/framework
  convention (Zilla headers, STOMP sessions, uProtocol attributes) — _not_ a declared
  `correlationId.location` a tool could read directly, reinforcing the limit set out in **Transports
  and correlation** above. (One service even replies with a hardcoded correlation id.)
- **Contracts drift from implementations.** Specs claim a transport the code does not use — gRPC with
  no code at all, Redis where the code uses Google Pub/Sub, AMQP where the code uses IBM MQ — so even
  the contract cannot be trusted at face value.
- **Hard external dependencies and licensing.** Real candidates are frequently gated by live SaaS
  (Salesforce, Firebase), Kubernetes stacks, or paid services, and a striking number ship **no
  license** at all — either of which blocks reuse as a controlled, redistributable test subject.

The practical consequence is itself part of the problem: **the public corpus does not supply ready
SUTs.** A corpus-grounded evaluation cannot simply harvest these repositories — it must re-implement
or heavily adapt the handful of genuine services, and/or build controlled SUTs whose transports,
correlation and licensing are known.

### Reading the code: AMQP/Kafka services without a declared correlation id

The per-repo read above keys off the AsyncAPI contract — a `reply` op (3.x) or a `correlationId`
(2.x). But a service can correlate a reply to its request **in code** while declaring neither: over
AMQP through the native `correlation-id`/`reply-to` properties, over Kafka through an application
header, or through a field inside the payload. To catch those, we searched the **AMQP and Kafka**
repositories of both corpora for a request/reply hint in the spec (a reply op, or — in 2.x —
request/reply-suggestive channel names or a duplex `publish`+`subscribe` channel) **without** a
declared `correlationId`, then read the implementations of every candidate service this surfaced across
both corpora — some two hundred in all: every product, demo, and otherwise-unclassified Kafka/AMQP
repository carrying such a signal, and, to be thorough, the services whose schema carries no
request/reply hint at all, where the code proved one-way too.

Most are one-way event streaming: the bidirectional hint is largely noise, and Kafka/AMQP are
overwhelmingly used fire-and-forget. A minority, though, genuinely correlate a reply to its request
without declaring it — over AMQP through native `correlation-id`/`reply-to` properties or an echoed
payload field, and over Kafka through an application header or, most often, an echoed payload field.

Three things follow. First, reading code **expands the usable-SUT set well beyond what the contract
implied** — roughly a dozen correlated request/reply services across both AsyncAPI versions, against the
roughly two usable as-is among the repositories that _declare_ a 3.x reply — yet they are almost all demos,
course projects, and workshops. Second, real **products** that hide request/reply in code are **vanishingly
rare**: only one is usable as a SUT (with work), one further real product correlates in code but is too
heavy and generic to drive cleanly, and other production services examined directly — including
government-platform services — turned out to be one-way event pipelines rather than request/reply. Third, and most telling for a black-box tool, **almost none of
these services correlate through the AsyncAPI `correlationId` keyword** — they use a native property, an
application header, or a payload field, recoverable only by reading the code; the lone service that
_does_ surface its correlation in the contract does so through a vendor header extension (and, in its
3.0 form, a native `reply`), the exception that proves the rule. The contract is thus an unreliable
_positive_ guide: real services correlate without declaring it far more often than not. Its one
dependable signal is the _negative_ — a purely one-directional contract (no reply, no duplex channel)
reliably predicted one-way code in every case read — so wherever a reply might exist the tool must
learn whether and how a service correlates from its behaviour, not its schema. (Full per-repo
evidence — every repository read, its mechanism, and its SUT usability — is in `corpus-suitability.md`.)

The same code-read, applied to the **payload-only transports** (WebSocket and MQTT), changes the
picture in two ways. There the request/reply pattern is JSON-RPC-style — a request carries an `id` the
server echoes on the response over the same socket — and it proves to be the richest seam of genuinely
**product-grade** correlated services in the corpus — roughly ten of them, several actively-maintained
real products — where Kafka/AMQP yielded almost none, because JSON-RPC-over-WebSocket makes request-id
correlation a natural, common pattern. (One must look past the noise: WebSocket is bidirectional by nature, so most WS
services are streaming or broadcast — chat fan-out, game-state push, telemetry — not request/reply.)
But the same blind spot recurs: even when these services **document** the correlating field in their
contract, they do so as an ordinary payload property (`id`, `reqid`, and the like), never through the
AsyncAPI `correlationId` construct. So across every transport the formal keyword goes essentially
unused — a black-box tool must take the correlation id from the message payload, from the schema where
it is documented and from the code where it is not.

## Appendix: How repositories are classified

The corpus survey classifies each surveyed repository as a **product**, **tool/library**,
**demo/fixture** or **spec/docs** repo — plus two excluded classes, **catalog** (apis.json API
directories) and **tangential** (repos that merely mention AsyncAPI, e.g. AI-agent "skills"
collections), and **uncategorized** for repos with no readable metadata. Classification is
two-layered, and every result is reproducible from the scripts under `asyncapi-survey/`.

**1. Deterministic rules** (`asyncapi_classify_repos.py`). A seedless, explainable scorer
accumulates evidence per bucket and takes the highest score (minimum 2 points; ties broken in the
order tool → demo → product → spec):

| Signal                         | Weight | Example                                                                                                                          |
| ------------------------------ | -----: | -------------------------------------------------------------------------------------------------------------------------------- |
| GitHub topic (substring match) |     +3 | `schema-registry` → product, `code-generator` → tool, `tutorial` → demo                                                          |
| description / README keywords  |     +2 | "broker/gateway/server" → product; "parser/SDK/generator" → tool; "sample/example/book companion" → demo; "specification" → spec |
| repository name                |   +1–2 | `*-sample` → demo, `*-cli` → tool, `*-spec` → spec                                                                               |
| location of the spec file      |     +1 | only under `tests/`/`fixtures/` → tool/demo; at repo root or `docs/` → product                                                   |

A few decisive rules run first: AsyncAPI Generator **templates** → tool, AI coding-agent "skills"
repos → tangential, apis.json directories → catalog. On its own this layer reaches roughly
**70–75 % precision**; its main systematic error is mislabeling hackathon/student/sample code as
products because such repos describe themselves as "services" or "APIs".

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
