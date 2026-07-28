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

The differences from OpenAPI that drive everything below are not about syntax but about what a tester
can rely on:

- **No single wire.** OpenAPI is always HTTP; AsyncAPI is an architectural concept realised over many
  _incompatible_ transports (Kafka, AMQP, MQTT, WebSocket, …). There is no universal client to point at.
- **Decoupled interaction — and often no response at all.** A published message is consumed and
  processed _later_; the broker acknowledges _delivery_, not _processing_. Where REST always returns a
  self-labelling response, many async operations are **fire-and-forget**: nothing ever comes back.
- **No synchronous round-trip.** Even when a response exists, there is no single point at which "the
  call returned" and an outcome can be read; that has to be reconstructed.

The consequence: **a reply message — when the service defines one at all — is the only status-code
analogue async has**, the one point at which a consumed message produces something observable from
outside the service.

That is why AsyncAPI's version split matters for testing. The two major versions, both still in active
use, express the same ideas with different vocabulary — but differ exactly on the reply. **2.x**
(versions 2.0–2.6) places each operation as a `publish` or `subscribe` block _inside_ its channel and
**cannot express a paired response at all**. **3.0** reorganises operations into top-level entries typed
`send` / `receive`, and a `receive` may declare a first-class **`reply`**:

```
AsyncAPI 2.x — operations nested           AsyncAPI 3.0 — operations top-level,
inside channels, direction by keyword      typed by action, reply first-class
────────────────────────────────────       ─────────────────────────────────────
channels:                                  channels:
  user/signup:                               signup:
    publish:        # others publish           address: user/signup
      message: …    #  → the app               messages: [SignupRequest]
                    #    RECEIVES it         signupReply:
    subscribe:      # the app emits            address: user/signup/reply
      message: …    #  → others read           messages: [SignupOk, SignupError]
                                           operations:
   (no slot anywhere to pair                 onSignup:
    a request with its reply)                  action: receive   # the app consumes
                                               channel: signup
                                               reply:            # ← the 3.0 novelty
                                                 channel: signupReply
```

The 2.x sketch has nowhere to attach a reply — and note its inverted vocabulary: `publish` marks what
_others_ publish, i.e. what the application _receives_. The 3.0 sketch names everything a black-box test
needs: the consume channel, the reply channel, and the message sets on each.

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

Even there, correlation is not free — and it has two halves. **Placing the id is our half, and the easy
one**: the contract's `correlationId` declaration says where it goes when present, and the metadata
transports offer a natural slot regardless (AMQP's native `correlation-id` property, a Kafka header).
**The pairing itself is the SUT's half**: a reply becomes ours only once the service copies our stamped
id onto it, and whether it does so cannot be read off the contract — the `correlationId` keyword is
almost never present and, when it is, often disagrees with the code. So whether correlation _works_ is
established **empirically**: stamp a fresh id, watch for the echo. A tool can _detect_ a missing or
mismatched id, but cannot supply it.

The black-box scope follows directly from §2.1's split. Stamp-and-watch is generic only where the id
rides in **metadata**; on the payload transports (MQTT, WebSocket) it would have to be re-implemented
per service, inside each hand-rolled message layout. **Black-box is therefore developed for Kafka and
AMQP, over AsyncAPI 3.x** — the combination where a first-class reply exists and its correlation is
recoverable without reading anyone's message body.

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

REST hands SMARTS a status code for free; async must manufacture one. The raw material is the contract:
a 3.0 `reply` declares the set of messages a reply may be — a `result`, an `error`, and so on. Which of
those declared messages an actual reply validates as is its **reply variant**: a discrete,
contract-enumerated label, and the closest thing async has to a status code.

Coverage targets follow directly: one binary target per observed **`(reply-variant × operation)`** pair
— the analogue of REST's `(status × endpoint)`. The archive machinery is reused unchanged; only the
target strings differ.

**Fault targets** sit on top, for outcomes that signal a defect rather than declared behaviour:

- a **missing reply** — nothing arrives within the window _W_, though every in-scope operation declares
  a reply: the contract's one promise, broken — the async analogue of a hung endpoint. The claim is
  deliberately about the reply, not the processing, which stays unknowable from outside; and the
  verdict is _W_-sensitive (a slow SUT and a stuck one look alike), so _W_ is set generously and
  reported with the result;
- a **server-fault** reply — a JSON-RPC `-32603`, a `status:"error"` server code, a crash mid-process;
- a **schema mismatch** — a reply that validates as none of the declared reply messages.

The line between the two matters: a well-formed _error_ reply is **not** a fault but valid, declared
behaviour — exactly as a 400 is in REST. Indeed the reply variant _distinguishes_ outcomes but cannot
_judge_ them: AsyncAPI defines **no way to mark a reply message as an error or a success** — that is
naming convention, not declared semantics, unlike REST's standardised 4xx/5xx classes — which is exactly
why the server-fault target leans on recognised payload conventions (a JSON-RPC `-32603`) rather than on
anything the schema declares.

The honest limitation: the target is only as discriminating as the contract is rich. When a contract
declares a **single** reply variant, `(reply-variant × operation)` collapses to one target per operation —
"did a reply come back" — and the search has nothing to optimize within the operation. Results must
therefore be reported separated by contract richness.

#### The driver

Async has no URL to point at, so — exactly like RPC — it needs a **driver**: a `SutController` holding
the transport client and doing the publish-and-await on the core's behalf. The core talks to it over the
usual control protocol and stays protocol-agnostic; the driver's whole surface, in sketch:

```
AsyncApiDriver (a SutController):
    getProblemInfo() = AsyncApiProblem:
        schema   # the AsyncAPI document, URL or inline — conveyed as OpenAPI is; the only part
                 #   that crosses to the core (no reflection: the document already IS the schema)
        client   # live wire handle (Kafka producer/consumer, AMQP channel) — never crosses

    executeAsyncAction(dto):     # the core calls this once per action — the executeRPCEndpoint analogue
        publish(dto.address, inject(dto.correlationId, dto.body))   # header (Kafka) / property (AMQP)
        return awaitReply(dto.replyAddress, match=dto.correlationId, within=dto.window)
        # black-box shape; white-box publishes and defers "done" to the completion hook (below)
```

A note on protocol _versions_: the document pins them only loosely. AMQP is the firm case — AsyncAPI
names the two AMQPs as different protocols, so `amqp` alone fixes 0-9-1 (the incompatible AMQP 1.0 is
`amqp1`). Everywhere else the version lives in the server's `protocolVersion` field, which is
**optional and free-text**, so when it is absent the driver falls back to a conservative default —
e.g. MQTT 3.1.1, the variant with no native correlation metadata. (The `bindingVersion` field inside
binding objects is no substitute: it versions the binding _definition_, not the protocol.)

The transport code (the Kafka/AMQP publish-and-await) sits in the driver, and can be supplied in one of
two ways — neither of which touches the core:

1. **A module EvoMaster ships** — optional and contract-driven, for a standard transport; the user just
   points it at the SUT. This is only possible because every AsyncAPI service carries the same
   machine-readable contract: the document already tells the module the broker URL, the channels and the
   message schemas, so one module can configure itself for any SUT.
2. **A driver the user writes** — when the SUT speaks a custom or proprietary transport that no shipped
   module covers.

It is **the same driver in both modes.** Black-box uses it purely for wire access — publish, await the
reply, classify — and never pulls code coverage; the reply is the signal. White-box is the identical
driver with instrumentation switched on plus a completion hook (below). This is why async is unlike
ordinary black-box (a URL, no driver): with no universal wire, a driver must always be present to hold the
client.

#### The individual

There is **one `AsyncApiIndividual`** (an `ApiWsIndividual`) for all transports — **not one per
transport**. The transport
appears nowhere in it; Kafka-vs-AMQP is decided below the driver interface. The subclass itself is as
thin as its REST/GraphQL/RPC siblings — the structure is all inherited:

```
AsyncApiIndividual (ApiWsIndividual):
    children (ordered, grouped):                 # all inherited from EnterpriseIndividual
      INITIALIZATION    # SQL / Mongo / Redis seeding — nothing async-specific to add
      MAIN              # one EnterpriseActionGroup per AsyncMessageAction
                        #   (the group also carries that action's external-service mocks)
      CLEANUP
    childTypeVerifier = AsyncMessageAction       # the one async-specific declaration
```

All the semantic content lives in its main action, which mirrors `RPCCallAction` almost exactly:

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
operation)` targets. One caveat on the inherited structure: the per-action external-service (WireMock)
mocking in the MAIN groups is shared machinery but wired for REST today, so a new problem type must wire
it in.

#### The sampler and the fitness function

The individual is inert; it is driven by the creation/execution pair every problem type supplies — the
two main core classes this proposal must build.

**`AsyncApiSampler` creates** — one class for **both modes**. The usual reason a sampler branches by
mode — black-box reading the schema from a config URL, white-box getting it from the controller —
vanishes here: a driver exists in both modes, so the document always arrives through its
`AsyncApiProblem`, and nothing else in creation (templates, sampling, gene randomisation) cares about
the mode:

```
AsyncApiSampler:
    init():                              # once, at start-up
        doc       = fetchOrParse(asyncApiProblem.schema)     # URL or inline
        templates = one AsyncMessageAction per triggerable operation in doc
    sample():                            # called by SMARTS / MIO each iteration
        ind = AsyncApiIndividual(copy of a chosen template)  # + optional seeding init actions
        randomise(ind.seeGenes())
        return ind
```

**`AsyncApiFitness` executes** — the **only class the mode split doubles**: the black-box variant shown
here is a subclass of the white-box parent (sketched in §3.2), overriding just the second half of the
loop, as `BlackBoxRestFitness` does to `RestFitness`:

```
AsyncApiBlackBoxFitness.calculateCoverage(ind):    # black-box (subclass)
    for action in ind.mainActions():
        cid   = freshNonce()
        reply = driver.executeAsyncAction(buildDto(action.genes, cid, action.channel))  # publish+await
        if sutCrashed():         record(server_fault, action.operationId)      # fault target
        elif reply == none:      record(no_reply, action.operationId)          # fault: declared reply missing
        else:
            variant = variantOf(reply, action.replyTemplate)
            if variant == none:  record(schema_mismatch, action.operationId)   # fault target
            else:                record(variant, action.operationId)           # the coverage key
    return evaluate(ind, recordedTargets)          # no coverage pull
```

Around the pair: an **`AsyncApiTestCaseWriter`** emits the retained individuals (next); the mutator and
archive are reused unchanged; and two thin Guice modules wire each mode, the black-box one binding the
controller connection unconditionally, since the driver is always needed for the wire.

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
client code **to match the protocol version**: an AMQP 0-9-1 test uses the native `correlation-id` /
`reply-to` properties, chosen automatically from the contract's binding and `protocolVersion`; once the
deferred transports are added, the same mechanism carries over (MQTT 5.0 → Correlation Data + a Response
Topic; MQTT 3.1.1 → the id hand-rolled into the payload).

### 3.2 White-box

White-box covers **AsyncAPI 3.x and 2.x, across all four transports**: coverage is the signal, so no
reply and no correlation are required — a 2.x `publish` block is as drivable as a 3.0 `receive`. The
cast is the one §3.1 introduced, and white-box changes less of it than one might expect: the **sampler**
is untouched; the **fitness**, the **individual** and the **driver** differ in the ways the subsections
below detail; and the **writer** is the same class emitting different assertions. What is genuinely new
is not a class but the **completion problem** — which is why this section runs problem-first.

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

#### The white-box individual — is it the black-box one?

Largely yes: the same `EnterpriseIndividual` spine and the same `AsyncMessageAction`. The one
**representational** difference: the consume action may carry **no `replyTemplate`** — fire-and-forget is
first-class, not a degenerate case. Everything else that changes in white-box is behaviour, not
representation, and lives in the fitness and the driver (next) — the same shared-action, per-mode-fitness
split REST already uses.

#### The fitness function in white-box

The white-box `AsyncApiFitness` is the parent that §3.1's black-box subclass overrides — same loop
opening (genes → DTO → `executeAsyncAction`), different second half:

```
AsyncApiFitness.calculateCoverage(ind):            # white-box (parent)
    for action in ind.mainActions():
        dto = buildDto(action.genes, freshNonce(), action.channel)
        driver.executeAsyncAction(dto)             # publish
        waitForCompletion(driver, within=W)        # the new wait-loop
    return evaluate(ind, driver.getTestResults())  # coverage targets
```

- **The outcome is branch-distance coverage**, collected at completion, not a reply variant; for a
  request/reply operation the black-box reply oracle can still ride along as extra targets.
- **The wait is explicit**: `waitForCompletion` polls the driver's completion hook
  (`isScheduleTaskCompleted`) in a bounded loop — the wait-loop this proposal adds — and only on "done",
  or on the timeout, does the fitness pull coverage (`getTestResults`) and score the individual.

#### Extending the driver for white-box

It is the **same `SutController`** as black-box with instrumentation switched on — wire access and
lifecycle unchanged, coverage flowing through the standard controller machinery (the core's
`getTestResults` pull). In sketch, only the delta:

```
AsyncApiDriver (white-box) — the same class; the additions:
    # getProblemInfo() / executeAsyncAction() as in black-box — publish half only
    isInstrumentationActivated() = true          # the switch black-box leaves off
    isScheduleTaskCompleted(invocation):         # NEW: what the core's wait-loop polls
        return probeInactivity() or sideEffectSeen()
            or brokerAdvanced() or handlerReturned()   # whichever mechanisms are wired (above)
```

(A driver may instead discharge the wait internally — block inside the invocation and return `COMPLETED`
directly — the same contract, resolved driver-side.)

Two pieces are genuinely new. The first is the **completion hook's wiring** — not the hook itself.
EvoMaster already declares the right pair of methods for its RPC schedule tasks:
`customizeScheduleTaskInvocation` triggers deferred work, and `isScheduleTaskCompleted` is meant to
report when it finished. But the second of these is defined and **never called** — nothing in the
framework polls it — and the whole path is welded to the RPC problem type. What this proposal actually
builds, then, is the missing caller (the wait-loop in the fitness) and the lift out of the RPC package.
The second new piece is the **per-library listener instrumentation** (Spring Kafka, Spring AMQP, JMS,
the MQTT/WebSocket client callbacks) that feeds the hook's `handlerReturned()` — so handler
entry/return, or a downstream effect, becomes observable. Everything else carries over unchanged from
what the driver already does for its other white-box modes.

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
SUTs are only run for evaluation, modified at most to get them running, never redistributed). Only the
bar differs by mode:

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
