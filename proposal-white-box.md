# White-Box Testing of AsyncAPI Services in EvoMaster

This is the **white-box** companion to `proposal.md`, which covers the black-box case and the AsyncAPI,
transport and correlation background this document assumes (and does not repeat). The two share a
problem — a message published into a service is consumed and processed **later**, off the request
thread — but they resolve it from opposite ends. Black-box can only observe what the service sends
_back_, which confined it to the rare **request/reply** subset. White-box adds **instrumentation**:
EvoMaster sees the SUT's code execute, so it can test an operation by its **coverage**, not by a reply.

That difference is decisive. It unlocks the **fire-and-forget** majority — the operations that consume a
message and answer nothing, which black-box called "publishing into a void" and could not test at all.
But it introduces a problem black-box never had: with no synchronous round-trip and no reply to wait on,
**when has the SUT finished processing the message we published?** Until that is answered, EvoMaster
cannot know when to read coverage and score the test. This proposal is built around that question. It
proceeds in four parts: the **problem** (async breaks the synchronous coverage-collection REST relies
on, while making fire-and-forget testable); a **corpus slice** (how much of the AsyncAPI world is
reachable by a white-box, JVM-instrumenting tool); the **approach** (reuse EvoMaster's MIO / Driver /
instrumentation, model a consume as an async action, and solve completion); and an **implementation
proposal** (extend the async-task machinery EvoMaster already has).

## The problem: when has the async test ended?

### White-box changes the signal

In REST white-box testing, EvoMaster runs the instrumented SUT behind a **Driver** and drives it with
HTTP. The call is **synchronous**: the handler executes _during_ the call, the instrumentation records
the lines, branches and **branch distances** it took, and MIO climbs that gradient toward uncovered
code. The HTTP response is almost incidental — **code coverage is the objective**, and it is available
the instant the call returns.

Async messaging removes that instant. When EvoMaster publishes a message, the SUT's consumer runs
**later, on a broker- or listener-driven thread**, after the publish call has already returned. There
is no synchronous point at which "the SUT has finished this message," so the core does not know when to
snapshot coverage and evaluate the individual:

|                            | REST (white-box)           | Async messaging (white-box)                                      |
| -------------------------- | -------------------------- | ---------------------------------------------------------------- |
| Trigger → processing       | same thread, same call     | publish returns; consumer runs later, another thread             |
| When is coverage complete? | when the HTTP call returns | **unknown** — no synchronous signal                              |
| What ends the test         | the response               | must be **detected** (instrumentation inactivity, a completion signal, or a timeout) |

So the central white-box-async problem is not _what to assert_ (coverage answers that) but **when to
collect it**: attributing a test's coverage requires knowing that the async processing it triggered has
finished.

### Fire-and-forget becomes testable — and it is the point

Black-box could only reach operations that reply, because the reply was its only observable signal;
`proposal.md`'s survey showed that subset is small and that products overwhelmingly use Kafka/AMQP for
**fire-and-forget** streaming, outside it. White-box needs no reply: if publishing a message drives the
consumer's code, the branch-distance gradient over that code **is** the signal, whether or not anything
is sent back. So the fire-and-forget majority — the bulk of real async operations — moves **into
scope**. The only thing standing between EvoMaster and testing them is the completion problem above.

For a request/reply operation, white-box gets **both**: the coverage gradient _and_ the reply, so the
black-box reply oracle of `proposal.md` still applies as an extra check. White-box therefore strictly
dominates black-box in _what_ it can test — at the cost of instrumentation and solving completion (a
driver is needed in both modes, since async has no universal wire; white-box just asks more of it).

### The secondary difficulties

- **Non-determinism / timing.** Completion is inherently racy; the same message may finish at different
  times across runs, so the mechanism that decides "done" must tolerate that without flaking.
- **Attribution under concurrency.** With several messages in flight on shared consumers, the coverage
  a run produces must be attributed to the message that caused it — or the tool falls back to
  **single-flight** execution (one outstanding message at a time).
- **The standing white-box requirements.** The SUT must be **instrumentable** — in EvoMaster's case, a
  **JVM** application — and reachable through a Driver. That requirement, more than anything, bounds how
  much of the AsyncAPI world this approach can address, which the next section measures.

## How much is reachable on the JVM: a corpus slice

White-box testing here needs two things at once: a **JVM** service EvoMaster can instrument
(Java / Kotlin / Scala / Groovy), and an **AsyncAPI** document telling it which consume operations to
drive. The reachable population is the intersection — JVM services expressed in AsyncAPI — so we sliced
the same corpus surveyed in `proposal.md` by each repository's primary language (from the survey's
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

| Of the 92 JVM products     | repos  |
| -------------------------- | -----: |
| drivable with modest effort |   **8** |
| drivable with real work     |    51 |
| not usable as a SUT         |    33 |

What the tiers mean — how much stands between the repository and a white-box run (licensing is not a
factor: the SUTs are booted for evaluation, not modified or redistributed):

- **drivable with modest effort** — a runnable JVM service (a container, a fat jar, or `./gradlew
  bootRun`) with an instrumentable consume listener that the AsyncAPI doc actually maps to, over a
  transport we can stand up locally (a Testcontainers broker, or localstack for SNS/SQS): write a thin
  Driver, boot it, point the tool at it.
- **drivable with real work** — a genuine consuming JVM service, but not drivable until real setup is
  done: a heavy platform or monorepo to build and boot, external dependencies to stub (auth servers,
  databases, sibling microservices), a streaming (Kafka Streams) or bespoke consume path to adapt, or
  consume-side spec drift to reconcile by reading the listener before the contract can be trusted.
- **not usable as a SUT** — cannot be driven as a white-box SUT at all: not a runnable service (a client
  or GUI, a library/engine, a codegen scaffold, or a packaging-only module), no async consumer
  (producer-only, or spec-only), an aspirational AsyncAPI file with no matching listener, a bespoke
  non-standard transport EvoMaster cannot instrument-and-drive, or a hard external dependency that
  cannot be stood up.

The reachability gain white-box promised is real: **70 of the 92 carry an instrumentable consumer** —
against black-box, where only a _reply_ counted and `proposal.md` found ~2 usable as-is and ~17 with
work of 81 request/reply repos. Driving by coverage rather than by reply widens the surface to **every
consume operation**, fire-and-forget included.

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
coherent seam is a different shape
entirely: **17 near-identical Ministry-of-Justice HMPPS services**, Kotlin Spring Boot consumers of
domain events over AWS SNS/SQS (16 of the 17 land in "real work," gated only by needing localstack and a
publish-oriented spec) — a ready homogeneous cohort a single Driver template could drive across all
sixteen.

Two caveats bound this. The pass measures only the JVM fraction of repositories that **are** in
AsyncAPI; the far larger population of JVM messaging systems carrying **no** AsyncAPI document is, by
construction, invisible to it. And the per-repo verdicts come from automated tree/archive inspection, so
the modest-effort shortlist should be **hand-confirmed** before it anchors an evaluation.

## The approach

The engine is reused wholesale: EvoMaster's **white-box search — MIO with the branch-distance gradient**,
its **Driver** (`SutController`) that starts, instruments and resets the SUT, its database seeding, and
its external-service (WireMock) machinery — all stay (though the last is wired only for REST today, so a
new problem type must wire it in). Async adds one thing: a **new kind of action** and the lifecycle to
run it.

**A consume operation is an async action.** For each `receive` operation (3.0) or consume block (2.x)
in the AsyncAPI document, EvoMaster generates the message payload from its **JSON Schema** — the same
gene representation, mutation and boundary-fuzzing it already uses for REST — publishes it to the SUT's
channel, and then **waits for the SUT to finish processing it** before reading coverage. With that wait
in place, coverage over the consumer's code is the fitness, and MIO climbs it exactly as for a REST
endpoint. No reply is required, so fire-and-forget operations are first-class.

**Solving "when did it end."** This is the crux. The signal can come from the SUT's own code, the effects
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

**What white-box buys over black-box.** The signal is the SUT's own code, so correlation — the crux of
the black-box proposal — matters far less: for fire-and-forget there is no reply to correlate at all,
and for request/reply the coverage gradient stands on its own with the reply as a bonus oracle. The
open cost moves entirely onto **completion detection** and the **instrumentability** requirement.

Crucially, black-box and white-box **share the action and the individual** — only the fitness differs.
This mirrors REST exactly: both REST modes use one `RestCallAction` and one `RestIndividual`, and
`BlackBoxRestFitness` is a _subclass_ of the white-box `RestFitness` with the coverage pull removed. So
the async consume action and its individual are the same across modes; white-box just swaps in a
coverage-reading, completion-aware fitness in place of the black-box reply oracle.

## Implementation proposal

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

| Piece                | Reused / extended                               | What it does for a consume operation                                                                                                                                               |
| -------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action + individual  | a **new MAIN consume action** in `EnterpriseIndividual` (modelled on `ScheduleTaskAction`'s lifecycle, but fitness-bearing — not an init `EnvironmentAction`) | one action per `receive`/consume operation, sampled and mutated by MIO |
| **Input generation** | REST's schema→gene builder                      | build the message payload from the AsyncAPI message JSON Schema                                                                                                                    |
| **Invocation**       | `customizeScheduleTaskInvocation` (Driver-side) | the Driver publishes the message to the SUT's broker/channel — it holds the transport client, exactly as an RPC Driver holds the RPC stub                                          |
| **Completion**       | `isScheduleTaskCompleted` hook + a **new wait-loop** that calls it | by default, detect completion agnostically — instrumentation-probe inactivity, a downstream write/emit, or broker/offset state — and, when the framework is known, sharpen it with a handler-boundary hook; timeout as last resort |
| **Fitness**          | standard branch-distance coverage               | collected at completion; for request/reply operations, add the black-box reply oracle as an extra target                                                                           |

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

## What the generated tests look like

One design question the coverage-driven search leaves open is the **output**: what does an emitted test
_assert_? Coverage cannot be the answer — it was the **search signal**, not a regression check; a test
that "asserts coverage" would be meaningless to a developer and brittle to any refactor. The emitted
test instead asserts on the **observable residue** of the processing that the completion mechanisms
already capture during the search:

- **the side effects** — the database rows the handler wrote (re-read and compared, via the same SQL
  snapshot that served as a completion signal), the message it emitted onto another channel, the
  external call it made;
- **completion itself** — the handler processed the message without crashing, within the window;
- **the reply**, where the operation has one — the black-box reply assertions ride along unchanged.

So a fire-and-forget test reads: publish the generated message with a concrete transport client (exactly
as in the black-box proposal — the driver governs the search, not the output), await the completion
proxy (the observable side effect, or a bounded wait), then assert on the state the handler left behind.
The test is meaningful without instrumentation, so the emitted suite runs against a plain, uninstrumented
deployment of the SUT.

Grounded in the same controlled NCS SUTs as the black-box proposal (`proposal.md`), the evaluation would
then measure what black-box could not even attempt: coverage achieved on **fire-and-forget** consume
operations, over the JVM transports, with completion resolved by instrumentation. One evaluation asset
must be built first: the current NCS messaging SUTs are **request/reply throughout** (every operation
declares a reply), so the suite must gain **fire-and-forget variants** — consume-only operations with no
reply and an observable side effect (a database write, an emitted event) — before the headline
fire-and-forget measurement can run. Authoring those variants is an explicit deliverable of this
proposal, not an assumption.
