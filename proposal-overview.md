# Testing AsyncAPI Services in EvoMaster: Black-Box and White-Box

This is a condensed proposal for extending EvoMaster to test **AsyncAPI** services, in both a **black-box**
and a **white-box** mode. It assumes familiarity with EvoMaster's engine (SMARTS/MIO, the Driver /
`SutController`, individuals and genes) and spends its words on the AsyncAPI-specific decisions. It runs
problem-first, then proposal, then a method appendix. The two modes have different reach, so their scope
is set deliberately: **black-box targets Kafka and AMQP over AsyncAPI 3.x**, while **white-box covers
AsyncAPI 3.x and 2.x** across all four transports. Why the split falls there is developed below.

## 1. AsyncAPI, and how it differs from OpenAPI

AsyncAPI is the event-driven counterpart of OpenAPI: a document describing how a service communicates over
message brokers and sockets rather than synchronous HTTP. It declares **channels** (topics, queues,
routing keys), **operations** on those channels, **messages** typed with **JSON Schema**, **servers**
(broker URL, protocol, auth), and protocol **bindings**.

AsyncAPI comes in two major versions, both still in active use, that express these same ideas with
different vocabulary — and the gap between them turns out to matter for testing. **2.x** (versions
2.0–2.6) places each operation as a `publish` or `subscribe` block _inside_ its channel, and has no notion
of a paired response. **3.0** reorganises that: operations become top-level entries typed `send` /
`receive`, and — the change that matters most here — a `receive` may declare a first-class **`reply`**.
That difference is not cosmetic: a reply is the only point at which a consumed message produces something
observable from outside the service, which is why the version a service speaks matters for what follows —
as the problem section makes precise.

Four differences from OpenAPI drive everything below:

- **No single wire.** OpenAPI is always HTTP; AsyncAPI is an architectural concept realised over many
  _incompatible_ transports (Kafka, AMQP, MQTT, WebSocket, …). There is no universal client to point at.
- **Decoupled interaction.** A publish is consumed and processed _later_; the broker acknowledges
  _delivery_, not _processing_, and in many designs there is no response at all.
- **The reply is the only status-code analogue, and only in 3.0.** Where REST always returns a
  self-labelling response, async offers at most a `reply` message — and 2.x cannot even express one.
- **No synchronous round-trip.** There is no single point at which "the call returned" and an outcome can
  be read; that has to be reconstructed.

## 2. The problem

### 2.1 The transports, and where correlation lives

The four transports that dominate the corpus share nothing at the API level, and a request/reply pair is
only recoverable if the tester can tell _which_ request a reply answers — a **correlation id** the
requester stamps and the responder echoes. Crucially, _where_ that id can ride differs by transport:

| Transport      | Where the correlation id rides             | Reply destination           | Nature                         |
| -------------- | ------------------------------------------ | --------------------------- | ------------------------------ |
| **AMQP** 0-9-1 | native `correlation-id` **property**       | `reply-to` property         | protocol-native metadata       |
| **Kafka**      | a record **header** (e.g. `correlationId`) | reply-topic header          | client-library convention      |
| **MQTT** 3.1.1 | inside the **payload**                     | encoded in the payload      | bespoke, no transport metadata |
| **WebSocket**  | inside the **payload**                     | same socket, in the payload | bespoke, per-service protocol  |

The line that matters runs between **metadata-level** correlation (AMQP, Kafka), which a tool can place
and read without understanding the message body, and **payload-level** correlation (MQTT 3.1.1,
WebSocket), which forces the tool to parse and mutate each service's hand-rolled message schema. That
distinction is what makes some transports tractable black-box and others not.

### 2.2 Black-box: the request/reply problem

In black-box mode, EvoMaster can assert only on what the SUT sends _back_. A fire-and-forget consume operation
returns nothing — publishing into it is publishing into a void, indistinguishable from a silently dropped
message. So the **only observable interaction is request/reply**: a `receive` operation with a paired
`reply` (a 3.0 construct — 2.x has none).

Even there, correlation is not free. The pairing is built by the **SUT**, not by us — a reply becomes ours
only once the service copies our stamped id onto it. That behaviour is rarely declared in the contract (the
`correlationId` keyword is almost never present and, when it is, often disagrees with the code), so
correlation must be established **empirically**: stamp a fresh id, watch for the echo. A tool can _detect_
a missing or mismatched id, but cannot supply it.

Combined with §2.1, this fixes the black-box scope. Where the id is **metadata** (AMQP's native property,
Kafka's header), the tool stamps and matches it without touching the body; where it is **payload** (MQTT,
WebSocket), the tool is coupled to each service's message format and bespoke framing. **Black-box is
therefore developed for Kafka and AMQP, over AsyncAPI 3.x** — the combination where a first-class reply
exists and its correlation is recoverable generically.

### 2.3 White-box: when to collect coverage

With instrumentation, the signal is no longer the reply but the **code the consumer executes** — so
fire-and-forget operations become testable, and they are the majority. Correlation stops being central:
for fire-and-forget there is no reply to pair, and for request/reply the coverage gradient stands on its
own. This is why **white-box can cover both 3.x and 2.x** — a 2.x `publish` block is just as drivable as a
3.0 `receive`, since neither needs a reply.

The cost moves elsewhere. Because the consumer runs **later, on a broker- or listener-driven thread**,
after the publish call has returned, there is no synchronous moment at which "the SUT has finished this
message." The central white-box problem is thus **completion detection** — knowing _when_ to snapshot
coverage and score the individual.

### 2.4 The corpus

We surveyed the public AsyncAPI corpus on GitHub to ground both modes. The same **classification** underlies
both views: every repository is bucketed as **product**, **tool/library**, **demo/fixture** or
**spec/docs** by deterministic rules plus an LLM pass (method in the appendix). The observable pattern is
measured by each version's native signal — 3.x structural `receive`+`reply`, 2.x message `correlationId`.

**Black-box view — request/reply is rare and thinly spread.** In 3.x, **122 specs across 81 repositories**
(~2.9% of parsed 3.x specs) declare a `receive`+`reply` (356 operations); in 2.x, **55 specs** (~2.0% of
parsed 2.x specs) declare a `correlationId`, but it is overwhelmingly _tracing_, with only **9 of the 55**
request/reply-shaped. The 81
reply repositories skew to tooling test-fixtures and teaching examples — only **13 are genuine products**.
And reading them as candidate systems-under-test, almost none are runnable as-is:

| Black-box SUT usability (of the 81 reply repos) | repos |
| ----------------------------------------------- | ----: |
| usable with minimal effort                      | **2** |
| usable with real work                           |   ~17 |
| not usable as a SUT                             |   ~62 |

The two minimal-effort repositories are worth running against directly, and the evaluation does so; but
two is far too thin a base to rest on, so it is anchored on **controlled SUTs** (the NCS numerical
services) with known transports and honest contracts, built to demonstrate the approach.

**White-box view — a larger reachable population.** White-box needs a JVM service to instrument and an
AsyncAPI document; the reachable set is their intersection. That is **92 distinct JVM AsyncAPI products**
(55 in 3.x, 43 in 2.x, 6 shared). A per-repo pass grading each against the white-box bar (runnable JVM
service + instrumentable consume listener + a mapping AsyncAPI doc + a standable transport) gives:

| White-box usability (of the 92 JVM products) | repos |
| -------------------------------------------- | ----: |
| drivable with modest effort                  | **8** |
| drivable with real work                      |    51 |
| not usable as a SUT                          |    33 |

**70 of the 92 carry an instrumentable consumer** — a far bigger reach than black-box's request/reply
slice, exactly because coverage, not a reply, is the signal. The binding constraint shifts to consume-side
**spec drift**: only **24** ship an AsyncAPI doc that maps cleanly to the listener (35 describe only what
the service _publishes_, 15 are aspirational, 10 have a real consumer but no file, 8 neither).

**Protocol complexity, both modes.** Pulling §2.1–§2.3 together, the two modes differ sharply in how much
the transport matters:

| Protocol   | Correlation lives in | Black-box complexity              | White-box complexity |
| ---------- | -------------------- | --------------------------------- | -------------------- |
| AMQP       | native property      | **low** — in scope                | low                  |
| Kafka      | header (convention)  | **low–medium** — in scope         | low                  |
| MQTT 3.1.1 | payload              | high — deferred (payload-coupled) | medium               |
| WebSocket  | payload (bespoke)    | high — deferred (payload-coupled) | medium               |

Black-box complexity tracks _where correlation lives_; white-box is far less transport-sensitive, since it
never correlates a reply — it only publishes and reads coverage. Version cuts the same way: black-box
needs 3.0's first-class reply, while white-box, needing only coverage, drives 2.x `publish` blocks and 3.0
`receive` operations alike. Hence the scoping this proposal adopts: **black-box → Kafka + AMQP + 3.x;
white-box → all four transports, 3.x and 2.x.**

## 3. The proposal

Both modes reuse EvoMaster's existing search, archive and Driver machinery; only the AsyncAPI-specific
parts are described here. Each subsection opens with its scope.

### 3.1 Black-box

_Scope: Kafka + AMQP, AsyncAPI 3.x — metadata-level correlation, first-class reply._

#### What counts as coverage

REST hands SMARTS a status code; async must manufacture one. The device is to treat the
**reply message as the synthesized status code**. Coverage targets are keyed on **`(reply-variant ×
operation)`** — which of the declared `reply` messages a given reply validates as (a `result`, an `error`,
…), per operation — plus a `no-reply` target. This is the direct analogue of REST's `(status × endpoint)`,
and it reuses the archive machinery unchanged; only the target strings differ.

On top sit **fault targets**: a **server-fault** reply (e.g. a JSON-RPC `-32603`, a `status:"error"` server
code, or a crash mid-process) or a **schema mismatch** (a reply matching no declared reply message). A well-formed _error_ reply is not a fault but valid, declared behaviour, exactly as a 400 is in REST.

The honest limitation: the target is only as discriminating as the contract is rich. When a contract
declares a **single** reply variant, `(reply-variant × operation)` collapses to one target per operation —
"did a reply come back" — and the search has nothing to optimize within the operation. Results must
therefore be reported separated by contract richness.

#### The driver

Async has no URL to point at, so — exactly like RPC — it needs a **driver**: a `SutController` holding
the transport client (a Kafka producer/consumer, an AMQP channel) and doing the publish-and-await on the
core's behalf. The core talks to it over the usual control protocol, and stays protocol-agnostic: the driver declares the
SUT via `getProblemInfo()` — a new `AsyncApiProblem` carrying the **AsyncAPI document** (the schema the
core reads to generate inputs, the only part that crosses to the core) and the **transport client** (a
live wire handle the driver keeps for the publish-and-await, never crossing to the core) — and the core
drives one action per call, the analogue of RPC's `executeRPCEndpoint`. The document is conveyed as
OpenAPI is (URL or inline); no reflection is needed — the document already _is_ the schema. (The protocol _version_ is only loosely pinned — the binding fixes
AMQP at 0-9-1, and the server's optional `protocolVersion` states the rest, defaulting to e.g. MQTT 3.1.1
when silent.)

The transport code (the Kafka/AMQP publish-and-await) sits in the driver, and can be supplied two ways,
neither of which touches the core: **(A)** an optional, contract-driven module EvoMaster ships for a
standard transport (feasible precisely because the AsyncAPI document is portable — RPC can't do this),
which the user just points at the SUT; or **(B)** a driver the user writes for a bespoke wire.

It is **the same driver in both modes.** Black-box uses it purely for wire access — publish, await the
reply, classify — and never pulls code coverage; the reply is the signal. White-box is the identical
driver with instrumentation switched on plus a completion hook (below). This is why async is unlike
ordinary black-box (a URL, no driver): with no universal wire, a driver must always be present to hold the
client.

#### The individual

There is **one `AsyncApiIndividual`** (an `ApiWsIndividual`) for all transports — **not one per
transport**. The transport
appears nowhere in it; Kafka-vs-AMQP is decided below the driver interface. Its main action mirrors
`RPCCallAction` almost exactly:

```
AsyncMessageAction:
    operationId        # the coverage unit (the 3.0 operation key)
    inputParameters    # THE GENES: payload from the message JSON Schema
    correlationId      # a fresh nonce stamped at each execution — deliberately NOT a gene
    channel            # addressing, from the contract — immutable, NOT a gene
    replyTemplate      # the declared reply message set — immutable; the reply-variant axis
    reply              # filled at execution; read by the classifier, never a gene
    seeGenes() = inputParameters.genes     # reply excluded, exactly as in RPC
```

The search mutates only the request; the reply is read at fitness time and drives the `(reply-variant ×
operation)` targets. Being an `EnterpriseIndividual`, it inherits database seeding for free; per-action
external-service (WireMock) mocking is the same shared machinery but wired for REST today, so a new
problem type must wire it in.

#### Test generation

Following RPC's `enablePureRPCTestGeneration`, the emitted test is written against a **concrete transport
client, not the driver**: a generated Kafka test uses a real producer/consumer, an AMQP test a real
channel — standard client code a developer can read and run. The driver governs the _search_; it is not
what the suite runs against. The consequence is that the emitted body is
concrete and **varies by transport** (a Kafka test differs from an AMQP one), and the suite carries a
dependency on the concrete transport-client library — the black-box price for having no universal wire.

Concretely, the Kafka tests for `bessj` — one per covered `(reply-variant × operation)` — take their
topic names, the header the id rides in, and the message shapes straight from the AsyncAPI document; only
the genes and the asserted variant change:

```
test ncs_bessj__DoubleResult:               # the success outcome
    cid      = freshId()
    producer = connectKafkaProducer("kafka:9092")
    consumer = connectKafkaConsumer("kafka:9092", topic="ncs.bessj.reply")
    producer.publish("ncs.bessj.request", headers={correlationId: cid}, body={n:3, x:2.0})   # genes
    reply = consumer.pollUntil(r -> r.headers.correlationId == cid, within=W)
    assert reply.body.resultAsDouble is finite and not reply.body.has("error")

test ncs_bessj__Error:                      # boundary-fuzzed genes (n < 3) → the Error variant
    cid      = freshId()
    producer = connectKafkaProducer("kafka:9092")
    consumer = connectKafkaConsumer("kafka:9092", topic="ncs.bessj.reply")
    producer.publish("ncs.bessj.request", headers={correlationId: cid}, body={n:2, x:2.0})   # n < 3
    reply = consumer.pollUntil(r -> r.headers.correlationId == cid, within=W)
    assert reply.body.error.code == 400
```

The correlation id rides in a Kafka **header** and never touches the payload; a real producer/consumer
pair is stood up in the test itself — no EvoMaster driver at run time. The generator also writes the
client code **to match the protocol version**: an MQTT 5.0 test uses Correlation Data + a Response Topic,
an MQTT 3.1.1 test hand-rolls the id into the payload, an AMQP 0-9-1 test uses the native
`correlation-id` / `reply-to` properties — chosen automatically from the contract's binding and
`protocolVersion`.

### 3.2 White-box

_Scope: AsyncAPI 3.x and 2.x — coverage is the signal, so no reply and no correlation are required; a 2.x
`publish` block is as drivable as a 3.0 `receive`._

#### Tackling completion (when to collect coverage)

The whole white-box difficulty is deciding when the consumer has finished processing our message. The
options form a spectrum, ordered by how little they must know about the SUT — the default assumes nothing
and sharpens only when the framework is known:

1. **Instrumentation-probe inactivity** — the SUT's coverage probes go quiet for a debounce interval;
   agnostic to framework and transport, and it reuses machinery already present.
2. **A downstream side effect** — a database write or outbound call the handler makes, already observed by
   the SQL snapshot and external-service interception; doubles as an oracle.
3. **Broker / transport-client signal** — a committed offset, a drained queue, an ack — one hook per
   transport, none per framework.
4. **A handler-boundary hook** — the listener method, ack/commit, or a framework interceptor; the precise
   option when the framework is known. Its strongest form is an **in-flight counter**: increment at
   handler entry, decrement at return, and follow the handler's thread hand-offs (instrumented
   `Thread.start` / `Executor.submit`) so background work is awaited too — zero means done.
5. **A timeout** — the last resort, a tuning parameter with the usual slow-vs-stuck ambiguity.

Two points the mechanisms turn on. **Attribution** — _which_ thread is ours — is not known in advance
(the broker picks the listener thread); it is learned at handler entry, where the probe runs on the
worker thread and the **id we stamped** into the message confirms the invocation is ours (the same id
black-box uses, present even for fire-and-forget). When the entry point can't be hooked, **single-flight**
makes attribution moot. **Reach** — collecting coverage is transport-agnostic (probes sit in the SUT's
own code), so _only the precise hook_ is per-library; it targets the transport library's delivery method
(Spring Kafka/AMQP/JMS; for WebSocket `jakarta.websocket`, Java-WebSocket, Spring `TextWebSocketHandler`,
Netty). A "custom WebSocket" rides one of these, so it is still hookable; only a raw-socket wire with no
library boundary falls back to agnostic completion + single-flight (or a per-SUT entry-point hint).

This is the shape EvoMaster's **`scheduletask`** machinery half-models — `customizeScheduleTaskInvocation`
(trigger) and `isScheduleTaskCompleted` (report done) — but only half: today `isScheduleTaskCompleted` is
defined yet **never called** (there is no wait-for-completion loop), and the path is RPC-bound. So the
proposal reuses the hooks and the lifecycle shape, but its real work is **adding the completion loop** and
giving AsyncAPI its own sampler/fitness route.

#### The white-box individual — is it the black-box one?

Largely yes: the same `EnterpriseIndividual` spine and the same `AsyncMessageAction`. The differences
follow from coverage-as-signal:

- The consume action may carry **no `replyTemplate`** — fire-and-forget is first-class, not a degenerate
  case.
- The outcome is **branch-distance coverage** collected at completion, not a reply variant; for a
  request/reply operation the black-box reply oracle can still ride along as an extra target.
- **Completion is Driver-side**, so the action's lifecycle gains a "wait for completion" step between
  invocation and fitness collection. Concretely: after the driver has published the message, the core
  polls the driver's completion hook (`isScheduleTaskCompleted`) in a bounded loop — the wait-loop this
  proposal adds — and the driver answers it from whichever completion mechanism is wired (probe
  inactivity, a downstream side effect, broker state, a handler hook). Only on "done" — or on the
  timeout — does the core pull coverage (`getTestResults`) and score the individual. (A driver may
  instead resolve the wait internally: block inside the invocation and return `COMPLETED` directly —
  the same contract, discharged driver-side.)

So the representation is shared; the fitness and the presence of a reply are what differ — the same
shared-action, per-mode-fitness split REST already uses.

#### Extending the driver for white-box

It is the **same `SutController`** as black-box, with instrumentation switched on: white-box adds
code-coverage collection (the `getTestResults` pull) over the black-box driver's wire access and
lifecycle. Two pieces are genuinely new: the **completion hook** (`isScheduleTaskCompleted`-style, wired
to the mechanisms above) so the core knows when to read coverage, and **per-framework listener
instrumentation** (Spring Kafka, Spring AMQP, JMS, the MQTT/WebSocket client callbacks) so handler
entry/return — or a downstream effect — is observable. Everything else carries over unchanged from what
the driver already does for its other white-box modes.

#### What the generated tests assert

An emitted white-box test asserts on the **observable residue** of the processing:

- **the side effects** the handler left behind — database rows re-read and compared, an emitted
  message, an external call;
- **completion without a crash**, within the window;
- **the reply**, where the operation declares one — the black-box reply assertions unchanged.

Structurally it is an ordinary EvoMaster white-box test: the suite scaffolds on the **driver**, which
starts the SUT and resets it between tests, and the SUT runs **uninstrumented** at replay. Only the wire
differs — the message goes out through a **concrete transport client** instead of an HTTP call. Emitting
the test reuses the existing writers almost wholesale:

- **reused** — payload matchers, exception and timeout handling, and the WireMock _stubbing_ (as
  stimulus, so the handler's outbound calls succeed);
- **new** — the subscribe/await plumbing, the database _re-read_, and a one-line WireMock `verify(...)`
  that turns the existing stub into an oracle for "the handler made this call."

Concretely, for a fire-and-forget NCS variant — a `bessj` operation that stores its computation in a
database instead of replying (such consume-only variants must still be authored; the current NCS SUTs
are request/reply throughout):

```
fixture:                                        # every white-box suite scaffolds on the driver
    controller = new NcsEvoMasterController()
    baseUrl    = controller.startSut()          # boots SUT + broker; SUT uninstrumented at replay
    beforeEach : controller.resetStateOfSUT()   # for async: also drains topics and queues

test ncs_recordBessj__computationStored:        # fire-and-forget: no reply to await
    producer = connectKafkaProducer("kafka:9092")            # concrete client — the wire only
    producer.publish("ncs.bessj.record", body={n:3, x:2.0})  # genes -> body; no exception = delivered
    row = awaitDbRow(controller, table="computations",       # completion proxy: the side effect,
                     where={fn:"bessj", n:3}, within=W)      #   under the test's @Timeout ceiling
    assert row != null                          # the handler processed our message
    assert row.result is finite                 # value observed at search time, baked in
    // reached BessjRecordHandler.onMessage; completed via DB write   <- comments, never assertions
```

Had the handler emitted a message onto another channel instead of writing a row, the test would
subscribe there and assert on that payload with the same matchers.

## Appendix: How the corpus was computed

The survey enumerated AsyncAPI documents across versions **2.0–2.6** and **3.0.0 / 3.1.0** via GitHub code
search, parsed each discoverable document, and attributed its transport from the declared **servers and
bindings**. Repository **kind** was assigned by a two-layer classifier: a deterministic, seedless scorer
over observable signals (GitHub topics, description/README, repository name, spec-file location, primary
language) into product / tool-library / demo-fixture / spec-docs, followed by an independent LLM pass whose
verdict fills gaps the rules left uncategorized (confidence ≥ 0.60) and overrides the rules where it is
confident they erred (≥ 0.78); combined accuracy is roughly 90%.

The **reply pattern** was measured per version by its native signal — a 3.x operation with `receive` and a
paired `reply`, and a 2.x message `correlationId` (then inspected to separate genuine request/reply from
tracing use). For the **white-box slice**, repositories were cross-tabulated by primary language to isolate
JVM products, and each of the resulting 92 was then read individually — fetching its file tree and source
archive to grep for a real message-consumer (`@KafkaListener`, `@SqsListener`, `@RabbitListener`,
`@Incoming`, `@MessageMapping`, Paho callbacks, WebSocket handlers, …) and opening its AsyncAPI document to
check whether the contract maps to that consumer — and graded against the runnable-SUT bar defined next.

**The three usability tiers.** Both usability tables in §2.4 grade each candidate into the same three
tiers by how much stands between the repository and a controlled run; licensing is _not_ a criterion (the
SUTs are booted for evaluation, not modified or redistributed). Only the bar differs by mode:

- **usable with minimal effort** (black-box) / **drivable with modest effort** (white-box) — a runnable
  service (a container, a fat jar, a one-command boot) that needs essentially no adaptation: for
  black-box, its request/reply and correlation work out of the box over a standable broker; for
  white-box, it exposes an instrumentable consume listener that the AsyncAPI document maps to. Stand it
  up and point the tool at it.
- **usable / drivable with real work** — a genuine service, but not runnable until real setup is done: a
  heavy platform or monorepo to build and boot, external dependencies to stub (auth servers, databases,
  sibling services), a broker or transport client to write, plus — black-box — correlation to recover by
  reading the code, or — white-box — consume-side spec drift to reconcile.
- **not usable as a SUT** — cannot be driven as a controlled SUT at all: not a runnable service (a
  client or GUI, a library or engine, a codegen scaffold, a spec-only or packaging-only repo), no
  drivable operation (one-way / producer-only for black-box; no instrumentable consumer for white-box),
  an aspirational spec with no matching implementation, a bespoke non-standard wire, or a hard external
  dependency that cannot be stood up.
