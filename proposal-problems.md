# Open problems & threats to validity — AsyncAPI black-box testing

A running record of problems uncovered while checking the proposal against the **real
AsyncAPI 3.x corpus** (`asyncapi-survey/`) and the **previous thesis** (`Thesis-old.md`).
These are the things the from-scratch work needs to design around or disclose. Evidence
lives in `asyncapi-survey-out/reply-protocols.md`, `asyncapi-llm-audit.md`, and the cited
`Thesis-old.md` sections.

---

## 1. The test oracle is **not** schema-derivable

**Problem.** The original framing (in `Thesis-old.md`, and the first draft of `proposal.md`)
claimed the test *oracle must be schema-derivable only — never SUT-specific*. That is wrong:
EvoMaster cannot know from the AsyncAPI document what a *correct* reply to a given request is.
The oracle / generated assertions must come from the **SUT's observed responses**; the schema
only supplies test **inputs** and a **conformance criterion** to check an observed reply against.

**Status.** Corrected in `proposal.md` (§Differences with REST, §Decisions, §Tests, §Proposed
changes). Recorded here because it was the conceptual error that prompted the restart.

---

## 2. The AsyncAPI 3.0 `reply:` construct is **rare**, and request/reply is usually expressed *without* it

**Problem.** The proposal keys black-box testability off operations with `action: receive` **and**
a `reply:` clause. In the wild that literal construct is scarce, and services that are *semantically*
request/reply frequently don't use it.

**Evidence (corpus survey).** Of **4,151** parsed AsyncAPI 3.x specs (~**984** repos), only **122
specs / 81 repos / 356 operations** declare `action: receive` + `reply:`. And the services the
previous thesis treated as request/reply mostly **don't** use the construct at all:

| Service | Spec(s) in corpus | `action: receive` | `receive`+`reply` | `correlationId` |
|---|---|--:|--:|--:|
| `openagents-org/openagents` | 10 modules (3.0.0) | many (5–14 each) | **0** | **0** |
| `NUWCDIVNPT/stig-manager` | `log-socket.yaml` (3.0.0, ws) | 2 | **0** | **0** |
| `pagopa/p4pa-iam-sync` | `generated.asyncapi.json` (3.0.0) | 2 | **0** | **0** |
| `pagopa/p4pa-registries` | `generated.asyncapi.json` (3.0.0) | 2 | **0** | **0** |

These express request/reply as **separate request/result operations** (openagents), a **stateful
send/receive state machine** (stig-manager, `Thesis-old.md` §31.2), or are plain **fire-and-forget
consumers** (pagopa).

**Implication.** A tool that requires the literal `reply:` field will find very few targets. Decide
explicitly whether the from-scratch engine also handles **convention-based** request/reply (separate
request/response channels linked by `correlationId`; stateful send/receive sequences), or whether the
scope is deliberately restricted to specs that use `reply:` (and that rarity is reported as a finding).

---

## 3. Real AsyncAPI 3.0 contracts are **systematically incomplete**

**Problem.** Published specs routinely omit facts the engine needs:

- **Transport.** Many declare no `servers:` / `protocol:`. In the survey, **186 of 356** reply
  operations are protocol-`undetermined` for this reason. `VoiceBlender/voiceblender` declares
  neither — its transport is only in prose — so it appears in our reply-set as `undetermined`.
- **Correlation.** Contracts omit how a reply correlates to its request. voiceblender stamps
  `request_id` on every message but never declares it as `correlationId.location`.
- **Reply.** The `reply:` field is missing even where reply behaviour exists (see §2).

**Implication.** A black-box tool that depends on a complete contract will under-perform on real
specs. Either the engine must **degrade gracefully** (infer transport, detect correlation
conventions) or the evaluation must restrict to complete contracts and say so. This is the
single biggest external-validity risk for the approach.

---

## 4. The previous thesis's results partly depended on **SUT-side contract patches**

**Problem.** To make some SUTs runnable, `Thesis-old.md` modified their schemas. The runtime
behaviour was never changed and every patch was reported upstream — but some headline numbers were
obtained on *completed* contracts, not the ones GitHub hosts.

| SUT | What was changed | Assessment |
|---|---|---|
| **EVerest** (§30) | **No schema edit.** 22 `_consumer_API.yaml` used as-is (verified vs C++ source). Tool/deploy config only: `--bbAsyncApiActorRole CLIENT`, MQTT port, per-run `restart` after a malformed payload crashed the manager (`nlohmann::json` assertion abort). | ✓ Clean. The crash was a **real fault found**, not a distortion. |
| **stig-manager** (§31) | `log-socket.yaml` used as-is. Only change is a *proposed* upstream PR (mark `data` required), triggered by a **real bug** the tool found: `{type:"command"}` crashes `logSocket.js:148`. | ✓ Positive result — fault-driven, not fabricated surface. |
| **voiceblender** (§31.18) | Three SUT-side patches: add `servers:` + `protocol: ws`; add `correlationId.location: $message.payload#/request_id` to **125 messages**. | ⚠ Defensible as *contract-completeness* (declares what the real service does), but on the **unpatched** contract the engine produced 66 tests, **62 `@Disabled`, every publish failing** — voiceblender's coverage exists *only because of the patch*. |

**Implication.** Patching each SUT is neither scalable nor externally valid (real users won't
pre-patch their schemas). The correct response — which `Thesis-old.md` itself moves toward — is to
push robustness into the **engine** (e.g. auto-detect `request_id`-shaped correlation, infer
transport) rather than the SUT. For the from-scratch work:

1. Treat contract-robustness as an **engine** responsibility, not a per-SUT fix.
2. In the evaluation, report **as-published** vs **completed-contract** results separately.
3. Treat genuine **fault-finds** (EVerest crash, stig-manager handler bug) as the real validation
   signal — not raw target/coverage counts on patched or echo-broker setups.

---

## 5. SUTs that cannot enter a public-corpus evaluation at all

`bitget` / `mexc` (used in `Thesis-old.md` §16) have **no upstream AsyncAPI repo** — a GitHub code
search returns nothing; their schemas were hand-derived from proprietary WSS client docs, and the
matching engines are closed-source. They are not deployable and not enumerable. Any corpus-based
evaluation should exclude this class up front rather than count echo-broker numbers against them.
