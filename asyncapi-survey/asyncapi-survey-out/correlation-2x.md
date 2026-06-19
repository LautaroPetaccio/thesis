# AsyncAPI 2.x correlation ids

_Generated 2026-06-15T20:31:23Z by `asyncapi_correlation_2x.py`._

**Question.** AsyncAPI 2.x has no first-class `reply:` construct; the native way to pair a reply with its request is the **Correlation ID Object** (a message `correlationId` whose `location` is a runtime expression). How often does the real-world 2.x corpus actually use it, where does the id live, and over which transports?

## Coverage funnel

| Stage | Count |
|-------|------:|
| Unique 2.x blobs (by sha) | 3189 |
| Fetch failed | 6 |
| Parse failed | 363 |
| Not AsyncAPI 2.x | 119 |
| Parsed AsyncAPI 2.x | 2701 |
| **Specs with ≥1 `correlationId`** | **55** |

## Correlation ids

**55 specs across 36 repos** declare a `correlationId` (2.0% of parsed 2.x specs).

### Where the id lives
| Location | specs | repos |
|----------|------:|------:|
| `header` | 46 | 29 |
| `payload` | 7 | 7 |
| `other` | 2 | 3 |

### Field the id maps to (top)
| Field | occurrences |
|-------|------:|
| `transactionId` | 90 |
| `correlationId` | 76 |
| `correlation_id` | 19 |
| `sentAt` | 17 |
| `traceId` | 10 |
| `businessId` | 10 |
| `x-correlation-id` | 8 |
| `reply` | 8 |
| `REQUEST_ID` | 5 |
| `messageId` | 4 |
| `not a valid runtime expression` | 3 |
| `MQMD/CorrelId` | 3 |
| `CountryCode` | 2 |
| `tenantId` | 2 |

### Transport of correlationId specs
| Protocol | specs | repos |
|----------|------:|------:|
| `amqp` | 23 | 18 |
| `kafka` | 19 | 18 |
| `mqtt` | 7 | 7 |
| `http` | 4 | 4 |
| `nats` | 1 | 1 |
| `redis` | 1 | 1 |

## Request/reply context

2.x cannot declare a reply, so request/reply is only a *convention*. Of **2701** parsed 2.x specs, **49** use request/reply-suggestive channel/operation names and **684** have a duplex channel (both `publish` and `subscribe`). Of the **55** specs that declare a `correlationId`, **9** also show one of those request/reply signals — i.e. the id is plausibly used to pair a reply with its request, not just to tag a one-way event.

## Caveats

- Corpus = the survey's `asyncapi: 2.0..2.6` GitHub code-search (`.yaml` only — 2.x `.yml`/`.json` were not separately enumerated), deduped by blob sha.

- `correlationId` presence is detected structurally (message `correlationId`, `$ref` to `components/correlationIds`, `oneOf`, and message `traits`); request/reply is a *naming* heuristic, not a structural reply (2.x has none).


## Appendix — 2.x specs declaring a correlationId

- [`4g3nt4333/Ascy-website`](https://github.com/4g3nt4333/Ascy-website) `public/resources/casestudies/adeo/asyncapi.yaml` — kafka — loc: `header:5`  ·  req/reply-ish
- [`LowellObservatory/Lorax`](https://github.com/LowellObservatory/Lorax) `PWMountAgent/extern/example_api.yaml` — amqp|mqtt — loc: `header:4`
- [`OI4/oi4-oec-service`](https://github.com/OI4/oi4-oec-service) `packages/oi4-oec-asyncapi/asyncapi.yaml` — mqtt — loc: `header:23`
- [`Redocly/redocly-cli`](https://github.com/Redocly/redocly-cli) `resources/async.yaml` — amqp|http|kafka|mqtt — loc: `payload:5`
- [`The-Microservice-Dungeon/game`](https://github.com/The-Microservice-Dungeon/game) `doc/asyncapi-doc.yaml` — kafka — loc: `header:7`
- [`The-Microservice-Dungeon/gamelog`](https://github.com/The-Microservice-Dungeon/gamelog) `docs/event-spec.yaml` — kafka — loc: `header:2`
- [`The-Microservice-Dungeon/robot`](https://github.com/The-Microservice-Dungeon/robot) `swagger/v3/asyncapi.yaml` — kafka — loc: `header:25`
- [`The-Microservice-Dungeon/robot`](https://github.com/The-Microservice-Dungeon/robot) `swagger/v4/asyncapi.yaml` — kafka — loc: `header:21`
- [`The-Microservice-Dungeon/robot`](https://github.com/The-Microservice-Dungeon/robot) `swagger/v5/asyncapi.yaml` — kafka — loc: `header:25`
- [`The-Microservice-Dungeon/trading`](https://github.com/The-Microservice-Dungeon/trading) `swagger/v1/asyncAPI.yaml` — kafka — loc: `header:10`
- [`TykTechnologies/graphql-translator`](https://github.com/TykTechnologies/graphql-translator) `asyncapi/fixtures/print-service-api-2.0.0.yaml` — amqp|mqtt — loc: `header:4`
- [`aml-org/als`](https://github.com/aml-org/als) `als-actions/shared/src/test/resources/actions/hover/async-api20-full.yaml` — amqp|kafka — loc: `header:8`  ·  req/reply-ish
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/cycle/async20/correlation-id/api.yaml` — undetermined — loc: `header:1`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/upanddown/cycle/async20/components/components-cycle.yaml` — amqp — loc: `header:3`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/upanddown/cycle/async20/rpc-server.yaml` — amqp — loc: `header:2`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/validations/async20/components/async-components.yaml` — amqp — loc: `header:2`  ·  req/reply-ish
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/validations/async20/message-obj.yaml` — undetermined — loc: `header:1`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/validations/async20/rpc-server.yaml` — amqp — loc: `header:2`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/validations/async20/validations/invalid-component-names.yaml` — undetermined — loc: `header:2`
- [`aml-org/amf`](https://github.com/aml-org/amf) `amf-cli/shared/src/test/resources/validations/async20/validations/invalid-runtime-expressions.yaml` — undetermined — loc: `other:1`
- [`aml-org/amf-metadata`](https://github.com/aml-org/amf-metadata) `transform/src/test/resources/specs/async20/components/async-components.yaml` — amqp — loc: `header:2`  ·  req/reply-ish
- [`aml-org/amf-metadata`](https://github.com/aml-org/amf-metadata) `transform/src/test/resources/specs/async20/message-obj.yaml` — undetermined — loc: `header:1`
- [`asyncapi/bundler`](https://github.com/asyncapi/bundler) `tests/gh-185.yaml` — amqp — loc: `header:1`
- [`asyncapi/dotnet-rabbitmq-template`](https://github.com/asyncapi/dotnet-rabbitmq-template) `example/asyncapi.yaml` — amqp — loc: `header:2`  ·  req/reply-ish
- [`asyncapi/dotnet-rabbitmq-template`](https://github.com/asyncapi/dotnet-rabbitmq-template) `example/publisher.yaml` — amqp — loc: `header:1`
- [`asyncapi/dotnet-rabbitmq-template`](https://github.com/asyncapi/dotnet-rabbitmq-template) `example/subscriber.yaml` — amqp — loc: `header:1`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Components Object/invalid-correlationIds-key.yaml` — undetermined — loc: `header:1`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Components Object/valid-complete.yaml` — kafka — loc: `header:6`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Correlation ID Object/Fields Types/invalid-description-type.yaml` — undetermined — loc: `header:2`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Correlation ID Object/invalid-location-expression.yaml` — undetermined — loc: `other:2`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Correlation ID Object/valid.yaml` — undetermined — loc: `header:2`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Message Object/valid.yaml` — undetermined — loc: `header:1`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Message Trait Object/valid-internal-ref-correlationId.yaml` — undetermined — loc: `header:3`
- [`asyncapi/tck`](https://github.com/asyncapi/tck) `tests/asyncapi-2.0/Message Trait Object/valid.yaml` — undetermined — loc: `header:2`
- [`dgomezs/learning-AI-agents`](https://github.com/dgomezs/learning-AI-agents) `apps/product-catalog/api/events/asyncapi.yaml` — kafka — loc: `header:2`
- [`edward-hsu-1994/asyncapi-viewer`](https://github.com/edward-hsu-1994/asyncapi-viewer) `src/assets/test.yaml` — http|kafka|mqtt — loc: `payload:5`
- [`fluximus-prime/fluximus-prime.github.io`](https://github.com/fluximus-prime/fluximus-prime.github.io) `docs/private/asyncapi.yaml` — kafka — loc: `header:10`
- [`hdulay/streaming-data-mesh`](https://github.com/hdulay/streaming-data-mesh) `kafka-pubsub.yaml` — kafka — loc: `payload:2`
- [`jbrannst/async`](https://github.com/jbrannst/async) `spec/async.yaml` — amqp|http|kafka|mqtt — loc: `payload:5`
- [`jstoiko/amf`](https://github.com/jstoiko/amf) `amf-client/shared/src/test/resources/upanddown/cycle/async20/components-cycle.yaml` — amqp — loc: `header:3`
- [`jstoiko/amf`](https://github.com/jstoiko/amf) `amf-client/shared/src/test/resources/validations/async20/components/async-components.yaml` — amqp — loc: `header:2`  ·  req/reply-ish
- [`jstoiko/amf`](https://github.com/jstoiko/amf) `amf-client/shared/src/test/resources/validations/async20/message-obj.yaml` — undetermined — loc: `header:1`
- [`leefreemanxyz/redocly-async-api-reproduction`](https://github.com/leefreemanxyz/redocly-async-api-reproduction) `bundled.yaml` — amqp|http|kafka|mqtt — loc: `payload:2`
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `examples/ping/v2/asyncapi.yaml` — undetermined — loc: `header:4`
- [`mcrawfo2/go-msx`](https://github.com/mcrawfo2/go-msx) `schema/asyncapi/testdata/compliance-asyncapi.yaml` — undetermined — loc: `payload:4`
- [`metricq/metricq-rpc-docs`](https://github.com/metricq/metricq-rpc-docs) `manager.asyncapi.yaml` — amqp — loc: `header:1`  ·  req/reply-ish
- [`periclescesar/event-processor`](https://github.com/periclescesar/event-processor) `docs/asyncapi.yaml` — amqp — loc: `header:3`
- [`prakhar47b/faststream-poc`](https://github.com/prakhar47b/faststream-poc) `asyncapi.yaml` — amqp — loc: `header:4`
- [`shashanksaxena-tz/munciplaityTax`](https://github.com/shashanksaxena-tz/munciplaityTax) `specs/1-withholding-reconciliation/contracts/event-w1-filed.yaml` — kafka|redis — loc: `payload:12`
- [`siom79/jasyncapicmp`](https://github.com/siom79/jasyncapicmp) `jasyncapicmp-maven-plugin/src/it/simple-it/new_2.6.0.yaml` — amqp — loc: `header:2`
- [`siom79/jasyncapicmp`](https://github.com/siom79/jasyncapicmp) `jasyncapicmp-maven-plugin/src/it/simple-it/old_2.6.0.yaml` — amqp — loc: `header:2`
- [`somosphi/ts-seed-hexagonal`](https://github.com/somosphi/ts-seed-hexagonal) `docs/asyncapi.yaml` — amqp — loc: `header:2`  ·  req/reply-ish
- [`weidmueller/u-os-hub-api`](https://github.com/weidmueller/u-os-hub-api) `variable-nats-asyncapi.yaml` — nats — loc: `header:8`  ·  req/reply-ish
- [`zuevrs/yanote`](https://github.com/zuevrs/yanote) `yanote-js/test/fixtures/asyncapi/trait-declarations-inline-v2.yaml` — kafka — loc: `header:1`
- [`zuevrs/yanote`](https://github.com/zuevrs/yanote) `yanote-js/test/fixtures/asyncapi/trait-declarations-trait-v2.yaml` — kafka — loc: `header:2`