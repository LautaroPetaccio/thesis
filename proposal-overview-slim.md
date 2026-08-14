# Testing AsyncAPI Services in EvoMaster: Black-Box and White-Box

This proposal extends EvoMaster to test **AsyncAPI** services, in both a **black-box** and a
**white-box** mode. It assumes familiarity with EvoMaster's engine (SMARTS/MIO, the Driver /
`SutController`, individuals and genes) and focuses on the AsyncAPI-specific decisions. The scope is the
same for both modes: **AsyncAPI 3.x only** — its first-class `reply` is the one observable both modes
anchor on. Black-box classifies that reply as the test's outcome; white-box collects coverage a short
settle window after the reply arrives — or at the full reply window when none does. Black-box is built on
**Kafka** first — the densest transport in the corpus, and one where correlation rides in metadata — with
**WebSocket**, the most widely adopted, as the stated next target; white-box covers the four dominant
transports. The document runs problem-first, then one proposal section per mode.

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

That consequence fixes this proposal's version scope. AsyncAPI has two major versions in active use, and
they differ exactly on the reply. **2.x** (versions 2.0–2.6) places each operation as a `publish` or
`subscribe` block _inside_ its channel and **cannot express a paired response at all**. **3.0**
reorganises operations into top-level entries typed `send` / `receive`, and a `receive` may declare a
first-class **`reply`**:

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
_others_ publish, i.e. what the application _receives_. The 3.0 sketch names everything this proposal
needs: the consume channel, the reply channel, and the message sets on each. **This is why we work with
3.x only**: the reply is both the one outcome black-box can observe and the only outside evidence of
processing white-box gets — and 2.x cannot express one.

## 2. The problem

### 2.1 The transports, and where correlation lives

Four transports dominate asynchronous messaging, and they share nothing at the API level. A
request/reply pair is only recoverable if the tester can tell _which_ request a reply answers — a
**correlation id** the requester stamps and the responder echoes. Crucially, _where_ that id can ride
differs by transport:

| Transport      | Where the correlation id rides             | Reply destination           | Nature                         |
| -------------- | ------------------------------------------ | --------------------------- | ------------------------------ |
| **AMQP** 0-9-1 | native `correlation-id` **property**       | `reply-to` property         | protocol-native metadata       |
| **Kafka**      | a record **header** (e.g. `correlationId`) | reply-topic header          | client-library convention      |
| **MQTT** 3.1.1 | inside the **payload**                     | encoded in the payload      | bespoke, no transport metadata |
| **WebSocket**  | inside the **payload**                     | same socket, in the payload | bespoke, per-service protocol  |

The line that matters runs between **metadata-level** correlation (AMQP, Kafka), which a tool can place
and read without understanding the message body, and **payload-level** correlation (MQTT 3.1.1,
WebSocket), which forces the tool to first understand each service's message format and its own invented
message layout before it can even place the id.

### 2.2 Black-box: the request/reply problem

In black-box mode, EvoMaster can assert only on what the SUT sends _back_. A fire-and-forget consume
operation returns nothing — publishing into it is publishing into a void, indistinguishable from a
silently dropped message. So the **only observable interaction is request/reply**: a `receive` operation
with a paired `reply`.

That exclusion is a scope decision rather than a permanent verdict, and it marks the clearest research
opening on the black-box side. What fire-and-forget denies us is not the message — we can always publish
one — but any way to tell **when, or whether, the SUT finished processing it**. Signals do exist outside
the service, though: the broker carries them (a consumer-group offset advancing past our record, a
queue's unacked count draining to zero), and the same contract often declares other channels the
application _sends_ on, whose traffic is a side effect we are entitled to watch. Turning those into a
**completion heuristic** — good enough to call a fire-and-forget action done, and so to give it a testable
outcome at all — is future work this proposal deliberately leaves open, and the outside-in half of a
question white-box faces from within (§3.2).

Within the request/reply subset itself, correlation is not free either — and it has two halves.
**Placing the id is our half, and the easy one**: the contract's `correlationId` declaration says where
it goes when present, and Kafka offers a natural metadata slot regardless — a record header. **The pairing itself is the SUT's half**: a reply
becomes ours only once the service copies our stamped id onto it, and whether it does so cannot be read
off the contract — the declaration is often absent and, when present, may disagree with the code. So
whether correlation _works_ is established **empirically**: stamp a fresh id, watch for the echo. A tool
can _detect_ a missing or mismatched id, but cannot supply it.

The transport scope follows from §2.1's split. Stamp-and-watch is generic only where the id rides in
**metadata**, so **black-box is built on Kafka** — the metadata transport with the densest declared usage
in the corpus (393 specs across 193 repositories in 3.x). **AMQP is dropped**: it offers the same
metadata slot, and so would be nearly free to add, but it is the least adopted of the four (107
repositories) and cheapness alone does not earn scope.

**WebSocket is the stated next target**, for two reasons. It is the **most widely adopted** transport in
the corpus — 203 repositories, more than any other — and its payload-level correlation is an
**architectural challenge worth pursuing** rather than a mechanical port. With no metadata slot to stamp,
the id has to ride inside the service's own message layout, so it cannot be placed by anything that has
not been told that layout. The answer is a boundary rather than a guess: the core mints the correlation
id and hands it down, and the transport client — the one piece written against that layout — places it on
the wire and matches it on the reply (§3.1). Drawing that line correctly is what puts a payload transport
in reach without teaching the core anyone's message format.

### 2.3 White-box: when to collect coverage

With instrumentation, the signal is no longer the reply but the **code the consumer executes**. The cost
moves elsewhere: because the consumer runs **later, on a broker- or listener-driven thread**, after the
publish call has returned, there is no synchronous moment at which "the SUT has finished this message" —
so the core does not know _when_ to snapshot coverage and score the individual.

And that question has no exact answer from outside. Even an arrived reply proves only that the handler
answered — the message may have triggered work that is still running in the background, and under
instrumentation that work is still **covering lines of code**: a handler can reply first and keep
executing, or hand off to another thread, so lines and branches keep being hit after the moment we
snapshot. Read coverage too early and that execution is missed — or attributed to the next action.
Completion is therefore **heuristic by nature**, in both modes: black-box must decide when to stop
waiting for a reply, white-box when coverage is ready to read. Several heuristics can answer it, with
varying precision (§3.2 names them); as its **first iteration**, this proposal answers with **two
timeouts**: a reply window shared by both modes, and — because a reply cannot certify that processing
finished — a short settle window that white-box waits out after one arrives (§3.2).

## 3. The proposal

Both modes reuse EvoMaster's existing search, archive and Driver machinery; only the AsyncAPI-specific
parts are described here.

### 3.1 Black-box

#### What counts as coverage

REST hands SMARTS a status code for free; async must manufacture one. The raw material is the contract:
a 3.0 `reply` declares the set of messages a reply may be — a `result`, an `error`, and so on. Which of
those declared messages an actual reply validates as is its **reply variant**: a discrete,
contract-enumerated label, and the closest thing async has to a status code.

Every executed request then lands in exactly one of **four buckets** — and the buckets are the targets:

1. **A reply validating as one of the declared messages** → the `(reply-variant × operation)` target,
   the direct analogue of REST's `(status × endpoint)`.
2. **No reply within the reply window _W_** → the `(no-response × operation)` **fault target**. Every
   in-scope operation declares a reply — the contract's one promise — so a request that draws silence
   for the whole window breaks it: the async analogue of a hung endpoint. The claim is deliberately
   about the reply, not the processing: whether the SUT processed the message — or is still running
   background work we cannot see — stays unknowable from outside; the declared-but-missing reply is
   itself the observable defect. The verdict is _W_-sensitive (a slow SUT and a stuck one look alike),
   so _W_ is set generously and reported with the result — white-box draws the same line (§3.2).
3. **A reply validating as none of the declared messages** → a **schema-mismatch** fault target.
4. **A crash or connection drop mid-process** → a **server-fault** target.

The first is the **coverage target** — declared behaviour, keeping one test per variant reached and
driving the search's diversity. The other three are **fault targets**, flagging defects. Note what the
reply variant can and cannot do: it _distinguishes_ outcomes but cannot _judge_ them, because the
AsyncAPI schema defines **no way to mark a reply message as an error or a success** — whether a variant
named `error` actually is one is naming convention, not declared semantics, unlike REST's standardised
4xx/5xx classes. So a well-formed _error_ reply is **not** a fault but valid, declared behaviour —
exactly as a 400 is in REST — and no `(reply-variant × operation)` target, by itself, ever signals
failure. The archive machinery is reused unchanged; only the target strings differ.

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
        client   # live wire handle (a Kafka producer/consumer pair) — never crosses

    executeAsyncAction(dto):     # the core calls this once per action — the executeRPCEndpoint analogue
        client.publish(dto.address, dto.body, correlationId=dto.correlationId)
        return client.awaitReply(dto.replyAddress, match=dto.correlationId, within=dto.window)
        # the CLIENT places the id on the wire and reads it back off the reply — a record
        #   header on Kafka, a payload field on a socket transport; neither the core nor
        #   the driver above it ever learns which
        # returns the reply — or nothing, when the window W expires
```

Note where the correlation id sits in that split. The **core mints it** — a fresh nonce per execution —
and passes it down as a plain value; the **transport client places it and matches it back**. Nothing in
between needs to know _how_: whether the id ends up in a Kafka record header or in a field of the
service's own JSON envelope is knowledge belonging to the client, which is written against the one
message layout it speaks. That is what keeps the core protocol-agnostic, and it is also what makes the
payload transports reachable at all — on WebSocket the id rides wherever that service's protocol puts it,
and the client is simply the piece that knows.

A note on protocol _versions_: the document pins them only loosely. For Kafka the version lives in the
server's `protocolVersion` field, which is **optional and free-text**, so when it is absent the driver
assumes a conservative default. (Occasionally AsyncAPI encodes the version in the protocol id itself —
`mqtt` and `mqtt5` are named as separate protocols — which pins it exactly; that is the exception, and it
matters mainly to the shared driver under white-box's wider transport set. The `bindingVersion` field
inside binding objects is no substitute either way: it versions the binding _definition_, not the
protocol.) WebSocket is the loose case and points ahead: `ws` versus `wss` distinguishes only transport
security, and **no field anywhere describes the service's own message framing** — which is precisely why
that framing, correlation id included, is the client's business and not the document's.

The transport code (the Kafka publish-and-await) sits in the driver, and can be supplied in one of
two ways — neither of which touches the core:

1. **A module EvoMaster ships** — optional and contract-driven, for a standard transport; the user just
   points it at the SUT. This is only possible because every AsyncAPI service carries the same
   machine-readable contract: the document already tells the module the broker URL, the channels and the
   message schemas, so one module can configure itself for any SUT.
2. **A driver the user writes** — when the SUT speaks a custom or proprietary transport that no shipped
   module covers.

It is **the same driver in both modes.** Black-box uses it purely for wire access — publish, await the
reply, classify — and never pulls code coverage; the reply is the signal. White-box is the identical
driver with instrumentation switched on (§3.2). This is why async is unlike ordinary black-box (a URL,
no driver): with no universal wire, a driver must always be present to hold the client.

#### The individual

There is **one `AsyncApiIndividual`** (an `ApiWsIndividual`) for all transports — **not one per
transport**. The transport appears nowhere in it; Kafka-vs-WebSocket is decided below the driver
interface — which is why the follow-on transport (§2.2) costs the representation nothing.
The subclass itself is as thin as its REST/GraphQL/RPC siblings — the structure is all inherited:

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

#### The fitness function

Sampling needs nothing new worth describing: EvoMaster's base sampler already owns the whole sampling
lifecycle, and per-problem samplers are thin shims over it — the only genuinely new piece is the parser
that derives the action templates from the AsyncAPI document. The **fitness function** is where async
differs, and it is the only class the mode split doubles — the black-box variant here, its white-box
parent in §3.2:

```
AsyncApiBlackBoxFitness.calculateCoverage(ind):    # black-box (subclass)
    for action in ind.mainActions():
        cid   = freshNonce()
        reply = driver.executeAsyncAction(buildDto(action.genes, cid, action.channel))  # publish+await
        if sutCrashed():         record(server_fault, action.operationId)     # bucket 4 — fault
        elif reply == none:      record(no_response, action.operationId)      # bucket 2 — fault: reply missing
        else:
            variant = variantOf(reply, action.replyTemplate)
            if variant == none:  record(schema_mismatch, action.operationId)  # bucket 3 — fault
            else:                record(variant, action.operationId)          # bucket 1 — the coverage key
    return evaluate(ind, recordedTargets)          # no coverage pull
```

Around it: an **`AsyncApiTestCaseWriter`** emits the retained individuals (next); the mutator and
archive are reused unchanged; and two thin Guice modules wire each mode, the black-box one binding the
controller connection unconditionally, since the driver is always needed for the wire.

#### Test generation

Following RPC's `enablePureRPCTestGeneration`, the emitted test is written against a **concrete transport
client, not the driver**: a generated Kafka test uses a real producer/consumer — and, once WebSocket
lands, a real socket client — standard client code a developer can read and run. The driver governs the
_search_; it is not what the suite runs against. The consequence is that the emitted body is concrete and
**varies by
transport**, and the suite carries a dependency on the concrete transport-client library — the black-box
price for having no universal wire.

Concretely, the Kafka tests for `bessj` (one of the controlled NCS services used to demonstrate the
approach) — one per covered `(reply-variant × operation)` — take their topic names, the header the id
rides in, and the message shapes straight from the AsyncAPI document; only the genes and the asserted
variant change:

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
pair is stood up in the test itself — no EvoMaster driver at run time. The generator writes the client
code **to match the wire it found**, reading the header name and the topics from the contract's binding
and `protocolVersion`; on a payload transport it would emit the same placement the transport client used
during the search, since that client is the piece that knows where the id belongs.

### 3.2 White-box

White-box also works **only with AsyncAPI 3.x**, across the four transports, and the reply again
matters, twice over: the same message black-box classifies rides along as white-box's oracle and its
only outside proof the message was consumed — and its arrival shrinks the wait, though it can never
end it outright (next). The cast is the one §3.1 introduced and barely
changes: the fitness gains its white-box parent (below); the
individual, the driver and the writer differ in small, stated ways.

#### Completion: two windows — wait for the reply, then let it settle

When the publish call returns, we do not know whether the SUT has finished processing the message — or
even started. The reply does not settle it either: its arrival proves the handler _answered_, not that
everything the message triggered has finished — a handler can reply first and keep executing, or hand
work off, and that background work is still covering code (§2.3). A single window would therefore have
to be sized for two unrelated things at once — the slowest acceptable reply _and_ the longest
background tail — and every action would wait it out in full. So the first iteration uses **two
windows**: await the correlated reply within the **reply window _W_** — the same _W_ black-box uses —
and, once it arrives, wait only a further **settle window _S_**, much shorter and sized to background
tails alone, before collecting coverage; when no reply arrives, collect at _W_. The reply still cannot
certify completion — that is exactly what _S_ absorbs — but it does prove the handler has run, so the
typical action costs reply-latency + _S_ rather than the full _W_. Operations that declare no reply
always wait the full _W_.

Both windows are heuristics, but not equally blind. _S_ proves nothing — it is only the line after
which we snapshot. _W_ is sharper wherever a reply is declared: the contract promised one, so silence
for the whole window is that promise broken — which is why §3.1 counts it as a fault, black-box and
white-box drawing the same line.

**Fire-and-forget is where both windows go blind at once**, and it is white-box's version of the gap
§2.2 leaves open on the black-box side. With no reply declared, nothing shortens the wait and nothing
confirms it: _W_ elapses in full for every such action and tells us only that time passed, so coverage is
snapshotted at a moment chosen for no reason connected to the SUT. Since these are also the operations
white-box exists to reach — the ones black-box cannot observe at all — the crude answer costs most
exactly where the mode is worth most.

Sharper completion detectors do exist, and instrumentation unlocks the strongest of them: watching the
probes themselves go quiet, tracking the worker threads a message spawns and hands off to, hooking the
listener framework's handler — each buying precision at the cost of knowing more about the SUT. The
outside-in signals of §2.2 stay available here as well; white-box simply has more to work with. **This
proposal deliberately takes the two fixed windows as its first iteration**, and leaves those detectors as
future work — which, with §2.2's black-box counterpart, makes one research question asked from two sides:
_when is a message done?_ Inside is the more tractable side, because the evidence there is the running
code rather than a broker's bookkeeping.

#### The fitness function in white-box

The white-box `AsyncApiFitness` is the parent that §3.1's black-box subclass overrides — same loop
opening, different second half:

```
AsyncApiFitness.calculateCoverage(ind):            # white-box (parent)
    for action in ind.mainActions():
        dto   = buildDto(action.genes, freshNonce(), action.channel)
        reply = driver.executeAsyncAction(dto)     # publish + await reply, within W
        if reply != none: wait(S)                  # settle window: let background work finish
                                                   # (no reply: W has already elapsed — snapshot now)
    return evaluate(ind, driver.getTestResults())  # coverage read at reply + S, or at W
```

- **The outcome is branch-distance coverage**, not a reply variant; for request/reply operations the
  black-box reply oracle rides along as extra targets.
- **The typical wait is reply-latency + _S_**, the full _W_ only when no reply comes — the driver's
  await is unchanged from black-box and returns at the reply; the settle wait is added here, in the one
  class the mode split already doubles. No new completion machinery is needed on the driver.

#### The white-box individual and driver

The individual is the black-box one; its single representational difference is that a consume action may
carry **no `replyTemplate`** (the contract declares no reply), in which case the wait is the full _W_.
The driver is the same `SutController` with instrumentation switched on — `isInstrumentationActivated()`
and `getPackagePrefixesToCover()`, the standard white-box switches; nothing else changes, since the
await already lives in `executeAsyncAction`.

#### What the generated tests assert

Coverage was the search signal, not something a regression test can check. An emitted white-box test
asserts on the observable residue instead: the **reply**, exactly as in §3.1, where one arrived; and the
**side effects** observed at search time — database rows written, messages emitted onto other channels —
baked in as assertions, with unstable values demoted to comments. Structurally it is an ordinary
EvoMaster white-box suite: the driver scaffold for start and reset, a concrete transport client for the
wire, and the SUT running uninstrumented at replay.
