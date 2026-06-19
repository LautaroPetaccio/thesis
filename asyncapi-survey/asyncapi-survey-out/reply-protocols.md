# AsyncAPI 3.x request-reply protocols

_Generated 2026-06-07T23:57:30Z by `asyncapi_reply_protocols.py`._

**Question.** For AsyncAPI 3.x specs, which messaging protocols are used by operations implementing the request-reply pattern where the SUT is the responder — i.e. operations with `action: receive` **and** a `reply` (the reply may target the same channel as the request, a different channel, or an address).

**Method.** The full 3.x corpus (yaml+yml+json, 3.0.0+3.1.0) enumerated by `asyncapi_adoption_survey.sh` was fetched and parsed. Reply operations were detected structurally; protocols were attributed **reply-scoped** (the channels the operation touches → their servers' `protocol` and/or `bindings`) for the headline, and **document-level** (any protocol declared in the spec) for context.

## Coverage funnel

| Stage | Count |
|-------|------:|
| Unique 3.x blobs (by sha) | 4339 |
| &nbsp;&nbsp;by extension | json=46, yaml=3719, yml=574 |
| Fetch failed (deleted/renamed since survey) | 11 |
| Parse failed | 36 |
| Not AsyncAPI 3.x (text-match false positives) | 141 |
| Parsed AsyncAPI 3.x | 4151 |
| &nbsp;&nbsp;with no `operations` map | 668 |
| **Specs with ≥1 `receive`+`reply` op** | **122** |
| Total `receive`+`reply` operations | 356 |

## Headline — protocols of receive+reply operations (reply-scoped)

Counted from the protocol of the request and reply channels each operation uses. An operation using multiple protocols contributes to each.

| Protocol | receive+reply ops | specs | repos |
|----------|------------------:|------:|------:|
| `kafka` | 27 | 24 | 20 |
| `mqtt` | 31 | 15 | 5 |
| `ws` | 73 | 11 | 9 |
| `http` | 18 | 9 | 6 |
| `amqp` | 13 | 6 | 6 |
| `sqs` | 8 | 6 | 4 |
| `wss` | 11 | 5 | 6 |
| `googlepubsub` | 4 | 2 | 2 |
| `redis` | 2 | 2 | 1 |
| `stomp` | 3 | 1 | 1 |
| _undetermined_ | 186 | | |

_`undetermined` = the spec declares no server `protocol` and no protocol `bindings` the operation can reach — i.e. a transport-agnostic spec (common in examples/fixtures/tooling). Where channels don't pin a server, the document's server protocol is used (flagged `viaAllServers`)._

## Document-level protocols (context)

Any protocol declared anywhere in a spec that has ≥1 receive+reply operation.

| Protocol | specs | repos |
|----------|------:|------:|
| `kafka` | 31 | 25 |
| `mqtt` | 16 | 6 |
| `ws` | 11 | 9 |
| `amqp` | 10 | 9 |
| `http` | 10 | 7 |
| `sqs` | 6 | 4 |
| `wss` | 5 | 6 |
| `googlepubsub` | 2 | 2 |
| `jms` | 2 | 2 |
| `redis` | 2 | 1 |
| `stomp` | 1 | 1 |

## Caveats

- Corpus seeded by the survey's `asyncapi: 3.0.0/3.1.0` GitHub code-search (yaml from the May snapshot; yml/json freshly enumerated) — a mild temporal mix. Parsing removes text-match false positives but cannot recover files GitHub never enumerated.

- Deduped by blob `sha` (identical content counted once); `repos` counts every repo containing that blob (forks inflate repo counts; `specs` does not).

- Only internal `#/...` `$ref`s are resolved; operations whose channels are external refs with no inline bindings fall into `undetermined`.

## Appendix — specs with receive+reply operations

- [`BackendFans83/Taxi`](https://github.com/BackendFans83/Taxi) `pricing-service/docs/asyncapi.yaml` (asyncapi 3.0.0)
    - `CalculatePriceOperation`: req=#/channels/CalculatePrice reply=#/channels/CalculatePrice (same channel) → **undetermined**
- [`CodeBeast357/webosapi-asyncapi`](https://github.com/CodeBeast357/webosapi-asyncapi) `kraken-websocket-request-reply-multiple-channels-asyncapi.yml` (asyncapi 3.0.0, +2 more repo(s))
    - `receivePing`: req=#/channels/ping reply=#/channels/pong → **undetermined**
    - `subscribe`: req=#/channels/subscribe reply=#/channels/currencyInfo → **undetermined**
    - `unsubscribe`: req=#/channels/unsubscribe reply=#/channels/currencyInfo → **undetermined**
- [`CodingFlow/rating-service-dotnet`](https://github.com/CodingFlow/rating-service-dotnet) `RatingService.Api/asyncapi.yaml` (asyncapi 3.0.0)
    - `getRatings`: req=#/channels/getRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
    - `postRatings`: req=#/channels/postRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
    - `deleteRatings`: req=#/channels/deleteRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
- [`CodingFlow/rating-service-dotnet`](https://github.com/CodingFlow/rating-service-dotnet) `RequestDecoratorGenerator/TestLibrary/asyncapi.yaml` (asyncapi 3.0.0)
    - `getRatings`: req=#/channels/getRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
    - `postRatings`: req=#/channels/postRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
    - `deleteRatings`: req=#/channels/deleteRatings reply={'location': '$message.payload#/originReplyTo'} → **undetermined**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/auth_token_validator_API.yaml` (asyncapi 3.0.0)
    - `receive_request_validate_token`: req=#/channels/receive_request_validate_token reply=#/channels/send_reply_validate_token → **mqtt**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/display_message_API.yaml` (asyncapi 3.0.0)
    - `receive_request_set_display_message`: req=#/channels/receive_request_set_display_message reply=#/channels/send_reply_set_display_message → **mqtt**
    - `receive_request_get_display_message`: req=#/channels/receive_request_get_display_message reply=#/channels/send_reply_get_display_message → **mqtt**
    - `receive_request_clear_display_message`: req=#/channels/receive_request_clear_display_message reply=#/channels/send_reply_clear_display_message → **mqtt**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/evse_board_support_API.yaml` (asyncapi 3.0.0)
    - `receive_request_reset`: req=#/channels/receive_request_reset reply=#/channels/send_reply_reset → **mqtt**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/ocpp_consumer_API.yaml` (asyncapi 3.0.0)
    - `receive_request_data_transfer_incoming`: req=#/channels/receive_request_data_transfer_incoming reply=#/channels/send_reply_data_transfer_incoming → **mqtt**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/powermeter_API.yaml` (asyncapi 3.0.0)
    - `receive_request_start_transaction`: req=#/channels/receive_request_start_transaction reply=#/channels/send_reply_start_transaction → **mqtt**
    - `receive_request_stop_transaction`: req=#/channels/receive_request_stop_transaction reply=#/channels/send_reply_stop_transaction → **mqtt**
- [`EVerest/EVerest`](https://github.com/EVerest/EVerest) `docs/source/reference/EVerest_API/system_API.yaml` (asyncapi 3.0.0)
    - `receive_request_update_firmware`: req=#/channels/receive_request_update_firmware reply=#/channels/send_reply_update_firmware → **mqtt**
    - `receive_request_upload_logs`: req=#/channels/receive_request_upload_logs reply=#/channels/send_reply_upload_logs → **mqtt**
    - `receive_request_is_reset_allowed`: req=#/channels/receive_request_is_reset_allowed reply=#/channels/send_reply_is_reset_allowed → **mqtt**
    - `receive_request_set_system_time`: req=#/channels/receive_request_set_system_time reply=#/channels/send_reply_set_system_time → **mqtt**
    - `receive_request_get_boot_reason`: req=#/channels/receive_request_get_boot_reason reply=#/channels/send_reply_get_boot_reason → **mqtt**
- [`Forsakringskassan/gradle-conventions`](https://github.com/Forsakringskassan/gradle-conventions) `examples/asyncapi/asyncapi.yaml` (asyncapi 3.0.0)
    - `onVahRtfRequest`: req=#/channels/vah.rtf.requests reply=#/channels/vah.rtf.responses → **undetermined**
- [`Forsakringskassan/rimfrost-regel-rtf-manuell-asyncapi`](https://github.com/Forsakringskassan/rimfrost-regel-rtf-manuell-asyncapi) `asyncapi.yaml` (asyncapi 3.0.0)
    - `RtfManuellRequest`: req=#/channels/rtf.manuell.requests reply=#/channels/rtf.manuell.responses → **undetermined**
- [`Forsakringskassan/template-asyncapi`](https://github.com/Forsakringskassan/template-asyncapi) `asyncapi.yaml` (asyncapi 3.0.0)
    - `onExempelRtfRequest`: req=#/channels/exempel.rtf.requests reply=#/channels/exempel.rtf.responses → **undetermined**
- [`G-USI/asyncapi-python`](https://github.com/G-USI/asyncapi-python) `examples/amqp-rpc/spec/server.asyncapi.yaml` (asyncapi 3.0.0)
    - `onPingRequest`: req=./common.asyncapi.yaml#/channels/ping reply=./common.asyncapi.yaml#/channels/pong → **undetermined**
- [`G-USI/asyncapi-python`](https://github.com/G-USI/asyncapi-python) `examples/specs/financial-trading-system.yaml` (asyncapi 3.0.0)
    - `analytics.process`: req=(inline) reply=(inline) (same channel) → **amqp, kafka, ws**
- [`G-USI/asyncapi-python`](https://github.com/G-USI/asyncapi-python) `tests/codegen/specs/rpc.yaml` (asyncapi 3.0.0)
    - `user.process`: req=#/channels/user_requests reply=#/channels/user_responses → **undetermined**
- [`GreenRover/async-api-validator`](https://github.com/GreenRover/async-api-validator) `tests/controllers/apis/monalesy_service_desc_3.0.yaml` (asyncapi 3.0.0)
    - `serviceDescRequestGlobal`: req=#/channels/servicedesc-request-global reply=#/channels/response → **undetermined**
    - `serviceDescRequestOne`: req=#/channels/servicedesc-request-one reply=#/channels/response → **undetermined**
    - `serviceStateRequestGlobal`: req=#/channels/servicedesc-request-global reply=#/channels/response → **undetermined**
    - `serviceStateRequestOne`: req=#/channels/servicedesc-request-one reply=#/channels/response → **undetermined**
- [`Integration-Project-2026-Groep-2/CRM`](https://github.com/Integration-Project-2026-Groep-2/CRM) `docs/crm-asyncapi-v1.yaml` (asyncapi 3.1.0)
    - `receiveCompanyDataRequest`: req=#/channels/facturatieCompanyRequested reply=#/channels/crmCompanyResponded → **amqp**
    - `receivePersonLookup`: req=#/channels/kassaPersonLookupRequested reply=#/channels/crmPersonLookupResponded → **amqp**
    - `receiveUnpaidRequest`: req=#/channels/kassaUnpaidRequested reply=#/channels/crmUnpaidResponded → **amqp**
- [`Jack-the-Pro101/vequate`](https://github.com/Jack-the-Pro101/vequate) `spec/asyncapi/lobby.asyncapi.yaml` (asyncapi 3.1.0)
    - `onChallenge`: req=#/channels/games.challenge reply=#/channels/games.challenge.response → **redis**
- [`Jack-the-Pro101/vequate`](https://github.com/Jack-the-Pro101/vequate) `spec/asyncapi/orchestrator.asyncapi.yaml` (asyncapi 3.1.0)
    - `onServerCreateRequest`: req=#/channels/servers.create reply=#/channels/servers.creating → **redis**
- [`KrushilProlink/studio-new`](https://github.com/KrushilProlink/studio-new) `src/examples/real-world/kraken-api-request-reply-filter.yml` (asyncapi 3.0.0, +5 more repo(s))
    - `receivePing`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveSubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveUnsubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
- [`Lap-Platform/LAP`](https://github.com/Lap-Platform/LAP) `examples/verbose/asyncapi/adeo-kafka-request-reply-asyncapi.yml` (asyncapi 3.1.0, +1 more repo(s))
    - `receiveACostingRequest`: req=#/channels/costingRequestChannel reply=#/channels/costingResponseChannel → **kafka**
- [`Lap-Platform/LAP`](https://github.com/Lap-Platform/LAP) `examples/verbose/asyncapi/kraken-websocket-request-reply-multiple-channels-asyncapi.yml` (asyncapi 3.1.0, +1 more repo(s))
    - `receivePing`: req=#/channels/ping reply=#/channels/pong → **undetermined**
    - `subscribe`: req=#/channels/subscribe reply=#/channels/currencyInfo → **undetermined**
    - `unsubscribe`: req=#/channels/unsubscribe reply=#/channels/currencyInfo → **undetermined**
- [`Matusko/flea`](https://github.com/Matusko/flea) `libs/flea/asyncapi-generator-typescript-cdk-event-bridge/src/lib/test-fixtures/test-hotel-asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveQueryHotelRoomList`: req=#/channels/hotel.query reply=#/channels/hotel.query (same channel) → **http**
- [`Netcracker/qubership-apihub-api-processor`](https://github.com/Netcracker/qubership-apihub-api-processor) `test/projects/asyncapi-changes/operation/change-reply/after.yaml` (asyncapi 3.0.0)
    - `operation1`: req=#/channels/channel1 reply={'location': '$message.header#/replyTo', 'description': 'Reply to the new address'} → **undetermined**
- [`Netcracker/qubership-integration-runtime-catalog`](https://github.com/Netcracker/qubership-integration-runtime-catalog) `src/test/resources/asyncapi/v3/kafka-v3-channel-ref-messages.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `receiveWithReply`: req=#/channels/inlineChannel reply=#/channels/replyTargetChannel → **undetermined**
- [`OAI/Arazzo-Specification`](https://github.com/OAI/Arazzo-Specification) `examples/1.1.0/pet-asyncapi.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/place-order reply=#/channels/confirm-order → **kafka**
- [`Ravip2006/Demo`](https://github.com/Ravip2006/Demo) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_v1.yaml` (asyncapi 3.0.0)
    - `onPlaceOrder`: req=#/channels/place-order reply=#/channels/process-order → **undetermined**
- [`Redocly/redocly-cli`](https://github.com/Redocly/redocly-cli) `tests/e2e/split/asyncapi3-complex/asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveUserLoggedIn`: req=#/channels/userLoggedIn reply=? → **undetermined**
- [`RobinTail/zod-sockets`](https://github.com/RobinTail/zod-sockets) `example/example-documentation.yaml` (asyncapi 3.0.0)
    - `RootRecvOperationPing`: req=#/channels/Root reply=#/channels/Root (same channel) → **http, ws**
- [`StableCoinTF/StableCoinBC_Adapter_Docs`](https://github.com/StableCoinTF/StableCoinBC_Adapter_Docs) `asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveAccountCreate`: req=#/channels/accountCreate reply=#/channels/accountCreated → **undetermined**
    - `receiveAccountDeploy`: req=#/channels/accountDeploy reply=#/channels/accountDeployed → **undetermined**
    - `receiveWithdrawRequest`: req=#/channels/withdrawRequest reply=#/channels/withdrawResult → **undetermined**
    - `receivePaymentRequest`: req=#/channels/paymentRequest reply=#/channels/paymentResult → **undetermined**
    - `receiveConfirm`: req=#/channels/commonConfirm reply=#/channels/commonConfirmed → **undetermined**
    - `receiveSettlementRequest`: req=#/channels/settlementRequest reply=#/channels/settlementResult → **undetermined**
    - `receiveBalanceInquiry`: req=#/channels/balanceInquiry reply=#/channels/balanceResult → **undetermined**
    - `receiveReconciliationInquiry`: req=#/channels/reconciliationInquiry reply=#/channels/reconciliationResult → **undetermined**
    - `receiveSubmissionInquiry`: req=#/channels/submissionInquiry reply=#/channels/submissionResult → **undetermined**
    - `receiveMonitorEntrypointTransfer`: req=#/channels/monitorEntrypointTransfer reply=#/channels/monitorEntrypointTransferResult → **undetermined**
    - `receiveMonitorMetricInquiry`: req=#/channels/monitorMetricInquiry reply=#/channels/monitorMetricResult → **undetermined**
    - `receiveMonitorContractInquiry`: req=#/channels/monitorContractInquiry reply=#/channels/monitorContractResult → **undetermined**
    - `receiveMonitorContractHistory`: req=#/channels/monitorContractHistory reply=#/channels/monitorContractHistoryResult → **undetermined**
    - `receiveMonitorInfraInquiry`: req=#/channels/monitorInfraInquiry reply=#/channels/monitorInfraResult → **undetermined**
- [`VoiceBlender/voiceblender`](https://github.com/VoiceBlender/voiceblender) `asyncapi.yaml` (asyncapi 3.0.0)
    - `recv_list_legs`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_get_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_create_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_answer_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_delete_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_mute_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_unmute_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_deaf_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_undeaf_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_hold_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_unhold_leg`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_send_leg_dtmf`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_accept_leg_dtmf`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_reject_leg_dtmf`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_send_leg_rtt`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_accept_leg_rtt`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_reject_leg_rtt`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_webrtc_offer`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_webrtc_add_candidate`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_webrtc_get_candidates`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_list_rooms`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_get_room`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_create_room`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_delete_room`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_add_leg_to_room`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_remove_leg_from_room`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_bridge_create`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_bridge_list`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_bridge_get`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_bridge_update`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_bridge_delete`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_routing_get`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_routing_set`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_routing_update`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_set_leg_role`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_ring`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_early_media`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_amd_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_record_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_record_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_record_pause`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_record_resume`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_record_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_record_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_record_pause`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_record_resume`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_play_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_play_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_play_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_play_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_play_volume`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_play_volume`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_stt_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_stt_start`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_stt_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_stt_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_tts`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_tts`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_transfer`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_elevenlabs`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_vapi`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_pipecat`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_deepgram`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_elevenlabs`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_vapi`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_pipecat`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_deepgram`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_stop`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_leg_agent_message`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
    - `recv_room_agent_message`: req=#/channels/vsi reply=#/channels/vsi (same channel) → **undetermined**
- [`WaleedAshraf/asyncapi-validator`](https://github.com/WaleedAshraf/asyncapi-validator) `test/schemas/v3.0.0/pingPong.yml` (asyncapi 3.0.0)
    - `pingRequest`: req=#/channels/ping reply=#/channels/pong → **undetermined**
- [`YOU54F/pact-asyncapi-comparator`](https://github.com/YOU54F/pact-asyncapi-comparator) `asyncapi/ping-pong-dynamic.yml` (asyncapi 3.0.0)
    - `pingRequest`: req=#/channels/ping reply=#/channels/pong → **undetermined**
- [`acidtango/ollert-backend`](https://github.com/acidtango/ollert-backend) `asyncapi.yml` (asyncapi 3.0.0)
    - `addColumn`: req=#/channels/boardCommands reply=#/channels/boardEvents → **ws**
- [`adreno255/nurtura-backend`](https://github.com/adreno255/nurtura-backend) `docs/asyncapi-websocket.yml` (asyncapi 3.0.0)
    - `onConnect`: req=#/channels/root reply=? → **ws, wss**
    - `broadcastSensorData`: req=#/channels/sensorUpdate reply=? → **ws, wss**
    - `broadcastDeviceStatus`: req=#/channels/deviceStatusUpdate reply=? → **ws, wss**
    - `broadcastNotification`: req=#/channels/notificationUpdate reply=? → **ws, wss**
    - `broadcastAutomationEvent`: req=#/channels/automationEventTriggered reply=? → **ws, wss**
    - `broadcastUserNotifications`: req=#/channels/userNotificationUpdate reply=? → **ws, wss**
- [`aklivity/todo-service`](https://github.com/aklivity/todo-service) `src/main/api/todo-service-asyncapi-v3.yaml` (asyncapi 3.0.0)
    - `createTask`: req=None reply=? → **undetermined**
    - `renameTask`: req=None reply=? → **undetermined**
    - `deleteTask`: req=None reply=? → **undetermined**
- [`aklivity/zilla-demos`](https://github.com/aklivity/zilla-demos) `extras-containers/todo/todo-command-service/src/main/api/todo-service-asyncapi-v3.yaml` (asyncapi 3.0.0)
    - `createTask`: req=None reply=? → **undetermined**
    - `updateTask`: req=None reply=? → **undetermined**
    - `deleteTask`: req=None reply=? → **undetermined**
- [`ambihome-gmbh/asyncapi`](https://github.com/ambihome-gmbh/asyncapi) `examples/multi_stack/priv/schema/service.yaml` (asyncapi 3.0.0)
    - `create`: req=#/channels/create reply=#/channels/create_response → **mqtt**
    - `pop`: req=#/channels/pop reply=#/channels/pop_response → **mqtt**
- [`asyncapi/converter-js`](https://github.com/asyncapi/converter-js) `test/output/openapi-to-asyncapi/callbacks_and_contents.yml` (asyncapi 3.0.0)
    - `subscribeWebhook`: req=#/channels/webhooks reply=#/channels/webhooks (same channel) → **http**
    - `getUser`: req=#/channels/users_{userId} reply=#/channels/users_{userId} (same channel) → **http**
    - `getUserPosts`: req=#/channels/users_{userId}_posts reply=#/channels/users_{userId}_posts (same channel) → **http**
    - `uploadFile`: req=#/channels/upload reply=#/channels/upload (same channel) → **http**
    - `getStream`: req=#/channels/stream reply=#/channels/stream (same channel) → **http**
- [`asyncapi/converter-js`](https://github.com/asyncapi/converter-js) `test/output/openapi-to-asyncapi/components_and_security.yml` (asyncapi 3.0.0)
    - `getsecure`: req=#/channels/secure reply=#/channels/secure (same channel) → **http**
    - `getoauth`: req=#/channels/oauth reply=#/channels/oauth (same channel) → **http**
- [`asyncapi/converter-js`](https://github.com/asyncapi/converter-js) `test/output/openapi-to-asyncapi/external_reference.yml` (asyncapi 3.0.0)
    - `gettest`: req=#/channels/test reply=#/channels/test (same channel) → **http**
- [`asyncapi/converter-js`](https://github.com/asyncapi/converter-js) `test/output/openapi-to-asyncapi/operation_and_parameter.yml` (asyncapi 3.0.0)
    - `listItems`: req=#/channels/items reply=#/channels/items (same channel) → **http**
    - `createItem`: req=#/channels/items reply=#/channels/items (same channel) → **http**
    - `getItem`: req=#/channels/items_{itemId} reply=#/channels/items_{itemId} (same channel) → **http**
    - `updateItem`: req=#/channels/items_{itemId} reply=#/channels/items_{itemId} (same channel) → **http**
    - `deleteItem`: req=#/channels/items_{itemId} reply=#/channels/items_{itemId} (same channel) → **http**
- [`asyncapi/generator`](https://github.com/asyncapi/generator) `packages/templates/clients/kafka/test/__fixtures__/asyncapi-adeo.yml` (asyncapi 3.0.0)
    - `requestCosting`: req=#/channels/costingRequest reply=#/channels/costingResponse → **kafka**
- [`asyncapi/generator`](https://github.com/asyncapi/generator) `packages/templates/clients/websocket/test/__fixtures__/asyncapi-slack-client.yml` (asyncapi 3.0.0)
    - `onEvent`: req=#/channels/root reply=#/channels/root (same channel) → **ws, wss**
- [`asyncapi/jasyncapi`](https://github.com/asyncapi/jasyncapi) `asyncapi-core/src/test/resources/examples/v3.0.0/adeo-kafka-request-reply-asyncapi.yml` (asyncapi 3.0.0, +1 more repo(s))
    - `receiveACostingRequest`: req=#/channels/costingRequestChannel reply=#/channels/costingResponseChannel → **kafka**
- [`asyncapi/jasyncapi`](https://github.com/asyncapi/jasyncapi) `asyncapi-core/src/test/resources/examples/v3.0.0/kraken-websocket-request-reply-message-filter-in-reply-asyncapi.yml` (asyncapi 3.0.0)
    - `receivePing`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveSubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveUnsubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
- [`asyncapi/jasyncapi`](https://github.com/asyncapi/jasyncapi) `asyncapi-core/src/test/resources/examples/v3.0.0/kraken-websocket-request-reply-multiple-channels-asyncapi.yml` (asyncapi 3.0.0)
    - `receivePing`: req=#/channels/ping reply=#/channels/pong → **undetermined**
    - `subscribe`: req=#/channels/subscribe reply=#/channels/currencyInfo → **undetermined**
    - `unsubscribe`: req=#/channels/unsubscribe reply=#/channels/currencyInfo → **undetermined**
- [`asyncapi/markdown-template`](https://github.com/asyncapi/markdown-template) `test/spec/asyncapi_v3.yml` (asyncapi 3.0.0)
    - `createSomeRequest`: req=#/channels/someRequest reply=#/channels/someRequestReply → **mqtt**
- [`asyncapi/spec`](https://github.com/asyncapi/spec) `examples/kraken-websocket-request-reply-message-filter-in-reply-asyncapi.yml` (asyncapi 3.1.0, +1 more repo(s))
    - `receivePing`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveSubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveUnsubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
- [`asyncapi/website`](https://github.com/asyncapi/website) `public/resources/casestudies/adeo/asyncapi.yaml` (asyncapi 3.0.0)
    - `requestCosting`: req=#/channels/costingRequest reply=#/channels/costingResponse → **kafka**
- [`codemonstersteam/mq-rest-sync-adapter`](https://github.com/codemonstersteam/mq-rest-sync-adapter) `contract-tests/testdata/structure_validator/request_reply_provider_asyncapi.yml` (asyncapi 3.0.0)
    - `receiveProcessEventRequest`: req=#/channels/process_event_request reply=#/channels/process_event_response → **amqp**
- [`codemonstersteam/pinout-asyncapi`](https://github.com/codemonstersteam/pinout-asyncapi) `cmd/testdata/cmd/producer-asyncapi-fixed.yml` (asyncapi 3.0.0, +1 more repo(s))
    - `receiveBalanceRequest`: req=#/channels/restGetBalanceRequest reply=#/channels/restGetBalanceRequest (same channel) → **http**
- [`codemonstersteam/pinout-asyncapi`](https://github.com/codemonstersteam/pinout-asyncapi) `testdata/channel_validator/provider.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `receiveUserEvent`: req=#/channels/notifications~1user-events reply=#/channels/notifications~1user-events (same channel) → **amqp**
- [`codemonstersteam/pinout-asyncapi`](https://github.com/codemonstersteam/pinout-asyncapi) `testdata/contract_validator/provider_external.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `receiveBalanceRequest`: req=#/channels/walletBalanceRequest reply=#/channels/walletBalanceResponse → **http**
- [`coinpaprika/coinpaprika-docs`](https://github.com/coinpaprika/coinpaprika-docs) `api-reference/streaming-api/asyncapi.yml` (asyncapi 3.0.0, +1 more repo(s))
    - `ping`: req=#/channels/~1ticks reply=? → **wss**
- [`davidtgillard/fits`](https://github.com/davidtgillard/fits) `docs/asyncapi.yaml` (asyncapi 3.1.0)
    - `handleGraphRpc`: req=#/channels/fitsStdin reply=#/channels/fitsStdout → **undetermined**
    - `handleGraphRpcOnSocket`: req=#/channels/socketInbound reply=#/channels/socketOutbound → **undetermined**
- [`dduartee/sigaa-socket-api`](https://github.com/dduartee/sigaa-socket-api) `asyncapi.yaml` (asyncapi 3.0.0)
    - `validateAuth`: req=#/channels/authValid reply=#/channels/authValid (same channel) → **ws**
    - `loginUser`: req=#/channels/userLogin reply=#/channels/userLogin (same channel) → **ws**
    - `getUserInfo`: req=#/channels/userInfo reply=#/channels/userInfo (same channel) → **ws**
    - `getBondsList`: req=#/channels/bondsList reply=#/channels/bondsList (same channel) → **ws**
    - `getCoursesList`: req=#/channels/coursesList reply=#/channels/coursesList (same channel) → **ws**
    - `getGradesList`: req=#/channels/gradesList reply=#/channels/gradesList (same channel) → **ws**
    - `getActivitiesList`: req=#/channels/activitiesList reply=#/channels/activitiesList (same channel) → **ws**
    - `getAbsencesList`: req=#/channels/absencesList reply=#/channels/absencesList (same channel) → **ws**
    - `getHomeworkContent`: req=#/channels/homeworkContent reply=#/channels/homeworkContent (same channel) → **ws**
    - `getLessonsList`: req=#/channels/lessonsList reply=#/channels/lessonsList (same channel) → **ws**
    - `getNewsList`: req=#/channels/newsList reply=#/channels/newsList (same channel) → **ws**
    - `getSyllabusContent`: req=#/channels/syllabusContent reply=#/channels/syllabusContent (same channel) → **ws**
    - `getInstitutionsList`: req=#/channels/institutionsList reply=#/channels/institutionsList (same channel) → **ws**
- [`dduartee/sigaa-socket-api`](https://github.com/dduartee/sigaa-socket-api) `asyncapi/asyncapi.yaml` (asyncapi 3.0.0)
    - `validateAuth`: req=#/channels/authValid reply=#/channels/authValid (same channel) → **ws**
    - `loginUser`: req=#/channels/userLogin reply=#/channels/userLogin (same channel) → **ws**
    - `getUserInfo`: req=#/channels/userInfo reply=#/channels/userInfo (same channel) → **ws**
    - `getBondsList`: req=#/channels/bondsList reply=#/channels/bondsList (same channel) → **ws**
    - `getCoursesList`: req=#/channels/coursesList reply=#/channels/coursesList (same channel) → **ws**
    - `getGradesList`: req=#/channels/gradesList reply=#/channels/gradesList (same channel) → **ws**
    - `getActivitiesList`: req=#/channels/activitiesList reply=#/channels/activitiesList (same channel) → **ws**
    - `getAbsencesList`: req=#/channels/absencesList reply=#/channels/absencesList (same channel) → **ws**
    - `getHomeworkContent`: req=#/channels/homeworkContent reply=#/channels/homeworkContent (same channel) → **ws**
    - `getLessonsList`: req=#/channels/lessonsList reply=#/channels/lessonsList (same channel) → **ws**
    - `getNewsList`: req=#/channels/newsList reply=#/channels/newsList (same channel) → **ws**
    - `getSyllabusContent`: req=#/channels/syllabusContent reply=#/channels/syllabusContent (same channel) → **ws**
    - `getInstitutionsList`: req=#/channels/institutionsList reply=#/channels/institutionsList (same channel) → **ws**
- [`dghilardi/asyncapiv3`](https://github.com/dghilardi/asyncapiv3) `test-res/3.0.0/adeo-kafka-request-reply-asyncapi.yml` (asyncapi 3.0.0)
    - `receiveACostingRequest`: req=#/channels/costingRequestChannel reply=#/channels/costingResponseChannel → **kafka**
- [`eclipse-uprotocol/symphony-target-example-rust`](https://github.com/eclipse-uprotocol/symphony-target-example-rust) `uservice/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `Get`: req=#/channels/getRequests reply=#/channels/getResponses → **undetermined**
    - `Update`: req=#/channels/updateRequests reply=#/channels/updateResponses → **undetermined**
    - `Delete`: req=#/channels/deleteRequests reply=#/channels/deleteResponses → **undetermined**
- [`evryfs/asyncapi-generator`](https://github.com/evryfs/asyncapi-generator) `asyncapi-generator-core/src/test/resources/asyncapi_kafka_single_file_example.yaml` (asyncapi 3.0.0)
    - `receiveLightMeasurement`: req=#/channels/lightingMeasured reply=#/channels/lightingMeasured (same channel) → **kafka**
- [`evryfs/asyncapi-generator`](https://github.com/evryfs/asyncapi-generator) `asyncapi-generator-core/src/test/resources/examples/asyncapi_kafka_request_reply_example.yaml` (asyncapi 3.0.0)
    - `receiveACostingRequest`: req=#/channels/costingRequestChannel reply=#/channels/costingResponseChannel → **kafka**
- [`evryfs/asyncapi-generator`](https://github.com/evryfs/asyncapi-generator) `asyncapi-generator-core/src/test/resources/parser/operations/asyncapi_parser_operations_valid.yaml` (asyncapi 3.0.0)
    - `receiveLightMeasurement`: req=#/channels/lightingMeasured reply=#/channels/lightingMeasured (same channel) → **undetermined**
- [`gematik/zeta-testfachdienst`](https://github.com/gematik/zeta-testfachdienst) `docs/async-api-docs.yml` (asyncapi 3.0.0)
    - `delete.{id}_receive_delete`: req=#/channels/delete.{id} reply=#/channels/_queue_erezept → **stomp**
    - `list_receive_list`: req=#/channels/list reply=#/channels/_queue_erezept → **stomp**
    - `read.{id}_receive_read`: req=#/channels/read.{id} reply=#/channels/_queue_erezept → **stomp**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/auth_token_validator_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_validate_token`: req=#/channels/receive_request_validate_token reply=#/channels/send_reply_validate_token → **mqtt**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/display_message_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_set_display_message`: req=#/channels/receive_request_set_display_message reply=#/channels/send_reply_set_display_message → **mqtt**
    - `receive_request_get_display_message`: req=#/channels/receive_request_get_display_message reply=#/channels/send_reply_get_display_message → **mqtt**
    - `receive_request_clear_display_message`: req=#/channels/receive_request_clear_display_message reply=#/channels/send_reply_clear_display_message → **mqtt**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/evse_board_support_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_reset`: req=#/channels/receive_request_reset reply=#/channels/send_reply_reset → **mqtt**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/ocpp_consumer_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_data_transfer_incoming`: req=#/channels/receive_request_data_transfer_incoming reply=#/channels/send_reply_data_transfer_incoming → **mqtt**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/powermeter_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_start_transaction`: req=#/channels/receive_request_start_transaction reply=#/channels/send_reply_start_transaction → **mqtt**
    - `receive_request_stop_transaction`: req=#/channels/receive_request_stop_transaction reply=#/channels/send_reply_stop_transaction → **mqtt**
- [`gopal45656/everest-core-release`](https://github.com/gopal45656/everest-core-release) `doc/everest_api_specs/system_API/asyncapi.yaml` (asyncapi 3.0.0)
    - `receive_request_update_firmware`: req=#/channels/receive_request_update_firmware reply=#/channels/send_reply_update_firmware → **mqtt**
    - `receive_request_upload_logs`: req=#/channels/receive_request_upload_logs reply=#/channels/send_reply_upload_logs → **mqtt**
    - `receive_request_is_reset_allowed`: req=#/channels/receive_request_is_reset_allowed reply=#/channels/send_reply_is_reset_allowed → **mqtt**
    - `receive_request_set_system_time`: req=#/channels/receive_request_set_system_time reply=#/channels/send_reply_set_system_time → **mqtt**
    - `receive_request_get_boot_reason`: req=#/channels/receive_request_get_boot_reason reply=#/channels/send_reply_get_boot_reason → **mqtt**
- [`holydocs/messageflow`](https://github.com/holydocs/messageflow) `pkg/schema/source/asyncapi/testdata/analytics.yaml` (asyncapi 3.0.0)
    - `replyAnalyticsReport`: req=#/channels/analytics.report.request reply=#/channels/analytics.report.request (same channel) → **undetermined**
- [`holydocs/messageflow`](https://github.com/holydocs/messageflow) `pkg/schema/source/asyncapi/testdata/analytics_ver2.yaml` (asyncapi 3.0.0)
    - `replyAnalyticsReport`: req=#/channels/analytics.report.request reply=#/channels/analytics.report.request (same channel) → **undetermined**
- [`holydocs/messageflow`](https://github.com/holydocs/messageflow) `pkg/schema/source/asyncapi/testdata/notification.yaml` (asyncapi 3.0.0)
    - `replyPreferences`: req=#/channels/notification.preferences.get reply=#/channels/notification.preferences.get (same channel) → **undetermined**
- [`holydocs/messageflow`](https://github.com/holydocs/messageflow) `pkg/schema/source/asyncapi/testdata/user.yaml` (asyncapi 3.0.0)
    - `replyUserInfo`: req=#/channels/user.info.request reply=#/channels/user.info.request (same channel) → **undetermined**
- [`huynguyengl99/chanx`](https://github.com/huynguyengl99/chanx) `sandbox_django/asyncapi/tests/test_results/asyncapi_schema.yaml` (asyncapi 3.0.0)
    - `handlePing`: req=#/channels/assistants reply=#/channels/assistants (same channel) → **ws**
    - `discussionListHandlePing`: req=#/channels/discussionList reply=#/channels/discussionList (same channel) → **ws**
    - `discussionTopicHandlePing`: req=#/channels/discussionTopic reply=#/channels/discussionTopic (same channel) → **ws**
    - `groupChatHandlePing`: req=#/channels/groupChat reply=#/channels/groupChat (same channel) → **ws**
    - `chatDetailHandlePing`: req=#/channels/chatDetail reply=#/channels/chatDetail (same channel) → **ws**
- [`huynguyengl99/chanx`](https://github.com/huynguyengl99/chanx) `sandbox_fastapi/tests/test_results/asyncapi_schema.yaml` (asyncapi 3.0.0)
    - `handle_chat`: req=#/channels/chat reply=#/channels/chat (same channel) → **ws**
    - `handle_extra_message`: req=#/channels/chat reply=#/channels/chat (same channel) → **ws**
    - `handle_ping`: req=#/channels/chat reply=#/channels/chat (same channel) → **ws**
    - `reliable_chat_handle_ping`: req=#/channels/reliable_chat reply=#/channels/reliable_chat (same channel) → **ws**
    - `handle_reliable_chat`: req=#/channels/reliable_chat reply=#/channels/reliable_chat (same channel) → **ws**
    - `handle_notification`: req=#/channels/notifications reply=#/channels/notifications (same channel) → **ws**
    - `notification_handle_ping`: req=#/channels/notifications reply=#/channels/notifications (same channel) → **ws**
    - `handle_analytics`: req=#/channels/analytics reply=#/channels/analytics (same channel) → **ws**
    - `analytics_handle_ping`: req=#/channels/analytics reply=#/channels/analytics (same channel) → **ws**
    - `system_message_handle_ping`: req=#/channels/system reply=#/channels/system (same channel) → **ws**
    - `handle_system`: req=#/channels/system reply=#/channels/system (same channel) → **ws**
    - `handle_job`: req=#/channels/background_jobs reply=#/channels/background_jobs (same channel) → **ws**
    - `background_job_handle_ping`: req=#/channels/background_jobs reply=#/channels/background_jobs (same channel) → **ws**
    - `room_chat_handle_ping`: req=#/channels/room_chat reply=#/channels/room_chat (same channel) → **ws**
    - `handle_room_chat`: req=#/channels/room_chat reply=#/channels/room_chat (same channel) → **ws**
- [`huynguyengl99/chanx-fastapi-tutorial`](https://github.com/huynguyengl99/chanx-fastapi-tutorial) `src/tests/test_results/asyncapi_schema.yaml` (asyncapi 3.0.0)
    - `handle_ping`: req=#/channels/system reply=#/channels/system (same channel) → **ws**
    - `handle_system`: req=#/channels/system reply=#/channels/system (same channel) → **ws**
    - `room_chat_handle_ping`: req=#/channels/room_chat reply=#/channels/room_chat (same channel) → **ws**
    - `handle_room_chat`: req=#/channels/room_chat reply=#/channels/room_chat (same channel) → **ws**
    - `handle_job`: req=#/channels/background_jobs reply=#/channels/background_jobs (same channel) → **ws**
    - `background_job_handle_ping`: req=#/channels/background_jobs reply=#/channels/background_jobs (same channel) → **ws**
    - `handle_chat`: req=#/channels/chat reply=#/channels/chat (same channel) → **ws**
    - `chat_handle_ping`: req=#/channels/chat reply=#/channels/chat (same channel) → **ws**
    - `reliable_chat_handle_ping`: req=#/channels/reliable_chat reply=#/channels/reliable_chat (same channel) → **ws**
    - `handle_reliable_chat`: req=#/channels/reliable_chat reply=#/channels/reliable_chat (same channel) → **ws**
    - `handle_notification`: req=#/channels/notifications reply=#/channels/notifications (same channel) → **ws**
    - `notification_handle_ping`: req=#/channels/notifications reply=#/channels/notifications (same channel) → **ws**
    - `handle_analytics`: req=#/channels/analytics reply=#/channels/analytics (same channel) → **ws**
    - `analytics_handle_ping`: req=#/channels/analytics reply=#/channels/analytics (same channel) → **ws**
- [`insspb/asyncapi3`](https://github.com/insspb/asyncapi3) `tests/fixtures/yaml_specs/valid/single_file/kraken-websocket-request-reply-message-filter-in-reply-asyncapi.yml` (asyncapi 3.0.0)
    - `receivePing`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveSubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveUnsubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
- [`insspb/asyncapi3`](https://github.com/insspb/asyncapi3) `tests/fixtures/yaml_specs/valid/single_file/kraken-websocket-request-reply-multiple-channels-asyncapi.yml` (asyncapi 3.0.0)
    - `receivePing`: req=#/channels/ping reply=#/channels/pong → **undetermined**
    - `subscribe`: req=#/channels/subscribe reply=#/channels/currencyInfo → **undetermined**
    - `unsubscribe`: req=#/channels/unsubscribe reply=#/channels/currencyInfo → **undetermined**
- [`l3wi/docs`](https://github.com/l3wi/docs) `websockets/asyncapi.yaml` (asyncapi 3.0.0)
    - `authenticate`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribeTrade`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribeBook`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribeCandle`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribePosition`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribeOrder`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `createOrder`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `cancelOrder`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribeTrade`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribeBook`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribeCandle`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribePosition`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribeOrder`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `subscribeBalance`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
    - `unsubscribeBalance`: req=#/channels/websocket reply=#/channels/websocket (same channel) → **undetermined**
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `examples/ping/v3/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `pingRequest`: req=#/channels/ping reply=#/channels/pong → **undetermined**
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `test/v3/issues/130/requestreply/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `ping`: req=#/channels/ping reply=#/channels/pong → **undetermined**
    - `pingWithID`: req=#/channels/pingWithID reply=#/channels/pongWithID → **undetermined**
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `test/v3/issues/145/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `pingRequest`: req=#/channels/ping reply=#/channels/pong → **undetermined**
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `test/v3/issues/148/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `GetServiceInfo`: req=#/channels/reception reply=#/channels/reply → **undetermined**
- [`lerenn/asyncapi-codegen`](https://github.com/lerenn/asyncapi-codegen) `test/v3/issues/181/asyncapi.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `GetServiceInfo`: req=#/channels/request reply=#/channels/reply → **undetermined**
- [`metalalive/e_commerce`](https://github.com/metalalive/e_commerce) `services/order/doc/api/asyncapi.yaml` (asyncapi 3.0.0)
    - `stock-level-edit`: req=#/channels/stock_level_edit reply={'description': 'The response destination is dynamically set according to the `replyTo` field in the request header', 'location': '$message.header#/replyTo'} → **amqp**
    - `stock-level-return`: req=#/channels/stock_return_cancelled reply={'location': '$message.header#/replyTo'} → **amqp**
    - `order-rsv-replica-inventory`: req=#/channels/order_reserved_replica_inventory reply={'location': '$message.header#/replyTo'} → **amqp**
    - `order-rsv-replica-payment`: req=#/channels/order_reserved_replica_payment reply={'location': '$message.header#/replyTo'} → **amqp**
    - `order-returned-replica-refund`: req=#/channels/order_returned_replica_refund reply={'location': '$message.header#/replyTo'} → **amqp**
    - `order-rsv-update-payment`: req=#/channels/order_reserved_update_payment reply={'location': '$message.header#/replyTo'} → **amqp**
- [`microcks/microcks`](https://github.com/microcks/microcks) `webapp/src/test/resources/io/github/microcks/util/asyncapi/user-signedup-asyncapi-3.0-reply.yaml` (asyncapi 3.0.0)
    - `onUserSignup`: req=#/channels/userSignup reply=#/channels/userSignupReply → **googlepubsub**
    - `onEmailVerification`: req=#/channels/emailVerification reply=#/channels/emailVerificationReply → **googlepubsub**
- [`sillygod/scaffold`](https://github.com/sillygod/scaffold) `go-web/{{ cookiecutter.project_slug }}/asyncapi.yaml` (asyncapi 3.0.0)
    - `pricefeedRequest`: req=#/channels/pricefeed_request reply=#/channels/pricefeed → **wss**
    - `pingRequest`: req=#/channels/ping reply=#/channels/pong → **wss**
- [`simliai/docs`](https://github.com/simliai/docs) `api-reference/asyncapi.yaml` (asyncapi 3.0.0)
    - `sendOffer`: req=#/channels/peer_to_peer reply=#/channels/peer_to_peer (same channel) → **wss**
- [`specmatic/aws-lambda-kafka-with-localstack`](https://github.com/specmatic/aws-lambda-kafka-with-localstack) `api-specifications/order-service-async-v3_0_0.yaml` (asyncapi 3.0.0)
    - `cancelOrder`: req=#/channels/cancel-order reply=#/channels/process-cancellation → **undetermined**
- [`specmatic/aws-lambda-kafka-with-localstack`](https://github.com/specmatic/aws-lambda-kafka-with-localstack) `xml_to_json.yaml` (asyncapi 3.0.0)
    - `jsonConversion`: req=#/channels/io.specmatic.json.request reply=#/channels/io.specmatic.json.reply → **undetermined**
- [`specmatic/docs.specmatic.io`](https://github.com/specmatic/docs.specmatic.io) `docs/supported_protocols/asyncapi/includes/index/order-service-mock/spec/order-service.yaml` (asyncapi 3.0.0)
    - `sendOrder`: req=#/channels/placeOrder reply=#/channels/wipOrder → **kafka, sqs**
- [`specmatic/docs.specmatic.io`](https://github.com/specmatic/docs.specmatic.io) `docs/supported_protocols/asyncapi/includes/index/order-service-sut/spec/order-service.yaml` (asyncapi 3.0.0)
    - `sendOrder`: req=#/channels/placeOrder reply=#/channels/wipOrder → **kafka, sqs**
- [`specmatic/enterprise-sample`](https://github.com/specmatic/enterprise-sample) `specs/inventory-asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveReserveCommand`: req=#/channels/inventory.reserve.cmd reply=#/channels/inventory.reserve.reply → **kafka**
- [`specmatic/enterprise-sample`](https://github.com/specmatic/enterprise-sample) `specs/payment-asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveAuthorizeCommand`: req=#/channels/payment.authorize.cmd reply=#/channels/payment.authorize.reply → **kafka**
- [`specmatic/enterprise-sample`](https://github.com/specmatic/enterprise-sample) `specs/placeorder-asyncapi.yaml` (asyncapi 3.0.0)
    - `receivePlaceOrderCommand`: req=#/channels/orders.place.cmd reply=#/channels/orders.place.reply → **kafka**
- [`specmatic/labs`](https://github.com/specmatic/labs) `arazzo-workflow-testing/specs/asyncapi/order.yaml` (asyncapi 3.0.0)
    - `createOrder`: req=#/channels/newOrders reply=#/channels/wipOrders → **kafka**
- [`specmatic/labs-contracts`](https://github.com/specmatic/labs-contracts) `asyncapi/kafka-avro/order-service-async-avro-v3_0_0.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/new-orders reply=#/channels/wip-orders → **undetermined**
- [`specmatic/labs-contracts`](https://github.com/specmatic/labs-contracts) `asyncapi/kafka-sqs-retry-dlq/order-service-sqs-kafka.yaml` (asyncapi 3.0.0)
    - `sendOrder`: req=#/channels/placeOrder reply=#/channels/wipOrder → **kafka, sqs**
- [`specmatic/labs-contracts`](https://github.com/specmatic/labs-contracts) `asyncapi/quick-start/async.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **kafka**
- [`specmatic/specmatic`](https://github.com/specmatic/specmatic) `application/src/test/resources/specifications/asyncapi.yaml` (asyncapi 3.0.0)
    - `pingRequest`: req=#/channels/ping_v2 reply=#/channels/pong → **undetermined**
- [`specmatic/specmatic-arazzo-openapi-asyncapi-sample`](https://github.com/specmatic/specmatic-arazzo-openapi-asyncapi-sample) `specifications/asyncapi/order.yaml` (asyncapi 3.0.0)
    - `createOrder`: req=#/channels/newOrders reply=#/channels/wipOrders → **kafka**
- [`specmatic/specmatic-async-sample`](https://github.com/specmatic/specmatic-async-sample) `spec/spec.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **kafka, sqs**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancelled → **kafka, sqs**
- [`specmatic/specmatic-kafka-avro-sample`](https://github.com/specmatic/specmatic-kafka-avro-sample) `api-specs/order-service-async-avro-v3_0_0.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/new-orders reply=#/channels/wip-orders → **undetermined**
- [`specmatic/specmatic-kafka-sample-asyncapi3`](https://github.com/specmatic/specmatic-kafka-sample-asyncapi3) `specs/async-order-service.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **undetermined**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancelled → **undetermined**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_multi_protocol.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **mqtt, sqs**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancelled → **mqtt, sqs**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_v1.yaml` (asyncapi 3.0.0)
    - `onPlaceOrder`: req=#/channels/place-order reply=#/channels/process-order → **undetermined**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_v2.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/NewOrderProcessed → **googlepubsub, kafka**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancellationProcessed → **googlepubsub, kafka**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_v3.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **undetermined**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancelled → **undetermined**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/order_service_async_v4.yaml` (asyncapi 3.0.0)
    - `placeOrder`: req=#/channels/NewOrderPlaced reply=#/channels/OrderInitiated → **undetermined**
    - `cancelOrder`: req=#/channels/OrderCancellationRequested reply=#/channels/OrderCancelled → **undetermined**
- [`specmatic/specmatic-order-contracts`](https://github.com/specmatic/specmatic-order-contracts) `io/specmatic/examples/store/asyncapi/3_0_0/sqs_kafka/order-service-sqs-kafka.yaml` (asyncapi 3.0.0)
    - `sendOrder`: req=#/channels/placeOrder reply=#/channels/wipOrder → **kafka, sqs**
- [`specmatic/studio-demo`](https://github.com/specmatic/studio-demo) `specs/workflow/asyncapi/order.yaml` (asyncapi 3.0.0, +1 more repo(s))
    - `PlaceOrder`: req=#/channels/place-order reply=#/channels/process-order → **kafka**
- [`stardew-valley-dedicated-server/asyncapi-generator-template-ts`](https://github.com/stardew-valley-dedicated-server/asyncapi-generator-template-ts) `test/fixtures/asyncapi.yaml` (asyncapi 3.0.0)
    - `updateMapData`: req=#/channels/root reply=#/channels/root (same channel) → **undetermined**
- [`stardew-valley-dedicated-server/web`](https://github.com/stardew-valley-dedicated-server/web) `asyncapi.yaml` (asyncapi 3.0.0)
    - `updateMap`: req=#/channels/root reply=#/channels/root (same channel) → **undetermined**
- [`the-codegen-project/cli`](https://github.com/the-codegen-project/cli) `test/blackbox/schemas/asyncapi/kraken-websocket-request-reply-message-filter-in-reply-asyncapi.yml` (asyncapi 3.0.0)
    - `receivePing`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveSubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
    - `receiveUnsubscribeRequest`: req=#/channels/currencyExchange reply=#/channels/currencyExchange (same channel) → **undetermined**
- [`the-codegen-project/cli`](https://github.com/the-codegen-project/cli) `test/configs/asyncapi-request.yaml` (asyncapi 3.0.0)
    - `pongResponse`: req=#/channels/ping reply=#/channels/ping (same channel) → **http**
- [`wohnheim/stueble`](https://github.com/wohnheim/stueble) `packages/frontend/static/api-spec/asyncapi.yaml` (asyncapi 3.0.0)
    - `receiveGuestListChanges`: req=#/channels/primary reply=? → **ws**
    - `receiveHostsChanges`: req=#/channels/primary reply=? → **ws**
    - `receiveTutorsChanges`: req=#/channels/primary reply=? → **ws**
- [`znsio/specmatic-async-order-api-kotlin`](https://github.com/znsio/specmatic-async-order-api-kotlin) `spec/order_service_async_v1.yaml` (asyncapi 3.0.0)
    - `createOrder`: req=#/channels/create-order-request reply=#/channels/create-order-reply → **undetermined**
- [`zuevrs/yanote`](https://github.com/zuevrs/yanote) `yanote-js/test/fixtures/asyncapi/spring-kafka-single-service-republish.yaml` (asyncapi 3.0.0)
    - `receiveUserCreated`: req=#/channels/userCreated reply=#/channels/userCreated (same channel) → **kafka**
    - `receiveUserRepublished`: req=#/channels/userRepublished reply=#/channels/userRepublished (same channel) → **kafka**
- [`zuevrs/yanote`](https://github.com/zuevrs/yanote) `yanote-js/test/fixtures/asyncapi/spring-kafka-two-service.yaml` (asyncapi 3.0.0)
    - `receiveUserCreated`: req=#/channels/userCreated reply=#/channels/userCreated (same channel) → **kafka**
- [`zuevrs/yanote`](https://github.com/zuevrs/yanote) `yanote-js/test/fixtures/asyncapi/spring-rabbitmq-two-service.yaml` (asyncapi 3.0.0)
    - `amqp receive users.created`: req=#/channels/userCreated reply=#/channels/userCreated (same channel) → **amqp**
