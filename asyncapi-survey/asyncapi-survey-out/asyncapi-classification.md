# AsyncAPI 3.x repository classification

Seedless, signal-scored classification of every unique repository surfaced by `asyncapi_adoption_survey.sh` for AsyncAPI 3.x. Each repo is assigned the highest-scoring bucket from GitHub topics, description, name, how it uses AsyncAPI (spec file locations), language, and homepage. See the module docstring for weights; `_scores`/`_reason` in `repo-classification.json` record the evidence per repo.

_1 of 984 repos are archived (recorded as `isArchived`, not a bucket)._

## Bucket counts

| Bucket | Count | % of total |
|---|---:|---:|
| `product` | 252 | 25.6 % |
| `tooling/library` | 211 | 21.4 % |
| `demo/fixture` | 172 | 17.5 % |
| `spec/docs` | 57 | 5.8 % |
| `catalog` | 48 | 4.9 % |
| `tangential` | 15 | 1.5 % |
| `uncategorized` | 229 | 23.3 % |
| **total** | **984** | 100 % |

## product (252)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 8127 | [pixel-agents-hq/pixel-agents](https://github.com/pixel-agents-hq/pixel-agents) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Pixel office. |
| 2724 | [event-catalog/eventcatalog](https://github.com/event-catalog/eventcatalog) | — | topic=event-driven-architecture,microservices (+3 product... | The discovery and governance layer for event-driven systems. Docume... |
| 2147 | [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | — | text~product (+2 product) | The semantic deployment platform. |
| 1956 | [microcks/microcks](https://github.com/microcks/microcks) | reply · kafka · channel-params | topic=event-driven,kubernetes,mock-server,mocking (+3 pro... | The open source, cloud native tool for API Mocking and Testing. Mic... |
| 1320 | [owasp-noir/noir](https://github.com/owasp-noir/noir) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... | Hunt every Endpoint in your code, expose Shadow APIs, map the Attac... |
| 986 | [wso2/product-apim](https://github.com/wso2/product-apim) | mqtt | topic=api-gateway,api-management,gateway,microservices (+... | Welcome to the WSO2 API Manager source code! For info on working wi... |
| 810 | [Apicurio/apicurio-registry](https://github.com/Apicurio/apicurio-registry) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | An API/Schema registry - stores APIs and Schemas. |
| 738 | [DarkflameUniverse/DarkflameServer](https://github.com/DarkflameUniverse/DarkflameServer) | — | topic=server,server-emulator (+3 product); text~product (... | The main repository for the Darkflame Universe Server Emulator proj... |
| 690 | [aklivity/zilla](https://github.com/aklivity/zilla) | reply · kafka · mqtt · channel-params | topic=api-gateway,event-driven-architecture,iot,server-se... | 🦎 A multi-protocol edge & service proxy. Seamlessly interface web a... |
| 631 | [Sunagatov/Iced-Latte](https://github.com/Sunagatov/Iced-Latte) | — | topic=kubernetes (+3 product); text~tool (+2 tooling/libr... | a online Marketplace for coffee retail (Backend) |
| 609 | [geopython/pygeoapi](https://github.com/geopython/pygeoapi) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | pygeoapi is a Python server implementation of the OGC API suite of ... |
| 554 | [chainloop-dev/chainloop](https://github.com/chainloop-dev/chainloop) | mqtt | topic=metadata-platform (+3 product); text~product(weak) ... | SDLC evidence store and policy engine for your Software Supply Chai... |
| 502 | [foxminchan/BookWorm](https://github.com/foxminchan/BookWorm) | — | topic=microservice (+3 product); text~product (+2 product... | The practical implementation of Aspire using Microservices, AI-Agents |
| 418 | [gravitee-io/gravitee-api-management](https://github.com/gravitee-io/gravitee-api-management) | — | topic=api-gateway,api-management,gateway (+3 product); te... | Gravitee.io - OpenSource API Management |
| 381 | [specmatic/specmatic](https://github.com/specmatic/specmatic) | reply | topic=microservices (+3 product); text~product(weak) (+1 ... | Eliminate API integration headaches with Specmatic's no-code AI-pow... |
| 218 | [NUWCDIVNPT/stig-manager](https://github.com/NUWCDIVNPT/stig-manager) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | An API and client for managing STIG assessments |
| 150 | [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) | channel-params | text~product (+2 product); text~spec (+2 spec/docs); spec... | An MCP server that provides access to Postman. |
| 82 | [wirenboard/wb-rules](https://github.com/wirenboard/wb-rules) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Rule engine for Wiren Board |
| 73 | [VoiceBlender/voiceblender](https://github.com/VoiceBlender/voiceblender) | reply | text~product (+2 product); spec-at-root/docs (+1 product) | A programmable voice platform: SIP and WebRTC call control, multi-p... |
| 51 | [eclipse-symphony/symphony](https://github.com/eclipse-symphony/symphony) | reply | text~product (+2 product); spec-at-root/docs (+1 product) | Symphony project |
| 32 | [aml-org/als](https://github.com/aml-org/als) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Language Server implementation for AML and AML-defined metadata |
| 27 | [barbacane-dev/barbacane](https://github.com/barbacane-dev/barbacane) | channel-params | topic=ai-gateway,ai-gateways,gateway,mcp-server (+3 produ... | Barbacane API and Bidirectional AI Gateway |
| 27 | [seanchatmangpt/dslmodel](https://github.com/seanchatmangpt/dslmodel) | mqtt | text~product (+2 product); spec-at-root/docs (+1 product) | Structured outputs from DSPy and Jinja2 |
| 25 | [PeterAlaks/lyric-display-app](https://github.com/PeterAlaks/lyric-display-app) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | LyricDisplay is a free, open-source lyric projection application fo... |
| 23 | [kanekoshoyu/exchange-collection](https://github.com/kanekoshoyu/exchange-collection) | — | topic=cross-platform (+3 product); text~tool (+2 tooling/... | Collection of Crypto Exchange OpenAPI and Generated Clients |
| 18 | [btravers/amqp-contract](https://github.com/btravers/amqp-contract) | — | topic=schema,standard-schema (+3 spec/docs); topic=messag... | Type-safe contracts for AMQP/RabbitMQ messaging with TypeScript |
| 17 | [aixigo/PREvant](https://github.com/aixigo/PREvant) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Composing Microservices into Reviewable and Testable Applications |
| 17 | [Kiloforge/kiloforge](https://github.com/Kiloforge/kiloforge) | — | text~product (+2 product) | 1,000x Productivity. Command AI agent swarms and ship code at the s... |
| 14 | [event-catalog/generators](https://github.com/event-catalog/generators) | — | topic=event-driven-architecture (+3 product); text~tool (... | Plugin integrations for EventCatalog |
| 12 | [ProsusAI/agentic-services-protocol](https://github.com/ProsusAI/agentic-services-protocol) | channel-params | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Agentic Services Protocol (ASP) - an open protocol for the complete... |
| 11 | [aklivity/zillabase](https://github.com/aklivity/zillabase) | kafka · mqtt · channel-params | text~product (+2 product) | An event-driven backend for the next generation of web, mobile and ... |
| 11 | [OpenSourceAGI/ai-broker-investing-agent](https://github.com/OpenSourceAGI/ai-broker-investing-agent) | — | text~product (+2 product) | 💱 Invest with news debate agents, 🤑 algorithmic entry/exit strategi... |
| 10 | [droso-hass/openab](https://github.com/droso-hass/openab) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... | Opensource Nabaztag Server |
| 10 | [meridianhub/meridian](https://github.com/meridianhub/meridian) | kafka | text~product (+2 product); spec-at-root/docs (+1 product) | Meridian is a Transaction Integrity Engine |
| 10 | [revue-org/revue](https://github.com/revue-org/revue) | — | topic=microservices-architecture,web-applications (+3 pro... | A distributed real-time system for video surveillance |
| 9 | [med-united/popp-smartphone-konnektor](https://github.com/med-united/popp-smartphone-konnektor) | — | text~product (+2 product) |  |
| 8 | [ekhodzitsky/gigastt](https://github.com/ekhodzitsky/gigastt) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Local STT server powered by GigaAM v3. |
| 7 | [hmajid2301/banterbus](https://github.com/hmajid2301/banterbus) | reply | topic=web-application (+3 product); text~product (+2 prod... | A multiplayer browser-based game built using htmx and Golang. Lever... |
| 6 | [Generacja-Cuzi/ai-present-finder](https://github.com/Generacja-Cuzi/ai-present-finder) | — | text~product (+2 product) |  |
| 6 | [rabbytesoftware/quiver.core](https://github.com/rabbytesoftware/quiver.core) | channel-params | topic=servers (+3 product); text~product (+2 product); sp... | Quiver is a multi-platform package manager - probably the only one ... |
| 5 | [cycleplatform/api-spec](https://github.com/cycleplatform/api-spec) | — | text~product (+2 product); name~spec (+1 spec/docs) | OpenAPI spec files for Cycle APIs |
| 4 | [kingak4/ft_transcendence](https://github.com/kingak4/ft_transcendence) | — | topic=webapp (+3 product); text~product (+2 product) | ft_transcendence is a team-based web application built as part of t... |
| 4 | [KTCrisis/event7](https://github.com/KTCrisis/event7) | kafka · amqp | topic=event-driven,schema-registry (+3 product); text~pro... | Schema registry governance for event-driven architectures — data co... |
| 4 | [Kuestenlogik/Bowire](https://github.com/Kuestenlogik/Bowire) | mqtt | topic=api-client,http-client (+3 tooling/library); topic=... | Multi-protocol API workbench for .NET — discover, invoke, record, m... |
| 4 | [motor-screwdriver/mts-true-tech-hack-26](https://github.com/motor-screwdriver/mts-true-tech-hack-26) | — | text~tool (+2 tooling/library); text~product (+2 product)... | WikiLive is a real-time document collaboration platform. The projec... |
| 4 | [openfoodfacts/openfoodfacts-query](https://github.com/openfoodfacts/openfoodfacts-query) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | This extracts key product data from MongoDB into a Postgres databas... |
| 3 | [45ck/Portarium](https://github.com/45ck/Portarium) | channel-params | topic=integration-platform,workflow-orchestration (+3 pro... | Open-source multi-tenant control plane for governable operations: p... |
| 3 | [doemefu/very-cool-karaoke-server](https://github.com/doemefu/very-cool-karaoke-server) | channel-params | text~product (+2 product) | Backend for our very cool karaoke app. |
| 3 | [MindGainsLabs/Stratus_Relayer](https://github.com/MindGainsLabs/Stratus_Relayer) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 3 | [ministryofjustice/offender-case-notes](https://github.com/ministryofjustice/offender-case-notes) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Offender Case Notes Service |
| 3 | [Netcracker/qubership-integration-platform](https://github.com/Netcracker/qubership-integration-platform) | reply · amqp | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 3 | [openfoodfacts/openfoodfacts-auth](https://github.com/openfoodfacts/openfoodfacts-auth) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Building an SSO platform for @openfoodfacts with @keycloak |
| 2 | [ahelme/mcp-claude-code-browser-tools](https://github.com/ahelme/mcp-claude-code-browser-tools) | — | text~product (+2 product) | An browser-tools mcp server for claude code |
| 2 | [AltairaLabs/Omnia](https://github.com/AltairaLabs/Omnia) | — | topic=kubernetes,kubernetes-operator (+3 product); topic=... | Kubernetes operator for deploying and managing AI agents with WebSo... |
| 2 | [ccradle/finding-a-bed-tonight](https://github.com/ccradle/finding-a-bed-tonight) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Open-source emergency shelter bed availability platform — Spring Bo... |
| 2 | [CDFmmgr9fLkRH453kRC33TrEp/matching-engine](https://github.com/CDFmmgr9fLkRH453kRC33TrEp/matching-engine) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 2 | [cjjohansen/drone-web](https://github.com/cjjohansen/drone-web) | — | text~product (+2 product) | drone ecommerce website using ADDR Design process |
| 2 | [devmentors/Mikroserwisy-Revisited](https://github.com/devmentors/Mikroserwisy-Revisited) | channel-params | topic=microservices (+3 product) | [PL] Mikroserwisy 6 lat później czyli... jak nie utonąć 😉 |
| 2 | [Integration-Project-2026-Groep-2/CRM](https://github.com/Integration-Project-2026-Groep-2/CRM) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 2 | [ivanztz/sandbox](https://github.com/ivanztz/sandbox) | kafka | text~product (+2 product); text~spec (+2 spec/docs) | Sandbox project |
| 2 | [ministryofjustice/hmpps-incentives-api](https://github.com/ministryofjustice/hmpps-incentives-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | HMPPS Incentives API |
| 2 | [ministryofjustice/hmpps-prison-visit-booker-registry](https://github.com/ministryofjustice/hmpps-prison-visit-booker-registry) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A microservice that will allow an authenticated public user to regi... |
| 2 | [ministryofjustice/hmpps-visit-allocation-api](https://github.com/ministryofjustice/hmpps-visit-allocation-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | A service to calculate visit allocations |
| 2 | [Netcracker/qubership-integration-runtime-catalog](https://github.com/Netcracker/qubership-integration-runtime-catalog) | reply · amqp | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 2 | [pfplay/pfplay-platform](https://github.com/pfplay/pfplay-platform) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 2 | [piedraprog/unified-personal-skills](https://github.com/piedraprog/unified-personal-skills) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | skills que voy acumulando que me funcionen para el desarrollo |
| 2 | [radiorabe/pathfinder-cloudevents-service](https://github.com/radiorabe/pathfinder-cloudevents-service) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Receives events from Pathfinder's RestApi and turn them into RaBe C... |
| 2 | [rainbow-mobile/web_robot_server](https://github.com/rainbow-mobile/web_robot_server) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 2 | [tachu2/transcendence](https://github.com/tachu2/transcendence) | — | text~product (+2 product); spec-at-root/docs (+1 product) | realtime pingpong game. |
| 1 | [adhitiad/quantsync](https://github.com/adhitiad/quantsync) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [Anomaliszt/Conquest](https://github.com/Anomaliszt/Conquest) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 1 | [asimarora/semantic-intelligence-layer](https://github.com/asimarora/semantic-intelligence-layer) | — | text~product (+2 product) | A source-agnostic semantic intelligence layer that transforms event... |
| 1 | [asklokesh/NEXT-Portal](https://github.com/asklokesh/NEXT-Portal) | mqtt · channel-params | text~product (+2 product) | Next Portal - The NEXT Gen IDP for Developers |
| 1 | [ayointegral/cloud-sandbox-backstage](https://github.com/ayointegral/cloud-sandbox-backstage) | amqp · channel-params | text~product (+2 product) | Cloud Sandbox - Backstage Developer Portal with custom catalog and ... |
| 1 | [brainsnorkel/hourstats-bsky](https://github.com/brainsnorkel/hourstats-bsky) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Bluesky HourStats - A Go-based AT Protocol/Bluesky client that anal... |
| 1 | [cajias/syncnode](https://github.com/cajias/syncnode) | channel-params | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 1 | [CardinalWave/cw-mqtt-gateway](https://github.com/CardinalWave/cw-mqtt-gateway) | mqtt | text~product (+2 product); spec-at-root/docs (+1 product) | Servico responsavel por receber as mensagens do broker e redirecion... |
| 1 | [CodingFlow/rating-service-dotnet](https://github.com/CodingFlow/rating-service-dotnet) | reply · channel-params | topic=microservices (+3 product); text~product (+2 product) | Prototype full-stack C#, Preact web app deployed on Azure AKS using... |
| 1 | [cryptoxdog/Cognitive.Engine.Graphs](https://github.com/cryptoxdog/Cognitive.Engine.Graphs) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... |  |
| 1 | [darken33/connaissance-client](https://github.com/darken33/connaissance-client) | kafka | text~product (+2 product) |  |
| 1 | [DEFRA/fcp-audit](https://github.com/DEFRA/fcp-audit) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Git repository for service fcp-audit |
| 1 | [Embiggenerd/spiritio](https://github.com/Embiggenerd/spiritio) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Zoom clone with authentication |
| 1 | [ermasavior/nebeng-jek](https://github.com/ermasavior/nebeng-jek) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Simple on-demand ride sharing service |
| 1 | [Floffah/echoform](https://github.com/Floffah/echoform) | — | text~product (+2 product) | Spiritual social exploration mmorpg game |
| 1 | [igmrrf/ecommerce_services](https://github.com/igmrrf/ecommerce_services) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 1 | [Jack-the-Pro101/vequate](https://github.com/Jack-the-Pro101/vequate) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Cloud based Minecraft server orchestration system |
| 1 | [jlfowle/asterism](https://github.com/jlfowle/asterism) | — | text~product (+2 product) |  |
| 1 | [joemphilips/bitCaster](https://github.com/joemphilips/bitCaster) | — | text~product (+2 product) |  |
| 1 | [mattys1/raptorChat](https://github.com/mattys1/raptorChat) | channel-params | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [metalalive/e_commerce](https://github.com/metalalive/e_commerce) | reply · amqp | topic=backend-services (+3 product); text~product (+2 pro... | E-commerce backend platform implemented in Python / C / Rust |
| 1 | [ministryofjustice/hmpps-challenge-support-intervention-plan-api](https://github.com/ministryofjustice/hmpps-challenge-support-intervention-plan-api) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Backend API to allow the creation and management of Challenge Suppo... |
| 1 | [ministryofjustice/hmpps-health-and-medication-api](https://github.com/ministryofjustice/hmpps-health-and-medication-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | An API providing access to HMPPS health and medication data. (boots... |
| 1 | [ministryofjustice/hmpps-incident-reporting-api](https://github.com/ministryofjustice/hmpps-incident-reporting-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | HMPPS Incident Reporting Service API |
| 1 | [ministryofjustice/hmpps-non-associations-api](https://github.com/ministryofjustice/hmpps-non-associations-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | HMPPS Non-associations API |
| 1 | [NalinDalal/modheshwari](https://github.com/NalinDalal/modheshwari) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | turbo repo to maintain website for local community |
| 1 | [openwop/openwop](https://github.com/openwop/openwop) | — | text~tool (+2 tooling/library); text~product (+2 product)... | openwop — Open Workflow Orchestration Protocol |
| 1 | [Poss111/ClashBot-Service](https://github.com/Poss111/ClashBot-Service) | — | text~product (+2 product) | A Spring Boot implementation of the Clash Bot's backend service. |
| 1 | [prajwalaher33/feeshr](https://github.com/prajwalaher33/feeshr) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Feeshr — Operating Engine for AI Agents |
| 1 | [rlarin/it-crowd-pixel-agents](https://github.com/rlarin/it-crowd-pixel-agents) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Pixel art office where your Claude Code agents come to life — with ... |
| 1 | [solace-cto-labs/platform-api](https://github.com/solace-cto-labs/platform-api) | — | text~product (+2 product) | Solace API Management Connector - AsyncAPI Management Integration. |
| 1 | [Sriramanenivikas/Intelligent-Warehouse-Orchestration-System](https://github.com/Sriramanenivikas/Intelligent-Warehouse-Orchestration-System) | — | topic=event-driven,kong-gateway,kubernetes,microservice (... | IWOS  is a unified fulfillment platform that combines quick commerc... |
| 1 | [tornado80/collaborative-whiteboard](https://github.com/tornado80/collaborative-whiteboard) | reply · channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... | Collaborative Whiteboard written in Erlang and React over Websocket... |
| 1 | [underpass-ai/underpass-runtime](https://github.com/underpass-ai/underpass-runtime) | — | topic=kubernetes (+3 product); spec-at-root/docs (+1 prod... | Governed execution plane for tool-driven AI agents — 99 tools, isol... |
| 1 | [UNIZAR-30226-2026-07/BombaVa-Backend](https://github.com/UNIZAR-30226-2026-07/BombaVa-Backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Backend del juego de Bomba Va |
| 1 | [VisioLab/cash-register-api](https://github.com/VisioLab/cash-register-api) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Specification of VisioLab's cash register API |
| 1 | [wirenboard/wb-mqtt-confed](https://github.com/wirenboard/wb-mqtt-confed) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Configuration editor backend service for Wiren Board |
| 1 | [wohnheim/stueble](https://github.com/wohnheim/stueble) | reply | text~product (+2 product) | Webseite für die Anmeldung zum Stüble |
| 1 | [Youka/api-snap](https://github.com/Youka/api-snap) | — | topic=kubernetes (+3 product); topic=documentation (+3 sp... | An application which collects API documents by kubernetes service d... |
| 0 | [21MokseM12/DevPulse](https://github.com/21MokseM12/DevPulse) | — | text~product (+2 product) |  |
| 0 | [5G-PreCiSe/edge-to-cloud-file-uploader](https://github.com/5G-PreCiSe/edge-to-cloud-file-uploader) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A Python tool for uploading files from a local directory to an S3 s... |
| 0 | [acharyaPawan/ecommerce-platform](https://github.com/acharyaPawan/ecommerce-platform) | — | text~product (+2 product) |  |
| 0 | [adreno255/nurtura-backend](https://github.com/adreno255/nurtura-backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) | The GitHub remote repository for the Nurtura API backend server. |
| 0 | [aequitas-aod/aequitas-backend](https://github.com/aequitas-aod/aequitas-backend) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | [WIP] AEQUITAS Backend Service: providing API for a Q/A-based syste... |
| 0 | [aescanero/dago](https://github.com/aescanero/dago) | — | text~product (+2 product) | DA Orchestrator core repository |
| 0 | [ahadify/VDL-gg](https://github.com/ahadify/VDL-gg) | channel-params | text~product (+2 product) | VDL Fantasy VALORANT Platform - real-time draft rooms, scoring engi... |
| 0 | [ai-digital-architect/asyncapi_discovery](https://github.com/ai-digital-architect/asyncapi_discovery) | kafka | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Scan repositories for event producers regardless of the broker and ... |
| 0 | [Aidin1998/finalex](https://github.com/Aidin1998/finalex) | channel-params | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [ak125/nestjs-remix-monorepo](https://github.com/ak125/nestjs-remix-monorepo) | — | text~product (+2 product) |  |
| 0 | [almashooq1/alawael-erp](https://github.com/almashooq1/alawael-erp) | — | text~product (+2 product); spec-at-root/docs (+1 product) | مشروع مراكز الاوائل |
| 0 | [aniccname/Q-Game](https://github.com/aniccname/Q-Game) | — | text~product (+2 product) | A Qwirkle inspired game using a Client-Server architecture. A brows... |
| 0 | [apakhbari/backstage](https://github.com/apakhbari/backstage) | mqtt · channel-params | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Backstage 🦾 |
| 0 | [Binit-Dhakal/Saarathi](https://github.com/Binit-Dhakal/Saarathi) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Ride-sharing App built with Golang and NextJS in event-driven archi... |
| 0 | [bishoy-alhanna/frightflow](https://github.com/bishoy-alhanna/frightflow) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Brico87/seed-kafka](https://github.com/Brico87/seed-kafka) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [briossant/BotAmoungUs](https://github.com/briossant/BotAmoungUs) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [CALLlA-74/bauman-poker](https://github.com/CALLlA-74/bauman-poker) | channel-params | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [calvinlee999/AI-Platform-for-FinTech-Evolution](https://github.com/calvinlee999/AI-Platform-for-FinTech-Evolution) | — | text~product (+2 product) |  |
| 0 | [capitanx9/llm-portrait](https://github.com/capitanx9/llm-portrait) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ChargeAndTrack/backend-spe](https://github.com/ChargeAndTrack/backend-spe) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Backend for the SPE project. |
| 0 | [Cirripide/local-rag-for-documents-be](https://github.com/Cirripide/local-rag-for-documents-be) | — | text~product (+2 product) | A completely local RAG. |
| 0 | [codeboltai/codeboltjs](https://github.com/codeboltai/codeboltjs) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | Js Library for Codebolt |
| 0 | [d0u6ur45u/reminder](https://github.com/d0u6ur45u/reminder) | — | topic=api-gateway,kubernetes,microservices-architecture (... | The Reminder project consists of frontend (Angular), backend (Java ... |
| 0 | [daniellmorris/EnvarynAI](https://github.com/daniellmorris/EnvarynAI) | — | text~product (+2 product) | Ambient speech capture and transcription app with a Flutter client,... |
| 0 | [davidtgillard/fits](https://github.com/davidtgillard/fits) | — | text~tool (+2 tooling/library); text~product (+2 product)... | One eighth of an agony |
| 0 | [DEFRA/fcp-fdm](https://github.com/DEFRA/fcp-fdm) | — | topic=backend (+3 product); text~product(weak) (+1 produc... | Git repository for service fcp-fdm |
| 0 | [DEFRA/fcp-sfd-comms](https://github.com/DEFRA/fcp-sfd-comms) | — | topic=backend (+3 product); text~product(weak) (+1 produc... | Git repository for service fcp-sfd-comms |
| 0 | [DEFRA/fcp-sfd-crm](https://github.com/DEFRA/fcp-sfd-crm) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Git repository for service fcp-sfd-crm |
| 0 | [DEFRA/fcp-sfd-object-processor](https://github.com/DEFRA/fcp-sfd-object-processor) | — | topic=backend (+3 product); text~product (+2 product); sp... | Git repository for service fcp-sfd-object-processor |
| 0 | [DEFRA/ffc-doc-statement-constructor](https://github.com/DEFRA/ffc-doc-statement-constructor) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [DEFRA/ffc-doc-statement-data](https://github.com/DEFRA/ffc-doc-statement-data) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [DEFRA/ffc-doc-statement-publisher](https://github.com/DEFRA/ffc-doc-statement-publisher) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [DEFRA/ffc-pay-enrichment](https://github.com/DEFRA/ffc-pay-enrichment) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC payment request enrichment service |
| 0 | [depsilon/shardloom](https://github.com/depsilon/shardloom) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Vortex-first, no-fallback compute workflow layer for auditable loca... |
| 0 | [Deutsche-FayTech-Korea/bridge_socket_server](https://github.com/Deutsche-FayTech-Korea/bridge_socket_server) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [DevashishBoini/attendanceSystem](https://github.com/DevashishBoini/attendanceSystem) | — | text~product (+2 product) |  |
| 0 | [Devathon-2024-team5/Preguntonic-backend](https://github.com/Devathon-2024-team5/Preguntonic-backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Preguntonic-Backend es el núcleo inteligente y robusto que impulsa ... |
| 0 | [ducbrick/real-time-messaging-api](https://github.com/ducbrick/real-time-messaging-api) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Backend API for a real-time messaging application |
| 0 | [EcoHub-AG/Api-Specs](https://github.com/EcoHub-AG/Api-Specs) | kafka · channel-params | text~product (+2 product); name~spec (+1 spec/docs); lang... | Specifications for all our APIs |
| 0 | [ErenAri/PulseStream--Real-Time-Event-Processing-Fabric](https://github.com/ErenAri/PulseStream--Real-Time-Event-Processing-Fabric) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [ericfitz/tmi](https://github.com/ericfitz/tmi) | — | text~product (+2 product) | TMI is a REST API server and platform for humans and agents to use ... |
| 0 | [facundo1220/asyncapi-eda-ecommerce](https://github.com/facundo1220/asyncapi-eda-ecommerce) | — | text~product (+2 product) |  |
| 0 | [filipepacheco/the-jam-app-frontend](https://github.com/filipepacheco/the-jam-app-frontend) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [FrankSpooren/HolidaiButler](https://github.com/FrankSpooren/HolidaiButler) | — | text~product (+2 product) | AI-platform Costa destinations |
| 0 | [fraunhoferfokus/dredger-todos](https://github.com/fraunhoferfokus/dredger-todos) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [GitEngHar/pointservice](https://github.com/GitEngHar/pointservice) | amqp | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [gokerDEV/node-chat-server](https://github.com/gokerDEV/node-chat-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Gradient-DS/AGORA](https://github.com/Gradient-DS/AGORA) | channel-params | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [GregTag/TheSpreadGame](https://github.com/GregTag/TheSpreadGame) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [hassanm0301/plasma-bridge](https://github.com/hassanm0301/plasma-bridge) | — | text~product (+2 product) | Qt 6 backend for KDE Plasma exposing selected desktop state and con... |
| 0 | [hungvo2010/free-note-service](https://github.com/hungvo2010/free-note-service) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [IATI/iati-message-queue-service](https://github.com/IATI/iati-message-queue-service) | amqp | text~product (+2 product); text~spec (+2 spec/docs) |  |
| 0 | [Insightpulseai/agents](https://github.com/Insightpulseai/agents) | — | text~product (+2 product) | Agent personas, skills, judges, evals, metadata, registries, and pr... |
| 0 | [Integration-Project-2026-Groep-2/Planning](https://github.com/Integration-Project-2026-Groep-2/Planning) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [itamm15/sync-async-docs](https://github.com/itamm15/sync-async-docs) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 0 | [jamesenki/vehicle-to-cloud-communications-architecture](https://github.com/jamesenki/vehicle-to-cloud-communications-architecture) | mqtt · channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | Production-ready MQTT5 Vehicle-to-Cloud communications architecture... |
| 0 | [jardelva96/Orqupay](https://github.com/jardelva96/Orqupay) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  Sistema de módulo de pagamentos para integração com múltiplos prov... |
| 0 | [jhamill34/disney-gen-ai-takehome](https://github.com/jhamill34/disney-gen-ai-takehome) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [jordancrombie/bsim](https://github.com/jordancrombie/bsim) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | A Banking Simulator |
| 0 | [joserprieto/practice-desk](https://github.com/joserprieto/practice-desk) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Professional practice management platform — document collection, ap... |
| 0 | [Kambolo/Picksy](https://github.com/Kambolo/Picksy) | channel-params | text~product (+2 product) |  |
| 0 | [kardasz/skipper-club-android](https://github.com/kardasz/skipper-club-android) | reply | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [kaucrow/mqtt-rest-bridge](https://github.com/kaucrow/mqtt-rest-bridge) | — | topic=mqtt-broker,mqtt-server (+3 product); text~product ... | MQTT broker & REST API for a demo SCADA system which bridges two mi... |
| 0 | [kelnishi/SatMouse](https://github.com/kelnishi/SatMouse) | — | text~product (+2 product) | 3D input device bridge for Web Applications |
| 0 | [kinoh/Tsuki](https://github.com/kinoh/Tsuki) | — | text~product (+2 product) |  |
| 0 | [latamteks-cmyk/SmartEdify_app](https://github.com/latamteks-cmyk/SmartEdify_app) | — | text~product (+2 product) |  |
| 0 | [LaurenCattoor/st-microservice-ticketing](https://github.com/LaurenCattoor/st-microservice-ticketing) | amqp | text~product (+2 product) |  |
| 0 | [LeonidasGarcia/puchamon](https://github.com/LeonidasGarcia/puchamon) | — | text~product (+2 product) | Proyecto universitario de clon de Pokemon Showdown con un bot IA pa... |
| 0 | [leynos/wildside](https://github.com/leynos/wildside) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [lgonzalezrouco/sensareal-backend](https://github.com/lgonzalezrouco/sensareal-backend) | mqtt · channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | Backend del proyecto de PTI |
| 0 | [LouisSappey/tp-nest-web-socket](https://github.com/LouisSappey/tp-nest-web-socket) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [loulou123546/kenshiata-shared](https://github.com/loulou123546/kenshiata-shared) | reply · channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | Shared files between server and clients, like types or some pure fu... |
| 0 | [Lulexs/iots-1](https://github.com/Lulexs/iots-1) | — | text~product (+2 product) |  |
| 0 | [makeevolution/SimplePizzaWinkel](https://github.com/makeevolution/SimplePizzaWinkel) | — | text~product (+2 product) |  |
| 0 | [MALIEV-Co-Ltd/Maliev.MessagingContracts](https://github.com/MALIEV-Co-Ltd/Maliev.MessagingContracts) | amqp | text~product (+2 product); spec-at-root/docs (+1 product) | Messaging contracts for all Maliev microservices — events, commands... |
| 0 | [Malmo-Skyttegille-Pistolsektionen/rotation_target_backend_resources](https://github.com/Malmo-Skyttegille-Pistolsektionen/rotation_target_backend_resources) | — | text~product (+2 product); text~spec (+2 spec/docs) | Resources used by the Rotation Target Backend |
| 0 | [manav-1/expense-ai-be](https://github.com/manav-1/expense-ai-be) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Voice-first expense tracker — Go backend, React Native mobile app |
| 0 | [ManuMarcos/mind-battle-backend](https://github.com/ManuMarcos/mind-battle-backend) | — | text~product (+2 product); lang=HTML (+1 spec/docs) | Backend for a real-time multiplayer quiz game inspired by Kahoot. B... |
| 0 | [MathTrail/contracts](https://github.com/MathTrail/contracts) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Schema Registry for MathTrail: Type-safe contracts and event defini... |
| 0 | [maxime-aube/ollama](https://github.com/maxime-aube/ollama) | reply · channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [maximilianoPizarro/platform-hub-spoke-config](https://github.com/maximilianoPizarro/platform-hub-spoke-config) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Multi-cluster GitOps platform using Red Hat Advanced Cluster Manage... |
| 0 | [MaximilianWalker/HexRelay](https://github.com/MaximilianWalker/HexRelay) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [miltonabdon/ecommerce-scalable-platform](https://github.com/miltonabdon/ecommerce-scalable-platform) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | E-Commerce platform demonstrating scalable architecture for Black F... |
| 0 | [ministryofjustice/hmpps-external-movements-api](https://github.com/ministryofjustice/hmpps-external-movements-api) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Allows for the scheduling, management and enquiry of various types ... |
| 0 | [ministryofjustice/hmpps-restricted-patients-api](https://github.com/ministryofjustice/hmpps-restricted-patients-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | API to manage restricted patients |
| 0 | [mjones3/interface-exception-collector-service](https://github.com/mjones3/interface-exception-collector-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [murithigeo/ogc-edr-api](https://github.com/murithigeo/ogc-edr-api) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... | A reference implementation for OGC EDR API |
| 0 | [myrobotaxi/telemetry](https://github.com/myrobotaxi/telemetry) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Go telemetry server for real-time Tesla Fleet Telemetry → WebSocket... |
| 0 | [nandorsilva/eda-fia-th](https://github.com/nandorsilva/eda-fia-th) | kafka · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ngscheurich/elixirconf-eu-2024](https://github.com/ngscheurich/elixirconf-eu-2024) | reply · channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | 🗺️ “Let’s Go on an Adventure” (ElixirConf EU 2024) |
| 0 | [nguyenvinhhuy/microservice-platform](https://github.com/nguyenvinhhuy/microservice-platform) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [nicolas-codemate/esp32-pixelcast](https://github.com/nicolas-codemate/esp32-pixelcast) | mqtt · channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | ESP32 firmware for HUB75 LED matrix displays with REST API and MQTT... |
| 0 | [nikescar/dure](https://github.com/nikescar/dure) | reply | text~product (+2 product); spec-at-root/docs (+1 product) | distributed e-commerce experience for small shop owner. |
| 0 | [nitu01019/weelobackend](https://github.com/nitu01019/weelobackend) | — | text~product (+2 product) |  |
| 0 | [ocampana-videotec/onvif-cloud](https://github.com/ocampana-videotec/onvif-cloud) | mqtt | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [omnai-project/OmnAIScope_DataServer_API_Doc](https://github.com/omnai-project/OmnAIScope_DataServer_API_Doc) | — | text~product (+2 product); spec-at-root/docs (+1 product)... | Async API description for the OmnAIView Backend  |
| 0 | [ONSdigital/dp-search-data-extractor](https://github.com/ONSdigital/dp-search-data-extractor) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Service to retrieve data to update search index |
| 0 | [Owen-Richards/ai-nutritionist](https://github.com/Owen-Richards/ai-nutritionist) | — | topic=serverless (+3 product); text~product(weak) (+1 pro... | � Serverless AI Nutritionist Assistant - WhatsApp/SMS bot powered b... |
| 0 | [paranoideed/webster](https://github.com/paranoideed/webster) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Pinit-Scheduler/pinit-notification](https://github.com/Pinit-Scheduler/pinit-notification) | amqp | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | 일정 관리/실행 서비스 Pinit의 알림 기능을 담당하는 마이크로서비스 |
| 0 | [position-pal/location-service](https://github.com/position-pal/location-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | PositionPal location service |
| 0 | [PriyanArora/Qeue](https://github.com/PriyanArora/Qeue) | — | text~product (+2 product) | Microservices event platform built with Java and Spring Boot where ... |
| 0 | [pseudotop/maekon-client](https://github.com/pseudotop/maekon-client) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Open-source desktop intelligence client that turns local work signa... |
| 0 | [pt9912/geodata-native-suite](https://github.com/pt9912/geodata-native-suite) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [qualtt/restful-slice](https://github.com/qualtt/restful-slice) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Headless REST application for 3D model processing |
| 0 | [Quiago/doble9](https://github.com/Quiago/doble9) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Remake1/GrokOA](https://github.com/Remake1/GrokOA) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); s... | Stealth coding Online Assessment and Interview cheat tool.   |
| 0 | [remidosol/real-time-trade-api](https://github.com/remidosol/real-time-trade-api) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | The "Real-Time Trading API" is a high-performance WebSocket-based p... |
| 0 | [RodolfoFigueroa/lyra](https://github.com/RodolfoFigueroa/lyra) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Geospatial indicators API |
| 0 | [romdj/tempsdarret.studio](https://github.com/romdj/tempsdarret.studio) | — | text~product (+2 product); name~tool (+1 tooling/library) | A modern portfolio and client portal for photographers, built with ... |
| 0 | [ross2p/mindlet-notification](https://github.com/ross2p/mindlet-notification) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [ross2p/mindlet-payment](https://github.com/ross2p/mindlet-payment) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [ross2p/mindlet-subscription](https://github.com/ross2p/mindlet-subscription) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [SchlexanderOlz/MatchMakerHub](https://github.com/SchlexanderOlz/MatchMakerHub) | — | text~product (+2 product) | The MatchMakerHub is the main server which tries to create connecti... |
| 0 | [shapeitapp/shapeit-github-app](https://github.com/shapeitapp/shapeit-github-app) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [Souvikns/greet-bot](https://github.com/Souvikns/greet-bot) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | A simple websocket API example using glee.  |
| 0 | [specmatic/specmatic-arazzo-openapi-asyncapi-sample](https://github.com/specmatic/specmatic-arazzo-openapi-asyncapi-sample) | reply | topic=api-mocking (+3 product); name~demo (+2 demo/fixture) | From REST to Events: API Workflow Testing and Mocking with a Single... |
| 0 | [SRinatR/RD](https://github.com/SRinatR/RD) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [StableCoinTF/StableCoinBC_Adapter_Docs](https://github.com/StableCoinTF/StableCoinBC_Adapter_Docs) | reply | text~tool (+2 tooling/library); text~product (+2 product)... | StableCoinBC_Adapter_Docs |
| 0 | [stardew-valley-dedicated-server/web](https://github.com/stardew-valley-dedicated-server/web) | reply | text~tool (+2 tooling/library); text~product (+2 product)... | A Linux Docker image to run a headless dedicated multiplayer server... |
| 0 | [StepanNazar/city-report-ai-assistance-service](https://github.com/StepanNazar/city-report-ai-assistance-service) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | university labs for software architecture |
| 0 | [Syed1012/kesselops](https://github.com/Syed1012/kesselops) | channel-params | text~product (+2 product); spec-at-root/docs (+1 product) | A modular monolith platform that digitizes gastronomy operations — ... |
| 0 | [takeruun/ws-ts-gen](https://github.com/takeruun/ws-ts-gen) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [Tanh1603/auction-hub](https://github.com/Tanh1603/auction-hub) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [Thomas-More-Digital-Innovation/2526-DI-004-GoStrategy](https://github.com/Thomas-More-Digital-Innovation/2526-DI-004-GoStrategy) | channel-params | text~product (+2 product) | Project 2025-2026 DI-004: GoStrategy |
| 0 | [thomascarter613/aic-smb-copilot-codebase](https://github.com/thomascarter613/aic-smb-copilot-codebase) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [TristanDeLil/ms-microservice-ticketing](https://github.com/TristanDeLil/ms-microservice-ticketing) | amqp | text~product (+2 product) |  |
| 0 | [ugaemi/gyeongdohalsaram-server](https://github.com/ugaemi/gyeongdohalsaram-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [underpass-ai/underpass-choreographer](https://github.com/underpass-ai/underpass-choreographer) | — | text~product (+2 product) | Event-driven coordinator of specialist agent councils. Use-case agn... |
| 0 | [V-ivek/workflow-engine](https://github.com/V-ivek/workflow-engine) | — | text~product (+2 product); spec-at-root/docs (+1 product) | An Event-Driven workflow orchestration engine |
| 0 | [VistA-Evolved/vista-evolved-platform](https://github.com/VistA-Evolved/vista-evolved-platform) | — | text~product (+2 product) | VistA Evolved Platform — clean canonical platform monorepo |
| 0 | [webitel/im-delivery-service](https://github.com/webitel/im-delivery-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [Xen0Xys/N2I-2024-API](https://github.com/Xen0Xys/N2I-2024-API) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [xingyug/service2mcp](https://github.com/xingyug/service2mcp) | amqp | topic=api-compiler (+3 tooling/library); topic=api-gatewa... | Compile any API (OpenAPI, GraphQL, gRPC, REST, SOAP, SQL, AsyncAPI,... |
| 0 | [yethan4/where-is-my-dog](https://github.com/yethan4/where-is-my-dog) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A mobile app to find lost dogs and help others find theirs. Current... |
| 0 | [Yeusepe/cdngine](https://github.com/Yeusepe/cdngine) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A high performance asset processing and delivery platform. |
| 0 | [yousuf7474/meerkat](https://github.com/yousuf7474/meerkat) | channel-params | text~product (+2 product) | React App for Multi-Agent RAG System |
| 0 | [yukihito-jokyu/postman-mcp-server](https://github.com/yukihito-jokyu/postman-mcp-server) | channel-params | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 0 | [yuvraj-chouhan-dev/ready-now-server](https://github.com/yuvraj-chouhan-dev/ready-now-server) | — | text~tool (+2 tooling/library); text~product (+2 product)... | ready now SDK Backend server |
| 0 | [zimoch84/HaggisProject](https://github.com/zimoch84/HaggisProject) | channel-params | text~product (+2 product) |  |
| 0 | [znsio/specmatic-async-order-api-kotlin](https://github.com/znsio/specmatic-async-order-api-kotlin) | reply | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Order API accepts request for an order which is created asynchronou... |
| 0 | [ZuzannaTabisz/snp-app](https://github.com/ZuzannaTabisz/snp-app) | — | text~product (+2 product) |  |
| 0 | [ZuzannaTabisz/snpapptests](https://github.com/ZuzannaTabisz/snpapptests) | — | text~product (+2 product) |  |

## tooling/library (211)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 15204 | [scalar/scalar](https://github.com/scalar/scalar) | channel-params | topic=api-client,http-client (+3 tooling/library); topic=... | Scalar is an open-source API platform:　　　　　　　　　　　　　　　　　　　　　　　　　　　　　... |
| 3737 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | reply · channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | OpenAgents - AI Agent Networks for Open Collaboration |
| 3654 | [fern-api/fern](https://github.com/fern-api/fern) | — | topic=docs-generator,sdk-generator (+3 tooling/library); ... | Input OpenAPI. Output SDKs and Docs. |
| 1464 | [Redocly/redocly-cli](https://github.com/Redocly/redocly-cli) | reply · channel-params | topic=linter,openapi-cli (+3 tooling/library); text~tool ... | ⚒️ Redocly CLI makes OpenAPI easy. Lint/validate to any standard, g... |
| 1059 | [asyncapi/generator](https://github.com/asyncapi/generator) | — | topic=documentation,get-global-docs-autoupdate (+3 spec/d... | Use your AsyncAPI definition to generate literally anything. Markdo... |
| 1047 | [openfoodfacts/openfoodfacts-server](https://github.com/openfoodfacts/openfoodfacts-server) | — | topic=recycling (+3 tooling/library); text~tool (+2 tooli... | Open Food Facts database, API server and web interface - 🐪🦋 Perl, C... |
| 476 | [Sovereign-Labs/sovereign-sdk](https://github.com/Sovereign-Labs/sovereign-sdk) | — | topic=verifiable-server (+3 product); topic=sdk (+3 tooli... | A flexible toolkit for building real-time blockchains |
| 436 | [asyncapi/modelina](https://github.com/asyncapi/modelina) | — | topic=json-schema (+3 spec/docs); topic=codegen,codegener... | A library for generating typed models based on inputs such as Async... |
| 343 | [springwolf/springwolf-core](https://github.com/springwolf/springwolf-core) | — | topic=documentation-generator (+3 tooling/library); text~... | Automated documentation for event-driven applications built with Sp... |
| 337 | [Lap-Platform/LAP](https://github.com/Lap-Platform/LAP) | kafka · amqp | topic=cli (+3 tooling/library); text~product (+2 product)... | Your agents are guessing at APIs. Give them the actual Agent-Native... |
| 327 | [CardanoSolutions/ogmios](https://github.com/CardanoSolutions/ogmios) | channel-params | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | ❇️ A WebSocket JSON/RPC bridge for Cardano |
| 267 | [asyncapi/cli](https://github.com/asyncapi/cli) | channel-params | topic=cli (+3 tooling/library); topic=get-global-docs-aut... | CLI to work with your AsyncAPI files. You can validate them and in ... |
| 233 | [flamewow/nestjs-asyncapi](https://github.com/flamewow/nestjs-asyncapi) | — | text~tool (+2 tooling/library); text~product (+2 product)... | NestJS AsyncAPI module - generate documentation of your event-based... |
| 207 | [EVerest/EVerest](https://github.com/EVerest/EVerest) | reply · mqtt · channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Main Repository of EVerest - an EV charging software stack |
| 205 | [asyncapi/studio](https://github.com/asyncapi/studio) | — | name~tool (+1 tooling/library); spec-only-in-fixtures (+1... | Visually design your AsyncAPI files and event-driven architecture. |
| 194 | [bian-official/public](https://github.com/bian-official/public) | channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | This is a repository of BIAN artefacts, currently the BIAN Semantic... |
| 157 | [lerenn/asyncapi-codegen](https://github.com/lerenn/asyncapi-codegen) | reply · channel-params | topic=asyncapi-generator,code-generation,generator (+3 to... | An AsyncAPI Golang Code generator that generates all Go code from t... |
| 149 | [huynguyengl99/chanx](https://github.com/huynguyengl99/chanx) | reply · channel-params | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | A batteries-included WebSocket framework for Django Channels, FastA... |
| 101 | [Goldziher/spikard](https://github.com/Goldziher/spikard) | channel-params | text~tool (+2 tooling/library) | Rust-powered, multi-language web toolkit with bindings for Python, ... |
| 99 | [swagger-api/apidom](https://github.com/swagger-api/apidom) | reply · kafka · amqp · channel-params | topic=parser (+3 tooling/library); text~tool (+2 tooling/... | Semantic parser for API specifications |
| 90 | [asyncapi/html-template](https://github.com/asyncapi/html-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | HTML template for AsyncAPI Generator. Use it to generate a static d... |
| 79 | [asyncapi/jasyncapi](https://github.com/asyncapi/jasyncapi) | — | topic=java-library,kotlin-library (+3 tooling/library); t... | /jay-sync-api/ is a Java code-first tool for AsyncAPI specification |
| 69 | [bump-sh/cli](https://github.com/bump-sh/cli) | — | topic=cli (+3 tooling/library); topic=api-specification,a... | Bump.sh CLI - Deploy your OpenAPI & AsyncAPI documentations from yo... |
| 61 | [sngular/scs-multiapi-plugin](https://github.com/sngular/scs-multiapi-plugin) | — | topic=asyncapi-generator,openapi-codegen,openapi-generato... | This is a Maven plugin designed to help developers automatizing the... |
| 60 | [asyncapi/vs-asyncapi-preview](https://github.com/asyncapi/vs-asyncapi-preview) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | VSCode AsyncAPI Preview Extension |
| 56 | [marle3003/mokapi](https://github.com/marle3003/mokapi) | kafka · mqtt · channel-params | text~tool (+2 tooling/library) | Your API mocking tool for OpenAPI and AsyncAPI using Go and JavaScr... |
| 56 | [ZenWave360/zenwave-sdk](https://github.com/ZenWave360/zenwave-sdk) | — | topic=code-generator (+3 tooling/library); text~tool (+2 ... | DDD and API-First tools for Event-Driven microservices. Create Soft... |
| 51 | [WaleedAshraf/asyncapi-validator](https://github.com/WaleedAshraf/asyncapi-validator) | — | topic=validator (+3 tooling/library); topic=asyncapi-spec... | Message validator for Kafka/RabbitMQ/Anything through AsyncAPI schema |
| 47 | [asyncapi/nodejs-template](https://github.com/asyncapi/nodejs-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | This template generates a server using your AsyncAPI document. It s... |
| 44 | [eventum-generator/eventum](https://github.com/eventum-generator/eventum) | — | topic=clickhouse (+3 tooling/library); text~product (+2 p... | Realistic synthetic events for testing, demos, and pipelines — stre... |
| 36 | [asyncapi/markdown-template](https://github.com/asyncapi/markdown-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Markdown template for the AsyncAPI Generator |
| 34 | [the-codegen-project/cli](https://github.com/the-codegen-project/cli) | reply · channel-params | topic=generator,openapi-generator,the-codegen-project (+3... | Your one stop boilerplate killer for any standard! |
| 33 | [asyncapi/avro-schema-parser](https://github.com/asyncapi/avro-schema-parser) | — | topic=avro-schema (+3 spec/docs); topic=avro-schema-regis... | An AsyncAPI schema parser for Avro 1.x schemas. |
| 33 | [asyncapi/bundler](https://github.com/asyncapi/bundler) | mqtt · channel-params | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Combine multiple AsyncAPI specification files into one. |
| 29 | [asyncapi/diff](https://github.com/asyncapi/diff) | — | topic=cli (+3 tooling/library); text~tool (+2 tooling/lib... | Diff is a library that compares two AsyncAPI Documents and provides... |
| 29 | [SchwarzIT/api-linter-rules](https://github.com/SchwarzIT/api-linter-rules) | — | topic=linting-rules (+3 tooling/library); text~tool (+2 t... | Schwarz API rule definitions for the Spectral API linter |
| 26 | [udamir/api-ref-bundler](https://github.com/udamir/api-ref-bundler) | reply · channel-params | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | Bundle all external $ref in Json based API document into single doc... |
| 24 | [asyncapi/converter-js](https://github.com/asyncapi/converter-js) | — | topic=converter (+3 tooling/library); text~tool (+2 tooli... | Convert to or migrate between AsyncAPI versions with the converter |
| 24 | [G-USI/asyncapi-python](https://github.com/G-USI/asyncapi-python) | reply · amqp · channel-params | topic=asyncapi-generator (+3 tooling/library); topic=asyn... | A command line interface to generate python code from asyncapi spec |
| 18 | [asyncapi/openapi-schema-parser](https://github.com/asyncapi/openapi-schema-parser) | — | topic=parser (+3 tooling/library); text~tool (+2 tooling/... | An AsyncAPI schema parser for OpenAPI 3.0.x and Swagger 2.x schemas. |
| 18 | [jacekzwpl/docueye](https://github.com/jacekzwpl/docueye) | — | topic=architecture-documentation,documentation (+3 spec/d... | DocuEye is a tool that lets You visualize views and documentation c... |
| 18 | [ZenWave360/json-schema-ref-parser-jvm](https://github.com/ZenWave360/json-schema-ref-parser-jvm) | — | topic=json-schema (+3 spec/docs); text~tool (+2 tooling/l... | Parse, Resolve, and Dereference JSON Schema $ref pointers for JVM |
| 17 | [daler-rahimov/sio-asyncapi](https://github.com/daler-rahimov/sio-asyncapi) | — | text~tool (+2 tooling/library); text~product (+2 product)... | SIO-AsyncAPI is a Python library built on the top of Flask-SocketIO... |
| 16 | [asyncapi/jasyncapi-idea-plugin](https://github.com/asyncapi/jasyncapi-idea-plugin) | — | topic=asyncapi-schemas,asyncapi-specification (+3 spec/do... | /jay-sync-api/-idea-plugin is a IDEA plugin for AsyncAPI specificat... |
| 14 | [asyncapi/java-template](https://github.com/asyncapi/java-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Java template for the AsyncAPI Generator |
| 14 | [yojo-generator/generator](https://github.com/yojo-generator/generator) | kafka · channel-params | topic=asyncapi-generator,yaml-parser (+3 tooling/library)... | This project is a core-library for generate POJO's from asyncApi ya... |
| 12 | [asyncapi/optimizer](https://github.com/asyncapi/optimizer) | mqtt · channel-params | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AsyncAPI offers many different ways to reuse certain parts of the d... |
| 12 | [quarkiverse/quarkus-asyncapi](https://github.com/quarkiverse/quarkus-asyncapi) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | AsyncAPI Quarkus configuration and metadata generator |
| 11 | [aml-org/amf](https://github.com/aml-org/amf) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | AMF (AML Modeling Framework) is an open-source library capable of p... |
| 11 | [asyncapi/protobuf-schema-parser](https://github.com/asyncapi/protobuf-schema-parser) | — | topic=schema (+3 spec/docs); topic=parser (+3 tooling/lib... | Schema parser for Protobuf compatible with AsyncAPI JS Parser |
| 11 | [microcks/microcks-spectral-ruleset](https://github.com/microcks/microcks-spectral-ruleset) | channel-params | topic=linting-rules (+3 tooling/library); topic=mocking (... | A set of rules for Spectral that allows linting OpenAPI and AsyncAP... |
| 10 | [holydocs/messageflow](https://github.com/holydocs/messageflow) | reply · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | System-architecture documentation and diagrams from AsyncAPI specif... |
| 9 | [allofmeng/streamline_project](https://github.com/allofmeng/streamline_project) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 9 | [openxapi/openxapi](https://github.com/openxapi/openxapi) | reply · channel-params | topic=sdk (+3 tooling/library); text~tool (+2 tooling/lib... | OpenAPI and AsyncAPI specifications for cryptocurrency exchanges an... |
| 8 | [Caldis/frameworks](https://github.com/Caldis/frameworks) | — | topic=frameworks (+3 tooling/library); text~tool (+2 tool... | Software Design Frameworks \| A curated collection for engineers, a... |
| 8 | [pactflow/openapi-pact-comparator](https://github.com/pactflow/openapi-pact-comparator) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 7 | [oracle-samples/websocket-client-template](https://github.com/oracle-samples/websocket-client-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) |  |
| 7 | [xraph/forge](https://github.com/xraph/forge) | — | text~tool (+2 tooling/library); text~product (+2 product)... | A very opionated distributed backend framework with everything in b... |
| 6 | [fredabila/oahl](https://github.com/fredabila/oahl) | — | topic=orchestration (+3 product); topic=ai-agents-framewo... | Open Agent Hardware Layer is an open-source framework for exposing ... |
| 5 | [EDALearn/EDA-TransactionalOutbox-Modulith-JPA](https://github.com/EDALearn/EDA-TransactionalOutbox-Modulith-JPA) | — | text~tool (+2 tooling/library); text~product (+2 product) | Implementing a Transactional OutBox With AsyncAPI, SpringModulith a... |
| 5 | [evryfs/asyncapi-generator](https://github.com/evryfs/asyncapi-generator) | reply · kafka · mqtt · channel-params | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | AsyncAPI Code Generator  |
| 5 | [Grinseteddy/DomainDrivenApiDesign](https://github.com/Grinseteddy/DomainDrivenApiDesign) | kafka | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) | Repository for ressources for trainings |
| 5 | [insspb/asyncapi3](https://github.com/insspb/asyncapi3) | mqtt · channel-params | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Python AsyncAPI 3.0 object model |
| 5 | [SolaceLabs/solace-tools-typescript](https://github.com/SolaceLabs/solace-tools-typescript) | — | text~tool (+2 tooling/library); text~product (+2 product)... | This repository contains tools to enable interaction with the Solac... |
| 4 | [derberg/python-mqtt-client-template](https://github.com/derberg/python-mqtt-client-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | This template generates MQTT Python client module. Its purpose is t... |
| 4 | [DigKick/DigKick](https://github.com/DigKick/DigKick) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) | DigKick is a system that detects goals and tracks players elo for t... |
| 4 | [Elhebert/asyncapi-validation](https://github.com/Elhebert/asyncapi-validation) | kafka · mqtt · channel-params | topic=validator (+3 tooling/library); topic=asyncapi-spec... | Message validation package from YAML and JSON AsyncAPI document |
| 4 | [lg-labs/blank-service](https://github.com/lg-labs/blank-service) | kafka · channel-params | topic=feign-client (+3 tooling/library); text~product(wea... | 👋 Management the blank service for the blanksystem as template. |
| 4 | [maxkrv/uchat](https://github.com/maxkrv/uchat) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Chat application |
| 4 | [openpx-trade/openpx](https://github.com/openpx-trade/openpx) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 3 | [apiaddicts/sonar-asyncapi](https://github.com/apiaddicts/sonar-asyncapi) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | Code analyzer for AsyncAPI specifications |
| 3 | [bitsy-ai/printnanny-webapp](https://github.com/bitsy-ai/printnanny-webapp) | channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 3 | [David-Parry/server-agents](https://github.com/David-Parry/server-agents) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 3 | [hkirat/asyncapi-fork](https://github.com/hkirat/asyncapi-fork) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 3 | [ir-kit/ir-kit](https://github.com/ir-kit/ir-kit) | amqp | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 3 | [kombifyio/SpeechKit](https://github.com/kombifyio/SpeechKit) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | kombify SpeechKit — Open-source Speech Processing Framework. STT, V... |
| 3 | [meteatamel/asyncapi-basics](https://github.com/meteatamel/asyncapi-basics) | mqtt · amqp | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | This repository contains information, references, and samples about... |
| 3 | [ministryofjustice/hmpps-accredited-programmes-manage-and-deliver-api](https://github.com/ministryofjustice/hmpps-accredited-programmes-manage-and-deliver-api) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | HMPPS Manage and Deliver Accredited Programmes API Layer (bootstrap... |
| 3 | [NHSDigital/nhs-notify-supplier-api](https://github.com/NHSDigital/nhs-notify-supplier-api) | — | text~tool (+2 tooling/library) | API Definitions, Sandbox and SDK for the NHS Notify Supplier API |
| 3 | [WaYdotNET/zen-generator](https://github.com/WaYdotNET/zen-generator) | reply | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | A bidirectional Python code generator that converts between AsyncAP... |
| 2 | [acidtango/ollert-backend](https://github.com/acidtango/ollert-backend) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 2 | [amer8/apibconv](https://github.com/amer8/apibconv) | — | topic=cli,converter (+3 tooling/library); spec-only-in-fi... | Convert between API Blueprint (*.apib), OpenAPI 2.0/3.0.x/3.1.x, an... |
| 2 | [bakabala27-svg/NAAS-Agentic-Core](https://github.com/bakabala27-svg/NAAS-Agentic-Core) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 2 | [Benzinga/benzinga-docs](https://github.com/Benzinga/benzinga-docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 2 | [bsv-blockchain/ts-stack](https://github.com/bsv-blockchain/ts-stack) | — | text~tool (+2 tooling/library); lang=HTML (+1 spec/docs) |  |
| 2 | [ekidenfi/ekiden-docs](https://github.com/ekidenfi/ekiden-docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 2 | [ingka-group/asyncapi-payload-validator](https://github.com/ingka-group/asyncapi-payload-validator) | — | topic=cli (+3 tooling/library); topic=jinja2-templates (+... | A Python library and CLI for validating message payloads against As... |
| 2 | [ministryofjustice/hmpps-find-and-refer-an-intervention-service](https://github.com/ministryofjustice/hmpps-find-and-refer-an-intervention-service) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Business/domain interface for providing Find and Refer an Intervent... |
| 2 | [neosun100/VibeVoice](https://github.com/neosun100/VibeVoice) | channel-params | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Open-Source Frontier Voice AI - Real-time Text-to-Speech with Docke... |
| 2 | [ripple/rippled-api-spec](https://github.com/ripple/rippled-api-spec) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A repository for OpenAPI / AsyncAPI specifications. This ideally ev... |
| 2 | [siom79/jasyncapicmp](https://github.com/siom79/jasyncapicmp) | kafka · amqp | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | jasyncapicmp is a tool to compare two versions of a asyncapi specif... |
| 2 | [TemplateMechanics/tilt](https://github.com/TemplateMechanics/tilt) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Tilt File Examples |
| 1 | [AcidicSoil/DSPyTeach](https://github.com/AcidicSoil/DSPyTeach) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) |  |
| 1 | [AcidicSoil/lms-llmsTxt](https://github.com/AcidicSoil/lms-llmsTxt) | — | text~tool (+2 tooling/library) | LM-Studio llms.txt generator using DSPy framework |
| 1 | [ajevans99/swift-asyncapi](https://github.com/ajevans99/swift-asyncapi) | kafka · channel-params | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A Swift library for generating AsyncAPI documents. |
| 1 | [AndreaGiulianelli/documentation-ghp-action](https://github.com/AndreaGiulianelli/documentation-ghp-action) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs);... | Github Action to generate code, OpenAPI and AsyncAPI documentation ... |
| 1 | [certifieddata/certifieddata-agent-commerce-public](https://github.com/certifieddata/certifieddata-agent-commerce-public) | — | topic=json-schema (+3 spec/docs); topic=sdk (+3 tooling/l... | Public API, SDKs, schemas, event contracts, and examples for Certif... |
| 1 | [cidverse/repoanalyzer](https://github.com/cidverse/repoanalyzer) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | a go library to analyze a project directory to determinate all modu... |
| 1 | [dcSpark/sovereign-sdk](https://github.com/dcSpark/sovereign-sdk) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | A flexible toolkit for building real-time blockchains |
| 1 | [ff-fab/cosalette](https://github.com/ff-fab/cosalette) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | An opinionated Python framework for building IoT-to-MQTT bridge app... |
| 1 | [ff-fab/cosalette-apps](https://github.com/ff-fab/cosalette-apps) | — | text~tool (+2 tooling/library); text~product (+2 product) | Monorepo for cosalette based smart home apps. |
| 1 | [finlayjn/asyncapi-swift-ws-template](https://github.com/finlayjn/asyncapi-swift-ws-template) | reply | AsyncAPI Generator codegen-template (tooling, not demo) | Generate a Swift client package from an AsyncAPI Specification |
| 1 | [forepath/agenstra](https://github.com/forepath/agenstra) | — | topic=framework (+3 tooling/library); text~product (+2 pr... | Centralized management platform for distributed AI agent infrastruc... |
| 1 | [gocobalt/mintlify-docs](https://github.com/gocobalt/mintlify-docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 1 | [hahnbeelee/docs-michal](https://github.com/hahnbeelee/docs-michal) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 1 | [Jacksonspencerd/tcss559-project](https://github.com/Jacksonspencerd/tcss559-project) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 1 | [JonathanGrocott/A2A-MQTT](https://github.com/JonathanGrocott/A2A-MQTT) | mqtt · channel-params | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Agent to agent protocol using MQTT |
| 1 | [kdwras/node-red-async-api-plugin](https://github.com/kdwras/node-red-async-api-plugin) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 1 | [NeatGuyCoding/spring-io](https://github.com/NeatGuyCoding/spring-io) | kafka | text~tool (+2 tooling/library) | spring io conference |
| 1 | [paddypawprints/VLMChat](https://github.com/paddypawprints/VLMChat) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 1 | [RossBugginsNHS/notify-asyncapi](https://github.com/RossBugginsNHS/notify-asyncapi) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 1 | [s-menne-inovex/async_api_pages](https://github.com/s-menne-inovex/async_api_pages) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Testing the asyncapi generator with github pages |
| 1 | [simliai/docs](https://github.com/simliai/docs) | reply | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 1 | [slng-ai/sdks](https://github.com/slng-ai/sdks) | — | text~tool (+2 tooling/library); text~product (+2 product) | A repository for sdks |
| 1 | [solace-cto-labs/solace-amplify-discovery-agent](https://github.com/solace-cto-labs/solace-amplify-discovery-agent) | channel-params | text~tool (+2 tooling/library); text~product (+2 product) | Solace-Amplify-Discovery-Agent for synchronizing Solace AsyncAPIs w... |
| 1 | [Souvikns/asyncapi-parser](https://github.com/Souvikns/asyncapi-parser) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | Asycnapi Parser written in rust  |
| 1 | [WSOL12/html-template](https://github.com/WSOL12/html-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) |  |
| 0 | [4g3nt4333/Ascy-website](https://github.com/4g3nt4333/Ascy-website) | amqp | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [AbhishekCS3459/URL-Shortner-using-GRPC](https://github.com/AbhishekCS3459/URL-Shortner-using-GRPC) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | This is a url service which uses grpc  for communicating to the url... |
| 0 | [acvigue/casa-bonita](https://github.com/acvigue/casa-bonita) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [AlexanderFromEarth/node-apifactory](https://github.com/AlexanderFromEarth/node-apifactory) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Web framework for API-first development via OpenAPI specification w... |
| 0 | [AlexandrePh/flywheel-starter-kit](https://github.com/AlexandrePh/flywheel-starter-kit) | channel-params | text~tool (+2 tooling/library); name~demo (+2 demo/fixture) |  |
| 0 | [aperim/production-city-web](https://github.com/aperim/production-city-web) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | Production City web application |
| 0 | [arc-framework/arc-platform](https://github.com/arc-framework/arc-platform) | channel-params | text~tool (+2 tooling/library); text~product (+2 product) | The official production monorepo for A.R.C. Houses the "Brain" (Pyt... |
| 0 | [BidnessForB/oas-converter-lambda](https://github.com/BidnessForB/oas-converter-lambda) | — | text~tool (+2 tooling/library) | Lambda function to convert API Definitions (schemas) from OAS 2.0 -... |
| 0 | [Bikxs/Skafu](https://github.com/Bikxs/Skafu) | channel-params | text~tool (+2 tooling/library); text~product (+2 product) | AI-powered microservices scaffolding platform that generates enterp... |
| 0 | [bmf-san/go-bitflyer-api-client](https://github.com/bmf-san/go-bitflyer-api-client) | — | topic=api-client (+3 tooling/library); text~demo (+2 demo... | bitFlyer Lightning API client for Go.  |
| 0 | [c-plus-plus-equals-c-plus-one/sovereign-sdk-wip](https://github.com/c-plus-plus-equals-c-plus-one/sovereign-sdk-wip) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [charlie-haley/asyncapi-go](https://github.com/charlie-haley/asyncapi-go) | kafka · amqp | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Go library for parsing and working with AsyncAPI specifications.  |
| 0 | [chem-gl/chemistry-apps](https://github.com/chem-gl/chemistry-apps) | channel-params | text~tool (+2 tooling/library); text~product (+2 product) | Apps de quimica de uso general |
| 0 | [cipher982/longhouse](https://github.com/cipher982/longhouse) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | centralized location for managing ai agents |
| 0 | [codemonstersteam/pinout-asyncapi](https://github.com/codemonstersteam/pinout-asyncapi) | reply · amqp | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AsyncAPI 3.0 contract validator. A module of the pinout ecosystem f... |
| 0 | [daksh0702/first-backstage-app](https://github.com/daksh0702/first-backstage-app) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [dalsgaard/account-service](https://github.com/dalsgaard/account-service) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [dalsgaard/asyncapi-template](https://github.com/dalsgaard/asyncapi-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) |  |
| 0 | [davidB/sandbox_cdevents_spec](https://github.com/davidB/sandbox_cdevents_spec) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | exploration of other way to define cdevents (and to generate doc, s... |
| 0 | [deepgram/starter-contracts](https://github.com/deepgram/starter-contracts) | — | text~tool (+2 tooling/library); name~demo (+2 demo/fixture) | Quickly build Deepgram Starter Apps from API specifications and Int... |
| 0 | [DEFRA/ffc-doc-statement-generator](https://github.com/DEFRA/ffc-doc-statement-generator) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [devone-demo/oracle-websocket-client-template](https://github.com/devone-demo/oracle-websocket-client-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) |  |
| 0 | [dimonoff/asyncapi-codegen](https://github.com/dimonoff/asyncapi-codegen) | reply · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | An AsyncAPI Golang Code generator that generates all Go code from t... |
| 0 | [dipaksodani/async-gen](https://github.com/dipaksodani/async-gen) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [donbagger/documentation](https://github.com/donbagger/documentation) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [E2RD0/digital-resources-transcription-service](https://github.com/E2RD0/digital-resources-transcription-service) | amqp | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [encypher-studio/newsware-docs](https://github.com/encypher-studio/newsware-docs) | reply | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Frontend for user documentation of the Newsware clients to interact... |
| 0 | [epieczko/betty](https://github.com/epieczko/betty) | — | text~tool (+2 tooling/library) |  |
| 0 | [exploding-CATs-42/ft_transcendence](https://github.com/exploding-CATs-42/ft_transcendence) | amqp | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [fraunhoferfokus/dredger](https://github.com/fraunhoferfokus/dredger) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [FreeTAKTeam/Reticulum_AsyncAPI_rs](https://github.com/FreeTAKTeam/Reticulum_AsyncAPI_rs) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | AsyncAPI-first Reticulum/LXMF framework in Rust |
| 0 | [fusion-powered-io/api-generator](https://github.com/fusion-powered-io/api-generator) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | A unified AsyncAPI and OpenAPI generator for EventCatalog for those... |
| 0 | [gonewton/newton](https://github.com/gonewton/newton) | channel-params | text~tool (+2 tooling/library); text~product (+2 product) | Newton |
| 0 | [GopiR17/backstage-prod](https://github.com/GopiR17/backstage-prod) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [GreenRover/async-api-validator](https://github.com/GreenRover/async-api-validator) | reply · channel-params | text~product (+2 product); name~tool (+1 tooling/library)... |  |
| 0 | [Hochfrequenz/verzeichnisdienst-python-models](https://github.com/Hochfrequenz/verzeichnisdienst-python-models) | — | topic=codegen (+3 tooling/library); text~demo (+2 demo/fi... | Pydantic Model Classes for the EDI@Energy Verzeichnisdienst API |
| 0 | [hotcode-dev/zerohub](https://github.com/hotcode-dev/zerohub) | — | text~tool (+2 tooling/library); text~product (+2 product)... | An open-source WebRTC signaling server |
| 0 | [IMAGINARY/track-n-truck](https://github.com/IMAGINARY/track-n-truck) | — | text~tool (+2 tooling/library); text~product (+2 product) | A game about Communication & Coordination. |
| 0 | [interruping/upbeat](https://github.com/interruping/upbeat) | — | topic=python-sdk (+3 tooling/library) | Python client for Upbit cryptocurrency exchange API — sync/async, W... |
| 0 | [Itshalffull/Concept-Oriented-Programming-Framework](https://github.com/Itshalffull/Concept-Oriented-Programming-Framework) | — | text~tool (+2 tooling/library) | A concept first, spec first, multi language programming framework |
| 0 | [JannikAlx/kafkaProducer](https://github.com/JannikAlx/kafkaProducer) | kafka | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [jason931225/oyatie](https://github.com/jason931225/oyatie) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Oyatie WIP |
| 0 | [jqassistant-plugin/jqassistant-asyncapi-plugin](https://github.com/jqassistant-plugin/jqassistant-asyncapi-plugin) | reply · kafka · channel-params | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [jstoiko/amf](https://github.com/jstoiko/amf) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AMF (AML Modeling Framework) is an open-source library capable of p... |
| 0 | [juliangracin/community-docs](https://github.com/juliangracin/community-docs) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs);... |  |
| 0 | [khulnasoft/RapidDocs](https://github.com/khulnasoft/RapidDocs) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 0 | [klurvio/sukko](https://github.com/klurvio/sukko) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [knowmadmood-poc-rhdevhub/backstage](https://github.com/knowmadmood-poc-rhdevhub/backstage) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [KrushilProlink/studio-new](https://github.com/KrushilProlink/studio-new) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [l3wi/docs](https://github.com/l3wi/docs) | reply | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [l3wi/fumadocs-async](https://github.com/l3wi/fumadocs-async) | kafka | text~tool (+2 tooling/library); text~product (+2 product)... | An AsyncAPI plugin for Fumadocs |
| 0 | [laat/asyncapi-generator-repro](https://github.com/laat/asyncapi-generator-repro) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [linkkotech/scalar](https://github.com/linkkotech/scalar) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [luistrigueiros/simple-asyncapi-codegen](https://github.com/luistrigueiros/simple-asyncapi-codegen) | kafka | text~tool (+2 tooling/library); text~product (+2 product)... | Experiments on Java code generation for AsyncAPI |
| 0 | [Matusko/flea](https://github.com/Matusko/flea) | reply | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) |  |
| 0 | [mayankshouche/docs](https://github.com/mayankshouche/docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [mayankshouche/docs-ally](https://github.com/mayankshouche/docs-ally) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [mmmnt/mmmnt](https://github.com/mmmnt/mmmnt) | — | topic=code-generation (+3 tooling/library); text~spec (+2... | A DSL and toolchain for temporal DDD modeling. |
| 0 | [MrS1lentcz/protobridge](https://github.com/MrS1lentcz/protobridge) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [mshogin/archctl](https://github.com/mshogin/archctl) | mqtt | topic=cli,linter (+3 tooling/library); topic=architecture... | Architecture-as-code validation tool |
| 0 | [Netcracker/qubership-apihub-api-processor](https://github.com/Netcracker/qubership-apihub-api-processor) | reply · kafka · amqp · channel-params | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 0 | [newstack-cloud/celerity](https://github.com/newstack-cloud/celerity) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | The backend toolkit that gets you moving fast |
| 0 | [OKArc/backstage](https://github.com/OKArc/backstage) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [opencaps/mqttcomms](https://github.com/opencaps/mqttcomms) | mqtt · channel-params | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [OpenDonationAssistant/docs](https://github.com/OpenDonationAssistant/docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [Opzet/EFDesignerExamples](https://github.com/Opzet/EFDesignerExamples) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Pakisan/jasyncapi-idea-plugin-demo](https://github.com/Pakisan/jasyncapi-idea-plugin-demo) | kafka · mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | Repository to show how AsyncAPI specification works in JetBrains IDE |
| 0 | [pascal-audio/px-api](https://github.com/pascal-audio/px-api) | reply · channel-params | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Public JSON-RPC based API for PX-Series |
| 0 | [Pinit-Scheduler/pinit-task](https://github.com/Pinit-Scheduler/pinit-task) | amqp | text~tool (+2 tooling/library); text~product (+2 product) | 일정 관리/실행 서비스 Pinit의 일정 관리/실행 기능을 담당하는 마이크로서비스 |
| 0 | [PolyAI-LDN/polyai-mintlify-doc](https://github.com/PolyAI-LDN/polyai-mintlify-doc) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | This is the source code of the PolyAI Agent Studio documentation |
| 0 | [postel-sh/postel](https://github.com/postel-sh/postel) | channel-params | topic=event-driven (+3 product); topic=library (+3 toolin... | Embeddable webhook delivery library for TypeScript. Be conservative... |
| 0 | [postman-cs/postman-aws-spec-discovery-action](https://github.com/postman-cs/postman-aws-spec-discovery-action) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs);... |  |
| 0 | [ppzxc/relaybox](https://github.com/ppzxc/relaybox) | channel-params | text~tool (+2 tooling/library) |  |
| 0 | [pv-udpv/dual-publish-platform](https://github.com/pv-udpv/dual-publish-platform) | channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | Reference scaffold: dual-publish OpenAPI/AsyncAPI specs as both UTC... |
| 0 | [RafaelAlmeida00/Plant-Simulador-Huggy](https://github.com/RafaelAlmeida00/Plant-Simulador-Huggy) | — | text~tool (+2 tooling/library); lang=HTML (+1 spec/docs) |  |
| 0 | [ravecat/asyncapi](https://github.com/ravecat/asyncapi) | reply · channel-params | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AsyncAPI to TypeScript and Zod code generator |
| 0 | [rbaxim/MOP](https://github.com/rbaxim/MOP) | — | text~tool (+2 tooling/library); text~product (+2 product) | A stdio ↔ HTTP(s) bridge |
| 0 | [roldaiateam/apis-especifications](https://github.com/roldaiateam/apis-especifications) | — | text~tool (+2 tooling/library); text~product (+2 product) | Este repositorio contiene las definiciones y especificaciones de la... |
| 0 | [samovers/OFARM](https://github.com/samovers/OFARM) | — | text~tool (+2 tooling/library) | Open semantic reference model and governance framework for traceabl... |
| 0 | [saujasn/accelerator](https://github.com/saujasn/accelerator) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [siom79/jopenapicmp](https://github.com/siom79/jopenapicmp) | kafka · amqp | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Comparison of two versions of an OpenAPI document |
| 0 | [smoya/asyncapi-parser-example](https://github.com/smoya/asyncapi-parser-example) | — | text~tool (+2 tooling/library); name~demo (+2 demo/fixtur... | This small and simple repository shows how to validate an AsyncAPI ... |
| 0 | [specmatic/aws-lambda-kafka-with-localstack](https://github.com/specmatic/aws-lambda-kafka-with-localstack) | reply | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [stardew-valley-dedicated-server/asyncapi-generator-template-ts](https://github.com/stardew-valley-dedicated-server/asyncapi-generator-template-ts) | reply | AsyncAPI Generator codegen-template (tooling, not demo) |  |
| 0 | [tanagraspace/ccsds-mo-to-asyncapi](https://github.com/tanagraspace/ccsds-mo-to-asyncapi) | reply · mqtt · channel-params | text~tool (+2 tooling/library); text~spec (+2 spec/docs) | Convert CCSDS MO XML specification files into AsyncAPI YAML documents. |
| 0 | [Tomeku-Development/AgentMesh](https://github.com/Tomeku-Development/AgentMesh) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | MESH is a fully decentralized multi-agent system where autonomous a... |
| 0 | [TomzBench/jsmn-tools](https://github.com/TomzBench/jsmn-tools) | mqtt · channel-params | text~tool (+2 tooling/library); text~product (+2 product)... | json parsing code generation for embedded targets. (https://tomzben... |
| 0 | [UTXOnly/oddrip](https://github.com/UTXOnly/oddrip) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Go Kalshi API client |
| 0 | [viktorSrk/quartogether](https://github.com/viktorSrk/quartogether) | channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Full-stack collaborative online text editor using the Quarto engine... |
| 0 | [vivekjava/Spring-Boot-Rest](https://github.com/vivekjava/Spring-Boot-Rest) | kafka · channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Standard service with low code and no code |
| 0 | [worried-networking/uptrakit](https://github.com/worried-networking/uptrakit) | — | text~tool (+2 tooling/library) | Your homelab’s little helper for tracking and applying updates. |
| 0 | [yaccob/teds](https://github.com/yaccob/teds) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 0 | [YOU54F/pact-asyncapi-comparator](https://github.com/YOU54F/pact-asyncapi-comparator) | mqtt | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | compare Message-Pact files against AsyncAPI descriptions |
| 0 | [Zenika/kafka-schema-registry-publish](https://github.com/Zenika/kafka-schema-registry-publish) | kafka | text~tool (+2 tooling/library); text~product (+2 product)... | Publish schemas to your schemas registry using CI-CD |

## demo/fixture (172)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 166 | [dotnet/maui-labs](https://github.com/dotnet/maui-labs) | — | topic=multi-platform (+3 product); text~tool (+2 tooling/... | Experimental and pre-release tools for .NET MAUI |
| 90 | [picodotdev/blog-ejemplos](https://github.com/picodotdev/blog-ejemplos) | — | text~demo (+2 demo/fixture) | Ejemplos y código de las herramientas que he explicado en el blog |
| 68 | [PacktPublishing/Software-Architecture-with-Cpp-2E](https://github.com/PacktPublishing/Software-Architecture-with-Cpp-2E) | reply | text~demo-strong (+3 demo/fixture) | Software Architecture with C++, Second Edition, Published by Packt |
| 63 | [qoretechnologies/qore](https://github.com/qoretechnologies/qore) | — | text~demo (+2 demo/fixture) | Qore Programming Language |
| 60 | [DataDog/serverless-sample-app](https://github.com/DataDog/serverless-sample-app) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Explore Datadog's serverless observability features with this sampl... |
| 50 | [WebFuzzing/Dataset](https://github.com/WebFuzzing/Dataset) | kafka · channel-params | topic=enterprise-applications (+3 product); topic=benchma... | Web Fuzzing Dataset (WFD): a set of web/enterprise applications for... |
| 48 | [agiopen-org/lux-desktop](https://github.com/agiopen-org/lux-desktop) | channel-params | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 47 | [icanbwell/fhir-server](https://github.com/icanbwell/fhir-server) | kafka | text~product (+2 product); text~demo (+2 demo/fixture) | Open Source FHIR Server backed by MongoDB |
| 42 | [NawafSwe/go-service-starter-kit](https://github.com/NawafSwe/go-service-starter-kit) | — | topic=microservice (+3 product); topic=template (+3 demo/... | Production-ready Golang starter kit for building HTTP APIs, gRPC se... |
| 34 | [salaboy/pizza](https://github.com/salaboy/pizza) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 26 | [inputlayer/inputlayer](https://github.com/inputlayer/inputlayer) | channel-params | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Streaming reasoning layer for AI. Incremental rules engine with vec... |
| 24 | [microcks/microcks.io](https://github.com/microcks/microcks.io) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); t... | Public website resources and templates |
| 13 | [tewhatuora/api-standards](https://github.com/tewhatuora/api-standards) | mqtt | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Health New Zealand \| Te Whatu Ora API Development and Security Sta... |
| 12 | [bpbpublications/Spring-Boot-3-API-Mastery](https://github.com/bpbpublications/Spring-Boot-3-API-Mastery) | kafka | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Spring Boot 3 API Mastery, by BPB Publications |
| 10 | [aklivity/zilla-demos](https://github.com/aklivity/zilla-demos) | reply · kafka · mqtt · channel-params | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Zilla Demos |
| 10 | [ArieGoldkin/ai-agent-hub](https://github.com/ArieGoldkin/ai-agent-hub) | kafka | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 9 | [allex-mitin/api-doc-conf](https://github.com/allex-mitin/api-doc-conf) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 9 | [Joaopdiasventura/Modularis](https://github.com/Joaopdiasventura/Modularis) | amqp | text~product (+2 product); text~demo (+2 demo/fixture); l... | A multilingual microservices ecosystem using NestJS, Spring Boot, a... |
| 7 | [DataDog/stickerlandia](https://github.com/DataDog/stickerlandia) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 6 | [specmatic/specmatic-order-contracts](https://github.com/specmatic/specmatic-order-contracts) | reply | topic=sample-project (+3 demo/fixture); text~demo-strong ... | Contracts for sample projects that use Specmatic to do contract dri... |
| 5 | [ARCircle/Kojirer](https://github.com/ARCircle/Kojirer) | — | text~demo (+2 demo/fixture); lang=HTML (+1 spec/docs) | AR会が学祭で提供するラーメン「こうじろう」の注文管理システム |
| 5 | [bicatu/event-catalog](https://github.com/bicatu/event-catalog) | — | topic=event-driven-architecture (+3 product); text~demo-s... | Event Catalog starter repository |
| 5 | [Harsh4902/kubecon-eu-2026-tutorials](https://github.com/Harsh4902/kubecon-eu-2026-tutorials) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | This repository contains tutorials of my talk at KubeCon + CloudNat... |
| 5 | [salaboy/spring-io-2026-workshop](https://github.com/salaboy/spring-io-2026-workshop) | — | text~product(weak) (+1 product); text~demo-strong (+3 dem... | Spring I/O 2026 Workshop |
| 4 | [EDALearn/EDA-Playground-Online-Food-Delivery](https://github.com/EDALearn/EDA-Playground-Online-Food-Delivery) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | SpringBoot Microservices for a "Food Delivery Service" for a AsyncA... |
| 4 | [eduardofesilva/async-eda-otel-workshop](https://github.com/eduardofesilva/async-eda-otel-workshop) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Repo that contains the files used during the Async Community Live S... |
| 3 | [EDALearn/EDA-Modulith-Playground](https://github.com/EDALearn/EDA-Modulith-Playground) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 3 | [Harmelodic/init-microservice](https://github.com/Harmelodic/init-microservice) | — | topic=kubernetes,microservice (+3 product); topic=templat... | How I build microservices (in Java). |
| 3 | [jimfil/raspberryPiProject](https://github.com/jimfil/raspberryPiProject) | mqtt · channel-params | text~demo (+2 demo/fixture) |  |
| 3 | [nemirlev/async-api-example](https://github.com/nemirlev/async-api-example) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | A demo project to get acquainted with AsyncAPI using the example of... |
| 3 | [Redocly/apidocs-starter](https://github.com/Redocly/apidocs-starter) | — | topic=example-project (+3 demo/fixture); topic=docs,docum... | Starter template for Redoc API reference docs projects |
| 3 | [ZenWave360/zenwave-playground](https://github.com/ZenWave360/zenwave-playground) | — | text~tool (+2 tooling/library); text~demo-strong (+3 demo... |  |
| 2 | [AlbertKellner/ClaudeDotNetPlayground](https://github.com/AlbertKellner/ClaudeDotNetPlayground) | — | text~demo (+2 demo/fixture) |  |
| 2 | [factory-x-contributions/async-aas-helm](https://github.com/factory-x-contributions/async-aas-helm) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture) | A helm chart to spin up various AAS implementations and connect the... |
| 2 | [kanekoshoyu/asyncapi-rust-ws-template](https://github.com/kanekoshoyu/asyncapi-rust-ws-template) | — | topic=codegen (+3 tooling/library); topic=template (+3 de... | AsyncAPI Template for Generating Rust WebSocket Client |
| 2 | [manuschillerdev/esphome-elero](https://github.com/manuschillerdev/esphome-elero) | — | text~demo (+2 demo/fixture) | An ESPHome component to control Devices with the bidirectional Eler... |
| 2 | [ministryofjustice/hmpps-locations-inside-prison-api](https://github.com/ministryofjustice/hmpps-locations-inside-prison-api) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | HMPPS Location Inside Prison Service API |
| 2 | [nekofar/warpcast](https://github.com/nekofar/warpcast) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | TypeScript client for interacting with Warpcast APIs |
| 2 | [openshift-hyperfleet/architecture](https://github.com/openshift-hyperfleet/architecture) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 2 | [ravecat/moda](https://github.com/ravecat/moda) | reply · channel-params | text~demo-strong (+3 demo/fixture) | Elixir, NextJS, Typescript, CRDT, Nx, PKCE |
| 2 | [salaboy/spring-ai-agentic-webinar](https://github.com/salaboy/spring-ai-agentic-webinar) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | Spring AI Agentic Observability with MCP, Microcks, OpenTelemetry a... |
| 2 | [specmatic/studio-demo](https://github.com/specmatic/studio-demo) | reply | topic=microservices (+3 product); text~product (+2 produc... | Demo project showcasing how to use Specmatic Studio for API contrac... |
| 2 | [XaaXaaX/eventcatalog-automation](https://github.com/XaaXaaX/eventcatalog-automation) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs) |  |
| 2 | [yoshioterada/Spec-Driven-Dev](https://github.com/yoshioterada/Spec-Driven-Dev) | amqp | text~demo (+2 demo/fixture); name~spec (+1 spec/docs) | Sample |
| 1 | [adimail/rocket-landing-rl](https://github.com/adimail/rocket-landing-rl) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | reinforcement learning simulation to land a spacex rocket booster v... |
| 1 | [alexandre-touret/api-first-workshop](https://github.com/alexandre-touret/api-first-workshop) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | This workshop aims to spread API First principles and illustrate ho... |
| 1 | [allex-mitin/asyncapi-highload-conf](https://github.com/allex-mitin/asyncapi-highload-conf) | — | text~demo-strong (+3 demo/fixture); spec-only-in-fixtures... | Example for highload conf |
| 1 | [andreacomo/apicurio-registry-poc](https://github.com/andreacomo/apicurio-registry-poc) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Playground project for learning Apicurio Registry |
| 1 | [AndreiBacs/EchipaMea](https://github.com/AndreiBacs/EchipaMea) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 1 | [codebricks-tech/taskbricks](https://github.com/codebricks-tech/taskbricks) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 1 | [CruelAddict/ori](https://github.com/CruelAddict/ori) | — | text~demo (+2 demo/fixture) | TUI DB Explorer |
| 1 | [DrBlury/Event-Driven-Service-Example](https://github.com/DrBlury/Event-Driven-Service-Example) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 1 | [eclipse-uprotocol/symphony-target-example-rust](https://github.com/eclipse-uprotocol/symphony-target-example-rust) | reply | text~product (+2 product); text~demo (+2 demo/fixture); n... | Example implementation of Eclipse Symphony Target using Rust |
| 1 | [FilippoPracucci/sap-assignment-03](https://github.com/FilippoPracucci/sap-assignment-03) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 1 | [higorsnt/ansible-workshop](https://github.com/higorsnt/ansible-workshop) | — | name~demo (+2 demo/fixture); lang=HTML (+1 spec/docs) |  |
| 1 | [jimfil/smartWasteBinProject](https://github.com/jimfil/smartWasteBinProject) | mqtt · channel-params | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 1 | [manosmax/Pie](https://github.com/manosmax/Pie) | — | text~demo (+2 demo/fixture) | Advanced Programming Techniques |
| 1 | [manosmax/Smart-Waste-Bin](https://github.com/manosmax/Smart-Waste-Bin) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Final Project for Advanced Programming Techniques |
| 1 | [monghithub/serialplab](https://github.com/monghithub/serialplab) | kafka · amqp · channel-params | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Proof of concept comparing serialization formats (Protocol Buffers,... |
| 1 | [portus84/smartorder-ms](https://github.com/portus84/smartorder-ms) | — | text~product (+2 product); text~demo (+2 demo/fixture) | SmartOrder is a microservices-based reference platform built with S... |
| 1 | [raphaeldelio/springwolf-demo-spring-io-2024](https://github.com/raphaeldelio/springwolf-demo-spring-io-2024) | kafka | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 1 | [tanishy7777/Joined_Words](https://github.com/tanishy7777/Joined_Words) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | This repo adds multiplayer functionality to the Joined Words Game |
| 1 | [up1/workshop-js-testing-202507](https://github.com/up1/workshop-js-testing-202507) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Full stack testing workshop with JavaScript |
| 1 | [XaaXaaX/aws-cloudevents-eda](https://github.com/XaaXaaX/aws-cloudevents-eda) | — | text~demo-strong (+3 demo/fixture); text~spec (+2 spec/docs) |  |
| 0 | [0xFivis/agentic-mesh-arch-kit](https://github.com/0xFivis/agentic-mesh-arch-kit) | — | text~demo (+2 demo/fixture) |  |
| 0 | [244Walyson/Strada](https://github.com/244Walyson/Strada) | — | text~demo (+2 demo/fixture) |  |
| 0 | [ajgarciaparadigma/backstage-example](https://github.com/ajgarciaparadigma/backstage-example) | kafka | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | backstage-example |
| 0 | [akash-mondal/mintlify-docs](https://github.com/akash-mondal/mintlify-docs) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); la... |  |
| 0 | [aleksa1205/iots](https://github.com/aleksa1205/iots) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [Amazon-Cloud-Club-for-KWU/3th-chat-api-demo](https://github.com/Amazon-Cloud-Club-for-KWU/3th-chat-api-demo) | channel-params | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | 3기 채팅 서버 데모 |
| 0 | [ambihome-gmbh/asyncapi](https://github.com/ambihome-gmbh/asyncapi) | reply · mqtt · channel-params | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | EXPERIMENTAL. Receive and send valid asyncapi messages over MQTT. |
| 0 | [andreaseger/homelab-tools](https://github.com/andreaseger/homelab-tools) | kafka · channel-params | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [AndriyKalashnykov/dapr-dotnet-zero-to-hero-event-driven-architecture](https://github.com/AndriyKalashnykov/dapr-dotnet-zero-to-hero-event-driven-architecture) | — | text~product (+2 product); text~demo (+2 demo/fixture) | DAPR .DotNet Pizza Shop |
| 0 | [ArneVcrs/howestprime-microservice-movies](https://github.com/ArneVcrs/howestprime-microservice-movies) | amqp | text~product (+2 product); text~demo (+2 demo/fixture) | Part of the project in my 4th semester at Howest studying software ... |
| 0 | [ArneVcrs/howestprime-microservice-ticketing](https://github.com/ArneVcrs/howestprime-microservice-ticketing) | amqp | text~product (+2 product); text~demo (+2 demo/fixture) | Part of the project in my 4th semester at Howest studying software ... |
| 0 | [arravo-co/hackathon-backend](https://github.com/arravo-co/hackathon-backend) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 0 | [artur-ciocanu/presentations](https://github.com/artur-ciocanu/presentations) | reply | text~demo-strong (+3 demo/fixture); lang=HTML (+1 spec/docs) |  |
| 0 | [BenediktusG/task-manager](https://github.com/BenediktusG/task-manager) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Multi Tenant Task Manager with real-time notification |
| 0 | [Bombatomica64/42-matcha](https://github.com/Bombatomica64/42-matcha) | — | text~product (+2 product); text~demo (+2 demo/fixture); l... |  |
| 0 | [boyney123/starter-catalog](https://github.com/boyney123/starter-catalog) | — | name~demo (+2 demo/fixture); lang=MDX (+1 spec/docs) |  |
| 0 | [call-sofia/callsofia-webhooks-docs](https://github.com/call-sofia/callsofia-webhooks-docs) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); sp... |  |
| 0 | [chrislyl/apidocs-starter](https://github.com/chrislyl/apidocs-starter) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); na... | API Documentation Management |
| 0 | [christopherblaisdell/continuous-architecture-platform-poc](https://github.com/christopherblaisdell/continuous-architecture-platform-poc) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Proof of concept for a continuous architecture platform that replac... |
| 0 | [cjjohansen/eventcatalog-examples](https://github.com/cjjohansen/eventcatalog-examples) | — | name~demo (+2 demo/fixture); lang=MDX (+1 spec/docs) |  |
| 0 | [CJovan02/iots](https://github.com/CJovan02/iots) | mqtt | text~product (+2 product); text~demo (+2 demo/fixture) | Group of projects from subject "Internet of things and Services" |
| 0 | [clecioantao/platform-state-repo](https://github.com/clecioantao/platform-state-repo) | mqtt · channel-params | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [DafeCpp/product_dev_course](https://github.com/DafeCpp/product_dev_course) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [daniellmorris/spechero](https://github.com/daniellmorris/spechero) | amqp | text~demo (+2 demo/fixture); text~spec (+2 spec/docs) | A Specification first starter monorepo project for AsyncAPI + OpenAPI |
| 0 | [dataGriff/outcome-app-pattern](https://github.com/dataGriff/outcome-app-pattern) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Repo for app - event - data product pattern |
| 0 | [eduardotourinho/candlesticks-hexagonal-architecture](https://github.com/eduardotourinho/candlesticks-hexagonal-architecture) | channel-params | text~product(weak) (+1 product); text~demo-strong (+3 dem... |  |
| 0 | [Emiltzav/asyncapi-iot-examples](https://github.com/Emiltzav/asyncapi-iot-examples) | kafka · mqtt · channel-params | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | A catalog of AsyncAPI 3.0 descriptions for asynchronous APIs of IoT... |
| 0 | [eoap/event-driven-with-argo](https://github.com/eoap/event-driven-with-argo) | kafka | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Sentinel-2 Water Bodies Detection with Argo Events and Calrissian |
| 0 | [fern-api/docs-examples](https://github.com/fern-api/docs-examples) | channel-params | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | Fern docs examples |
| 0 | [fern-demo/postman-quickstart](https://github.com/fern-demo/postman-quickstart) | channel-params | text~tool (+2 tooling/library); text~demo-strong (+3 demo... |  |
| 0 | [fern-support/universal-shuttle-348791](https://github.com/fern-support/universal-shuttle-348791) | — | text~tool (+2 tooling/library); text~demo-strong (+3 demo... | Documentation for universal-shuttle-348791 |
| 0 | [Forsakringskassan/rimfrost-service-oul-asyncapi](https://github.com/Forsakringskassan/rimfrost-service-oul-asyncapi) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... |  |
| 0 | [Forsakringskassan/template-asyncapi](https://github.com/Forsakringskassan/template-asyncapi) | reply | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [frankkilcommins/arazzo-examples](https://github.com/frankkilcommins/arazzo-examples) | mqtt · amqp · channel-params | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | Examples of Arazzo workflows spanning OpenAPI and AsyncAPI |
| 0 | [Freundschaft-ist-Magie/M241_Team0](https://github.com/Freundschaft-ist-Magie/M241_Team0) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [gematik/zeta-testfachdienst](https://github.com/gematik/zeta-testfachdienst) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Lightweight test service used in ZETA/PEP integration scenarios |
| 0 | [gpdeoli/revit-api](https://github.com/gpdeoli/revit-api) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... | API do ecossistema Revit, Trabalho de Conclusão de Curso para o IFS... |
| 0 | [huynguyengl99/chanx-fastapi-tutorial](https://github.com/huynguyengl99/chanx-fastapi-tutorial) | reply · channel-params | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [HyPolDev/Bot](https://github.com/HyPolDev/Bot) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [Ihor-Mykytiuk/software-architecture](https://github.com/Ihor-Mykytiuk/software-architecture) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [ImadSai/asyncAPI-POC](https://github.com/ImadSai/asyncAPI-POC) | mqtt | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [indiealexh/quarkus-json-rpc-ws-next-example](https://github.com/indiealexh/quarkus-json-rpc-ws-next-example) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | An example implementation of JsonRPC 2.0 using Quarkus Websocket Next |
| 0 | [izertis/spring-boot-kotlin-playground](https://github.com/izertis/spring-boot-kotlin-playground) | — | text~product(weak) (+1 product); text~demo-strong (+3 dem... |  |
| 0 | [J0SAL/kafka-playground](https://github.com/J0SAL/kafka-playground) | — | name~demo (+2 demo/fixture) |  |
| 0 | [jamescarr/async-api-demo](https://github.com/jamescarr/async-api-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | Demo of using async api spec |
| 0 | [jamescarr/jetstream-messaging](https://github.com/jamescarr/jetstream-messaging) | — | text~product(weak) (+1 product); text~demo-strong (+3 dem... | Little demo project exploring nats jestream for messaging |
| 0 | [jhekasoft/e-backend](https://github.com/jhekasoft/e-backend) | — | text~product (+2 product); text~demo (+2 demo/fixture) | e-backend is a backend for all the projects |
| 0 | [jijingkun-commits/fastapi](https://github.com/jijingkun-commits/fastapi) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | ai agent |
| 0 | [johnmarios/advanced-programming-techniques-lab](https://github.com/johnmarios/advanced-programming-techniques-lab) | mqtt · channel-params | name~demo (+2 demo/fixture) |  |
| 0 | [jonathan-prout/tic-tac-toe](https://github.com/jonathan-prout/tic-tac-toe) | channel-params | text~tool (+2 tooling/library); text~demo-strong (+3 demo... | Demo project for websocket and rest api |
| 0 | [jonathaneichenhofer/workshop-eric](https://github.com/jonathaneichenhofer/workshop-eric) | — | name~demo (+2 demo/fixture) |  |
| 0 | [justynroberts/emea-backstage-demo](https://github.com/justynroberts/emea-backstage-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | PagerDuty EMEA Developer Portal - Backstage demo with PagerDuty, Ru... |
| 0 | [juvi07/bs-templates](https://github.com/juvi07/bs-templates) | mqtt · channel-params | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | A collection of remotely available Backstage example templates |
| 0 | [kondoumh/asyncapi-study](https://github.com/kondoumh/asyncapi-study) | kafka | text~tool (+2 tooling/library); text~demo-strong (+3 demo... |  |
| 0 | [Kuestenlogik/Bowire.Samples](https://github.com/Kuestenlogik/Bowire.Samples) | mqtt · channel-params | topic=demo,examples (+3 demo/fixture); text~product (+2 p... | Reference sample apps for Bowire — one per protocol (REST, gRPC, Gr... |
| 0 | [Leandroyyy/async-api-example](https://github.com/Leandroyyy/async-api-example) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... | Examples for async api |
| 0 | [LucasKonrath/arch-kata-mr-bill](https://github.com/LucasKonrath/arch-kata-mr-bill) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... |  |
| 0 | [lufyxz7/xpogo](https://github.com/lufyxz7/xpogo) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Backend Detail : https://xpogo-backend.vercel.app |
| 0 | [Malcolmston/dta-final](https://github.com/Malcolmston/dta-final) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [marle3003/mokapi-kafka-workflow](https://github.com/marle3003/mokapi-kafka-workflow) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | This repository demonstrates how to build and test Kafka workflows ... |
| 0 | [MatiasNAmendola/real-time-risk-lab](https://github.com/MatiasNAmendola/real-time-risk-lab) | kafka | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | No es producto real, es una exploración técnica seria sobre decisio... |
| 0 | [Matse-DD/HowestPrime-microservice-movies](https://github.com/Matse-DD/HowestPrime-microservice-movies) | amqp | text~demo-strong (+3 demo/fixture) | This is part of a school project I have completed in my 2nd year in... |
| 0 | [Matse-DD/HowestPrime-microservice-ticketing](https://github.com/Matse-DD/HowestPrime-microservice-ticketing) | amqp | text~demo-strong (+3 demo/fixture) | This is part of a school project I have completed in my 2nd year in... |
| 0 | [medmo/backstage-templates](https://github.com/medmo/backstage-templates) | — | name~demo (+2 demo/fixture); lang=None (+1 spec/docs) |  |
| 0 | [mmussett/flogo-hello-world-event-driven](https://github.com/mmussett/flogo-hello-world-event-driven) | — | text~demo (+2 demo/fixture); lang=None (+1 spec/docs) | Developer Hub Event Driven Architecture PoC |
| 0 | [nashspence/pyspec](https://github.com/nashspence/pyspec) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... |  |
| 0 | [nba-amtgroup/4424rr-2](https://github.com/nba-amtgroup/4424rr-2) | mqtt | text~demo (+2 demo/fixture) | trackbot2  |
| 0 | [Netcracker/qubership-apihub-test-service](https://github.com/Netcracker/qubership-apihub-test-service) | amqp · channel-params | text~product (+2 product); text~demo (+2 demo/fixture); t... |  |
| 0 | [niteesh-reddy91/cloudevents-kafka-demo](https://github.com/niteesh-reddy91/cloudevents-kafka-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) |  |
| 0 | [nivreddy14/event-mesh](https://github.com/nivreddy14/event-mesh) | kafka | text~demo (+2 demo/fixture) |  |
| 0 | [noeliajimenezg/mokapi_issue](https://github.com/noeliajimenezg/mokapi_issue) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) | Reproducing an issue with mokapi and KafkaListener |
| 0 | [ONSdigital/dp-search-data-importer](https://github.com/ONSdigital/dp-search-data-importer) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Service to store searchable content into elasticsearch |
| 0 | [Or3nges/howestprime-microservice-movies](https://github.com/Or3nges/howestprime-microservice-movies) | amqp | text~demo-strong (+3 demo/fixture) | This is part of a school project I have completed in my 2nd year in... |
| 0 | [Or3nges/howestprime-microservice-ticketing](https://github.com/Or3nges/howestprime-microservice-ticketing) | amqp | text~product (+2 product); text~demo-strong (+3 demo/fixt... | This is part of a school project I have completed in my 2nd year in... |
| 0 | [pingxin403/platform-console](https://github.com/pingxin403/platform-console) | channel-params | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Personal learning project: Backstage IDP reference implementation. ... |
| 0 | [pmdartus/mintlify-docs](https://github.com/pmdartus/mintlify-docs) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); la... | Test Mintlify documentation |
| 0 | [pokerjocke70/cds-poc](https://github.com/pokerjocke70/cds-poc) | — | name~demo (+2 demo/fixture) | Testing spring cds |
| 0 | [quenbyako/asyncapi-example](https://github.com/quenbyako/asyncapi-example) | kafka | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [rafaelgpimenta/go-base-project](https://github.com/rafaelgpimenta/go-base-project) | kafka | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [rajeshrsinha/template](https://github.com/rajeshrsinha/template) | mqtt · channel-params | name~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... |  |
| 0 | [Ravip2006/Demo](https://github.com/Ravip2006/Demo) | reply | text~demo-strong (+3 demo/fixture); name~demo (+2 demo/fi... |  |
| 0 | [sap-2025-2026/lab-activity-10](https://github.com/sap-2025-2026/lab-activity-10) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture); n... | Lab Activity #10 - 20251128 |
| 0 | [sarkr72/practice](https://github.com/sarkr72/practice) | kafka | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [ScrKiddie/AtoiTalkAPI](https://github.com/ScrKiddie/AtoiTalkAPI) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | RESTful API for real-time chat applications with WebSocket events, ... |
| 0 | [ShuVeriDa/distahilar-back](https://github.com/ShuVeriDa/distahilar-back) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 0 | [sillygod/scaffold](https://github.com/sillygod/scaffold) | reply | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [socrateasehq/autoproctor-mintlify-docs](https://github.com/socrateasehq/autoproctor-mintlify-docs) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); la... |  |
| 0 | [spbu-ds-practicum-2025/example-project](https://github.com/spbu-ds-practicum-2025/example-project) | amqp | name~demo (+2 demo/fixture) | Пример проекта |
| 0 | [specmatic/enterprise-sample](https://github.com/specmatic/enterprise-sample) | reply | topic=sample-project (+3 demo/fixture); text~product(weak... | Sample project to understand how to use Specmatic Enterprise |
| 0 | [specmatic/labs](https://github.com/specmatic/labs) | reply | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Contains all the Labs used during the Specmatic hands-on Workshop |
| 0 | [specmatic/labs-contracts](https://github.com/specmatic/labs-contracts) | reply · kafka | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Central Contracts Repo for projects inside Labs |
| 0 | [specmatic/specmatic-async-sample](https://github.com/specmatic/specmatic-async-sample) | reply | topic=sample-project (+3 demo/fixture); text~demo-strong ... | Sample project to demonstrate how specmatic-async can contract test... |
| 0 | [specmatic/specmatic-kafka-avro-sample](https://github.com/specmatic/specmatic-kafka-avro-sample) | reply · kafka | topic=sample-project (+3 demo/fixture); text~product (+2 ... | Sample project to demonstrate how specmatic-kafka can be used to ru... |
| 0 | [specmatic/specmatic-kafka-sample-asyncapi3](https://github.com/specmatic/specmatic-kafka-sample-asyncapi3) | reply · kafka | topic=sample-project (+3 demo/fixture); text~product(weak... | Specmatic Kafka Sample AsyncAPI 3.0.0 |
| 0 | [specmatic/specmatic-studio-playwright-ts-tests](https://github.com/specmatic/specmatic-studio-playwright-ts-tests) | reply | text~demo (+2 demo/fixture); name~tool (+1 tooling/library) | Automated tests for Specmatic Studio |
| 0 | [taonaben/grupus-frontend](https://github.com/taonaben/grupus-frontend) | channel-params | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [tassosgomes/poc-event-system](https://github.com/tassosgomes/poc-event-system) | amqp | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Repositório para POC de ferramentas como Springwolf, Neuroglia.Asyn... |
| 0 | [timnavigate/DAC](https://github.com/timnavigate/DAC) | — | text~demo (+2 demo/fixture) | docs as code |
| 0 | [timonback/springwolf-demo](https://github.com/timonback/springwolf-demo) | kafka | text~product(weak) (+1 product); text~demo-strong (+3 dem... |  |
| 0 | [tomascejka/microcks.labs](https://github.com/tomascejka/microcks.labs) | — | name~demo (+2 demo/fixture); lang=None (+1 spec/docs) | All about Microcks  |
| 0 | [TykTechnologies/exp](https://github.com/TykTechnologies/exp) | — | text~demo (+2 demo/fixture) | This repository holds experimental and deprecated tooling |
| 0 | [up1/workshop-asyncapi-services-2025](https://github.com/up1/workshop-asyncapi-services-2025) | kafka | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [up1/workshop-event-based-golang](https://github.com/up1/workshop-event-based-golang) | — | name~demo (+2 demo/fixture) |  |
| 0 | [Vellum-IO/keeper-api-contracts](https://github.com/Vellum-IO/keeper-api-contracts) | channel-params | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | The openAPI contracts for back and frontends. |
| 0 | [WebSecDetectives/fluffy-plushies-webshop](https://github.com/WebSecDetectives/fluffy-plushies-webshop) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [yourbourse/trade-server-trading-view-js](https://github.com/yourbourse/trade-server-trading-view-js) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Public Repository for Trading View integration with Trade Server |
| 0 | [zachariep/spring-petclinic-saga-refactor](https://github.com/zachariep/spring-petclinic-saga-refactor) | channel-params | text~product (+2 product); text~demo (+2 demo/fixture) | Refactoring of Spring Petclinic Microservices to implement the Saga... |
| 0 | [zuevrs/yanote](https://github.com/zuevrs/yanote) | reply · kafka · mqtt · amqp | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... |  |

## spec/docs (57)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 5781 | [cloudevents/spec](https://github.com/cloudevents/spec) | — | topic=serverless (+3 product); topic=specification (+3 sp... | CloudEvents Specification |
| 5205 | [asyncapi/spec](https://github.com/asyncapi/spec) | — | topic=specification (+3 spec/docs); text~product(weak) (+... | The AsyncAPI specification allows you to create machine-readable de... |
| 708 | [asyncapi/website](https://github.com/asyncapi/website) | reply · kafka · amqp · channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | AsyncAPI specification website |
| 439 | [OAI/Arazzo-Specification](https://github.com/OAI/Arazzo-Specification) | reply | topic=arazzo-specification (+3 spec/docs); text~spec (+2 ... | The Arazzo Specification - A Tapestry for Deterministic API Workflows |
| 375 | [DocHubTeam/DocHub](https://github.com/DocHubTeam/DocHub) | mqtt | topic=architecture-as-code,architecture-as-code-dsl,archi... | Управление архитектурой как кодом |
| 116 | [RobinTail/zod-sockets](https://github.com/RobinTail/zod-sockets) | reply | topic=server (+3 product); topic=asyncapi-specification (... | Socket.IO solution with I/O validation and the ability to generate ... |
| 92 | [DeepLcom/openapi](https://github.com/DeepLcom/openapi) | channel-params | text~spec (+2 spec/docs); spec-at-root/docs (+1 product);... | OpenAPI specification of the DeepL API |
| 74 | [asyncapi/spec-json-schemas](https://github.com/asyncapi/spec-json-schemas) | — | text~spec (+2 spec/docs); name~spec (+1 spec/docs); spec-... | AsyncAPI schema versions |
| 69 | [opengeospatial/ogcapi-environmental-data-retrieval](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval) | mqtt | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | A Web API that provides a family of lightweight interfaces for acce... |
| 51 | [intent-driven-dev/openspec-schemas](https://github.com/intent-driven-dev/openspec-schemas) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); la... | Collection of OpenSpec Custom Schema for Workflows other than stand... |
| 50 | [otto-de/api-guidelines](https://github.com/otto-de/api-guidelines) | kafka | topic=guidelines (+3 spec/docs); text~spec (+2 spec/docs)... | A set of rules to build consistent and high quality REST and Async ... |
| 39 | [fern-api/docs-starter](https://github.com/fern-api/docs-starter) | channel-params | topic=openapi-documentation,swagger-documentation (+3 spe... | Publish beautiful documentation from OpenAPI and markdown (MDX) |
| 33 | [Kong/spec-renderer](https://github.com/Kong/spec-renderer) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A lightweight, pluggable spec renderer built by Kong. Designed to p... |
| 20 | [heikkilamarko/todo-app](https://github.com/heikkilamarko/todo-app) | — | topic=json-schema (+3 spec/docs); text~product(weak) (+1 ... | Todo App |
| 16 | [pardeike/GABP](https://github.com/pardeike/GABP) | channel-params | text~spec (+2 spec/docs); spec-at-root/docs (+1 product) | Game Agent Bridge Protocol |
| 13 | [ByteBardOrg/AsyncAPI.NET](https://github.com/ByteBardOrg/AsyncAPI.NET) | — | topic=asyncapi-schemas,asyncapi-specification,avro-schema... | The official continuation of LEGO.AsyncAPI.NET from the original au... |
| 12 | [asyncapi/tck](https://github.com/asyncapi/tck) | — | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | (WIP) Test Compatibility Suite for AsyncAPI |
| 11 | [bdragon300/go-asyncapi](https://github.com/bdragon300/go-asyncapi) | — | topic=schema-first (+3 spec/docs); text~tool (+2 tooling/... | AsyncAPI tool: codegen, no-code CLI app, server definitions, diagra... |
| 9 | [asynq-io/pydantic-asyncapi](https://github.com/asynq-io/pydantic-asyncapi) | mqtt · channel-params | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | Pydantic models for AsyncAPI schema |
| 9 | [DeepLcom/api-docs](https://github.com/DeepLcom/api-docs) | channel-params | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Source code of the DeepL API documentation |
| 9 | [gematik/api-ehcl](https://github.com/gematik/api-ehcl) | — | topic=specification (+3 spec/docs); text~spec (+2 spec/do... | This repository contains interface definitions as accompanying spec... |
| 8 | [microcks/microcks.github.io](https://github.com/microcks/microcks.github.io) | channel-params | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Public website for Microcks |
| 6 | [fishaudio/docs](https://github.com/fishaudio/docs) | — | topic=docs (+3 spec/docs); topic=sdk (+3 tooling/library)... | Official documentation for products, services, and projects by Fish... |
| 5 | [speechmatics/docs](https://github.com/speechmatics/docs) | channel-params | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Documentation site for Speechmatics APIs and products |
| 4 | [gladiaio/docs](https://github.com/gladiaio/docs) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 4 | [openfoodfacts/documentation](https://github.com/openfoodfacts/documentation) | — | topic=openapi-spec (+3 spec/docs); text~product (+2 produ... | OpenFoodFacts Documentation provides up-to-date API docs, generated... |
| 3 | [dghilardi/asyncapiv3](https://github.com/dghilardi/asyncapiv3) | — | text~spec (+2 spec/docs) |  |
| 3 | [specmatic/docs.specmatic.io](https://github.com/specmatic/docs.specmatic.io) | reply | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | The specmatic documentation website |
| 2 | [Reya-Labs/reya-api-specs](https://github.com/Reya-Labs/reya-api-specs) | reply · channel-params | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 1 | [babelforce/rtvbp-spec](https://github.com/babelforce/rtvbp-spec) | reply | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... | Realtime Voice-Bridge Protocol |
| 1 | [Echo-Chat-Systems/docs](https://github.com/Echo-Chat-Systems/docs) | — | text~spec (+2 spec/docs); name~spec (+1 spec/docs) | Documentation for Echo-Chat |
| 1 | [InkbridgeNetworks/SubMan-API-schema](https://github.com/InkbridgeNetworks/SubMan-API-schema) | channel-params | text~spec (+2 spec/docs) | The Network RADIUS standard subscriber API |
| 1 | [ministryofjustice/curious-API](https://github.com/ministryofjustice/curious-API) | — | text~spec (+2 spec/docs) | Placeholder repository for Curious - a 3rd party supplied system fo... |
| 1 | [pagopa/pn-lab-docs](https://github.com/pagopa/pn-lab-docs) | — | text~spec (+2 spec/docs); name~demo (+2 demo/fixture); na... | An experiment repo to share documentation |
| 1 | [Rycen7822/ExAP](https://github.com/Rycen7822/ExAP) | — | text~spec (+2 spec/docs) | External Awareness Protocol: a verifiable attention contract for ex... |
| 1 | [Wavix/wavix-openapi](https://github.com/Wavix/wavix-openapi) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | OpenAPI specification for the Wavix API  |
| 1 | [whitebit-exchange/docs](https://github.com/whitebit-exchange/docs) | channel-params | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Official documentation for WhiteBIT APIs |
| 0 | [alliander-opensource/lsis-api-specs](https://github.com/alliander-opensource/lsis-api-specs) | amqp · channel-params | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | This repository provides the API specs for LSIS |
| 0 | [belgif/openapi-cloudevents](https://github.com/belgif/openapi-cloudevents) | — | topic=standard (+3 spec/docs); spec-only-in-fixtures (+1 ... | OpenAPI definitions for CloudEvents |
| 0 | [cedalo/documentation-staging](https://github.com/cedalo/documentation-staging) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... |  |
| 0 | [cedalo/streamsheets-documentation](https://github.com/cedalo/streamsheets-documentation) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... | Streamsheets documentation |
| 0 | [coinpaprika/coinpaprika-docs](https://github.com/coinpaprika/coinpaprika-docs) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 0 | [CryptoSmartNow/bizmarket-docs](https://github.com/CryptoSmartNow/bizmarket-docs) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | BizFi Docs |
| 0 | [eclipse-canought/can-translator](https://github.com/eclipse-canought/can-translator) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | can-translator |
| 0 | [eyw520/inspirited-docs](https://github.com/eyw520/inspirited-docs) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Public documentation for the `inspirited` platform. |
| 0 | [FAForever/faf-api-specs](https://github.com/FAForever/faf-api-specs) | — | topic=docs (+3 spec/docs); text~product(weak) (+1 product... | API first-specs for FAForever |
| 0 | [jambonz/jambonz-fern-config](https://github.com/jambonz/jambonz-fern-config) | — | topic=developer-documentation (+3 spec/docs); text~tool (... | The Fern Configuration for generating jambonz's Developer Documenta... |
| 0 | [KibbeWater/wfm-openapi](https://github.com/KibbeWater/wfm-openapi) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product) |  |
| 0 | [Koh0920/webapp_specs](https://github.com/Koh0920/webapp_specs) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) |  |
| 0 | [Leandroyyy/async-api-translator](https://github.com/Leandroyyy/async-api-translator) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product);... | Translator for async api specification |
| 0 | [maciekpapiez/redocly-1](https://github.com/maciekpapiez/redocly-1) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); la... |  |
| 0 | [quub-fi/quub-exchange-docs](https://github.com/quub-fi/quub-exchange-docs) | channel-params | text~product (+2 product); text~spec (+2 spec/docs); name... | Quub Exchange Platform Documentation |
| 0 | [r--w/documentation](https://github.com/r--w/documentation) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 0 | [Scott-HW-OU/shw-616172](https://github.com/Scott-HW-OU/shw-616172) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Documentation for shw-616172 |
| 0 | [smallest-inc/smallest-ai-documentation](https://github.com/smallest-inc/smallest-ai-documentation) | channel-params | topic=sdks (+3 tooling/library); topic=docs (+3 spec/docs... | Smallest AI Documentation and SDK Generation |
| 0 | [ToweringDragoon/mintlify-docs](https://github.com/ToweringDragoon/mintlify-docs) | amqp · channel-params | name~spec (+1 spec/docs); lang=MDX (+1 spec/docs) |  |
| 0 | [wirenboard/wb-device-manager](https://github.com/wirenboard/wb-device-manager) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product) | Wiren Board modbus devices manager |

## catalog (48)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 1 | [api-evangelist/api-pulse](https://github.com/api-evangelist/api-pulse) | — | apis.json API-profile catalog (excluded) | API Pulse is a comprehensive survey and benchmarking platform creat... |
| 1 | [api-evangelist/assemblyai](https://github.com/api-evangelist/assemblyai) | — | apis.json API-profile catalog (excluded) | Built by AI experts, AssemblyAI's Speech AI models include accurate... |
| 1 | [api-evangelist/deepl](https://github.com/api-evangelist/deepl) | — | apis.json API-profile catalog (excluded) | DeepL is an AI-powered translation service that delivers high-quali... |
| 1 | [api-evangelist/shodan](https://github.com/api-evangelist/shodan) | — | apis.json API-profile catalog (excluded) | Shodan is the world's first search engine for Internet-connected de... |
| 0 | [api-evangelist/ably](https://github.com/api-evangelist/ably) | — | apis.json API-profile catalog (excluded) | Realtime messaging and WebSocket platform. |
| 0 | [api-evangelist/amazon-api-gateway](https://github.com/api-evangelist/amazon-api-gateway) | — | apis.json API-profile catalog (excluded) | Amazon API Gateway is a fully managed service that makes it easy fo... |
| 0 | [api-evangelist/amazon-kinesis](https://github.com/api-evangelist/amazon-kinesis) | — | apis.json API-profile catalog (excluded) | Amazon Kinesis makes it easy to collect, process, and analyze real-... |
| 0 | [api-evangelist/amazon-sqs](https://github.com/api-evangelist/amazon-sqs) | — | apis.json API-profile catalog (excluded) | Amazon Simple Queue Service (SQS) is a fully managed message queuin... |
| 0 | [api-evangelist/amqp](https://github.com/api-evangelist/amqp) | — | apis.json API-profile catalog (excluded) | AMQP (Advanced Message Queuing Protocol) is an open standard for me... |
| 0 | [api-evangelist/async-apis](https://github.com/api-evangelist/async-apis) | — | apis.json API-profile catalog (excluded) | An index and topic collection covering AsyncAPI — the open specific... |
| 0 | [api-evangelist/asyncapi](https://github.com/api-evangelist/asyncapi) | — | apis.json API-profile catalog (excluded) | AsyncAPI is a Linux Foundation project that improves the state of e... |
| 0 | [api-evangelist/athena-health](https://github.com/api-evangelist/athena-health) | — | apis.json API-profile catalog (excluded) | athenahealth is a cloud-based electronic health record (EHR), reven... |
| 0 | [api-evangelist/backstage](https://github.com/api-evangelist/backstage) | — | apis.json API-profile catalog (excluded) | Backstage is an open-source developer portal platform created by Sp... |
| 0 | [api-evangelist/clickhouse](https://github.com/api-evangelist/clickhouse) | — | apis.json API-profile catalog (excluded) | ClickHouse is a fast open-source column-oriented database managemen... |
| 0 | [api-evangelist/coingecko](https://github.com/api-evangelist/coingecko) | — | apis.json API-profile catalog (excluded) | CoinGecko is a cryptocurrency data aggregator providing market data... |
| 0 | [api-evangelist/confluence](https://github.com/api-evangelist/confluence) | — | apis.json API-profile catalog (excluded) | APIs for Atlassian Confluence - team collaboration and knowledge ma... |
| 0 | [api-evangelist/crewai-cloud](https://github.com/api-evangelist/crewai-cloud) | — | apis.json API-profile catalog (excluded) | CrewAI Cloud (CrewAI AMP) is the managed Agent Management Platform ... |
| 0 | [api-evangelist/docusign](https://github.com/api-evangelist/docusign) | — | apis.json API-profile catalog (excluded) | DocuSign helps organizations connect and automate how they prepare,... |
| 0 | [api-evangelist/dynamodb](https://github.com/api-evangelist/dynamodb) | — | apis.json API-profile catalog (excluded) | A fully managed NoSQL database service that provides fast and predi... |
| 0 | [api-evangelist/eigenlayer](https://github.com/api-evangelist/eigenlayer) | — | apis.json API-profile catalog (excluded) | EigenLayer — restaking + AVS (actively validated services) |
| 0 | [api-evangelist/fieldwire](https://github.com/api-evangelist/fieldwire) | — | apis.json API-profile catalog (excluded) | Fieldwire — construction field management software (Hilti subsidiary) |
| 0 | [api-evangelist/filevine](https://github.com/api-evangelist/filevine) | — | apis.json API-profile catalog (excluded) | API Evangelist profile of Filevine — legal case management and oper... |
| 0 | [api-evangelist/interface-research](https://github.com/api-evangelist/interface-research) | — | apis.json API-profile catalog (excluded) | Interface Research explores the overlap across multiple interface s... |
| 0 | [api-evangelist/intuit](https://github.com/api-evangelist/intuit) | — | apis.json API-profile catalog (excluded) | Collection of APIs offered by Intuit for financial and business man... |
| 0 | [api-evangelist/jito](https://github.com/api-evangelist/jito) | — | apis.json API-profile catalog (excluded) | Jito Labs — Solana MEV infrastructure: Jito-Solana validator client... |
| 0 | [api-evangelist/lever-co](https://github.com/api-evangelist/lever-co) | — | apis.json API-profile catalog (excluded) | The Lever Data API exposes the full recruiting workflow — Opportuni... |
| 0 | [api-evangelist/mercado-pago](https://github.com/api-evangelist/mercado-pago) | — | apis.json API-profile catalog (excluded) | Mercado Pago is the payments and financial-services arm of Mercado ... |
| 0 | [api-evangelist/microsoft-outlook](https://github.com/api-evangelist/microsoft-outlook) | — | apis.json API-profile catalog (excluded) | Microsoft Outlook is a personal information manager and email clien... |
| 0 | [api-evangelist/nats](https://github.com/api-evangelist/nats) | — | apis.json API-profile catalog (excluded) | A high-performance, cloud-native messaging system for microservices... |
| 0 | [api-evangelist/oddsjam](https://github.com/api-evangelist/oddsjam) | — | apis.json API-profile catalog (excluded) | OddsJam's Sports Betting API offers real-time betting odds from 100... |
| 0 | [api-evangelist/olo](https://github.com/api-evangelist/olo) | — | apis.json API-profile catalog (excluded) | Olo is a leading on-demand commerce platform powering the digital e... |
| 0 | [api-evangelist/phonely](https://github.com/api-evangelist/phonely) | — | apis.json API-profile catalog (excluded) | Phonely - AI voice agent platform for business phone calls (real-ti... |
| 0 | [api-evangelist/pinnacle](https://github.com/api-evangelist/pinnacle) | — | apis.json API-profile catalog (excluded) | Pinnacle is an online gaming website that was founded in 1998. Sinc... |
| 0 | [api-evangelist/plivo](https://github.com/api-evangelist/plivo) | — | apis.json API-profile catalog (excluded) | Cloud communications platform: voice and messaging APIs. |
| 0 | [api-evangelist/polygon](https://github.com/api-evangelist/polygon) | — | apis.json API-profile catalog (excluded) | Historical stock market data |
| 0 | [api-evangelist/pubnub](https://github.com/api-evangelist/pubnub) | — | apis.json API-profile catalog (excluded) | Realtime communication and IoT messaging platform. |
| 0 | [api-evangelist/regal-ai](https://github.com/api-evangelist/regal-ai) | — | apis.json API-profile catalog (excluded) | Regal AI - outbound AI phone agents and contact center platform |
| 0 | [api-evangelist/roku](https://github.com/api-evangelist/roku) | — | apis.json API-profile catalog (excluded) | Roku is the leading TV streaming platform in the U.S., Canada, and ... |
| 0 | [api-evangelist/sendgrid](https://github.com/api-evangelist/sendgrid) | — | apis.json API-profile catalog (excluded) | SendGrid is a cloud-based email delivery platform that provides rel... |
| 0 | [api-evangelist/sendle](https://github.com/api-evangelist/sendle) | — | apis.json API-profile catalog (excluded) | Sendle is a 100%-carbon-neutral parcel shipping service built for s... |
| 0 | [api-evangelist/slack](https://github.com/api-evangelist/slack) | — | apis.json API-profile catalog (excluded) | Slack is a cloud-based team collaboration platform that provides ch... |
| 0 | [api-evangelist/statsd](https://github.com/api-evangelist/statsd) | — | apis.json API-profile catalog (excluded) | API and integration profile for StatsD. |
| 0 | [api-evangelist/tensor](https://github.com/api-evangelist/tensor) | — | apis.json API-profile catalog (excluded) | Tensor is the Solana-native NFT marketplace and trading protocol fo... |
| 0 | [api-evangelist/tripleseat](https://github.com/api-evangelist/tripleseat) | — | apis.json API-profile catalog (excluded) | API Evangelist provider profile for Tripleseat |
| 0 | [api-evangelist/webflux](https://github.com/api-evangelist/webflux) | — | apis.json API-profile catalog (excluded) | Spring WebFlux is a fully non-blocking, reactive-stack web framewor... |
| 0 | [api-evangelist/websockets](https://github.com/api-evangelist/websockets) | — | apis.json API-profile catalog (excluded) | WebSockets is a communication protocol providing full-duplex commun... |
| 0 | [api-evangelist/zendesk](https://github.com/api-evangelist/zendesk) | — | apis.json API-profile catalog (excluded) | Zendesk provides customer service and engagement software that help... |
| 0 | [api-evangelist/zoom](https://github.com/api-evangelist/zoom) | — | apis.json API-profile catalog (excluded) | Zoom is a communications platform that allows users to connect with... |

## tangential (15)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 371 | [ancoleman/ai-design-components](https://github.com/ancoleman/ai-design-components) | — | AI coding-skill / agent repo (excluded): claude-code,clau... | Comprehensive UI/UX and Backend component design skills for AI-assi... |
| 350 | [aiskillstore/marketplace](https://github.com/aiskillstore/marketplace) | kafka | AI coding-skill / agent repo (excluded): ai-skills,claude... | Security-audited skills for Claude, Codex & Claude Code. One-click ... |
| 183 | [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) | kafka | AI coding-skill / agent repo (excluded): claude-code,clau... | The Complete AI Development Toolkit for Claude Code — 103 skills, 3... |
| 69 | [AsiaOstrich/universal-dev-standards](https://github.com/AsiaOstrich/universal-dev-standards) | — | AI coding-skill / agent repo (excluded): claude-code | Universal, language-agnostic development standards for software pro... |
| 47 | [ComeOnOliver/skillshub](https://github.com/ComeOnOliver/skillshub) | kafka | AI coding-skill / agent repo (excluded): agent-skills | 🧠 The right skill, one API call. AI agent skills registry with toke... |
| 23 | [geekatron/jerry](https://github.com/geekatron/jerry) | — | AI coding-skill / agent repo (excluded): claude-code | A Claude Code plugin for behavior and workflow guardrails with know... |
| 19 | [jmanhype/speckit](https://github.com/jmanhype/speckit) | channel-params | AI coding-skill / agent repo (excluded): claude-code | Specification-Driven Development with Beads Integration - A compreh... |
| 7 | [ammario/kalshi-docs](https://github.com/ammario/kalshi-docs) | — | AI coding-skill repo (excluded): strong text marker | LLM-friendly, auto-updating markdown repository of the Kalshi API docs |
| 4 | [0xHoneyJar/loa-hounfour](https://github.com/0xHoneyJar/loa-hounfour) | — | AI coding-skill / agent repo (excluded): agent-coordinati... | a schema-only protocol library defining the wire format for service... |
| 3 | [OptimalMatch/clode](https://github.com/OptimalMatch/clode) | channel-params | text~product(weak) (+1 product); AI coding-skill/agent ma... |  |
| 2 | [joserprieto/ai-skills](https://github.com/joserprieto/ai-skills) | — | AI coding-skill repo (excluded): strong text marker | Reusable AI agent skills for Claude Code and other AI tools |
| 1 | [masermediagroup-stack/CursorSkills](https://github.com/masermediagroup-stack/CursorSkills) | — | AI coding-skill repo (excluded): strong text marker | Skills for Cursor. Used across OS and Windows platforms. |
| 1 | [MRX1205/AIflow](https://github.com/MRX1205/AIflow) | — | AI coding-skill/agent markers in text (excluded) |  |
| 0 | [aidansunbury/docs-agent](https://github.com/aidansunbury/docs-agent) | channel-params | name~spec (+1 spec/docs); AI coding-skill/agent markers i... | docs agent for searching codebases |
| 0 | [resultakak/argos](https://github.com/resultakak/argos) | — | AI coding-skill / agent repo (excluded): claude-code | Full-stack ve platform mühendisleri için Claude Code plugin |

## uncategorized (229)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 1870 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | — |  | CCXT for prediction markets. PMXT is a unified API for trading on P... |
| 103 | [ballerina-platform/asyncapi-triggers](https://github.com/ballerina-platform/asyncapi-triggers) | — | spec-at-root/docs (+1 product) | This repo will contain the trigger source code generated through ba... |
| 59 | [batterypass/BatteryPassDataModel](https://github.com/batterypass/BatteryPassDataModel) | channel-params | lang=HTML (+1 spec/docs) | Battery Passport Data Model repository from the Battery Pass Project |
| 38 | [tadelv/reaprime](https://github.com/tadelv/reaprime) | — |  | Decent.app |
| 34 | [christianrowlands/network-survey-messaging](https://github.com/christianrowlands/network-survey-messaging) | — |  | Defines the messages that are sent from the Network Survey Android App |
| 22 | [ldynia/learning-api-styles](https://github.com/ldynia/learning-api-styles) | — | text~product(weak) (+1 product) |  |
| 20 | [Open-Locker/Open-Locker](https://github.com/Open-Locker/Open-Locker) | — | spec-at-root/docs (+1 product) | This is an open source project to build both the software and the h... |
| 16 | [FinamWeb/finam-trade-api](https://github.com/FinamWeb/finam-trade-api) | — |  |  |
| 13 | [codex-k8s/kodex](https://github.com/codex-k8s/kodex) | — |  | 🧠 Your personal IT company in the cloud powered by Codex AI agents |
| 13 | [LarsArtmann/typespec-asyncapi](https://github.com/LarsArtmann/typespec-asyncapi) | — | text~product(weak) (+1 product) | [WARNING-VERY_EARLY_DEVELOPMENT] TypeSpec emitter for AsyncAPI 3.0 ... |
| 9 | [Apress/Crafting-Great-APIs-with-Domain-Driven-Design](https://github.com/Apress/Crafting-Great-APIs-with-Domain-Driven-Design) | kafka |  | Original source code for Crafting Great APIs with Domain-Driven Des... |
| 9 | [kubestellar/console-kb](https://github.com/kubestellar/console-kb) | — |  | Community knowledge base for KubeStellar Console AI missions — shar... |
| 8 | [Dometrain/zero-to-hero-event-driven-architecture](https://github.com/Dometrain/zero-to-hero-event-driven-architecture) | — |  |  |
| 7 | [flameboss/fb-api-doc](https://github.com/flameboss/fb-api-doc) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 7 | [it-incubator/nestjs](https://github.com/it-incubator/nestjs) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Examples |
| 6 | [hongmaple0820/agent-academy](https://github.com/hongmaple0820/agent-academy) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Agent Academy 是一个开源的 AI Agent 训练知识库，致力于为 AI 助手（如 OpenClaw、Claude、Ch... |
| 5 | [amosproj/amos2025ws04-robot-visual-perception](https://github.com/amosproj/amos2025ws04-robot-visual-perception) | — |  |  |
| 5 | [c2siorg/genie](https://github.com/c2siorg/genie) | — | spec-at-root/docs (+1 product) |  |
| 5 | [Grinseteddy/AiCollections](https://github.com/Grinseteddy/AiCollections) | kafka · amqp · channel-params | lang=HTML (+1 spec/docs) | Collections of AI generated API specifications |
| 3 | [bian-official/staging](https://github.com/bian-official/staging) | — | lang=None (+1 spec/docs) |  |
| 3 | [darken33/design-first-allinone](https://github.com/darken33/design-first-allinone) | kafka | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 3 | [eHealthCardLink/Spezifikation](https://github.com/eHealthCardLink/Spezifikation) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | Die vorliegende Spezifikation hat das Ziel, notwendige Ergänzungen ... |
| 3 | [IsmaelMartinez/repo-butler](https://github.com/IsmaelMartinez/repo-butler) | — | spec-at-root/docs (+1 product) | Continuous roadmap planner agent — analyses GitHub repos, maintains... |
| 3 | [ministryofjustice/hmpps-prison-offender-events](https://github.com/ministryofjustice/hmpps-prison-offender-events) | — | spec-at-root/docs (+1 product) | Publishes Events about offender change to Pub / Sub Topics |
| 3 | [pb33f/libasyncapi](https://github.com/pb33f/libasyncapi) | kafka · mqtt · channel-params |  |  |
| 3 | [ranchat-kr/ranchat-api](https://github.com/ranchat-kr/ranchat-api) | channel-params |  |  |
| 3 | [ravecat/songy](https://github.com/ravecat/songy) | reply · channel-params |  | 🎵 Feel the beats? Multiplayer music game. Challenge friends. Rank t... |
| 3 | [solace-cto-labs/solace-axway-agent](https://github.com/solace-cto-labs/solace-axway-agent) | channel-params |  | Axway-Solace-AsyncAPI Agent |
| 3 | [will-break-it/wallet-architecture](https://github.com/will-break-it/wallet-architecture) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 3 | [wirenboard/wb-mqtt-dali](https://github.com/wirenboard/wb-mqtt-dali) | — | spec-at-root/docs (+1 product) | MQTT DALI bridge for Wiren Board |
| 3 | [xavisavvy/scrum-monsters](https://github.com/xavisavvy/scrum-monsters) | — |  | Slay the beasts of bad software development and turn sprint plannin... |
| 2 | [AceTheCreator/eda-workshops](https://github.com/AceTheCreator/eda-workshops) | — |  | A repo for all the source code to my asyncapi event driven architec... |
| 2 | [aklivity/todo-service](https://github.com/aklivity/todo-service) | reply · kafka |  |  |
| 2 | [apiaddicts/sonarasyncapi-rules](https://github.com/apiaddicts/sonarasyncapi-rules) | mqtt · amqp | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | A set of rules to analize AsyncAPI documents |
| 2 | [bpbpublications/DDD-Toolbox](https://github.com/bpbpublications/DDD-Toolbox) | — | lang=None (+1 spec/docs) | DDD Toolbox, By BPB Publications |
| 2 | [cm-nishida-masayuki/odyssey-osaka-cx](https://github.com/cm-nishida-masayuki/odyssey-osaka-cx) | — | spec-at-root/docs (+1 product) |  |
| 2 | [EDI-Energy/api-directory-service](https://github.com/EDI-Energy/api-directory-service) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | API-Webdienste für die Verzeichnisdienste zum Austausch der Endpunk... |
| 2 | [Grinseteddy/MasteringDdd](https://github.com/Grinseteddy/MasteringDdd) | — |  |  |
| 2 | [kakao-tech-campus-3rd-step3/Team8_BE](https://github.com/kakao-tech-campus-3rd-step3/Team8_BE) | reply · channel-params | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | 🚀 여행 관리용 공용 플래너 |
| 2 | [lg-labs/food-ordering-system](https://github.com/lg-labs/food-ordering-system) | kafka · channel-params | text~product(weak) (+1 product) |  |
| 2 | [ODS-IS-UASL/safety-management](https://github.com/ODS-IS-UASL/safety-management) | mqtt · channel-params | text~product(weak) (+1 product) | ドローン航路システム 安全管理 |
| 2 | [romanchaa997/st-risk-platform](https://github.com/romanchaa997/st-risk-platform) | — | spec-at-root/docs (+1 product) |  |
| 2 | [RubizZ/flAIghts](https://github.com/RubizZ/flAIghts) | — |  | Aplicación web que calcula la ruta aérea optima desde un origen a u... |
| 2 | [Schreglmann/gameshow](https://github.com/Schreglmann/gameshow) | — |  |  |
| 2 | [Sejsel/ksplang-programs](https://github.com/Sejsel/ksplang-programs) | — |  | WASM implementation and Advent of Code solutions in ksplang |
| 2 | [solacecommunity/spring-cloud-stream-request-reply](https://github.com/solacecommunity/spring-cloud-stream-request-reply) | reply | spec-at-root/docs (+1 product) |  |
| 2 | [SpecterOps/SpecterOpsDocs](https://github.com/SpecterOps/SpecterOpsDocs) | amqp · channel-params | lang=MDX (+1 spec/docs) |  |
| 2 | [vsk-api/papi](https://github.com/vsk-api/papi) | — | spec-at-root/docs (+1 product) |  |
| 2 | [ZevMM/ColumbiaTradingCompetition](https://github.com/ZevMM/ColumbiaTradingCompetition) | — | text~product(weak) (+1 product) |  |
| 1 | [allex-mitin/rome-api](https://github.com/allex-mitin/rome-api) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 1 | [BackendFans83/Taxi](https://github.com/BackendFans83/Taxi) | reply · amqp | lang=None (+1 spec/docs) |  |
| 1 | [codemonstersteam/mq-rest-sync-adapter](https://github.com/codemonstersteam/mq-rest-sync-adapter) | reply · amqp |  | Пример рефакторинга по кукбуку из серии стетей для https://tproger.ru/ |
| 1 | [cryptoxdog/Enrichment.Inference.Engine](https://github.com/cryptoxdog/Enrichment.Inference.Engine) | — | spec-at-root/docs (+1 product) |  |
| 1 | [DasOxymoron/takeaway-challenge](https://github.com/DasOxymoron/takeaway-challenge) | — | text~product(weak) (+1 product) |  |
| 1 | [dduartee/sigaa-socket-api](https://github.com/dduartee/sigaa-socket-api) | reply | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | integração do modulo sigaa-api com websockets |
| 1 | [ElementAstro/lithium-next](https://github.com/ElementAstro/lithium-next) | channel-params | spec-at-root/docs (+1 product) | Next Generation of Lithium |
| 1 | [escrivivir-co/aleph-scriptorium](https://github.com/escrivivir-co/aleph-scriptorium) | mqtt · channel-params | lang=HTML (+1 spec/docs) | El objetivo: demostrar que es posible usar inteligencia artificial ... |
| 1 | [giannisgkountras/web-dsl](https://github.com/giannisgkountras/web-dsl) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 1 | [hsborges/TDSOFT-FACOM-UFMS](https://github.com/hsborges/TDSOFT-FACOM-UFMS) | — |  |  |
| 1 | [Jonas-du-bois/phenom](https://github.com/Jonas-du-bois/phenom) | — | text~product(weak) (+1 product) |  |
| 1 | [Kamuyin/schachroboter](https://github.com/Kamuyin/schachroboter) | mqtt | spec-at-root/docs (+1 product) | Seminararbeit Mechatronik - Schachroboter |
| 1 | [Karfev/Product-base-Spec-Kit](https://github.com/Karfev/Product-base-Spec-Kit) | — | name~spec (+1 spec/docs) | Build high-quality product faster. |
| 1 | [letya999/support_rag](https://github.com/letya999/support_rag) | channel-params | spec-at-root/docs (+1 product) |  |
| 1 | [MehdiMaachi/tp-xml-meteo](https://github.com/MehdiMaachi/tp-xml-meteo) | channel-params | lang=HTML (+1 spec/docs) | TP XML - Relevés de températures avec DTD, XSD, XSLT |
| 1 | [ministryofjustice/hmpps-alerts-api](https://github.com/ministryofjustice/hmpps-alerts-api) | — | spec-at-root/docs (+1 product) | HMPPS Alerts API |
| 1 | [ministryofjustice/hmpps-prisoner-search](https://github.com/ministryofjustice/hmpps-prisoner-search) | — | text~product(weak) (+1 product) | A service for searching for prisoners in NOMIS, augmented by data f... |
| 1 | [navikt/veilarboppfolging](https://github.com/navikt/veilarboppfolging) | — |  | Tjeneste som lagrer informasjon om status for arbeidsrettet oppfølg... |
| 1 | [netbarros/Production-MagicSaas-Sofia-IA-Software-Lotus](https://github.com/netbarros/Production-MagicSaas-Sofia-IA-Software-Lotus) | channel-params | spec-at-root/docs (+1 product) | Agente SaaS |
| 1 | [Order-of-Hospitallers/gru_emoney_token-factory](https://github.com/Order-of-Hospitallers/gru_emoney_token-factory) | — | spec-at-root/docs (+1 product) |  |
| 1 | [paga16-hash/anonymous-shard](https://github.com/paga16-hash/anonymous-shard) | — | spec-at-root/docs (+1 product) | Anonymous shard for master thesis at Unibo |
| 1 | [SolaceLabs/sol-ep-asyncapi-importer](https://github.com/SolaceLabs/sol-ep-asyncapi-importer) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... |  |
| 1 | [sun475300-sudo/Swarm-control-in-sc2bot](https://github.com/sun475300-sudo/Swarm-control-in-sc2bot) | kafka · amqp | spec-at-root/docs (+1 product) |  |
| 1 | [wirenboard/wb-diag-collect](https://github.com/wirenboard/wb-diag-collect) | — | spec-at-root/docs (+1 product) | Wirenboard collector of data and logs |
| 1 | [wirenboard/wb-mqtt-db](https://github.com/wirenboard/wb-mqtt-db) | — | spec-at-root/docs (+1 product) | Wiren Board database logger |
| 1 | [zon/wurbs](https://github.com/zon/wurbs) | — |  |  |
| 0 | [2025tf20/KTB-LoadTest-team-20](https://github.com/2025tf20/KTB-LoadTest-team-20) | — |  |  |
| 0 | [244Walyson/GWApp](https://github.com/244Walyson/GWApp) | — | text~product(weak) (+1 product) |  |
| 0 | [a-grasso/master-thesis-public](https://github.com/a-grasso/master-thesis-public) | — |  | Repository with resources associated with my master thesis |
| 0 | [Aarass/IOT](https://github.com/Aarass/IOT) | mqtt | lang=HTML (+1 spec/docs) | Internet of Things Project |
| 0 | [acdgbrasil/contracts](https://github.com/acdgbrasil/contracts) | — | text~product(weak) (+1 product); lang=None (+1 spec/docs) | Repositório central de contratos da organização, com especificações... |
| 0 | [AdanHdzF/event-flow](https://github.com/AdanHdzF/event-flow) | kafka · amqp |  | Bootcamp Sistemas Distribuidos - El Paradigma de Eventos con Java y... |
| 0 | [adheeshmishra/BitscrunchAssignment](https://github.com/adheeshmishra/BitscrunchAssignment) | channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [aerdman1/aerdman1.github.io](https://github.com/aerdman1/aerdman1.github.io) | reply · kafka · mqtt · channel-params | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [Alamoalone/Project-of-Desertation](https://github.com/Alamoalone/Project-of-Desertation) | — |  |  |
| 0 | [alcaann/OpenFaceWeb](https://github.com/alcaann/OpenFaceWeb) | — |  |  |
| 0 | [AlexChiquito/SAP-Maintenance-order-adaptor](https://github.com/AlexChiquito/SAP-Maintenance-order-adaptor) | — | text~product(weak) (+1 product) | SAP Adaptor system for using maintenance order interfaces from S4/HANA |
| 0 | [Andersonfrfilho/backend-websocket](https://github.com/Andersonfrfilho/backend-websocket) | — | spec-at-root/docs (+1 product) |  |
| 0 | [andre-nk/bangkit-cloud-migration-tools](https://github.com/andre-nk/bangkit-cloud-migration-tools) | — |  |  |
| 0 | [barrynauta/simpl-repo-tryout](https://github.com/barrynauta/simpl-repo-tryout) | channel-params | text~product(weak) (+1 product) | Restructuring of Simpl documentation |
| 0 | [BattMoTeam/BattMoAPI](https://github.com/BattMoTeam/BattMoAPI) | channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [Berthje/envirosense-deno-server](https://github.com/Berthje/envirosense-deno-server) | — | spec-at-root/docs (+1 product) |  |
| 0 | [bjuvensjo/backstage-slask](https://github.com/bjuvensjo/backstage-slask) | — | lang=None (+1 spec/docs) | A repository for testing Backstage discovery |
| 0 | [boyney123/my-eventcatalog](https://github.com/boyney123/my-eventcatalog) | — | lang=MDX (+1 spec/docs) | Testing features of EventCatalog (CI/CD) |
| 0 | [BrentIO/FireFly-Client](https://github.com/BrentIO/FireFly-Client) | — |  |  |
| 0 | [BrentIO/FireFly-Controller](https://github.com/BrentIO/FireFly-Controller) | — |  | Software-defined lighting controller |
| 0 | [bru-oliveirax/bark2d2-dog-feeder](https://github.com/bru-oliveirax/bark2d2-dog-feeder) | — |  | iot system for dog feeding with real-time monitoring via mobile app :) |
| 0 | [CEhresmann/Redocly-api-specificatons](https://github.com/CEhresmann/Redocly-api-specificatons) | kafka | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | API спецификации (OpenAPI/AsyncAPI) с интерактивной документацией н... |
| 0 | [CodeBeast357/webosapi-asyncapi](https://github.com/CodeBeast357/webosapi-asyncapi) | channel-params | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [codertjay/solax-audit](https://github.com/codertjay/solax-audit) | — |  |  |
| 0 | [dalsgaard/account-service-local](https://github.com/dalsgaard/account-service-local) | — | spec-at-root/docs (+1 product) |  |
| 0 | [danabrams/m](https://github.com/danabrams/m) | channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [DEFRA/ffc-pay-data-hub](https://github.com/DEFRA/ffc-pay-data-hub) | — | text~product(weak) (+1 product) | FFC payment data hub |
| 0 | [delokoseni/apigateway](https://github.com/delokoseni/apigateway) | amqp | spec-at-root/docs (+1 product) |  |
| 0 | [derchrischkya/k8s-async-api](https://github.com/derchrischkya/k8s-async-api) | reply · amqp | text~product(weak) (+1 product) |  |
| 0 | [DevFranzen/dethroned](https://github.com/DevFranzen/dethroned) | channel-params |  |  |
| 0 | [dhanisetti/Tenderlink](https://github.com/dhanisetti/Tenderlink) | — |  |  |
| 0 | [DigitalFemsa-Genesys/test-backstage-asynapi](https://github.com/DigitalFemsa-Genesys/test-backstage-asynapi) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [dlopezby93/digital-femsa-gaia](https://github.com/dlopezby93/digital-femsa-gaia) | channel-params | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [DLShomies/FluffyPlushiesWebShop](https://github.com/DLShomies/FluffyPlushiesWebShop) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [dmytmeln/eshop-microservices](https://github.com/dmytmeln/eshop-microservices) | — |  |  |
| 0 | [dnonakolesax/cccad-locks](https://github.com/dnonakolesax/cccad-locks) | reply · channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [Eclipse-SDV-Hackathon-Chapter-Three/Den-Team](https://github.com/Eclipse-SDV-Hackathon-Chapter-Three/Den-Team) | reply |  |  |
| 0 | [eda-ecommerce/shoppingBasket-service](https://github.com/eda-ecommerce/shoppingBasket-service) | — | text~product(weak) (+1 product) | A service related to the cart (Shopping Basket) aggregate |
| 0 | [edulucca/api-autenticacao](https://github.com/edulucca/api-autenticacao) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | api-autenticacao [backstage] |
| 0 | [ETI-Software-Solutions/api-specifications](https://github.com/ETI-Software-Solutions/api-specifications) | kafka | lang=None (+1 spec/docs) |  |
| 0 | [fedykvitalik2004/library-book-service](https://github.com/fedykvitalik2004/library-book-service) | — |  |  |
| 0 | [fedykvitalik2004/library-notification-service](https://github.com/fedykvitalik2004/library-notification-service) | — |  |  |
| 0 | [fedykvitalik2004/library-user-service](https://github.com/fedykvitalik2004/library-user-service) | — |  |  |
| 0 | [fernandoeqc/log_stream](https://github.com/fernandoeqc/log_stream) | reply | spec-at-root/docs (+1 product) |  |
| 0 | [floormatgen/sock-vote-2](https://github.com/floormatgen/sock-vote-2) | — |  |  |
| 0 | [fmvilas/meiac](https://github.com/fmvilas/meiac) | kafka · mqtt | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [Forsakringskassan/gradle-conventions](https://github.com/Forsakringskassan/gradle-conventions) | reply | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Shared Gradle code. |
| 0 | [Forsakringskassan/rimfrost-regel-rtf-manuell-asyncapi](https://github.com/Forsakringskassan/rimfrost-regel-rtf-manuell-asyncapi) | reply | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Async API Vård av hund - Rätt till försäkring - Manuellt uppgiftslager |
| 0 | [freaz/eventcatalog-asyncapi-order-issue](https://github.com/freaz/eventcatalog-asyncapi-order-issue) | — | lang=MDX (+1 spec/docs) |  |
| 0 | [freaz/eventcatalog-bug-reporting](https://github.com/freaz/eventcatalog-bug-reporting) | — | spec-at-root/docs (+1 product); lang=MDX (+1 spec/docs) |  |
| 0 | [fsgeek/lares](https://github.com/fsgeek/lares) | channel-params |  | Lares Project |
| 0 | [GabrielAderaldo/Merma_a_musica](https://github.com/GabrielAderaldo/Merma_a_musica) | channel-params |  |  |
| 0 | [gdg-garage/garage-trip-chores](https://github.com/gdg-garage/garage-trip-chores) | — | spec-at-root/docs (+1 product) |  |
| 0 | [giannisgkountras/ShelobDSL](https://github.com/giannisgkountras/ShelobDSL) | — | lang=None (+1 spec/docs) |  |
| 0 | [gopal45656/everest-core-release](https://github.com/gopal45656/everest-core-release) | reply · mqtt | spec-at-root/docs (+1 product) |  |
| 0 | [grace88888884/respo](https://github.com/grace88888884/respo) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [graviteeqa/testrepo](https://github.com/graviteeqa/testrepo) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [Gulvan0/IntellectorServerV2](https://github.com/Gulvan0/IntellectorServerV2) | — |  |  |
| 0 | [han243786/Quantpilot](https://github.com/han243786/Quantpilot) | — | spec-at-root/docs (+1 product) |  |
| 0 | [hbtrack/official](https://github.com/hbtrack/official) | — |  |  |
| 0 | [herostrat/arcturus](https://github.com/herostrat/arcturus) | — |  | ALPHA: A tileserver for signalk and freeboard |
| 0 | [HexRohit/cardano](https://github.com/HexRohit/cardano) | channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [hollyplankdev/emptystream-monolithic](https://github.com/hollyplankdev/emptystream-monolithic) | — |  | A quick, monolithic take on `emptystream` |
| 0 | [hongkongkiwi/yorked-docs](https://github.com/hongkongkiwi/yorked-docs) | reply · channel-params | name~spec (+1 spec/docs); spec-at-root/docs (+1 product) |  |
| 0 | [Hullow/Concord](https://github.com/Hullow/Concord) | — | text~product(weak) (+1 product) |  |
| 0 | [Instaconct/instaconct-api](https://github.com/Instaconct/instaconct-api) | — | spec-at-root/docs (+1 product) |  |
| 0 | [jlikeme/fileserver](https://github.com/jlikeme/fileserver) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [JordanNoah/sync-student-hexagonal](https://github.com/JordanNoah/sync-student-hexagonal) | amqp | spec-at-root/docs (+1 product) |  |
| 0 | [jrevillard/edulift](https://github.com/jrevillard/edulift) | — |  |  |
| 0 | [juniorcmauricio/INF332_SOA](https://github.com/juniorcmauricio/INF332_SOA) | — | lang=None (+1 spec/docs) | INF332 - Arquitetura Orientada a Serviços - SOA & WebServices: Conc... |
| 0 | [justaksi7/b2b-sap-payment-bridge](https://github.com/justaksi7/b2b-sap-payment-bridge) | — | spec-at-root/docs (+1 product) |  |
| 0 | [kakabisht/AsyncAPITemplate](https://github.com/kakabisht/AsyncAPITemplate) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [kakaoboot-19/19-load-test](https://github.com/kakaoboot-19/19-load-test) | — |  | Team 19 load test project based on BootcampChat |
| 0 | [KeertiPusarlaa/idp-platform](https://github.com/KeertiPusarlaa/idp-platform) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [KempDewulf/envirosense-deno-server](https://github.com/KempDewulf/envirosense-deno-server) | — | spec-at-root/docs (+1 product) |  |
| 0 | [KevinShabanaj386/SmartGridAnalytics](https://github.com/KevinShabanaj386/SmartGridAnalytics) | kafka | text~product(weak) (+1 product) |  |
| 0 | [Khrisseh1995/event-catalogue-test-2](https://github.com/Khrisseh1995/event-catalogue-test-2) | — |  |  |
| 0 | [ktb3-team5/ktb-BootcampChat](https://github.com/ktb3-team5/ktb-BootcampChat) | — |  |  |
| 0 | [ktbloadtest-03/ktb-BootcampChat](https://github.com/ktbloadtest-03/ktb-BootcampChat) | — |  |  |
| 0 | [lafette21/smart-gardening](https://github.com/lafette21/smart-gardening) | mqtt | spec-at-root/docs (+1 product) |  |
| 0 | [LaurenCattoor/st-microservice-movies](https://github.com/LaurenCattoor/st-microservice-movies) | amqp |  |  |
| 0 | [LeonidasGarcia/basic-chat-app](https://github.com/LeonidasGarcia/basic-chat-app) | — |  |  |
| 0 | [lihs-ie/alpha-mind](https://github.com/lihs-ie/alpha-mind) | — |  |  |
| 0 | [livestorm/frontend-engineer-hiring-test](https://github.com/livestorm/frontend-engineer-hiring-test) | — | text~product(weak) (+1 product) |  |
| 0 | [Lulexs/gis](https://github.com/Lulexs/gis) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [madebykrol/formr](https://github.com/madebykrol/formr) | — |  |  |
| 0 | [makeevolution/messaging](https://github.com/makeevolution/messaging) | — |  |  |
| 0 | [Maksim-yo/chat](https://github.com/Maksim-yo/chat) | — | spec-at-root/docs (+1 product) |  |
| 0 | [marcopaga/config_api](https://github.com/marcopaga/config_api) | channel-params | spec-at-root/docs (+1 product) | Hacking with elixir |
| 0 | [mattmeye/payara-6-ibm-queue](https://github.com/mattmeye/payara-6-ibm-queue) | reply · channel-params |  |  |
| 0 | [mcavicchiaUADE/desapps2](https://github.com/mcavicchiaUADE/desapps2) | amqp | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [medmo/ft-event-catalog](https://github.com/medmo/ft-event-catalog) | — |  |  |
| 0 | [MikeMDV/riden](https://github.com/MikeMDV/riden) | reply | spec-at-root/docs (+1 product) | A system for booking reservations for fictional boat rides |
| 0 | [mindwm/mindwm-api](https://github.com/mindwm/mindwm-api) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [mishasdk/mipt-ml-async](https://github.com/mishasdk/mipt-ml-async) | — | spec-at-root/docs (+1 product); lang=Jupyter Notebook (+1... |  |
| 0 | [mnemitz/webpack-asyncapi-schema-loader](https://github.com/mnemitz/webpack-asyncapi-schema-loader) | kafka · channel-params | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Webpack loader for parsing AsyncAPI documents |
| 0 | [mtturner57/AsyncApiGenerator](https://github.com/mtturner57/AsyncApiGenerator) | — | spec-at-root/docs (+1 product) | Geenrate models or yaml from supplied file |
| 0 | [mumia/wallet-accountant](https://github.com/mumia/wallet-accountant) | — |  | Your Accountant in you Wallet |
| 0 | [nandinimukherjeeblr/testing_dita](https://github.com/nandinimukherjeeblr/testing_dita) | channel-params | lang=None (+1 spec/docs) |  |
| 0 | [navikt/ao-oppfolgingskontor](https://github.com/navikt/ao-oppfolgingskontor) | — |  | Oppfølgingskontor for Arbeidsrettet Oppfølging |
| 0 | [navikt/dp-soknad-orkestrator](https://github.com/navikt/dp-soknad-orkestrator) | — | spec-at-root/docs (+1 product) |  |
| 0 | [nezia1/missive-documentation](https://github.com/nezia1/missive-documentation) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product) |  |
| 0 | [NHSDigital/nhs-notify-supplier-config](https://github.com/NHSDigital/nhs-notify-supplier-config) | — |  | Supplier configuration model and event schemas for NHS Notify |
| 0 | [nivoragit/authord-mkdocs](https://github.com/nivoragit/authord-mkdocs) | — |  |  |
| 0 | [Notaduck/settlers-from-catan](https://github.com/Notaduck/settlers-from-catan) | — | spec-at-root/docs (+1 product) |  |
| 0 | [notnullptr-gh/architechture-sprint-3](https://github.com/notnullptr-gh/architechture-sprint-3) | — |  |  |
| 0 | [nstsai/SAproject](https://github.com/nstsai/SAproject) | amqp |  |  |
| 0 | [ODS-IS-UASL/asset](https://github.com/ODS-IS-UASL/asset) | mqtt · channel-params | spec-at-root/docs (+1 product) |  離着陸場及び機体リソースを管理・提供する機能 |
| 0 | [pagopa/pn-paper-tracker](https://github.com/pagopa/pn-paper-tracker) | — | spec-at-root/docs (+1 product) |  |
| 0 | [parmendes/API_Doc](https://github.com/parmendes/API_Doc) | amqp |  |  |
| 0 | [parmendes/MessageBrokerExample](https://github.com/parmendes/MessageBrokerExample) | amqp | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [peguidotte/aegis-test-pubsub-interfaces](https://github.com/peguidotte/aegis-test-pubsub-interfaces) | — | spec-at-root/docs (+1 product) | Aegis Test shared interfaces for all repos |
| 0 | [peterjaberau/mock-data](https://github.com/peterjaberau/mock-data) | — |  |  |
| 0 | [picodotdev/blog-bitix](https://github.com/picodotdev/blog-bitix) | — |  | Blog sobre al lenguaje de programación Java y la distribución GNU/L... |
| 0 | [Pinit-Scheduler/pinit-auth](https://github.com/Pinit-Scheduler/pinit-auth) | amqp |  | 일정 관리/실행 서비스 Pinit의 인증 기능을 담당하는 마이크로서비스 |
| 0 | [pre-backstage/producer-repo-public](https://github.com/pre-backstage/producer-repo-public) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Validate catalog apis repository |
| 0 | [qbem-repos/standards](https://github.com/qbem-repos/standards) | — | name~spec (+1 spec/docs); spec-only-in-fixtures (+1 tooli... | Regras e guias oficiais (APIs, webhooks, async, observabilidade). |
| 0 | [RafaelAlmeida00/Plant-Simulador](https://github.com/RafaelAlmeida00/Plant-Simulador) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [RafaelAlmeida00/Simulador-UI](https://github.com/RafaelAlmeida00/Simulador-UI) | — | text~product(weak) (+1 product) |  |
| 0 | [redman2004/tinyXfixer](https://github.com/redman2004/tinyXfixer) | — |  |  |
| 0 | [roalcantara/dots](https://github.com/roalcantara/dots) | — |  | Dotfiles |
| 0 | [rock-hu/architecture-catalog](https://github.com/rock-hu/architecture-catalog) | — |  |  |
| 0 | [sanzhanggui/grandma_cook_agent](https://github.com/sanzhanggui/grandma_cook_agent) | — |  | 外婆家菜谱实现方案 |
| 0 | [seboraid/asyncapitest](https://github.com/seboraid/asyncapitest) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [sfpostman/PokemonBrightbox](https://github.com/sfpostman/PokemonBrightbox) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [Shurtu-gal/action-test-bed](https://github.com/Shurtu-gal/action-test-bed) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [siemendev/asyncapi-php](https://github.com/siemendev/asyncapi-php) | amqp | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [Souvikns/pokemon-trade-api](https://github.com/Souvikns/pokemon-trade-api) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | A socket.io API that helps users find users to trade pokemon on the... |
| 0 | [Split-Receipt/explosive-puppies-contract](https://github.com/Split-Receipt/explosive-puppies-contract) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [ssstijn/movies-backend-sem4](https://github.com/ssstijn/movies-backend-sem4) | amqp |  |  |
| 0 | [stojkovic-a/IOT-Project-2](https://github.com/stojkovic-a/IOT-Project-2) | mqtt | lang=HTML (+1 spec/docs) |  |
| 0 | [stojkovic-a/IOT-project-3](https://github.com/stojkovic-a/IOT-project-3) | mqtt | text~product(weak) (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [straylight-archive/render-api](https://github.com/straylight-archive/render-api) | channel-params | spec-at-root/docs (+1 product); lang=CSS (+1 spec/docs) | // weyl // render // api |
| 0 | [strukovsv/yclients-micro](https://github.com/strukovsv/yclients-micro) | — | spec-at-root/docs (+1 product) |  |
| 0 | [suwa-sh/lineage-to-graph](https://github.com/suwa-sh/lineage-to-graph) | — |  | Column-level Data Lineage Visualization Tools |
| 0 | [SwissDataScienceCenter/renku-schema](https://github.com/SwissDataScienceCenter/renku-schema) | — | lang=None (+1 spec/docs) | Repository for all message queue schemas |
| 0 | [Tadonkeng/project1](https://github.com/Tadonkeng/project1) | — |  |  |
| 0 | [Tafseerhussain/zillabase_portal](https://github.com/Tafseerhussain/zillabase_portal) | kafka · channel-params | text~product(weak) (+1 product) |  |
| 0 | [TahaShahid203/async-api-issue](https://github.com/TahaShahid203/async-api-issue) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [taonaben/grupus](https://github.com/taonaben/grupus) | channel-params |  |  |
| 0 | [Team-Nyong/KTB-Chat-Load-Testing](https://github.com/Team-Nyong/KTB-Chat-Load-Testing) | — |  | 카테부 부하테스트 6팀 저장소 |
| 0 | [tenacious89/open_agent_hackathon](https://github.com/tenacious89/open_agent_hackathon) | reply · channel-params |  | 性设计兼顾 “怼” 的效果和 “有趣不伤人” 的分寸的智能体 |
| 0 | [thealmikey/zilla-kt](https://github.com/thealmikey/zilla-kt) | reply · kafka · mqtt · channel-params | text~product(weak) (+1 product) | Zilla with kotlin, custom kotlin manager with custom kotlin binding... |
| 0 | [thelonggoodbuy/cryptowallet](https://github.com/thelonggoodbuy/cryptowallet) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [TristanDeLil/ms-client-backoffice](https://github.com/TristanDeLil/ms-client-backoffice) | amqp |  |  |
| 0 | [TristanDeLil/ms-microservice-movies](https://github.com/TristanDeLil/ms-microservice-movies) | amqp |  |  |
| 0 | [tudor-upt/urban-pulse-ada](https://github.com/tudor-upt/urban-pulse-ada) | amqp | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [Turisas/solaxy](https://github.com/Turisas/solaxy) | — |  |  |
| 0 | [vasilisalmpanis/ft_transcendence](https://github.com/vasilisalmpanis/ft_transcendence) | — |  |  |
| 0 | [vasudevgrg/stock_exchange](https://github.com/vasudevgrg/stock_exchange) | — | spec-at-root/docs (+1 product) |  |
| 0 | [vondacho/my-api-portal](https://github.com/vondacho/my-api-portal) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... | API developer portal with design guidelines, registration, catalog,... |
| 0 | [wirenboard/wb-mqtt-logs](https://github.com/wirenboard/wb-mqtt-logs) | — | spec-at-root/docs (+1 product) |  |
| 0 | [XplorodoX/ITS](https://github.com/XplorodoX/ITS) | mqtt · channel-params | spec-at-root/docs (+1 product) |  |
| 0 | [zikratski/LinguaConnect](https://github.com/zikratski/LinguaConnect) | — |  | Документация к LinguaConnect - сервису для разговорных клубов на ин... |
