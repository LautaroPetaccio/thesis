# AsyncAPI 3.x repository classification

Seedless, signal-scored classification of every unique repository surfaced by `asyncapi_adoption_survey.sh` for AsyncAPI 3.x. Each repo is assigned the highest-scoring bucket from GitHub topics, description, name, how it uses AsyncAPI (spec file locations), language, and homepage. See the module docstring for weights; `_scores`/`_reason` in `repo-classification.json` record the evidence per repo.

_6 of 1103 repos are archived (recorded as `isArchived`, not a bucket)._

## Bucket counts

| Bucket | Count | % of total |
|---|---:|---:|
| `product` | 294 | 26.7 % |
| `tooling/library` | 224 | 20.3 % |
| `demo/fixture` | 217 | 19.7 % |
| `spec/docs` | 55 | 5.0 % |
| `catalog` | 0 | 0.0 % |
| `tangential` | 11 | 1.0 % |
| `uncategorized` | 302 | 27.4 % |
| **total** | **1103** | 100 % |

## product (294)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 2600 | [absmach/magistrala](https://github.com/absmach/magistrala) | — | topic=iot-cloud,iot-gateway,iot-platform,message-broker (... | IoT Platform Framework |
| 1963 | [microcks/microcks](https://github.com/microcks/microcks) | — | topic=event-driven,kubernetes,mock-server,mocking (+3 pro... | The open source, cloud native tool for API Mocking and Testing. Mic... |
| 987 | [wso2/product-apim](https://github.com/wso2/product-apim) | — | topic=api-gateway,api-management,gateway,microservices (+... | Welcome to the WSO2 API Manager source code! For info on working wi... |
| 833 | [jniebuhr/gaggimate](https://github.com/jniebuhr/gaggimate) | — | topic=iot (+3 product); spec-at-root/docs (+1 product) | This project upgrades a Gaggia espresso machine with smart controls... |
| 815 | [Apicurio/apicurio-registry](https://github.com/Apicurio/apicurio-registry) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | An API/Schema registry - stores APIs and Schemas. |
| 690 | [aklivity/zilla](https://github.com/aklivity/zilla) | — | topic=api-gateway,event-driven-architecture,iot,server-se... | 🦎 A multi-protocol edge & service proxy. Seamlessly interface web a... |
| 558 | [chainloop-dev/chainloop](https://github.com/chainloop-dev/chainloop) | — | topic=metadata-platform (+3 product); text~product(weak) ... | SDLC evidence store and policy engine for your Software Supply Chai... |
| 313 | [wso2/product-microgateway](https://github.com/wso2/product-microgateway) | — | topic=api-gateway,api-management,gateway,microgateway,mic... | Choreo Connect is a cloud-native, open-source, and developer-centri... |
| 154 | [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... | An MCP server that provides access to Postman. |
| 93 | [lornajane/streamdeck-tricks](https://github.com/lornajane/streamdeck-tricks) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Code to use streamdeck lib and tie in obs/mqtt/other things |
| 63 | [LordMoMA/Intelli-Mall](https://github.com/LordMoMA/Intelli-Mall) | — | topic=event-driven,event-driven-architecture,microservice... | A distributed system that simulates a retail experience coupled wit... |
| 61 | [allenheltondev/gopher-holes-unlimited](https://github.com/allenheltondev/gopher-holes-unlimited) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Example OpenAPI Spec for fictional website: Gopher Holes Unlimited |
| 52 | [cryostatio/cryostat](https://github.com/cryostatio/cryostat) | — | topic=kubernetes (+3 product); text~product (+2 product);... | Self-hosted performance data capture, storage, and analysis for con... |
| 39 | [open-edge-platform/scenescape](https://github.com/open-edge-platform/scenescape) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Multimodal object tracking and scene analytics for highly actionabl... |
| 32 | [aml-org/als](https://github.com/aml-org/als) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Language Server implementation for AML and AML-defined metadata |
| 26 | [Jet-labs/jet-admin](https://github.com/Jet-labs/jet-admin) | — | topic=webapp (+3 product); text~product (+2 product); spe... | 🚀 Open-source low-code platform with multi-datasource support, visu... |
| 23 | [kanekoshoyu/exchange-collection](https://github.com/kanekoshoyu/exchange-collection) | — | topic=cross-platform (+3 product); text~tool (+2 tooling/... | Collection of Crypto Exchange OpenAPI and Generated Clients |
| 18 | [btravers/amqp-contract](https://github.com/btravers/amqp-contract) | — | topic=schema,standard-schema (+3 spec/docs); topic=messag... | Type-safe contracts for AMQP/RabbitMQ messaging with TypeScript |
| 16 | [golemfoundation/octant](https://github.com/golemfoundation/octant) | — | text~product (+2 product) | Octant is a novel platform for experiments in participatory public ... |
| 14 | [event-catalog/generators](https://github.com/event-catalog/generators) | — | topic=event-driven-architecture (+3 product); text~tool (... | Plugin integrations for EventCatalog |
| 13 | [DiamondLightSource/blueapi](https://github.com/DiamondLightSource/blueapi) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Lightweight bluesky-as-a-service |
| 12 | [rsksmart/rif-wallet-services](https://github.com/rsksmart/rif-wallet-services) | — | text~product (+2 product); spec-at-root/docs (+1 product) | RIF Wallet services |
| 10 | [Jan-IngenHousz-Institute/open-jii](https://github.com/Jan-IngenHousz-Institute/open-jii) | — | text~product (+2 product); spec-at-root/docs (+1 product) | openJII is an open-source platform for analyzing photosynthesis dat... |
| 10 | [microcks/microcks-testcontainers-go](https://github.com/microcks/microcks-testcontainers-go) | — | topic=mocking (+3 product); text~tool (+2 tooling/library... | Go lib for Testcontainers that enables embedding Microcks into your... |
| 8 | [runwisp/runwisp](https://github.com/runwisp/runwisp) | — | topic=self-hosted (+3 product); text~product (+2 product) | Cron job manager + process supervisor in a single binary. Web dashb... |
| 8 | [teekay/jcomments](https://github.com/teekay/jcomments) | — | text~tool (+2 tooling/library); text~product (+2 product)... | A headless commenting platform for publishers. Usable with any CMS ... |
| 7 | [dulerabbit/GaggiBre](https://github.com/dulerabbit/GaggiBre) | — | text~product (+2 product); spec-at-root/docs (+1 product) | This is GaggiBre! a fork of Gaggimate with Manual Brew Control and ... |
| 7 | [ministryofjustice/visit-scheduler](https://github.com/ministryofjustice/visit-scheduler) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... | A microservice for managing the schedule of prison visits |
| 7 | [opengeospatial/developer-website](https://github.com/opengeospatial/developer-website) | — | text~product (+2 product); name~spec (+1 spec/docs); spec... | OGC Developer Website |
| 7 | [yelaco/ludofy](https://github.com/yelaco/ludofy) | — | topic=game-backend,serverless (+3 product); text~product ... | PaaS solution for deploying and managing serverless game backends |
| 6 | [danilfg/bank-test-platform](https://github.com/danilfg/bank-test-platform) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 6 | [EvenToNight/EvenToNight](https://github.com/EvenToNight/EvenToNight) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | DOCS ROOT |
| 5 | [DevOpsMadDog/Fixops](https://github.com/DevOpsMadDog/Fixops) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | ALdeci — AI-powered Decision Intelligence for Security Teams. Multi... |
| 5 | [ha-securemtr/ha-securemtr](https://github.com/ha-securemtr/ha-securemtr) | — | topic=iot (+3 product); spec-at-root/docs (+1 product) | Home Assistant integration for E7+ Secure Meters Smart Water Heatre... |
| 5 | [jfunfor/chess_robot](https://github.com/jfunfor/chess_robot) | — | text~product (+2 product) |  |
| 5 | [SolaceLabs/solace-tools-typescript](https://github.com/SolaceLabs/solace-tools-typescript) | — | text~tool (+2 tooling/library); text~product (+2 product)... | This repository contains tools to enable interaction with the Solac... |
| 5 | [somosphi/ts-seed-jest](https://github.com/somosphi/ts-seed-jest) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Typescript backend template with Jest |
| 4 | [bitrockteam/kafka-dvs-api](https://github.com/bitrockteam/kafka-dvs-api) | — | text~product (+2 product) |  |
| 4 | [Chinitsu-Challenge/chinitsu-demo](https://github.com/Chinitsu-Challenge/chinitsu-demo) | — | text~product (+2 product); name~demo (+2 demo/fixture); s... |  |
| 4 | [dgnsrekt/gexbot-faker-api](https://github.com/dgnsrekt/gexbot-faker-api) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 4 | [energywebfoundation/ddhub-client-gateway](https://github.com/energywebfoundation/ddhub-client-gateway) | — | text~product (+2 product) |  |
| 4 | [harmony-ai-solutions/harmony-link](https://github.com/harmony-ai-solutions/harmony-link) | — | text~product (+2 product); spec-at-root/docs (+1 product)... | Harmony Link is a multi-platform AI-middleware, which allows for ea... |
| 4 | [IMAGINARY/future-mobility](https://github.com/IMAGINARY/future-mobility) | — | text~product (+2 product) | An exhibit about the Future of Mobility |
| 4 | [KTCrisis/event7](https://github.com/KTCrisis/event7) | — | topic=event-driven,schema-registry (+3 product); text~pro... | Schema registry governance for event-driven architectures — data co... |
| 4 | [Kuestenlogik/Bowire](https://github.com/Kuestenlogik/Bowire) | — | topic=api-client,http-client (+3 tooling/library); topic=... | Multi-protocol API workbench for .NET — discover, invoke, record, m... |
| 4 | [litmuschaos/m-agent](https://github.com/litmuschaos/m-agent) | — | text~product (+2 product); spec-at-root/docs (+1 product) | LitmusChaos Machine Agent |
| 4 | [mdl29/donkeycarLPH](https://github.com/mdl29/donkeycarLPH) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Front + backend to manage donkeycars during demonstrations events |
| 4 | [Yodata/real-estate](https://github.com/Yodata/real-estate) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | standard events for real estate software and data integration |
| 3 | [atharvagadkari05/template_EDA_API](https://github.com/atharvagadkari05/template_EDA_API) | — | text~product (+2 product) | API developed by the use of AsyncAPI tool which helps to document a... |
| 3 | [caochun/tollgate](https://github.com/caochun/tollgate) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 3 | [d34dman/notification-server](https://github.com/d34dman/notification-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 3 | [junyoung011019/aws-serverless-shortform-platform](https://github.com/junyoung011019/aws-serverless-shortform-platform) | — | text~product (+2 product); spec-at-root/docs (+1 product) | 👑 Serverless 숏폼 외국어 회화 플랫폼 (DATA VENTURE 문제 해결 챌린지) |
| 3 | [kubescape/synchronizer](https://github.com/kubescape/synchronizer) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 3 | [mcrawfo2/go-msx](https://github.com/mcrawfo2/go-msx) | — | topic=microservices (+3 product); text~tool (+2 tooling/l... | Go library for building MSX microservices |
| 3 | [Netcracker/qubership-integration-platform](https://github.com/Netcracker/qubership-integration-platform) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 3 | [paynejacob/speakerbob](https://github.com/paynejacob/speakerbob) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 3 | [robev2252060/2247107_MAP](https://github.com/robev2252060/2247107_MAP) | — | text~product (+2 product) | Mars Automation Platform (MAP) is an event-driven system that inges... |
| 3 | [The-All-Knowing/cosmiccpp](https://github.com/The-All-Knowing/cosmiccpp) | — | topic=event-driven (+3 product); topic=example-project (+... | Сервис управления распределением позиций заказов в партиях. |
| 3 | [vincenzocorso/car-sharing](https://github.com/vincenzocorso/car-sharing) | — | topic=microservices,microservices-patterns (+3 product); ... | A microservice application developed to practise implementing some ... |
| 3 | [wso2-open-operations/cs-tools](https://github.com/wso2-open-operations/cs-tools) | — | text~product (+2 product) | OpenSource tools beneficial to customer success. |
| 2 | [bb-frc-workshops/wpilib-ws-schema](https://github.com/bb-frc-workshops/wpilib-ws-schema) | — | text~product (+2 product); spec-at-root/docs (+1 product)... | Schema for the WPILib WebSocket extension |
| 2 | [changtraisitinh/digital-bank-hub](https://github.com/changtraisitinh/digital-bank-hub) | — | text~product (+2 product) | Digital Bank Hub with all in one solutions  |
| 2 | [devmentors/Mikroserwisy-Revisited](https://github.com/devmentors/Mikroserwisy-Revisited) | — | topic=microservices (+3 product) | [PL] Mikroserwisy 6 lat później czyli... jak nie utonąć 😉 |
| 2 | [ewanvidal/SimuMarty](https://github.com/ewanvidal/SimuMarty) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | SimuMarty est une application web moderne de simulation robotique é... |
| 2 | [gravitee-io/gravitee-apim-mcp-server](https://github.com/gravitee-io/gravitee-apim-mcp-server) | — | text~product (+2 product); text~spec (+2 spec/docs) |  |
| 2 | [guilhermerodrigues680/globo-terrestre-iot](https://github.com/guilhermerodrigues680/globo-terrestre-iot) | — | topic=iot,webapp,webserver (+3 product); text~product(wea... | O Globo Terrestre IoT usa de várias tecnologias sem fio e web para ... |
| 2 | [hmecruz/chat-service](https://github.com/hmecruz/chat-service) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 2 | [IMAGINARY/citizen-quest](https://github.com/IMAGINARY/citizen-quest) | — | text~product (+2 product) | An exhibit about the Future of Democracy |
| 2 | [jsa4000/Internal-Development-Platform](https://github.com/jsa4000/Internal-Development-Platform) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Backstage as Internal Developer Platform (IDP) |
| 2 | [kaje94/slek-link](https://github.com/kaje94/slek-link) | — | topic=kubernetes (+3 product) | A high-performance, free URL shortener built for speed and simplici... |
| 2 | [KamilMarszalek/checkers-online](https://github.com/KamilMarszalek/checkers-online) | — | text~product (+2 product) | Checkers - online multiplayer game |
| 2 | [masechkacat/tic-tac-toe-server](https://github.com/masechkacat/tic-tac-toe-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) | This API allows real-time interaction in a Tic Tac Toe game via Web... |
| 2 | [mindsmiths/docs](https://github.com/mindsmiths/docs) | — | text~product (+2 product); name~spec (+1 spec/docs); lang... | Mindsmiths Platform Docs |
| 2 | [music10/server](https://github.com/music10/server) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Nest.js Server for Musiq |
| 2 | [n-bolanos/FastEventManager](https://github.com/n-bolanos/FastEventManager) | — | text~product (+2 product); spec-at-root/docs (+1 product)... |  |
| 2 | [Netcracker/qubership-integration-runtime-catalog](https://github.com/Netcracker/qubership-integration-runtime-catalog) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 2 | [officialdavidtaylor/leftover-label-printer](https://github.com/officialdavidtaylor/leftover-label-printer) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A digital rube goldberg machine for printing thermal labels for my ... |
| 2 | [periclescesar/event-processor](https://github.com/periclescesar/event-processor) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 2 | [pfarkya/asyncApi_AccountManagerEDA](https://github.com/pfarkya/asyncApi_AccountManagerEDA) | — | text~tool (+2 tooling/library); text~product (+2 product)... | This is an Account Management Application in Event Driven Architect... |
| 2 | [radiorabe/minio-cloudevents-service](https://github.com/radiorabe/minio-cloudevents-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Consumes S3/MinIO-Events from Kafka and forwards them to another to... |
| 2 | [radiorabe/pathfinder-cloudevents-service](https://github.com/radiorabe/pathfinder-cloudevents-service) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Receives events from Pathfinder's RestApi and turn them into RaBe C... |
| 2 | [sentient-io/microservice-docs](https://github.com/sentient-io/microservice-docs) | — | text~product (+2 product); name~spec (+1 spec/docs); lang... |  |
| 2 | [SoftwareEngineerUB/SmartEnergy](https://github.com/SoftwareEngineerUB/SmartEnergy) | — | topic=iot (+3 product); spec-at-root/docs (+1 product) | SmartEnergy este o aplicatie IoT al cărei scop este de a interacțio... |
| 2 | [TeleGrammy/backend](https://github.com/TeleGrammy/backend) | — | text~product (+2 product) | Telegrammy replicates Telegram's backend functionalities from scrat... |
| 2 | [victorrentea/training-assistant](https://github.com/victorrentea/training-assistant) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | training assistant tool |
| 2 | [way-platform/mbz-go](https://github.com/way-platform/mbz-go) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Go SDK for the Mercedes-Benz Fleet API |
| 1 | [a-l-a-z-a-r/Socialbook](https://github.com/a-l-a-z-a-r/Socialbook) | — | text~product (+2 product); lang=HTML (+1 spec/docs) |  |
| 1 | [anonymousc/ft_transcendance-42](https://github.com/anonymousc/ft_transcendance-42) | — | text~product (+2 product) | digitalyzing travel planning stuff |
| 1 | [ayointegral/cloud-sandbox-backstage](https://github.com/ayointegral/cloud-sandbox-backstage) | — | text~product (+2 product) | Cloud Sandbox - Backstage Developer Portal with custom catalog and ... |
| 1 | [BitKa-Exchange/bitka-exchange](https://github.com/BitKa-Exchange/bitka-exchange) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Bitkub Clone project for learning  |
| 1 | [bshongwe/fintech-api](https://github.com/bshongwe/fintech-api) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [daithang59/sagelms](https://github.com/daithang59/sagelms) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Hệ thống Web LMS microservices tích hợp AI Tutor. Giai đoạn 2 mở rộ... |
| 1 | [danieldan0/microservice-store](https://github.com/danieldan0/microservice-store) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [decker757/Smart-Clinic-Queue-ESD](https://github.com/decker757/Smart-Clinic-Queue-ESD) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 1 | [DEFRA/aphw-ddi-events](https://github.com/DEFRA/aphw-ddi-events) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [El-khamisi/whatsapp-web.js](https://github.com/El-khamisi/whatsapp-web.js) | — | text~tool (+2 tooling/library); text~product (+2 product)... | A real-time bot using node.js, socket.io, and MongoDB to store user... |
| 1 | [FrackiewiczP/info_bubbles](https://github.com/FrackiewiczP/info_bubbles) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 1 | [gemini-fieldtest/RACE](https://github.com/gemini-fieldtest/RACE) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 1 | [hefarica/arbitragex-v2](https://github.com/hefarica/arbitragex-v2) | — | text~product (+2 product) | MEV/arbitrage platform v2 - Rust hot-path + TS control-plane + CF W... |
| 1 | [Jack-the-Pro101/vequate](https://github.com/Jack-the-Pro101/vequate) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Cloud based Minecraft server orchestration system |
| 1 | [joshwambere/Galileo](https://github.com/joshwambere/Galileo) | — | text~tool (+2 tooling/library); text~product (+2 product)... | is a blazing fast rest API for chatting application |
| 1 | [junmoku/pokeraid](https://github.com/junmoku/pokeraid) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [kishoretvk/AgentAI](https://github.com/kishoretvk/AgentAI) | — | text~product (+2 product); spec-at-root/docs (+1 product) | this is a collection of AI agents which can indpdently work with an... |
| 1 | [manassehkafoh/superapp-platform](https://github.com/manassehkafoh/superapp-platform) | — | topic=kubernetes,microservices (+3 product); text~product... | SuperApp Ghana — enterprise financial platform monorepo (6 microser... |
| 1 | [montionugera/atlas-world-svc](https://github.com/montionugera/atlas-world-svc) | — | text~product (+2 product) | Atlas World Service - Real-time multiplayer game server built with ... |
| 1 | [n2nstreams/seas-factory-infra](https://github.com/n2nstreams/seas-factory-infra) | — | text~product (+2 product); spec-at-root/docs (+1 product) | an ai saas factory ran by agents |
| 1 | [olaviolacerda/notification](https://github.com/olaviolacerda/notification) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 1 | [phalanxduel/phalanxduel](https://github.com/phalanxduel/phalanxduel) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Arm yourself for battle with spades and clubs and shields against y... |
| 1 | [prafulrana/asyncAPIExamples](https://github.com/prafulrana/asyncAPIExamples) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Collection of AsyncAPI specs with real world broker channels. |
| 1 | [RidaNaz/Agentic-Todo](https://github.com/RidaNaz/Agentic-Todo) | — | text~product (+2 product) |  |
| 1 | [sepa79/PocketHive](https://github.com/sepa79/PocketHive) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 1 | [SoldierrBoy/EventTicketBookingSystem](https://github.com/SoldierrBoy/EventTicketBookingSystem) | — | text~product (+2 product) |  |
| 1 | [SourceOS-Linux/sourceos-spec](https://github.com/SourceOS-Linux/sourceos-spec) | — | text~product (+2 product); text~spec (+2 spec/docs); name... | sourceos-spec |
| 1 | [Sriramanenivikas/Intelligent-Warehouse-Orchestration-System](https://github.com/Sriramanenivikas/Intelligent-Warehouse-Orchestration-System) | — | topic=event-driven,kong-gateway,kubernetes,microservice (... | IWOS  is a unified fulfillment platform that combines quick commerc... |
| 1 | [The-Microservice-Dungeon/gamelog](https://github.com/The-Microservice-Dungeon/gamelog) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 1 | [The-Microservice-Dungeon/trading](https://github.com/The-Microservice-Dungeon/trading) | — | text~product (+2 product) |  |
| 1 | [vkputhenmadhom/smarthiringassistant](https://github.com/vkputhenmadhom/smarthiringassistant) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Smart Hiring Assistant |
| 1 | [zynax-io/zynax](https://github.com/zynax-io/zynax) | — | topic=kubernetes (+3 product); text~product(weak) (+1 pro... | Declarative, cloud-native, engine-agnostic control plane for AI age... |
| 0 | [adalbertocajueiro/edscorbot-c-cpp](https://github.com/adalbertocajueiro/edscorbot-c-cpp) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... |  |
| 0 | [adityasneo/Backstage.io](https://github.com/adityasneo/Backstage.io) | — | text~product (+2 product) |  |
| 0 | [ajgarciaparadigma/asyncapi-publisher](https://github.com/ajgarciaparadigma/asyncapi-publisher) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Alex009/architecture-sprint-3](https://github.com/Alex009/architecture-sprint-3) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Практическое задание по разделению на микросервисы |
| 0 | [Analytics4Change/A4C-AppSuite](https://github.com/Analytics4Change/A4C-AppSuite) | — | text~product (+2 product) | Analytics4Change monorepo - medication management platform |
| 0 | [andreitudose2000/ingineria-programarii](https://github.com/andreitudose2000/ingineria-programarii) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Smart deskchair IoT app |
| 0 | [ArturVyklynets/HireMe](https://github.com/ArturVyklynets/HireMe) | — | text~product (+2 product); spec-at-root/docs (+1 product)... |  |
| 0 | [Ashish8951/poker-docs](https://github.com/Ashish8951/poker-docs) | — | text~product (+2 product); name~spec (+1 spec/docs); spec... |  |
| 0 | [axvg/store-microservices](https://github.com/axvg/store-microservices) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Sample store application using microservices |
| 0 | [BalaNarvar/BackStage1](https://github.com/BalaNarvar/BackStage1) | — | text~product (+2 product) |  |
| 0 | [baldimir/kie-backend](https://github.com/baldimir/kie-backend) | — | text~product (+2 product) | All the backend code for the Apache KIE project (testing repository... |
| 0 | [bfl-ajay/AsyncApi-Example](https://github.com/bfl-ajay/AsyncApi-Example) | — | text~product (+2 product); text~spec (+2 spec/docs); name... | This is a secure, production-ready WebSocket-based API built using ... |
| 0 | [BillyBolton/menace](https://github.com/BillyBolton/menace) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Go server implementing Donald Michie's MENACE (Machine Educable Nou... |
| 0 | [blagoySimandov/takgo](https://github.com/blagoySimandov/takgo) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Brico87/event-gateway](https://github.com/Brico87/event-gateway) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Event gateway with Spring Cloud Stream stack |
| 0 | [Brico87/seed-kafka](https://github.com/Brico87/seed-kafka) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [bulatminnakhmetov/brigadka-backend](https://github.com/bulatminnakhmetov/brigadka-backend) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [Central-University-IT-prod/2026-final-command-team-27-backend](https://github.com/Central-University-IT-prod/2026-final-command-team-27-backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [chess-vn/slchess](https://github.com/chess-vn/slchess) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [ChiragSethi-1153/RMHA](https://github.com/ChiragSethi-1153/RMHA) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ChunPingWang/saga-kafka](https://github.com/ChunPingWang/saga-kafka) | — | text~product (+2 product) |  |
| 0 | [cibanezb95STG/quoteAssessmentCIB](https://github.com/cibanezb95STG/quoteAssessmentCIB) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Assessment for backend position. Project for financial quotes. |
| 0 | [ClearEyesFullHearts/asyncapi-pub-middleware](https://github.com/ClearEyesFullHearts/asyncapi-pub-middleware) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Add a validating publisher object, from an AsyncAPI file descriptio... |
| 0 | [ClearEyesFullHearts/asyncapi-sub-middleware](https://github.com/ClearEyesFullHearts/asyncapi-sub-middleware) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... | Create routes and validation for an express-like async server |
| 0 | [cristianve/VibrationsGame-Backend](https://github.com/cristianve/VibrationsGame-Backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Backend for Vibration game |
| 0 | [cyberlytics/Conversphere](https://github.com/cyberlytics/Conversphere) | — | text~product (+2 product) |  |
| 0 | [d1m1tur/PGJ-2026](https://github.com/d1m1tur/PGJ-2026) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Plovdiv Game Jam 2026 project |
| 0 | [daniellmorris/EnvarynAI](https://github.com/daniellmorris/EnvarynAI) | — | text~product (+2 product) | Ambient speech capture and transcription app with a Flutter client,... |
| 0 | [dataGriff/dog-walking](https://github.com/dataGriff/dog-walking) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 0 | [dataGriff/dog.rescue.api](https://github.com/dataGriff/dog.rescue.api) | — | text~product (+2 product); spec-at-root/docs (+1 product)... |  |
| 0 | [dataGriff/pet.insurance.domain.app.v1](https://github.com/dataGriff/pet.insurance.domain.app.v1) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [davidosantos/backstage](https://github.com/davidosantos/backstage) | — | text~product (+2 product) |  |
| 0 | [DEFRA/ffc-doc-alerting](https://github.com/DEFRA/ffc-doc-alerting) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [DEFRA/ffc-pay-alerting](https://github.com/DEFRA/ffc-pay-alerting) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Publish alerts for Payment Hub warnings |
| 0 | [DEFRA/ffc-pay-batch-processor](https://github.com/DEFRA/ffc-pay-batch-processor) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC payment batch processor |
| 0 | [DEFRA/ffc-pay-event-hub](https://github.com/DEFRA/ffc-pay-event-hub) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC Pay event hub |
| 0 | [DEFRA/ffc-pay-file-publisher](https://github.com/DEFRA/ffc-pay-file-publisher) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | FFC publish payment files to DAX |
| 0 | [DEFRA/ffc-pay-file-receiver](https://github.com/DEFRA/ffc-pay-file-receiver) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Process DAX responses |
| 0 | [DEFRA/ffc-pay-processing](https://github.com/DEFRA/ffc-pay-processing) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC Payment service |
| 0 | [DEFRA/ffc-pay-responses](https://github.com/DEFRA/ffc-pay-responses) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC Payment service to process responses from Dynamics 365 |
| 0 | [DEFRA/ffc-pay-submission](https://github.com/DEFRA/ffc-pay-submission) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FFC SFI payment submission service to support integration with Dyna... |
| 0 | [DevOpsMadDog/aldeci-core](https://github.com/DevOpsMadDog/aldeci-core) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [DiamondLightSource/subscriptions](https://github.com/DiamondLightSource/subscriptions) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [djoleant/IoTS-Smart-building](https://github.com/djoleant/IoTS-Smart-building) | — | topic=iot,microservices (+3 product) | Internet of Things and Services project for Smart buildings |
| 0 | [dlcastra/WABToDo-back-end-](https://github.com/dlcastra/WABToDo-back-end-) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [dsbaars/btclock-ws-nostr-publish](https://github.com/dsbaars/btclock-ws-nostr-publish) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [dtanwer/video-service](https://github.com/dtanwer/video-service) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [EdithRW/rw-backend-dashboard](https://github.com/EdithRW/rw-backend-dashboard) | — | text~product (+2 product) | backend test for rw dashboard |
| 0 | [edulucca/gateway-stripe-adapter](https://github.com/edulucca/gateway-stripe-adapter) | — | text~product (+2 product); spec-at-root/docs (+1 product)... | gateway-stripe-adapter [backstage] |
| 0 | [EduRS14/sistema-recomendacion-distribuido-peliculas](https://github.com/EduRS14/sistema-recomendacion-distribuido-peliculas) | — | text~product (+2 product) | Sistema de Recomendación Distribuido hecho con Go para el Backend y... |
| 0 | [EthanSheehan/Grid-Sentinel](https://github.com/EthanSheehan/Grid-Sentinel) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [faraz7321/robot-elevator-middleware](https://github.com/faraz7321/robot-elevator-middleware) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [fenix-hub/cns-project-backend](https://github.com/fenix-hub/cns-project-backend) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [FlorinaMt/SEP4](https://github.com/FlorinaMt/SEP4) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [funny-bunny-corp/payment-service](https://github.com/funny-bunny-corp/payment-service) | — | text~product (+2 product) |  |
| 0 | [GitEngHar/pointservice](https://github.com/GitEngHar/pointservice) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Gradient-DS/AGORA](https://github.com/Gradient-DS/AGORA) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [GUR-ok/otus-microservice-architecture](https://github.com/GUR-ok/otus-microservice-architecture) | — | text~product (+2 product) | Домашние задания по курсу "OTUS 2022. Микросервисная Архитектура". ... |
| 0 | [heartbridgeapp/heartbridge-server](https://github.com/heartbridgeapp/heartbridge-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Python / FastAPI server implementation of the HeartBridge API |
| 0 | [henrykey/kone-elevator](https://github.com/henrykey/kone-elevator) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [IlijaIvanovic78/F1DataStream](https://github.com/IlijaIvanovic78/F1DataStream) | — | text~product (+2 product) |  |
| 0 | [imaksb/quizy](https://github.com/imaksb/quizy) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [immonel/e-runout](https://github.com/immonel/e-runout) | — | text~product (+2 product) |  |
| 0 | [imorrish/blackmagic_camera_control](https://github.com/imorrish/blackmagic_camera_control) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Blackmagic REST API camera control app for Android/Linux/Windows/Ma... |
| 0 | [isehuetdk/backstage](https://github.com/isehuetdk/backstage) | — | text~product (+2 product) | Test deployment of Backstage for Azure Self-service  |
| 0 | [ivankahl/asyncapi-food-delivery](https://github.com/ivankahl/asyncapi-food-delivery) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [j-alonso-guerra/open-api-public](https://github.com/j-alonso-guerra/open-api-public) | — | text~product (+2 product); spec-at-root/docs (+1 product)... |  |
| 0 | [jaekop/ContextLens](https://github.com/jaekop/ContextLens) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [jean0313/k2a](https://github.com/jean0313/k2a) | — | text~tool (+2 tooling/library); text~product (+2 product)... | k2a |
| 0 | [jeancharles-roger/BlackMagicRestControlUI](https://github.com/jeancharles-roger/BlackMagicRestControlUI) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Kotlin Compose UI for Black Magic Camera control using the provided... |
| 0 | [jfriisj/real-time-speech-translation-mvp](https://github.com/jfriisj/real-time-speech-translation-mvp) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [jjoeluna/building-os-platform](https://github.com/jjoeluna/building-os-platform) | — | text~tool (+2 tooling/library); text~product (+2 product)... | The central platform for intelligent building management |
| 0 | [JLanders96/abw-processor](https://github.com/JLanders96/abw-processor) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Workflows provide durable step execution, retries, and sleeps betwe... |
| 0 | [joass1/ESD-Ticket-booking](https://github.com/joass1/ESD-Ticket-booking) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [josebusv/enterprise-integration-platform](https://github.com/josebusv/enterprise-integration-platform) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [jprofessionals/shopping-list](https://github.com/jprofessionals/shopping-list) | — | text~product (+2 product) | Project to make sharing and creating shopping lists easier |
| 0 | [kaaaaakun/AsyncAPI-mock-server](https://github.com/kaaaaakun/AsyncAPI-mock-server) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [karlosdaniel451/message-chat](https://github.com/karlosdaniel451/message-chat) | — | topic=messaging (+3 product); text~product(weak) (+1 prod... | Message chat application using Go and NATS. |
| 0 | [klurvio/sukko](https://github.com/klurvio/sukko) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [konrad2002/ludo](https://github.com/konrad2002/ludo) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Play ludo in the browser alone or with friends online or offline |
| 0 | [krisnaganesha1609/IoTDrainage-BE](https://github.com/krisnaganesha1609/IoTDrainage-BE) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [krittamark/incident-tracking-service](https://github.com/krittamark/incident-tracking-service) | — | text~product (+2 product); lang=HTML (+1 spec/docs) | Microservice for the source of truth for fundamental incident data.... |
| 0 | [kyleczhang/cits5506-iot-parkreserve-group29](https://github.com/kyleczhang/cits5506-iot-parkreserve-group29) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [L4VA-Technologies-Inc/scanner](https://github.com/L4VA-Technologies-Inc/scanner) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A Cardano Blockchain Scanner that triggers Webhooks |
| 0 | [L4VA-Technologies-Inc/scanner-webui](https://github.com/L4VA-Technologies-Inc/scanner-webui) | — | text~product (+2 product); spec-at-root/docs (+1 product) | A simple Web UI for the L4va Scanner |
| 0 | [latamteks-cmyk/desarrollo](https://github.com/latamteks-cmyk/desarrollo) | — | text~product (+2 product); spec-at-root/docs (+1 product)... |  |
| 0 | [latamteks-cmyk/SmartEdify_app](https://github.com/latamteks-cmyk/SmartEdify_app) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [LingshijunRenzy/ICS-guard-next](https://github.com/LingshijunRenzy/ICS-guard-next) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Next generation of ICS-IDS |
| 0 | [lloydchang/harness-backstage](https://github.com/lloydchang/harness-backstage) | — | text~product (+2 product) | Backstage is an open platform for building developer portals |
| 0 | [lok-hit/CarRentalApp](https://github.com/lok-hit/CarRentalApp) | — | text~product (+2 product) |  |
| 0 | [lucasheld/wg-ha-app-backend](https://github.com/lucasheld/wg-ha-app-backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [lxbme/E-ee](https://github.com/lxbme/E-ee) | — | text~tool (+2 tooling/library); text~product (+2 product)... | a end-to-end encrypt chat backend |
| 0 | [Lynda1423/gestion-vehicules](https://github.com/Lynda1423/gestion-vehicules) | — | text~product (+2 product) |  |
| 0 | [manassehkafoh/nexustreasury](https://github.com/manassehkafoh/nexustreasury) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Treasury Management System |
| 0 | [marcgr9/ptbox-assignment](https://github.com/marcgr9/ptbox-assignment) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [mariabrykulskaa/robond](https://github.com/mariabrykulskaa/robond) | — | text~product (+2 product); lang=HTML (+1 spec/docs) |  |
| 0 | [MariamElsoufyx/IMMERSA-Voice-Chat-API](https://github.com/MariamElsoufyx/IMMERSA-Voice-Chat-API) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [mattlat21/homeassistant](https://github.com/mattlat21/homeassistant) | — | text~product (+2 product) | Anything Home Assistant Related |
| 0 | [maximilianoPizarro/platform-hub-spoke-config](https://github.com/maximilianoPizarro/platform-hub-spoke-config) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Multi-cluster GitOps platform using Red Hat Advanced Cluster Manage... |
| 0 | [MaximilianWalker/HexRelay](https://github.com/MaximilianWalker/HexRelay) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [MaxwellGBrown/aws_websockets_eventbus](https://github.com/MaxwellGBrown/aws_websockets_eventbus) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Example Eventbus with a WebSocket API Gateway |
| 0 | [MCI-MS-WS2025-Advanced-Project/crazy-labyrinth-gameserver](https://github.com/MCI-MS-WS2025-Advanced-Project/crazy-labyrinth-gameserver) | — | text~product (+2 product); spec-at-root/docs (+1 product) | The Amazing Labyrinth - Game Server |
| 0 | [McLaouth/backstage](https://github.com/McLaouth/backstage) | — | text~product (+2 product) |  |
| 0 | [Mesteriis/rune-tasks-mesh](https://github.com/Mesteriis/rune-tasks-mesh) | — | topic=task-orchestration (+3 product); text~product (+2 p... | Local-first task orchestration control plane with Kanban UI, sync m... |
| 0 | [Metsuk1/bybitParser](https://github.com/Metsuk1/bybitParser) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [Minister2405/my-docs](https://github.com/Minister2405/my-docs) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ministryofjustice/hmpps-complexity-of-need](https://github.com/ministryofjustice/hmpps-complexity-of-need) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... | Complexity of Need microservice |
| 0 | [Minwsun/IntelligentRouteX](https://github.com/Minwsun/IntelligentRouteX) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [mjones3/interface-exception-collector-service](https://github.com/mjones3/interface-exception-collector-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [mnabli94/ecommerce-microservices](https://github.com/mnabli94/ecommerce-microservices) | — | topic=microservices (+3 product); text~product (+2 product) | Event-driven e-commerce microservices with Java 17, Spring Boot 3, ... |
| 0 | [naomesh/naomesh-onion-orchestrator](https://github.com/naomesh/naomesh-onion-orchestrator) | — | topic=orchestrator (+3 product); text~product (+2 product... | Distributed computing orchestrator for green photogrammetry with pr... |
| 0 | [naomesh/naomesh-web-api](https://github.com/naomesh/naomesh-web-api) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | REST api for the demonstator webapp |
| 0 | [Navdeep-12/Backstage](https://github.com/Navdeep-12/Backstage) | — | text~product (+2 product) |  |
| 0 | [Navvyaa/ChatBE](https://github.com/Navvyaa/ChatBE) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | A production-ready real-time chat backend featuring JWT authenticat... |
| 0 | [nesaa-a/SPDD-EventSystem](https://github.com/nesaa-a/SPDD-EventSystem) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... |  |
| 0 | [netbill/auth-svc](https://github.com/netbill/auth-svc) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | SSO service REST, jwt and OAuth2 (Google) |
| 0 | [newsukarun/async-api](https://github.com/newsukarun/async-api) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [ngscheurich/elixirconf-eu-2024](https://github.com/ngscheurich/elixirconf-eu-2024) | — | text~product (+2 product); spec-at-root/docs (+1 product) | 🗺️ “Let’s Go on an Adventure” (ElixirConf EU 2024) |
| 0 | [NoTIPswe/notip-data-api](https://github.com/NoTIPswe/notip-data-api) | — | text~product (+2 product) |  |
| 0 | [NoTIPswe/notip-data-consumer](https://github.com/NoTIPswe/notip-data-consumer) | — | text~product (+2 product) |  |
| 0 | [NoTIPswe/notip-infra](https://github.com/NoTIPswe/notip-infra) | — | text~product (+2 product) |  |
| 0 | [NoTIPswe/notip-management-api](https://github.com/NoTIPswe/notip-management-api) | — | text~product (+2 product) |  |
| 0 | [NoTIPswe/notip-provisioning-service](https://github.com/NoTIPswe/notip-provisioning-service) | — | text~product (+2 product) |  |
| 0 | [NoTIPswe/notip-simulator-backend](https://github.com/NoTIPswe/notip-simulator-backend) | — | text~product (+2 product) | simulator-backend |
| 0 | [Okan-wqm/aquaculture_platform](https://github.com/Okan-wqm/aquaculture_platform) | — | text~product (+2 product) |  |
| 0 | [om-nitrox/dating](https://github.com/om-nitrox/dating) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [otherjamesbrown/penfold](https://github.com/otherjamesbrown/penfold) | — | text~product (+2 product) |  |
| 0 | [Owen-Richards/ai-nutritionist](https://github.com/Owen-Richards/ai-nutritionist) | — | topic=serverless (+3 product); text~product(weak) (+1 pro... | � Serverless AI Nutritionist Assistant - WhatsApp/SMS bot powered b... |
| 0 | [paradisemay/tradingexchange](https://github.com/paradisemay/tradingexchange) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [PikPakPik/T-JSF-600](https://github.com/PikPakPik/T-JSF-600) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Playproof-Umc/Playproof-Backend](https://github.com/Playproof-Umc/Playproof-Backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [postman-cs/postman-aws-spec-discovery-action](https://github.com/postman-cs/postman-aws-spec-discovery-action) | — | topic=api-gateway (+3 product); text~tool (+2 tooling/lib... | Public customer preview GitHub Action that discovers and exports AP... |
| 0 | [project-ascend-io/intracom-backend](https://github.com/project-ascend-io/intracom-backend) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Intracom's backend uses ExpressJS with Typescript, MongoDB |
| 0 | [qconn-io/apim-backstage](https://github.com/qconn-io/apim-backstage) | — | text~product (+2 product) | apim-backstage |
| 0 | [rahul-10-byte/multi-video-conferencing-app](https://github.com/rahul-10-byte/multi-video-conferencing-app) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Ramonjrtan/event-driven-order-platform-qa](https://github.com/Ramonjrtan/event-driven-order-platform-qa) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | QA portfolio simulating testing of an event-driven microservices pl... |
| 0 | [raulgonzalezdev/eda-backend-plus](https://github.com/raulgonzalezdev/eda-backend-plus) | — | text~product (+2 product) |  |
| 0 | [Remake1/lambda-server](https://github.com/Remake1/lambda-server) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [reza-sanjari/2L1nk](https://github.com/reza-sanjari/2L1nk) | — | topic=self-hosted (+3 product); text~product (+2 product) | Self-hosted encrypted chat in a single binary. Zero-knowledge serve... |
| 0 | [rizrmd/zlay](https://github.com/rizrmd/zlay) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 0 | [robond-fintech/robond](https://github.com/robond-fintech/robond) | — | text~product (+2 product); lang=HTML (+1 spec/docs) | An automated bond trading robot |
| 0 | [Sakshamjain98/skillforge-meet](https://github.com/Sakshamjain98/skillforge-meet) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [SayReal-US/API-designs---Software-Engineer-Thesis-K22](https://github.com/SayReal-US/API-designs---Software-Engineer-Thesis-K22) | — | text~product (+2 product); spec-at-root/docs (+1 product)... | API design for a microservice-based driver rental service with REST... |
| 0 | [SEP4Y-2025/SEP4](https://github.com/SEP4Y-2025/SEP4) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [SmartSleepIoT/SmartSleepCoding](https://github.com/SmartSleepIoT/SmartSleepCoding) | — | topic=iot (+3 product); text~demo (+2 demo/fixture) | SmartSleep - an API for an IoT bed device |
| 0 | [snatalija/IOT](https://github.com/snatalija/IOT) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [sohailhaider/backstage-search-github-issues-plugin](https://github.com/sohailhaider/backstage-search-github-issues-plugin) | — | text~product (+2 product); name~tool (+1 tooling/library) |  |
| 0 | [sonra44/LEGACY](https://github.com/sonra44/LEGACY) | — | text~product (+2 product); spec-at-root/docs (+1 product) | Digital twin simulation platform with ORION operator console and si... |
| 0 | [springwolf/springwolf-app](https://github.com/springwolf/springwolf-app) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |
| 0 | [sqwoz-hrov/sqwoz-payment-system](https://github.com/sqwoz-hrov/sqwoz-payment-system) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Startempire-Wire/Startempire-Wire-Network-Websockets](https://github.com/Startempire-Wire/Startempire-Wire-Network-Websockets) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Plugin to provide websocket support for the Startempire Wire Networ... |
| 0 | [SynapticFour/sc-specs](https://github.com/SynapticFour/sc-specs) | — | text~product (+2 product); name~spec (+1 spec/docs) |  |
| 0 | [szaher/crewz](https://github.com/szaher/crewz) | — | text~product (+2 product) |  |
| 0 | [The-Microservice-Dungeon/game](https://github.com/The-Microservice-Dungeon/game) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [thushalya/asyncapi-tools](https://github.com/thushalya/asyncapi-tools) | — | topic=websocket-server (+3 product); topic=asyncapi-speci... | Source code for Ballerina WebSocket service to AsyncAPI generator c... |
| 0 | [tianshi04/rent-a-girlfriend](https://github.com/tianshi04/rent-a-girlfriend) | — | text~product (+2 product) |  |
| 0 | [UNIZAR-30226-2025-05/adrenalux-backend](https://github.com/UNIZAR-30226-2025-05/adrenalux-backend) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [Unizar-30226-2026-11/Backend](https://github.com/Unizar-30226-2026-11/Backend) | — | text~product (+2 product) | Repositorio para el backend del proyecto Tale of Recognition. |
| 0 | [Unizar-30226-2026-11/Movil](https://github.com/Unizar-30226-2026-11/Movil) | — | text~product (+2 product) | Repositorio para el frontend móvil del proyecto Tale of Recognition.  |
| 0 | [uri157/trading-chart](https://github.com/uri157/trading-chart) | — | text~product (+2 product) | Real-time market data platform with C++ API, DuckDB time-series sto... |
| 0 | [vdm-systems/swifty-server](https://github.com/vdm-systems/swifty-server) | — | text~product (+2 product); spec-at-root/docs (+1 product) | FastAPI Server with WebSockets |
| 0 | [Veriflite/portal-api](https://github.com/Veriflite/portal-api) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... | Veriflite Portal API Specification |
| 0 | [vhurryharry/OOT](https://github.com/vhurryharry/OOT) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | Olive Oil Times |
| 0 | [wallaceespindola/contract-first-integrations](https://github.com/wallaceespindola/contract-first-integrations) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Contract First Integrations |
| 0 | [wilsoniaan/backstage](https://github.com/wilsoniaan/backstage) | — | text~product (+2 product) |  |
| 0 | [Xen0Xys/N2I-2024-API](https://github.com/Xen0Xys/N2I-2024-API) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [XerxesDGreat/tt-booking-service](https://github.com/XerxesDGreat/tt-booking-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Service for booking trips |
| 0 | [XerxesDGreat/tt-metrics-service](https://github.com/XerxesDGreat/tt-metrics-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Service for collecting metrics from other services and storing them... |
| 0 | [XerxesDGreat/tt-notif-service](https://github.com/XerxesDGreat/tt-notif-service) | — | text~product(weak) (+1 product); spec-at-root/docs (+1 pr... | Service for publishing notifications |
| 0 | [YarikRevich/kubernetes-websocket-integration](https://github.com/YarikRevich/kubernetes-websocket-integration) | — | topic=kubernetes (+3 product); text~product(weak) (+1 pro... | WebSocket integration for kubernetes cluster |
| 0 | [yousuf7474/meerkat](https://github.com/yousuf7474/meerkat) | — | text~product (+2 product) | React App for Multi-Agent RAG System |
| 0 | [yuiyeong/bzero-api](https://github.com/yuiyeong/bzero-api) | — | text~product (+2 product); spec-at-root/docs (+1 product) | B0 의 Backend Server |
| 0 | [yukihito-jokyu/postman-mcp-server](https://github.com/yukihito-jokyu/postman-mcp-server) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... |  |
| 0 | [zdmooc/TradeOps-GenAI-Integration](https://github.com/zdmooc/TradeOps-GenAI-Integration) | — | text~product (+2 product); spec-at-root/docs (+1 product) |  |
| 0 | [zimoch84/HaggisProject](https://github.com/zimoch84/HaggisProject) | — | text~product (+2 product) |  |
| 0 | [ziyashaw/backstage_demo2](https://github.com/ziyashaw/backstage_demo2) | — | text~product (+2 product); spec-only-in-fixtures (+1 tool... |  |

## tooling/library (224)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 3784 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) | OpenAgents - AI Agent Networks for Open Collaboration |
| 1470 | [Redocly/redocly-cli](https://github.com/Redocly/redocly-cli) | — | topic=linter,openapi-cli (+3 tooling/library); text~tool ... | ⚒️ Redocly CLI makes OpenAPI easy. Lint/validate to any standard, g... |
| 907 | [mulesoft/api-console](https://github.com/mulesoft/api-console) | — | text~tool (+2 tooling/library); text~product (+2 product)... | An interactive REST console based on RAML/OAS files |
| 817 | [kweaver-ai/kweaver-core](https://github.com/kweaver-ai/kweaver-core) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) | KWeaver Core is a harness-first foundation for enterprise decision ... |
| 341 | [Sofie-Automation/sofie-core](https://github.com/Sofie-Automation/sofie-core) | — | topic=automation-framework (+3 tooling/library); text~pro... | Sofie Core: A Part of the Sofie TV Studio Automation System |
| 339 | [Lap-Platform/LAP](https://github.com/Lap-Platform/LAP) | — | topic=cli (+3 tooling/library); text~product (+2 product)... | Your agents are guessing at APIs. Give them the actual Agent-Native... |
| 327 | [CardanoSolutions/ogmios](https://github.com/CardanoSolutions/ogmios) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | ❇️ A WebSocket JSON/RPC bridge for Cardano |
| 267 | [asyncapi/cli](https://github.com/asyncapi/cli) | — | topic=cli (+3 tooling/library); topic=get-global-docs-aut... | CLI to work with your AsyncAPI files. You can validate them and in ... |
| 157 | [lerenn/asyncapi-codegen](https://github.com/lerenn/asyncapi-codegen) | — | topic=asyncapi-generator,code-generation,generator (+3 to... | An AsyncAPI Golang Code generator that generates all Go code from t... |
| 142 | [asyncapi/parser-js](https://github.com/asyncapi/parser-js) | — | topic=get-global-docs-autoupdate,json-schema (+3 spec/doc... | AsyncAPI parser for Javascript (browser-compatible too). |
| 112 | [elevenlabs/elevenlabs-swift-sdk](https://github.com/elevenlabs/elevenlabs-swift-sdk) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | ElevenLabs Conversational AI Swift SDK |
| 109 | [ballerina-platform/asyncapi-tools](https://github.com/ballerina-platform/asyncapi-tools) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | This repository is the code base for the ballerina async-api tool |
| 106 | [elevenlabs/packages](https://github.com/elevenlabs/packages) | — | text~tool (+2 tooling/library) | The ElevenLabs Agents SDK for TypeScript. |
| 100 | [swagger-api/apidom](https://github.com/swagger-api/apidom) | — | topic=parser (+3 tooling/library); text~tool (+2 tooling/... | Semantic parser for API specifications |
| 95 | [pproenca/agent-tui](https://github.com/pproenca/agent-tui) | — | topic=cli (+3 tooling/library); text~tool (+2 tooling/lib... | TUI automation for AI agents. Control any terminal app from code. |
| 89 | [swaggest/go-asyncapi](https://github.com/swaggest/go-asyncapi) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) | AsyncAPI spec from Go code |
| 81 | [asyncapi/java-spring-template](https://github.com/asyncapi/java-spring-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Java Spring template for the AsyncAPI Generator |
| 76 | [confluentinc/cli](https://github.com/confluentinc/cli) | — | topic=platform,schema-registry (+3 product); topic=cli (+... | CLI for Confluent Cloud and Confluent Platform |
| 58 | [asyncapi/go-watermill-template](https://github.com/asyncapi/go-watermill-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Go template for the AsyncAPI Generator using Watermill module |
| 57 | [vitalets/tinkoff-invest-api](https://github.com/vitalets/tinkoff-invest-api) | — | text~tool (+2 tooling/library) | Node.js SDK для работы с Tinkoff Invest API |
| 56 | [marle3003/mokapi](https://github.com/marle3003/mokapi) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Your API mocking tool for OpenAPI and AsyncAPI using Go and JavaScr... |
| 55 | [SmartBear/swaggerhub-cli](https://github.com/SmartBear/swaggerhub-cli) | — | topic=cli (+3 tooling/library); topic=saas (+3 product); ... | SwaggerHub CLI |
| 51 | [WaleedAshraf/asyncapi-validator](https://github.com/WaleedAshraf/asyncapi-validator) | — | topic=validator (+3 tooling/library); topic=asyncapi-spec... | Message validator for Kafka/RabbitMQ/Anything through AsyncAPI schema |
| 50 | [OkieOth/yacg](https://github.com/OkieOth/yacg) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | yet another code generation |
| 47 | [dweber019/backstage-plugins](https://github.com/dweber019/backstage-plugins) | — | text~tool (+2 tooling/library); text~product (+2 product) | A collection of Backstage plugins |
| 46 | [christian-photo/ninaAPI](https://github.com/christian-photo/ninaAPI) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs) | A webapi (and websocket) to control N.I.N.A. |
| 46 | [dutradda/asyncapi-python](https://github.com/dutradda/asyncapi-python) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Publish events using broadcaster lib from asyncapi specification |
| 43 | [SDA-SE/sda-dropwizard-commons](https://github.com/SDA-SE/sda-dropwizard-commons) | — | topic=microservice (+3 product); topic=framework (+3 tool... | A set of libraries to bootstrap services easily that follow the pat... |
| 39 | [canton-network/wallet](https://github.com/canton-network/wallet) | — | text~tool (+2 tooling/library); text~product (+2 product) | Wallet Gateway |
| 36 | [asyncapi/java-spring-cloud-stream-template](https://github.com/asyncapi/java-spring-cloud-stream-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Java Spring Cloud Stream template for the AsyncAPI Generator |
| 36 | [Verdenroz/finance-query](https://github.com/Verdenroz/finance-query) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Open-source API for financial data. Get quotes, historical data, te... |
| 35 | [climateandtech/report-analyst](https://github.com/climateandtech/report-analyst) | — | topic=climate,climate-change,climate-change-adaptation,cl... | OpenSustainabilityAnalyst ReportAnalyst is an open-source / open-co... |
| 34 | [the-codegen-project/cli](https://github.com/the-codegen-project/cli) | — | topic=generator,openapi-generator,the-codegen-project (+3... | Your one stop boilerplate killer for any standard! |
| 33 | [asyncapi/avro-schema-parser](https://github.com/asyncapi/avro-schema-parser) | — | topic=avro-schema (+3 spec/docs); topic=parser (+3 toolin... | An AsyncAPI schema parser for Avro 1.x schemas. |
| 32 | [asyncapi/bundler](https://github.com/asyncapi/bundler) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Combine multiple AsyncAPI specification files into one. |
| 30 | [asyncapi/python-paho-template](https://github.com/asyncapi/python-paho-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Python Paho template for the AsyncAPI generator |
| 29 | [SchwarzIT/api-linter-rules](https://github.com/SchwarzIT/api-linter-rules) | — | topic=linting-rules (+3 tooling/library); text~tool (+2 t... | Schwarz API rule definitions for the Spectral API linter |
| 28 | [holstein13/mcp-config-manager](https://github.com/holstein13/mcp-config-manager) | — | topic=preset-application (+3 product); topic=cli (+3 tool... | Manage MCP server configs across Claude, Gemini & other AI systems.... |
| 25 | [metaseller/tinkoff-invest-api-v2-php](https://github.com/metaseller/tinkoff-invest-api-v2-php) | — | topic=sdk-php,t-invest-php-sdk,tinkoff-sdk (+3 tooling/li... | Неофициальный PHP7 SDK для работы с API Т-Инвестиций v2 через GRPC |
| 24 | [G-USI/asyncapi-python](https://github.com/G-USI/asyncapi-python) | — | topic=asyncapi-schemas,asyncapi-specification (+3 spec/do... | A command line interface to generate python code from asyncapi spec |
| 24 | [MTSWebServices/ApiCodeGenerator](https://github.com/MTSWebServices/ApiCodeGenerator) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | Generate code from Swagger, OpenApi or AsyncApi documents. |
| 22 | [tromgy/swagger-yaml-to-json-schema](https://github.com/tromgy/swagger-yaml-to-json-schema) | — | topic=schema (+3 spec/docs); text~tool (+2 tooling/librar... | Node.js CLI tool to generate JSON schema from Swagger YAML file |
| 19 | [asyncapi/openapi-schema-parser](https://github.com/asyncapi/openapi-schema-parser) | — | topic=parser (+3 tooling/library); text~tool (+2 tooling/... | An AsyncAPI schema parser for OpenAPI 3.0.x and Swagger 2.x schemas. |
| 17 | [grafana/backstage-plugin-grafana-catalog](https://github.com/grafana/backstage-plugin-grafana-catalog) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 16 | [asyncapi/jasyncapi-idea-plugin](https://github.com/asyncapi/jasyncapi-idea-plugin) | — | topic=asyncapi-schemas,asyncapi-specification (+3 spec/do... | /jay-sync-api/-idea-plugin is a IDEA plugin for AsyncAPI specificat... |
| 16 | [specmesh/specmesh-build](https://github.com/specmesh/specmesh-build) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 15 | [Axway/agent-sdk](https://github.com/Axway/agent-sdk) | — | topic=sdk-go (+3 tooling/library); text~tool (+2 tooling/... | A development kit for building agents (Discovery / Traceability) th... |
| 14 | [yojo-generator/generator](https://github.com/yojo-generator/generator) | — | topic=asyncapi-generator,yaml-parser (+3 tooling/library)... | This project is a core-library for generate POJO's from asyncApi ya... |
| 13 | [asyncapi/dotnet-rabbitmq-template](https://github.com/asyncapi/dotnet-rabbitmq-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | This template is for generating a .NET C# wrapper for the RabbitMQ ... |
| 12 | [8cH9azbsFifZ/hangboard](https://github.com/8cH9azbsFifZ/hangboard) | — | topic=climbing (+3 tooling/library); text~demo (+2 demo/f... | A universal force and velocity sensing hangboard mount with exercis... |
| 12 | [eBay/event-notification-java-sdk](https://github.com/eBay/event-notification-java-sdk) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 12 | [trustedshops-public/schema2pyarrow](https://github.com/trustedshops-public/schema2pyarrow) | — | topic=jsonschema,schema (+3 spec/docs); text~tool (+2 too... | Converts AsyncApi and JsonSchema to PyArrow schema |
| 11 | [aml-org/amf](https://github.com/aml-org/amf) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | AMF (AML Modeling Framework) is an open-source library capable of p... |
| 11 | [arielril/hexagonal-architecture](https://github.com/arielril/hexagonal-architecture) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Repository that contains some project that have been designed follo... |
| 11 | [asyncapi/protobuf-schema-parser](https://github.com/asyncapi/protobuf-schema-parser) | — | topic=schema (+3 spec/docs); topic=parser (+3 tooling/lib... | Schema parser for Protobuf compatible with AsyncAPI JS Parser |
| 10 | [IntelIP/Neural](https://github.com/IntelIP/Neural) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Kalshi-first SDK for prediction market trading |
| 10 | [ivamuno/redoc-asyncapi](https://github.com/ivamuno/redoc-asyncapi) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 10 | [kdcube/kdcube-ai-app](https://github.com/kdcube/kdcube-ai-app) | — | topic=agent-framework,copilot-sdk (+3 tooling/library); t... | Ship customer-facing AI with isolation, spend controls, and provena... |
| 10 | [Programmierpraktikum-MVA/AsyncAPI](https://github.com/Programmierpraktikum-MVA/AsyncAPI) | — | text~tool (+2 tooling/library); text~product (+2 product)... | 🔥 Generates a blazingly fast ⚡️ microservice in Rust 🦀, from an asy... |
| 9 | [firestoned/firestone](https://github.com/firestoned/firestone) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 9 | [openxapi/openxapi](https://github.com/openxapi/openxapi) | — | topic=sdk (+3 tooling/library); text~tool (+2 tooling/lib... | OpenAPI and AsyncAPI specifications for cryptocurrency exchanges an... |
| 9 | [SaaSy-Solutions/mockforge](https://github.com/SaaSy-Solutions/mockforge) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | Comprehensive mocking framework for REST, gRPC, GraphQL & WebSocket... |
| 9 | [yojo-generator/gradle-plugin](https://github.com/yojo-generator/gradle-plugin) | — | topic=code-generation,code-generator,gradle-plugin (+3 to... | This is gradle-plugin for spring-boot application. |
| 8 | [TIBCOSoftware/cic-cli-plugin-asyncapi](https://github.com/TIBCOSoftware/cic-cli-plugin-asyncapi) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | CLI Plugin for transforming AsyncAPI specs into flogo templates |
| 7 | [thim81/asyncapi-format](https://github.com/thim81/asyncapi-format) | — | topic=cli (+3 tooling/library); text~tool (+2 tooling/lib... | Format an AsyncAPI document by ordering, formatting and filtering f... |
| 7 | [xraph/forge](https://github.com/xraph/forge) | — | text~tool (+2 tooling/library); text~product (+2 product)... | A very opionated distributed backend framework with everything in b... |
| 6 | [eclipse-thingweb/td-tools](https://github.com/eclipse-thingweb/td-tools) | — | topic=iot (+3 product); text~tool (+2 tooling/library); s... | Utility libraries for W3C Thing Descriptions and Thing Models |
| 6 | [Sanix-Darker/skill-md.dev](https://github.com/Sanix-Darker/skill-md.dev) | — | text~tool (+2 tooling/library); text~product (+2 product)... | skill-md |
| 5 | [CreditMutuelArkea/asyncapi-parser](https://github.com/CreditMutuelArkea/asyncapi-parser) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 5 | [hatchbed/opensw](https://github.com/hatchbed/opensw) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Open source client SDK for communicating with SlamTec Slamware devices |
| 5 | [openpx-trade/openpx](https://github.com/openpx-trade/openpx) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 4 | [asyncapi-go/asyncapigo](https://github.com/asyncapi-go/asyncapigo) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | AsyncAPI spec generator from Golang code |
| 4 | [AsyncAPITools/parser-java-wrapper](https://github.com/AsyncAPITools/parser-java-wrapper) | — | topic=parser,validator (+3 tooling/library); text~tool (+... | AsyncAPI Parser Java Wrapper ( over JavaScript Parser ) |
| 4 | [deltaeight/ma2-websocket-api](https://github.com/deltaeight/ma2-websocket-api) | — | text~tool (+2 tooling/library); lang=None (+1 spec/docs) | A documentation of the GrandMA 2 websocket API |
| 4 | [derberg/shrekapp-asyncapi-designed](https://github.com/derberg/shrekapp-asyncapi-designed) | — | topic=code-generation,codegen (+3 tooling/library); topic... | This repository stores a WebSocket project designed with AsyncAPI. ... |
| 4 | [Elhebert/asyncapi-validation](https://github.com/Elhebert/asyncapi-validation) | — | topic=validator (+3 tooling/library); topic=asyncapi-spec... | Message validation package from YAML and JSON AsyncAPI document |
| 4 | [jjunho/HsJupyter](https://github.com/jjunho/HsJupyter) | — | text~tool (+2 tooling/library) |  |
| 4 | [timonback/asyncapi-portal](https://github.com/timonback/asyncapi-portal) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 3 | [aml-org/amf-custom-validator](https://github.com/aml-org/amf-custom-validator) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 3 | [apiaddicts/sonar-asyncapi](https://github.com/apiaddicts/sonar-asyncapi) | — | text~tool (+2 tooling/library) | Code analyzer for AsyncAPI specifications |
| 3 | [arih1299/solacedemo-kafkasummitapac2021](https://github.com/arih1299/solacedemo-kafkasummitapac2021) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 3 | [bitsy-ai/printnanny-webapp](https://github.com/bitsy-ai/printnanny-webapp) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 3 | [c0olix/asyncApiCodeGen](https://github.com/c0olix/asyncApiCodeGen) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 3 | [Chief-Strategist-J/llm-observability-platform](https://github.com/Chief-Strategist-J/llm-observability-platform) | — | topic=clickhouse (+3 tooling/library); text~product (+2 p... | High-performance LLM observability and evaluation platform with aut... |
| 3 | [code-lab-org/nost-tools](https://github.com/code-lab-org/nost-tools) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | Novel Observing Strategies Testbed Tools |
| 3 | [David-DAM/kafka-cero-a-experto](https://github.com/David-DAM/kafka-cero-a-experto) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Proyecto final del curso Spring Boot Async de cero a Experto |
| 3 | [hazamashoken/ft_trancendence](https://github.com/hazamashoken/ft_trancendence) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 3 | [hkirat/asyncapi-fork](https://github.com/hkirat/asyncapi-fork) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) |  |
| 3 | [MEF-GIT/MEF-LSO-Legato-SDK](https://github.com/MEF-GIT/MEF-LSO-Legato-SDK) | — | topic=sdk (+3 tooling/library); text~tool (+2 tooling/lib... |  The SDK includes APIs for Service Catalog, Service Order, Service ... |
| 3 | [meteatamel/asyncapi-basics](https://github.com/meteatamel/asyncapi-basics) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | This repository contains information, references, and samples about... |
| 3 | [Mrc0113/asyncapi-codegen-scst](https://github.com/Mrc0113/asyncapi-codegen-scst) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Code Artifacts used for AsyncAPI Code Generation Blog + Video |
| 3 | [rpeyron/plugin-drawio-editors](https://github.com/rpeyron/plugin-drawio-editors) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 3 | [v08nike/Cli-Node](https://github.com/v08nike/Cli-Node) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 3 | [WaYdotNET/zen-generator](https://github.com/WaYdotNET/zen-generator) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | A bidirectional Python code generator that converts between AsyncAP... |
| 3 | [yankeeinlondon/rusty-biscuit](https://github.com/yankeeinlondon/rusty-biscuit) | — | text~tool (+2 tooling/library) | A monorepo for AI-powered research and automation tools |
| 2 | [amer8/apibconv](https://github.com/amer8/apibconv) | — | topic=cli,converter (+3 tooling/library); spec-only-in-fi... | Convert between API Blueprint (*.apib), OpenAPI 2.0/3.0.x/3.1.x, an... |
| 2 | [canton-network/cf-docs](https://github.com/canton-network/cf-docs) | — | text~tool (+2 tooling/library); text~product (+2 product)... | home for the new unified Canton Foundation docs |
| 2 | [durable-workflow/durable-workflow.github.io](https://github.com/durable-workflow/durable-workflow.github.io) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Documentation website for Durable Workflow, built with Docusaurus a... |
| 2 | [GreenRover/proto-schema-parser](https://github.com/GreenRover/proto-schema-parser) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | ProtoBuff parser for AsyncApi |
| 2 | [ingka-group/asyncapi-payload-validator](https://github.com/ingka-group/asyncapi-payload-validator) | — | topic=jinja2-templates (+3 demo/fixture); topic=cli (+3 t... | A Python library and CLI for validating message payloads against As... |
| 2 | [jonaslagoni/asyncapi-miniseries](https://github.com/jonaslagoni/asyncapi-miniseries) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | This repository contains all resources related to the mini series a... |
| 2 | [ripple/rippled-api-spec](https://github.com/ripple/rippled-api-spec) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A repository for OpenAPI / AsyncAPI specifications. This ideally ev... |
| 2 | [servaasvdc/whatstack](https://github.com/servaasvdc/whatstack) | — | topic=cli (+3 tooling/library); spec-only-in-fixtures (+1... | whatstack detects the tech stack of a project. Built for humans and... |
| 2 | [siom79/jasyncapicmp](https://github.com/siom79/jasyncapicmp) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs) | jasyncapicmp is a tool to compare two versions of a asyncapi specif... |
| 2 | [TemplateMechanics/tilt](https://github.com/TemplateMechanics/tilt) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Tilt File Examples |
| 2 | [TykTechnologies/graphql-translator](https://github.com/TykTechnologies/graphql-translator) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | graphql-translator is a library that takes OpenAPI and AsyncAPI doc... |
| 1 | [advanced-rest-client/api-endpoint-documentation](https://github.com/advanced-rest-client/api-endpoint-documentation) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | ⛔️ DEPRECATED This component is being deprecated. Use `api-document... |
| 1 | [advanced-rest-client/api-request](https://github.com/advanced-rest-client/api-request) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | ⛔️ DEPRECATED This component is being deprecated. Use `@api-compone... |
| 1 | [ArabotHXL/BTC_project](https://github.com/ArabotHXL/BTC_project) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 1 | [Arkhe-Network/Arkhe-OS](https://github.com/Arkhe-Network/Arkhe-OS) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | ASI |
| 1 | [coiouhkc/asyncapi-generator](https://github.com/coiouhkc/asyncapi-generator) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 1 | [Contio-AI/partner-sdk](https://github.com/Contio-AI/partner-sdk) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | Official TypeScript/JavaScript SDK for integrating with the Contio ... |
| 1 | [ff-fab/cosalette](https://github.com/ff-fab/cosalette) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | An opinionated Python framework for building IoT-to-MQTT bridge app... |
| 1 | [imaginestudio-ai/golang-ninja](https://github.com/imaginestudio-ai/golang-ninja) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  This repository contains a collection of tutorials and hands-on pr... |
| 1 | [Jacksonspencerd/tcss559-project](https://github.com/Jacksonspencerd/tcss559-project) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 1 | [JonathanGrocott/A2A-MQTT](https://github.com/JonathanGrocott/A2A-MQTT) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Agent to agent protocol using MQTT |
| 1 | [konfig-dev/backstage-plugin-konfig](https://github.com/konfig-dev/backstage-plugin-konfig) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | Generate SDKs for APIs in Backstage. |
| 1 | [MEF-GIT/MEF-LSO-Allegro-SDK](https://github.com/MEF-GIT/MEF-LSO-Allegro-SDK) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... | This repository contains the MEF LSO Allegro SDK.  |
| 1 | [n1md7/IoT-Device-Manager](https://github.com/n1md7/IoT-Device-Manager) | — | text~tool (+2 tooling/library); text~product (+2 product)... | IoT device manager with microcontroller clients such as Arduino(uno... |
| 1 | [nikolay-e/diffctx](https://github.com/nikolay-e/diffctx) | — | topic=cli (+3 tooling/library); spec-only-in-fixtures (+1... | Smart git diff context for LLMs - selects the minimal code fragment... |
| 1 | [panovps/t-invest-api](https://github.com/panovps/t-invest-api) | — | text~tool (+2 tooling/library); lang=HTML (+1 spec/docs) | Node.js SDK for Tinkoff Invest API |
| 1 | [solace-cto-labs/solace-amplify-discovery-agent](https://github.com/solace-cto-labs/solace-amplify-discovery-agent) | — | text~tool (+2 tooling/library); text~product (+2 product) | Solace-Amplify-Discovery-Agent for synchronizing Solace AsyncAPIs w... |
| 1 | [SolaceLabs/solace-ep-codegen](https://github.com/SolaceLabs/solace-ep-codegen) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 1 | [specmesh/getting-started-apachekafka](https://github.com/specmesh/getting-started-apachekafka) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 1 | [supermodel/asyncapi-cli](https://github.com/supermodel/asyncapi-cli) | — | topic=asyncapi-specification,json-schema (+3 spec/docs); ... | Simple CLI to validate Async API documents |
| 1 | [ThomasWimprine/LangChangeWorkflows](https://github.com/ThomasWimprine/LangChangeWorkflows) | — | text~tool (+2 tooling/library); text~product (+2 product)... | LangGraph-based PRP workflow orchestration with multi-agent coordin... |
| 0 | [4g3nt4333/Ascy-website](https://github.com/4g3nt4333/Ascy-website) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [actions-marketplace-validations/asyncapi_github-action-for-generator](https://github.com/actions-marketplace-validations/asyncapi_github-action-for-generator) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [advanced-rest-client/amf-helper-mixin](https://github.com/advanced-rest-client/amf-helper-mixin) | — | text~tool (+2 tooling/library) | ⛔️ DEPRECATED This component is being deprecated. Use `@api-compone... |
| 0 | [advanced-rest-client/api-body-document](https://github.com/advanced-rest-client/api-body-document) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | ⛔️ DEPRECATED This component is being deprecated. Use `api-document... |
| 0 | [advanced-rest-client/api-documentation](https://github.com/advanced-rest-client/api-documentation) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs);... | ⛔️ DEPRECATED This component is being deprecated. Use `@api-compone... |
| 0 | [advanced-rest-client/api-headers-document](https://github.com/advanced-rest-client/api-headers-document) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | ⛔️ DEPRECATED This component is being deprecated. Use `api-document... |
| 0 | [advanced-rest-client/api-method-documentation](https://github.com/advanced-rest-client/api-method-documentation) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs);... | ⛔️ DEPRECATED This component is being deprecated. Use `api-document... |
| 0 | [api-components/api-model-generator](https://github.com/api-components/api-model-generator) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | AMF model generator for API components |
| 0 | [api-now/amf-store](https://github.com/api-now/amf-store) | — | text~tool (+2 tooling/library) | A library to work with the AMF parser and model in a web worker. Ex... |
| 0 | [AravindRTW/APIStrategyPOC](https://github.com/AravindRTW/APIStrategyPOC) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | StyleGuide as Code |
| 0 | [arc-archive/api-navigation](https://github.com/arc-archive/api-navigation) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | ⛔️ DEPRECATED This component is being deprecated. Use `@api-compone... |
| 0 | [arc-archive/api-request-panel](https://github.com/arc-archive/api-request-panel) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | This component has been moved to api-request. Use the other one ins... |
| 0 | [arc-framework/arc-platform](https://github.com/arc-framework/arc-platform) | — | text~tool (+2 tooling/library); text~product (+2 product) | The official production monorepo for A.R.C. Houses the "Brain" (Pyt... |
| 0 | [Arcanon-hub/arcanon-scanner](https://github.com/Arcanon-hub/arcanon-scanner) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [ArshdevSinghji/iffy-backend](https://github.com/ArshdevSinghji/iffy-backend) | — | text~tool (+2 tooling/library); text~product (+2 product) | Iffy is a location-based dating app built with a modular monolith b... |
| 0 | [ashtanko/log4fit-api](https://github.com/ashtanko/log4fit-api) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Log4Fit is a backend application for an exercise tracking platform,... |
| 0 | [asyncapi-actions-testing/website](https://github.com/asyncapi-actions-testing/website) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | clone of website for testing |
| 0 | [BidnessForB/postman-sdk](https://github.com/BidnessForB/postman-sdk) | — | topic=postman-sdk,sdk (+3 tooling/library); text~tool (+2... | SDK for Postman API in NodeJS |
| 0 | [Bikxs/Skafu](https://github.com/Bikxs/Skafu) | — | text~tool (+2 tooling/library); text~product (+2 product) | AI-powered microservices scaffolding platform that generates enterp... |
| 0 | [charlie-haley/asyncapi-go](https://github.com/charlie-haley/asyncapi-go) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Go library for parsing and working with AsyncAPI specifications.  |
| 0 | [ChunPingWang/saga-axon](https://github.com/ChunPingWang/saga-axon) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [chvanam/fdp-rust-manifest](https://github.com/chvanam/fdp-rust-manifest) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 0 | [claudioed/equipment-metadata](https://github.com/claudioed/equipment-metadata) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [codacy/codacy-spectral](https://github.com/codacy/codacy-spectral) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Codacy Tool for Spectral |
| 0 | [coiouhkc/asyncapi-generator-examples](https://github.com/coiouhkc/asyncapi-generator-examples) | — | text~tool (+2 tooling/library); name~demo (+2 demo/fixtur... |  |
| 0 | [conversales/convai-widget-embed](https://github.com/conversales/convai-widget-embed) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) |  |
| 0 | [CoolSpy3/CSPackets](https://github.com/CoolSpy3/CSPackets) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | An implementation of most 1.8.9 Minecraft packets for use with CSMo... |
| 0 | [crustacgen/asyncapi-rust-generator](https://github.com/crustacgen/asyncapi-rust-generator) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [dataGriff/contract.catalog](https://github.com/dataGriff/contract.catalog) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [dataGriff/contracts.cli](https://github.com/dataGriff/contracts.cli) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A cli tool that allows you to interact with different contract types |
| 0 | [davesienkowski/mastercontrol-apidocs-conversion](https://github.com/davesienkowski/mastercontrol-apidocs-conversion) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... |  |
| 0 | [deathbycaptcha/deathbycaptcha-agent-api-metadata](https://github.com/deathbycaptcha/deathbycaptcha-agent-api-metadata) | — | topic=api-client (+3 tooling/library); text~tool (+2 tool... | Deathbycaptcha main http and sockets api IA agent metadata |
| 0 | [DEFRA/ahwr-message-generator-backend](https://github.com/DEFRA/ahwr-message-generator-backend) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Git repository for service ahwr-message-generator-backend |
| 0 | [DEFRA/ffc-pay-request-editor](https://github.com/DEFRA/ffc-pay-request-editor) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Edit payment requests |
| 0 | [DevOpsMadDog/aldeci_core](https://github.com/DevOpsMadDog/aldeci_core) | — | text~tool (+2 tooling/library); text~product (+2 product)... | ALDECI core — cleaned source snapshot (no legacy docs/contexts). AI... |
| 0 | [dimonoff/asyncapi-codegen](https://github.com/dimonoff/asyncapi-codegen) | — | text~tool (+2 tooling/library); text~product (+2 product)... | An AsyncAPI Golang Code generator that generates all Go code from t... |
| 0 | [edward-hsu-1994/asyncapi-viewer](https://github.com/edward-hsu-1994/asyncapi-viewer) | — | text~tool (+2 tooling/library); text~product (+2 product) | ref. https://github.com/asyncapi/asyncapi-react |
| 0 | [edwmurph/api-docs](https://github.com/edwmurph/api-docs) | — | text~tool (+2 tooling/library); name~spec (+1 spec/docs) |  |
| 0 | [ekozynin/asyncapi-kafka-template](https://github.com/ekozynin/asyncapi-kafka-template) | — | AsyncAPI Generator codegen-template (tooling, not demo) | Confluent Kafka template for the AsyncAPI Generator |
| 0 | [encypher-studio/newsware-docs](https://github.com/encypher-studio/newsware-docs) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Frontend for user documentation of the Newsware clients to interact... |
| 0 | [ep-infosec/14_mulesoft_api-console](https://github.com/ep-infosec/14_mulesoft_api-console) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ep-infosec/35_mulesoft_api-console](https://github.com/ep-infosec/35_mulesoft_api-console) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [Flissel/Coding_engine](https://github.com/Flissel/Coding_engine) | — | topic=code-generation (+3 tooling/library); text~tool (+2... | Society of Mind autonomous code generation platform — 37+ AI agents... |
| 0 | [Flissel/DaveFelix-Coding-Engine](https://github.com/Flissel/DaveFelix-Coding-Engine) | — | text~tool (+2 tooling/library); text~product (+2 product) | Engine for generating code snippets and templates. |
| 0 | [fraunhoferfokus/dredger](https://github.com/fraunhoferfokus/dredger) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [fulmenhq/goneat](https://github.com/fulmenhq/goneat) | — | text~tool (+2 tooling/library); text~product (+2 product)... | All about smoothly delivering neat code at scale |
| 0 | [funny-bunny-corp/ledger](https://github.com/funny-bunny-corp/ledger) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [gedeondt/reatilerworkflow-charla](https://github.com/gedeondt/reatilerworkflow-charla) | — | text~tool (+2 tooling/library) |  |
| 0 | [GeniaV/stellar-burgers-backend](https://github.com/GeniaV/stellar-burgers-backend) | — | topic=cookie-parser (+3 tooling/library); text~product (+... | :dog: :hamburger: Backend for Stellar Burgers Project (pet project) |
| 0 | [GreenRover/async-api-validator](https://github.com/GreenRover/async-api-validator) | — | text~product (+2 product); name~tool (+1 tooling/library)... |  |
| 0 | [gregoriocarranza/APPS-II-Core-Backend](https://github.com/gregoriocarranza/APPS-II-Core-Backend) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [H1lp0p/fins-web](https://github.com/H1lp0p/fins-web) | — | text~tool (+2 tooling/library) |  |
| 0 | [hasathcharu/ballerina-websockets-test](https://github.com/hasathcharu/ballerina-websockets-test) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [hschaffner/AsyncAPI_Test](https://github.com/hschaffner/AsyncAPI_Test) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Test to use AsyncAPI and Solace code generator to create Spring Clo... |
| 0 | [iqb-specifications/response](https://github.com/iqb-specifications/response) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | Data output of assessments |
| 0 | [isurunix/async-api-message-validator](https://github.com/isurunix/async-api-message-validator) | — | text~tool (+2 tooling/library); text~product (+2 product)... | An AsyncAPI validation server with web interface that supports both... |
| 0 | [jamarcer/openapi-schema-parsers](https://github.com/jamarcer/openapi-schema-parsers) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | OpenAPI / AsyncApi parser utilities |
| 0 | [joefrancisGA/ArchLucid](https://github.com/joefrancisGA/ArchLucid) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [jpxcz/websocket_template_nodejs](https://github.com/jpxcz/websocket_template_nodejs) | — | text~tool (+2 tooling/library); text~product (+2 product)... | NodeJs + Fastify + AsyncApi for documentation generator |
| 0 | [jrcryer/evently-codegen](https://github.com/jrcryer/evently-codegen) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [jstoiko/amf](https://github.com/jstoiko/amf) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AMF (AML Modeling Framework) is an open-source library capable of p... |
| 0 | [junjiepro/mango](https://github.com/junjiepro/mango) | — | text~tool (+2 tooling/library) |  |
| 0 | [kaje94/choreo-connect-test](https://github.com/kaje94/choreo-connect-test) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [kwontaeim/event-notification-java-sdk](https://github.com/kwontaeim/event-notification-java-sdk) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | event-notification-java-sdk test repo |
| 0 | [Leonardo-Santos-oficial/jose-diego](https://github.com/Leonardo-Santos-oficial/jose-diego) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [Lur1an/schema2code](https://github.com/Lur1an/schema2code) | — | text~tool (+2 tooling/library) | Build tool to generate classes/structs to serialize/deserialize asy... |
| 0 | [MakShuk/t-invest-grpc-sdk](https://github.com/MakShuk/t-invest-grpc-sdk) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [Matusko/flea](https://github.com/Matusko/flea) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [MEF-GIT/MEF-LSO-Interlude-SDK](https://github.com/MEF-GIT/MEF-LSO-Interlude-SDK) | — | topic=sdk (+3 tooling/library); text~tool (+2 tooling/lib... |  |
| 0 | [nanoyan/metadata-store](https://github.com/nanoyan/metadata-store) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [Netcracker/qubership-apihub-api-processor](https://github.com/Netcracker/qubership-apihub-api-processor) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... |  |
| 0 | [nikita-volkov/modeliero](https://github.com/nikita-volkov/modeliero) | — | topic=json-schema (+3 spec/docs); topic=code-generation (... | Swiss army knife for model code-generation (in beta) |
| 0 | [obedito-lab/document-services-s](https://github.com/obedito-lab/document-services-s) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [omiga-group/omiga](https://github.com/omiga-group/omiga) | — | text~tool (+2 tooling/library) | Omiga |
| 0 | [online-bridge-hackathon/gcp-cf-docsgen](https://github.com/online-bridge-hackathon/gcp-cf-docsgen) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | GCP Cloud Function to generate API Docs |
| 0 | [Pakisan/jasyncapi-idea-plugin-demo](https://github.com/Pakisan/jasyncapi-idea-plugin-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Repository to show how AsyncAPI specification works in JetBrains IDE |
| 0 | [panand13/backstage](https://github.com/panand13/backstage) | — | text~tool (+2 tooling/library); text~product (+2 product) |  |
| 0 | [pascal-audio/px-api](https://github.com/pascal-audio/px-api) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Public JSON-RPC based API for PX-Series |
| 0 | [philCryoport/jasyncapi-idea-plugin](https://github.com/philCryoport/jasyncapi-idea-plugin) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | /jay-sync-api/-idea-plugin is a IDEA plugin for AsyncAPI specificat... |
| 0 | [PlutoneonConsultancy/api-console](https://github.com/PlutoneonConsultancy/api-console) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Plutoneon - API Console \| Andrew J. Shepherd presents API design d... |
| 0 | [prichelle/prichelle.github.io](https://github.com/prichelle/prichelle.github.io) | — | text~tool (+2 tooling/library) |  |
| 0 | [qmg-vgalcenco/asyncapi-validator](https://github.com/qmg-vgalcenco/asyncapi-validator) | — | text~tool (+2 tooling/library); name~tool (+1 tooling/lib... |  |
| 0 | [rahulmehta25/Smart-Legal-Contracts](https://github.com/rahulmehta25/Smart-Legal-Contracts) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... |  |
| 0 | [rakeshmani35/springboot-openAPI](https://github.com/rakeshmani35/springboot-openAPI) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [ravecat/asyncapi](https://github.com/ravecat/asyncapi) | — | text~tool (+2 tooling/library); spec-only-in-fixtures (+1... | AsyncAPI to TypeScript and Zod code generator |
| 0 | [sekharbans-ebay/event-notification-sdk](https://github.com/sekharbans-ebay/event-notification-sdk) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [siom79/jopenapicmp](https://github.com/siom79/jopenapicmp) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs) | Comparison of two versions of an OpenAPI document |
| 0 | [SolaceLabs/ep-asyncapi](https://github.com/SolaceLabs/ep-asyncapi) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [SolaceLabs/solace-ansible-plugin](https://github.com/SolaceLabs/solace-ansible-plugin) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Test Ansible Playbooks using Solace Ansible Galaxy |
| 0 | [SolaceLabs/solace-jenkins-plugin](https://github.com/SolaceLabs/solace-jenkins-plugin) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | Contains AsyncAPI sample files to use for testing with AWX/Ansible ... |
| 0 | [SolaceLabs/solace-tryme-cli-mcp-server](https://github.com/SolaceLabs/solace-tryme-cli-mcp-server) | — | text~tool (+2 tooling/library); text~product (+2 product)... | MCP server for solace-tryme-cli |
| 0 | [sroigmas/asyncapi](https://github.com/sroigmas/asyncapi) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixture) | Small practice of AsyncAPI definition and Spring code generation |
| 0 | [UTXOnly/oddrip](https://github.com/UTXOnly/oddrip) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | Go Kalshi API client |
| 0 | [verona-interfaces/editor](https://github.com/verona-interfaces/editor) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Interface for task/unit authoring applications |
| 0 | [viruskizz/42bangkok_ft-transcendence](https://github.com/viruskizz/42bangkok_ft-transcendence) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [yuvraj-chouhan-dev/ready-now-server](https://github.com/yuvraj-chouhan-dev/ready-now-server) | — | text~tool (+2 tooling/library); text~product (+2 product)... | ready now SDK Backend server |
| 0 | [Zenika/kafka-schema-registry-publish](https://github.com/Zenika/kafka-schema-registry-publish) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Publish schemas to your schemas registry using CI-CD |
| 0 | [ZiyamSanthosh/AsyncApiAmf](https://github.com/ZiyamSanthosh/AsyncApiAmf) | — | text~tool (+2 tooling/library); spec-at-root/docs (+1 pro... | A project to try the combination of AsyncAPI and AMF parser |

## demo/fixture (217)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 2734 | [event-catalog/eventcatalog](https://github.com/event-catalog/eventcatalog) | — | topic=event-driven-architecture,microservices (+3 product... | The discovery and governance layer for event-driven systems. Docume... |
| 455 | [PacktPublishing/Event-Driven-Architecture-in-Golang](https://github.com/PacktPublishing/Event-Driven-Architecture-in-Golang) | — | text~demo-strong (+3 demo/fixture) | Event-Driven Architecture in Golang, published by Packt |
| 217 | [ibm-messaging/mq-dev-patterns](https://github.com/ibm-messaging/mq-dev-patterns) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) | Code samples and messaging patterns for IBM MQ developers |
| 172 | [Mermade/openapi-filter](https://github.com/Mermade/openapi-filter) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); sp... | Filter internal paths, operations, parameters, schemas etc from Ope... |
| 144 | [open-data-fabric/open-data-fabric](https://github.com/open-data-fabric/open-data-fabric) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Open protocol for decentralized exchange and transformation of data |
| 68 | [PacktPublishing/Software-Architecture-with-Cpp-2E](https://github.com/PacktPublishing/Software-Architecture-with-Cpp-2E) | — | text~demo-strong (+3 demo/fixture) | Software Architecture with C++, Second Edition, Published by Packt |
| 60 | [DataDog/serverless-sample-app](https://github.com/DataDog/serverless-sample-app) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Explore Datadog's serverless observability features with this sampl... |
| 51 | [WebFuzzing/Dataset](https://github.com/WebFuzzing/Dataset) | — | topic=enterprise-applications (+3 product); topic=benchma... | Web Fuzzing Dataset (WFD): a set of web/enterprise applications for... |
| 51 | [wso2/choreo-samples](https://github.com/wso2/choreo-samples) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | This will contain integration and service samples displayed in choreo. |
| 50 | [launchany/addr-examples](https://github.com/launchany/addr-examples) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Examples of the Align-Define-Design-Define (ADDR) API process |
| 48 | [agiopen-org/lux-desktop](https://github.com/agiopen-org/lux-desktop) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 42 | [microcks/api-lifecycle](https://github.com/microcks/api-lifecycle) | — | topic=demo (+3 demo/fixture); text~demo (+2 demo/fixture)... | Full lifecycle demonstration on Microcks usages |
| 33 | [schetinnikov-otus/arch-labs](https://github.com/schetinnikov-otus/arch-labs) | — | name~demo (+2 demo/fixture) |  |
| 29 | [microcks/microcks-testcontainers-java-spring-demo](https://github.com/microcks/microcks-testcontainers-java-spring-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Spring Boot demonstration app on how to use Microcks Testcontainers... |
| 24 | [allenheltondev/serverless-websockets](https://github.com/allenheltondev/serverless-websockets) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Get started with websockets with this serverless solution |
| 23 | [Kong/developer.konghq.com](https://github.com/Kong/developer.konghq.com) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) | 🦍 Source code for developer.konghq.com website. |
| 21 | [Raiffeisen-DGTL/rest-api-guide](https://github.com/Raiffeisen-DGTL/rest-api-guide) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | В этом репозитории находится REST API Best Practices. |
| 20 | [maarten-vandeperre/developer-hub-documentation](https://github.com/maarten-vandeperre/developer-hub-documentation) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 19 | [SDA-SE/sda-spring-boot-commons](https://github.com/SDA-SE/sda-spring-boot-commons) | — | text~demo (+2 demo/fixture) | A set of libraries to bootstrap spring boot services easily that fo... |
| 15 | [appkr/msa-starter](https://github.com/appkr/msa-starter) | — | text~product (+2 product); name~demo (+2 demo/fixture) | spring-boot msa project starter(Microservice Chassis Pattern) |
| 11 | [WaleedAshraf/asyncapi-github-action](https://github.com/WaleedAshraf/asyncapi-github-action) | — | topic=asyncapi-specification (+3 spec/docs); text~demo (+... | GitHub action to validate if AsyncAPI schema file is valid or not. |
| 10 | [aklivity/zilla-demos](https://github.com/aklivity/zilla-demos) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Zilla Demos |
| 10 | [lambertlabs/learning-sessions](https://github.com/lambertlabs/learning-sessions) | — | text~demo (+2 demo/fixture) | Repo to place all source code used in learning sessions |
| 10 | [PacktPublishing/Building-an-API-Product](https://github.com/PacktPublishing/Building-an-API-Product) | — | text~demo-strong (+3 demo/fixture); lang=None (+1 spec/docs) | Building an API Product, published by Packt |
| 9 | [hdulay/streaming-data-mesh](https://github.com/hdulay/streaming-data-mesh) | — | text~demo-strong (+3 demo/fixture); spec-at-root/docs (+1... |  |
| 9 | [nandorsilva/arc-dados](https://github.com/nandorsilva/arc-dados) | — | text~demo (+2 demo/fixture) |  |
| 9 | [Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i](https://github.com/Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i) | — | text~demo (+2 demo/fixture) | GitOps resources for IBM Cloud Pak for Integration |
| 8 | [dash0hq/otel-platform-demo](https://github.com/dash0hq/otel-platform-demo) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Repository containing demo presented at Cloud Native Bergen, KubeCo... |
| 8 | [microcks/microcks-quarkus-demo](https://github.com/microcks/microcks-quarkus-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Quarkus demonstration app on how to use Microcks DevServices/Testco... |
| 8 | [weidmueller/u-os-hub-api](https://github.com/weidmueller/u-os-hub-api) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | API specifications of the u-OS Data Hub |
| 7 | [amadeus4dev-examples/amadeus-async-flight-status](https://github.com/amadeus4dev-examples/amadeus-async-flight-status) | — | topic=event-driven-architecture,microservices (+3 product... | Event-driven prototype for getting asynchronous flight status notif... |
| 7 | [David-DAM/spring-boot-async-template-ultimate](https://github.com/David-DAM/spring-boot-async-template-ultimate) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Una plantilla de Spring Boot que implementa patrones de arquitectur... |
| 7 | [dedoussis/asyncapi-socket.io-example](https://github.com/dedoussis/asyncapi-socket.io-example) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 6 | [bump-sh/examples](https://github.com/bump-sh/examples) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A curated list of example public OpenAPI and AsyncAPI definition files |
| 6 | [mattbishop/asyncapi-hotels](https://github.com/mattbishop/asyncapi-hotels) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... | Small example showing an event-sourced Hotel domain driven by Async... |
| 6 | [microcks/microcks-testcontainers-go-demo](https://github.com/microcks/microcks-testcontainers-go-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Go demonstration app on how to use Microcks Testcontainers in your ... |
| 6 | [migarci2/ft_transcendence](https://github.com/migarci2/ft_transcendence) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) | Surprise |
| 6 | [specmatic/specmatic-order-contracts](https://github.com/specmatic/specmatic-order-contracts) | — | topic=sample-project (+3 demo/fixture); text~demo-strong ... | Contracts for sample projects that use Specmatic to do contract dri... |
| 5 | [fmvilas/asyncapi-websockets-example](https://github.com/fmvilas/asyncapi-websockets-example) | — | text~tool (+2 tooling/library); text~product (+2 product)... | An example demoing how to use AsyncAPI and WebSockets |
| 5 | [Harsh4902/kubecon-eu-2026-tutorials](https://github.com/Harsh4902/kubecon-eu-2026-tutorials) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | This repository contains tutorials of my talk at KubeCon + CloudNat... |
| 5 | [microcks/microcks-testcontainers-java-workshop](https://github.com/microcks/microcks-testcontainers-java-workshop) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Workshop to learn Microcks Testcontainers Java binding |
| 5 | [ora0600/confluentstreamgovernance](https://github.com/ora0600/confluentstreamgovernance) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Confluent Stream Governance demo with Stream Goverance package "adv... |
| 5 | [UnibucProjects/SmartAquarium](https://github.com/UnibucProjects/SmartAquarium) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 4 | [dalelane/event-endpoint-management-demo](https://github.com/dalelane/event-endpoint-management-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Event Endpoint Management demo  |
| 4 | [kirya522/distributed-systems-course](https://github.com/kirya522/distributed-systems-course) | — | text~product (+2 product); text~demo (+2 demo/fixture); l... | Паттерны и компоненты современных распределенных систем |
| 4 | [microcks/microcks-testcontainers-dotnet-demo](https://github.com/microcks/microcks-testcontainers-dotnet-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | .NET demonstration app on how to use Microcks Testcontainers in you... |
| 3 | [amaralc/explore](https://github.com/amaralc/explore) | — | text~demo (+2 demo/fixture) |  |
| 3 | [bike4life-organization/bike4life](https://github.com/bike4life-organization/bike4life) | — | text~demo (+2 demo/fixture); lang=HTML (+1 spec/docs) |  |
| 3 | [Mrc0113/workshop-scs-s1p](https://github.com/Mrc0113/workshop-scs-s1p) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | 2019 Spring One Platform Workshop |
| 3 | [razvanguta/SmartLight](https://github.com/razvanguta/SmartLight) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 3 | [redhat-france-sa/microservices-saga-blueprint](https://github.com/redhat-france-sa/microservices-saga-blueprint) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Architecture blueprint for demonstrating Saga with microservices |
| 3 | [skunkforce/node-agnostic-datastream-interface](https://github.com/skunkforce/node-agnostic-datastream-interface) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); sp... |  |
| 3 | [wso2/bijira-samples](https://github.com/wso2/bijira-samples) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | This repository contains API proxy samples for WSO2 Bijira |
| 2 | [AzizX25/Esprit-PIDS-4DS4-2026-QOS_Buddy](https://github.com/AzizX25/Esprit-PIDS-4DS4-2026-QOS_Buddy) | — | text~product (+2 product); text~demo (+2 demo/fixture); l... | Developed at Esprit School of Engineering – Tunisia \| Academic Yea... |
| 2 | [dickeyf/esp32-mqtt](https://github.com/dickeyf/esp32-mqtt) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 2 | [GramBelleg/Whisper_BackEnd](https://github.com/GramBelleg/Whisper_BackEnd) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Backend for the Telegram clone app Whisper  |
| 2 | [jbadeau/frontseat-demo](https://github.com/jbadeau/frontseat-demo) | — | text~product (+2 product); name~demo (+2 demo/fixture) |  |
| 2 | [kanekoshoyu/asyncapi-rust-ws-template](https://github.com/kanekoshoyu/asyncapi-rust-ws-template) | — | topic=template (+3 demo/fixture); topic=codegen (+3 tooli... | AsyncAPI Template for Generating Rust WebSocket Client |
| 2 | [kiransth77/aionmcp](https://github.com/kiransth77/aionmcp) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | Autonomous Go MCP Server - Dynamic API specification importer with ... |
| 2 | [manuschillerdev/esphome-elero](https://github.com/manuschillerdev/esphome-elero) | — | text~demo (+2 demo/fixture) | An ESPHome component to control Devices with the bidirectional Eler... |
| 2 | [microcks/microcks-aspire-demo](https://github.com/microcks/microcks-aspire-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Aspire .NET demonstration app on how to use Microcks Aspire extensi... |
| 2 | [microcks/microcks-quarkus-workshop](https://github.com/microcks/microcks-quarkus-workshop) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Workshop to learn Microcks Quarkus Dev Services |
| 2 | [Mik-Grzeg/krewetka](https://github.com/Mik-Grzeg/krewetka) | — | text~demo (+2 demo/fixture) |  |
| 2 | [Mrc0113/smarttown](https://github.com/Mrc0113/smarttown) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | SmartTown Workshop Materials |
| 2 | [MSA-SA-OTUS/architecture-labs](https://github.com/MSA-SA-OTUS/architecture-labs) | — | name~demo (+2 demo/fixture) |  |
| 2 | [NASA-AMMOS/anms](https://github.com/NASA-AMMOS/anms) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs) | Asynchronous Network Management System (ANMS) |
| 2 | [nekofar/warpcast](https://github.com/nekofar/warpcast) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | TypeScript client for interacting with Warpcast APIs |
| 2 | [ravecat/moda](https://github.com/ravecat/moda) | — | text~demo-strong (+3 demo/fixture) | Elixir, NextJS, Typescript, CRDT, Nx, PKCE |
| 2 | [RuiEusebio/confluent-selfservice](https://github.com/RuiEusebio/confluent-selfservice) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 2 | [victorbahl/mulequiz](https://github.com/victorbahl/mulequiz) | — | text~demo (+2 demo/fixture); lang=HTML (+1 spec/docs) | MuleQuiz allows you to play with your friends / colleagues and impr... |
| 2 | [XaaXaaX/eventcatalog-automation](https://github.com/XaaXaaX/eventcatalog-automation) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs) |  |
| 2 | [yoshioterada/Spec-Driven-Dev](https://github.com/yoshioterada/Spec-Driven-Dev) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs) | Sample |
| 1 | [bcwilsondotcom/nx-monorepo-template](https://github.com/bcwilsondotcom/nx-monorepo-template) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); na... |  |
| 1 | [daniloab/async-api-react-example](https://github.com/daniloab/async-api-react-example) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) |  |
| 1 | [daniloab/bull-named-asyncapi-example](https://github.com/daniloab/bull-named-asyncapi-example) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) |  |
| 1 | [fkatsaras/functionality-dsl](https://github.com/fkatsaras/functionality-dsl) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | A DSL for creating low code backend applications  |
| 1 | [fmvilas/workshop-ride-app](https://github.com/fmvilas/workshop-ride-app) | — | name~demo (+2 demo/fixture); lang=HTML (+1 spec/docs) |  |
| 1 | [illyay2017/async-api-streetlights](https://github.com/illyay2017/async-api-streetlights) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | AsyncAPI Streetlight Tutorial |
| 1 | [innovatrics/smartface-integrations](https://github.com/innovatrics/smartface-integrations) | — | text~demo (+2 demo/fixture) |  |
| 1 | [jhsenjaliya/data-product-demo](https://github.com/jhsenjaliya/data-product-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | data product demo app |
| 1 | [junjun-1345/miro-example](https://github.com/junjun-1345/miro-example) | — | text~product (+2 product); name~demo (+2 demo/fixture) |  |
| 1 | [kevinswiber/spectral-function-past-tense](https://github.com/kevinswiber/spectral-function-past-tense) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | Test values in Spectral to ensure the text is in past-tense.  Good ... |
| 1 | [Mesteriis/fullstack-template](https://github.com/Mesteriis/fullstack-template) | — | topic=template (+3 demo/fixture); text~product (+2 produc... | Opinionated FastAPI + Vue fullstack template with contract parity c... |
| 1 | [mknoufi/STOCK_VERIFY_ui](https://github.com/mknoufi/STOCK_VERIFY_ui) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 1 | [RabotaRu/DocHubDemo](https://github.com/RabotaRu/DocHubDemo) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | Demo сайт DocHub |
| 1 | [sebastienblanc/quarkus-review-triage](https://github.com/sebastienblanc/quarkus-review-triage) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 1 | [StereoSachiiii/Devops.Lab](https://github.com/StereoSachiiii/Devops.Lab) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Like kodekloud but postmortem-driven an experimental open source pl... |
| 1 | [TamimiGitHub/solace-retail-workshop](https://github.com/TamimiGitHub/solace-retail-workshop) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 1 | [ThinkportRepo/kafka-summit-solace-demo](https://github.com/ThinkportRepo/kafka-summit-solace-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 1 | [tiagobento/kie-monorepo](https://github.com/tiagobento/kie-monorepo) | — | text~demo (+2 demo/fixture) | Apache KIE :: Monorepo PoC |
| 1 | [tkubica12/gh-copilot-constitution](https://github.com/tkubica12/gh-copilot-constitution) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 1 | [tyayers/apigee-dashboard-demo](https://github.com/tyayers/apigee-dashboard-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 1 | [XaaXaaX/aws-events-standardization](https://github.com/XaaXaaX/aws-events-standardization) | — | text~demo-strong (+3 demo/fixture); spec-at-root/docs (+1... |  |
| 1 | [XaaXaaX/stream-based-service-template](https://github.com/XaaXaaX/stream-based-service-template) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 1 | [yaraPB/RICER-project](https://github.com/yaraPB/RICER-project) | — | text~product (+2 product); text~demo (+2 demo/fixture) | RICER (Resilient Infrastructures and Coordinated Emergency Response... |
| 0 | [AccelByte/extend-event-handler-with-mongodb-csharp](https://github.com/AccelByte/extend-event-handler-with-mongodb-csharp) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [actions-marketplace-validations/WaleedAshraf_asyncapi-github-action](https://github.com/actions-marketplace-validations/WaleedAshraf_asyncapi-github-action) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... |  |
| 0 | [AdayevKP/warmhouse](https://github.com/AdayevKP/warmhouse) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Architecture course project |
| 0 | [afmancilla/poc-submodule](https://github.com/afmancilla/poc-submodule) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | poc-submodule |
| 0 | [afmancilla/poc-subtree](https://github.com/afmancilla/poc-subtree) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | poc-subtree |
| 0 | [aimerzarashi/ts-cqrs-es-v1](https://github.com/aimerzarashi/ts-cqrs-es-v1) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [aleksei-klak-polimi/MeshPlay-Lab](https://github.com/aleksei-klak-polimi/MeshPlay-Lab) | — | text~product (+2 product); name~demo (+2 demo/fixture) |  |
| 0 | [aml-org/examples](https://github.com/aml-org/examples) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [ankush98m/harmonyHub](https://github.com/ankush98m/harmonyHub) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [api-components/amf-components](https://github.com/api-components/amf-components) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | A set of web components based on LitElement that creates the visual... |
| 0 | [ArtPro9/architecture-warmhouse](https://github.com/ArtPro9/architecture-warmhouse) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [atishagarwaal/SampleMicroservice.Net8](https://github.com/atishagarwaal/SampleMicroservice.Net8) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | A sample Microservices solution |
| 0 | [avU8989/locationSearchApp](https://github.com/avU8989/locationSearchApp) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | This is a project from my course Enterprise Information Systems, an... |
| 0 | [BakangMonei/PolyGlot-Demo-Examples](https://github.com/BakangMonei/PolyGlot-Demo-Examples) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | Enterprise-Grade MySQL + MongoDB Implementation for Financial Services |
| 0 | [BNAV01/ecommerce](https://github.com/BNAV01/ecommerce) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [caiquedebrito/logistics-platform](https://github.com/caiquedebrito/logistics-platform) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Sistema distribuído para monitorar entregas em tempo real: recebe p... |
| 0 | [call-sofia/callsofia-webhooks-docs](https://github.com/call-sofia/callsofia-webhooks-docs) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); sp... |  |
| 0 | [ChathurangaKCD/bus-tracking-mqtt-websocket-demo](https://github.com/ChathurangaKCD/bus-tracking-mqtt-websocket-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [choseenonee/websocket_example](https://github.com/choseenonee/websocket_example) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Simple thread-safe websocket realistaion on golang |
| 0 | [chr1sbest/delayed-wallet-transactions](https://github.com/chr1sbest/delayed-wallet-transactions) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Exploratory project for delayed atomic transactions between wallets |
| 0 | [christopherblaisdell/continuous-architecture-platform-poc](https://github.com/christopherblaisdell/continuous-architecture-platform-poc) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Proof of concept for a continuous architecture platform that replac... |
| 0 | [ChunPingWang/tracing-otel-agent-poc](https://github.com/ChunPingWang/tracing-otel-agent-poc) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 0 | [ClearEyesFullHearts/mft](https://github.com/ClearEyesFullHearts/mft) | — | text~product (+2 product); text~demo (+2 demo/fixture); l... | mft invoicing app |
| 0 | [Client-Engineering-Indonesia/workshop-event-automation](https://github.com/Client-Engineering-Indonesia/workshop-event-automation) | — | text~product(weak) (+1 product); name~demo (+2 demo/fixture) |  |
| 0 | [crivetechie/backstage-demo-component-producer](https://github.com/crivetechie/backstage-demo-component-producer) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | producer component to be used in backstage demo |
| 0 | [crustacgen/playground](https://github.com/crustacgen/playground) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | playground for stuff that doesnt belong in the main repo yet |
| 0 | [CZSK-MicroHacks/MicroHack-GitHub-engineering-constitution](https://github.com/CZSK-MicroHacks/MicroHack-GitHub-engineering-constitution) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [dalelane/eem-demo-datagen](https://github.com/dalelane/eem-demo-datagen) | — | name~demo (+2 demo/fixture) |  |
| 0 | [danf425/idp-examples-public](https://github.com/danf425/idp-examples-public) | — | text~product(weak) (+1 product); name~demo (+2 demo/fixtu... |  |
| 0 | [dataGriff/domain-api-template](https://github.com/dataGriff/domain-api-template) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [dataGriff/Outbox.events](https://github.com/dataGriff/Outbox.events) | — | text~product(weak) (+1 product); text~demo-strong (+3 dem... |  |
| 0 | [dataGriff/whiskey-reviews-api](https://github.com/dataGriff/whiskey-reviews-api) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Whiskey review api |
| 0 | [DEFRA/coreai-mcu-event](https://github.com/DEFRA/coreai-mcu-event) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Event store for MCU PoC |
| 0 | [DEFRA/ffc-demo-payment-service](https://github.com/DEFRA/ffc-demo-payment-service) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | FFC demo payment service |
| 0 | [dgomezs/learning-AI-agents](https://github.com/dgomezs/learning-AI-agents) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [dvxam/example-backstage-app](https://github.com/dvxam/example-backstage-app) | — | name~demo (+2 demo/fixture); lang=None (+1 spec/docs) |  |
| 0 | [echohello-dev/backstage](https://github.com/echohello-dev/backstage) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | 🚪 A production-ready Backstage in a showcase environment |
| 0 | [eduardotourinho/candlesticks-hexagonal-architecture](https://github.com/eduardotourinho/candlesticks-hexagonal-architecture) | — | text~product(weak) (+1 product); text~demo-strong (+3 dem... |  |
| 0 | [eharishgit/hello-world](https://github.com/eharishgit/hello-world) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [enisspahi/async-api-example](https://github.com/enisspahi/async-api-example) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | AsyncAPI Example |
| 0 | [fern-demo/stress-test](https://github.com/fern-demo/stress-test) | — | text~demo-strong (+3 demo/fixture); text~spec (+2 spec/do... | Stress Test of Fern Docs |
| 0 | [Fortellis/example-spec](https://github.com/Fortellis/example-spec) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | Example Fortellis Specification |
| 0 | [genelaz/blue_viper_pro](https://github.com/genelaz/blue_viper_pro) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | BlueViper — saha haritası ve atış araçları gibi. |
| 0 | [germanProgq/crypto-hackathon](https://github.com/germanProgq/crypto-hackathon) | — | topic=hackathon (+3 demo/fixture); text~product(weak) (+1... | A crypto hackathon auction bot for telegram |
| 0 | [GruppeNice/DLS_Exam](https://github.com/GruppeNice/DLS_Exam) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [gsperim/account-engine-lab](https://github.com/gsperim/account-engine-lab) | — | text~product(weak) (+1 product); name~demo (+2 demo/fixtu... | Core engine focused on debit and credit postings with daily balance... |
| 0 | [hanEck/distributed-software-architecture](https://github.com/hanEck/distributed-software-architecture) | — | text~demo-strong (+3 demo/fixture) |  |
| 0 | [HenderOrlando/booklyapp](https://github.com/HenderOrlando/booklyapp) | — | text~demo (+2 demo/fixture) | Plataforma diseñada para la gestión eficiente de reservas |
| 0 | [HeshanSudarshana/product-apim-workflow](https://github.com/HeshanSudarshana/product-apim-workflow) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... |  |
| 0 | [ibm-cloud-architecture/vaccine-freezer-mgr](https://github.com/ibm-cloud-architecture/vaccine-freezer-mgr) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) |  |
| 0 | [invivo-digital-factory/openapi-compiler-ts](https://github.com/invivo-digital-factory/openapi-compiler-ts) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... | A project to compile openapi doc to ts type and joi validation |
| 0 | [J0SAL/kafka-playground](https://github.com/J0SAL/kafka-playground) | — | name~demo (+2 demo/fixture) |  |
| 0 | [jabrena/asyncapi-poc](https://github.com/jabrena/asyncapi-poc) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A POC to review Async API Spec and some tools related. |
| 0 | [jabrena/codespaces-asyncapi-template](https://github.com/jabrena/codespaces-asyncapi-template) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A starting point to use the tools from Async API ecosystem. |
| 0 | [jbcodeforce/eda-demo-order-ms](https://github.com/jbcodeforce/eda-demo-order-ms) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [jh4843/devitworld-nodejs-basic](https://github.com/jh4843/devitworld-nodejs-basic) | — | text~demo (+2 demo/fixture) | node.js basic tutorial repository |
| 0 | [jmcastellanojimenez/ecotrack](https://github.com/jmcastellanojimenez/ecotrack) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Cloud-native, microservices, Hexagonal Architecture, Java-Spring ap... |
| 0 | [justynroberts/emea-backstage-demo](https://github.com/justynroberts/emea-backstage-demo) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | PagerDuty EMEA Developer Portal - Backstage demo with PagerDuty, Ru... |
| 0 | [kaje94/choreo-websocket-chat-app](https://github.com/kaje94/choreo-websocket-chat-app) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [kasrasabertehrani/mancala](https://github.com/kasrasabertehrani/mancala) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Multiplayer game of Mancala |
| 0 | [kaushik-rishi/poc-template-aim](https://github.com/kaushik-rishi/poc-template-aim) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | How we want the generated template to look like in the end. |
| 0 | [kaushik-rishi/templates-collection-nodejs-templates](https://github.com/kaushik-rishi/templates-collection-nodejs-templates) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture) | Some sample nodejs templates generated using @asyncapi/nodejs-template |
| 0 | [kaviththiranga/choreo-test-samples](https://github.com/kaviththiranga/choreo-test-samples) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 0 | [kondoumh/asyncapi-study](https://github.com/kondoumh/asyncapi-study) | — | text~tool (+2 tooling/library); text~demo-strong (+3 demo... |  |
| 0 | [krishi-agrawal/generator-template](https://github.com/krishi-agrawal/generator-template) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [lbaker2/nest-cqrs-example](https://github.com/lbaker2/nest-cqrs-example) | — | text~product(weak) (+1 product); name~demo (+2 demo/fixtu... | Simple NestJS CQRS with Redis PubSub |
| 0 | [ldynia/rabbitmq](https://github.com/ldynia/rabbitmq) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Walk through rabbitmq tutorial |
| 0 | [LeonardoVincent07/MissionSmith-Demo](https://github.com/LeonardoVincent07/MissionSmith-Demo) | — | text~demo-strong (+3 demo/fixture); name~demo (+2 demo/fi... | Mission Smith Demonstration Project |
| 0 | [leynos/bournemouth](https://github.com/leynos/bournemouth) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Raggy Graph Chat |
| 0 | [lmeilibr/asyncapi-demo](https://github.com/lmeilibr/asyncapi-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... |  |
| 0 | [manuelottlik/rest-vs-eda-talk](https://github.com/manuelottlik/rest-vs-eda-talk) | — | text~demo-strong (+3 demo/fixture); spec-at-root/docs (+1... | Slides and example files for talk about REST vs. Event-Driven Archi... |
| 0 | [markbac/examples-diags-apis](https://github.com/markbac/examples-diags-apis) | — | name~demo (+2 demo/fixture); lang=None (+1 spec/docs) |  |
| 0 | [markusfc/distributed-systems](https://github.com/markusfc/distributed-systems) | — | text~demo-strong (+3 demo/fixture) |  |
| 0 | [masterjohndoe/pw-auto](https://github.com/masterjohndoe/pw-auto) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Playwright template |
| 0 | [mdurrani808/umdloop_gui](https://github.com/mdurrani808/umdloop_gui) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [medmo/backstage-templates](https://github.com/medmo/backstage-templates) | — | name~demo (+2 demo/fixture); lang=None (+1 spec/docs) |  |
| 0 | [Metatavu/mqtt-demo-spec](https://github.com/Metatavu/mqtt-demo-spec) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [Minister2405/docs-as-code](https://github.com/Minister2405/docs-as-code) | — | text~demo (+2 demo/fixture); name~spec (+1 spec/docs); la... |  |
| 0 | [mknoufi/stck-new](https://github.com/mknoufi/stck-new) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixture) | new |
| 0 | [mknoufi/stock-verify-system](https://github.com/mknoufi/stock-verify-system) | — | text~product (+2 product); text~demo (+2 demo/fixture) | Stock Verification System - Core Application (Backend & Frontend) |
| 0 | [monteirom-ppb/clc-poc](https://github.com/monteirom-ppb/clc-poc) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... |  |
| 0 | [mul14/backstage-demo](https://github.com/mul14/backstage-demo) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... |  |
| 0 | [mvillarrealb/liquibase-demo](https://github.com/mvillarrealb/liquibase-demo) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Database Migrations for Micronaut/Spring With Liquibase |
| 0 | [mx-kshitij/filedropper](https://github.com/mx-kshitij/filedropper) | — | text~demo-strong (+3 demo/fixture) |  |
| 0 | [mzegarras/asyncapi-labs](https://github.com/mzegarras/asyncapi-labs) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 produc... |  |
| 0 | [nandorsilva/asyncapi-demo](https://github.com/nandorsilva/asyncapi-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... |  |
| 0 | [nsivanoly/bank-demo](https://github.com/nsivanoly/bank-demo) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... |  |
| 0 | [oimiragieo/atp-main](https://github.com/oimiragieo/atp-main) | — | text~demo (+2 demo/fixture) |  |
| 0 | [one-2-one/task-manager](https://github.com/one-2-one/task-manager) | — | text~product (+2 product); text~demo (+2 demo/fixture); l... |  |
| 0 | [online-bridge-hackathon/data-formats](https://github.com/online-bridge-hackathon/data-formats) | — | text~demo (+2 demo/fixture); lang=None (+1 spec/docs) | Specifications and Example JSONs |
| 0 | [paulus85/companion](https://github.com/paulus85/companion) | — | text~demo-strong (+3 demo/fixture) | Monorepo for the Companion project, the app for your office |
| 0 | [peter-rr/record-store](https://github.com/peter-rr/record-store) | — | text~product (+2 product); text~demo (+2 demo/fixture) | This is a repo created just to test some AsyncAPI concepts. |
| 0 | [pingxin403/platform-console](https://github.com/pingxin403/platform-console) | — | text~product (+2 product); text~demo-strong (+3 demo/fixt... | Personal learning project: Backstage IDP reference implementation. ... |
| 0 | [ppppng/microcks-demo](https://github.com/ppppng/microcks-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | repository for microcks demo |
| 0 | [prakhar47b/faststream-poc](https://github.com/prakhar47b/faststream-poc) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [quenbyako/asyncapi-example](https://github.com/quenbyako/asyncapi-example) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [rapidcoderx/eventuate-tram-demo](https://github.com/rapidcoderx/eventuate-tram-demo) | — | text~tool (+2 tooling/library); text~product (+2 product)... | Demo application to learn eventuate tram. |
| 0 | [Ravip2006/Demo](https://github.com/Ravip2006/Demo) | — | text~demo-strong (+3 demo/fixture); name~demo (+2 demo/fi... |  |
| 0 | [reselbob/simpleasyncapi](https://github.com/reselbob/simpleasyncapi) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | A project that demonstrates the essential concepts of the Async API... |
| 0 | [RidgeRun/ridgerun-immersive-teleoperation](https://github.com/RidgeRun/ridgerun-immersive-teleoperation) | — | text~product (+2 product); text~demo (+2 demo/fixture) | RidgeRun Immersive Teleoperation is a platform for remotely control... |
| 0 | [RResabala2015/express-template](https://github.com/RResabala2015/express-template) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... |  |
| 0 | [SebastianBorchardt1984/incubator-kie-kogito-runtimes](https://github.com/SebastianBorchardt1984/incubator-kie-kogito-runtimes) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [sjarmak/CodeContextBench_Dashboard](https://github.com/sjarmak/CodeContextBench_Dashboard) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [sonra44/QIKI_DTMP](https://github.com/sonra44/QIKI_DTMP) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... | Truth-first space-simulation game with ORION operator surface and s... |
| 0 | [specdojo/specdojo](https://github.com/specdojo/specdojo) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... |  |
| 0 | [specmesh/helloworld-demo](https://github.com/specmesh/helloworld-demo) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... |  |
| 0 | [sswastioyono18/schema-registry-poc](https://github.com/sswastioyono18/schema-registry-poc) | — | text~product (+2 product); text~demo (+2 demo/fixture); n... | Schema Registry CI/CD POC with Apicurio + Microcks |
| 0 | [starnold-redhat/rhdh-install](https://github.com/starnold-redhat/rhdh-install) | — | text~product(weak) (+1 product); text~demo (+2 demo/fixtu... |  |
| 0 | [The-Microservice-Dungeon/robot](https://github.com/The-Microservice-Dungeon/robot) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [Thushani-Jayasekera/websocket-chat-application](https://github.com/Thushani-Jayasekera/websocket-chat-application) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [treeder/async-toy-store](https://github.com/treeder/async-toy-store) | — | text~demo (+2 demo/fixture) | Demo for AsyncAPI |
| 0 | [tsurdilo/async-demo](https://github.com/tsurdilo/async-demo) | — | name~demo (+2 demo/fixture); spec-at-root/docs (+1 product) |  |
| 0 | [twimprine/GitWorkflow](https://github.com/twimprine/GitWorkflow) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [ueisele/showcase-asyncapi-api](https://github.com/ueisele/showcase-asyncapi-api) | — | text~demo-strong (+3 demo/fixture); spec-at-root/docs (+1... | Schemas and AsyncAPI Definitions |
| 0 | [umdloop/umdloop_gui](https://github.com/umdloop/umdloop_gui) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [VALAWAI/C1_llm_email_replier](https://github.com/VALAWAI/C1_llm_email_replier) | — | text~demo (+2 demo/fixture); spec-at-root/docs (+1 product) | Reply automatically any received mail using a large language model ... |
| 0 | [varunaditya27/sentinel-orchestrator-network](https://github.com/varunaditya27/sentinel-orchestrator-network) | — | text~product (+2 product); text~demo (+2 demo/fixture) |  |
| 0 | [VersaceXcodes/ad-performance](https://github.com/VersaceXcodes/ad-performance) | — | text~demo (+2 demo/fixture) | Project ad-performance generated. |
| 0 | [VersaceXcodes/airbnb-management-properties-eco-friendly](https://github.com/VersaceXcodes/airbnb-management-properties-eco-friendly) | — | text~demo (+2 demo/fixture) | Project airbnb-management-properties-eco-friendly generated. |
| 0 | [ziyashaw/backstage_demo](https://github.com/ziyashaw/backstage_demo) | — | text~product (+2 product); text~demo (+2 demo/fixture); s... | Demo for backstage testing |
| 0 | [znsio/scheduler-demo](https://github.com/znsio/scheduler-demo) | — | text~demo (+2 demo/fixture); name~demo (+2 demo/fixture);... | Scheduler Demo |
| 0 | [zuevrs/yanote](https://github.com/zuevrs/yanote) | — | text~demo (+2 demo/fixture); spec-only-in-fixtures (+1 to... |  |

## spec/docs (55)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 707 | [asyncapi/website](https://github.com/asyncapi/website) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | AsyncAPI specification website |
| 98 | [unfoldedcircle/core-api](https://github.com/unfoldedcircle/core-api) | — | topic=documentation (+3 spec/docs) | API specifications for Remote Two/3 by Unfolded Circle |
| 59 | [jgazeau/shadocs](https://github.com/jgazeau/shadocs) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) | Shadocs Theme for Hugo |
| 51 | [dedoussis/asynction](https://github.com/dedoussis/asynction) | — | topic=asyncapi-specification (+3 spec/docs); text~tool (+... | SocketIO python framework driven by the AsyncAPI specification. Bui... |
| 35 | [flexiblepower/s2-ws-json](https://github.com/flexiblepower/s2-ws-json) | — | text~spec (+2 spec/docs); lang=None (+1 spec/docs) | A WebSockets and JSON based protocol specification implementing the... |
| 33 | [Kong/spec-renderer](https://github.com/Kong/spec-renderer) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | A lightweight, pluggable spec renderer built by Kong. Designed to p... |
| 14 | [albertnadal/asyncapi-schema-pydantic](https://github.com/albertnadal/asyncapi-schema-pydantic) | — | topic=asyncapi-schemas,asyncapi-specification (+3 spec/do... | Pydantic model for the AsyncAPI (v2) specification schema |
| 12 | [asyncapi/tck](https://github.com/asyncapi/tck) | — | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | (WIP) Test Compatibility Suite for AsyncAPI |
| 11 | [apideck-io/api-registry](https://github.com/apideck-io/api-registry) | — | topic=asyncapi-specification,graphql-schemas,openapi-spec... | The API registry is an API specifications registry that indexes spe... |
| 10 | [CardanoSolutions/cardanonical](https://github.com/CardanoSolutions/cardanonical) | — | topic=json-schema (+3 spec/docs); spec-at-root/docs (+1 p... | Canonical JSON schemas for Cardano objects, with reference encoders... |
| 10 | [PcComponentes/open-api-messaging-context](https://github.com/PcComponentes/open-api-messaging-context) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | Little context in behat for validate published messages according t... |
| 9 | [asynq-io/pydantic-asyncapi](https://github.com/asynq-io/pydantic-asyncapi) | — | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | Pydantic models for AsyncAPI schema |
| 8 | [golemfactory/ya-client](https://github.com/golemfactory/ya-client) | — | text~spec (+2 spec/docs) | Specification for REST API in yagna |
| 7 | [daveshanley/asyncapi-tutorials](https://github.com/daveshanley/asyncapi-tutorials) | — | topic=asyncapi-schemas,asyncapi-specification (+3 spec/do... | Looking to get started with AsyncAPI, React, WebSockets and Go? Thi... |
| 5 | [speechmatics/docs](https://github.com/speechmatics/docs) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Documentation site for Speechmatics APIs and products |
| 5 | [tradeparadex/paradex-docs](https://github.com/tradeparadex/paradex-docs) | — | text~spec (+2 spec/docs); name~spec (+1 spec/docs); lang=... | Official documentation for Paradex |
| 4 | [asyncapi/enterprise-patterns](https://github.com/asyncapi/enterprise-patterns) | — | text~spec (+2 spec/docs); lang=None (+1 spec/docs) | Enterprise patterns using AsyncAPI |
| 2 | [specmesh/docs](https://github.com/specmesh/docs) | — | topic=documentation (+3 spec/docs); text~product(weak) (+... | SpecMesh Documentation Portal. Statically served docs |
| 1 | [alexandramartinez/asyncapis-accounts-email](https://github.com/alexandramartinez/asyncapis-accounts-email) | — | topic=asyncapi-specification (+3 spec/docs); text~product... | All the resources you need to implement a functional simple archite... |
| 1 | [crybapp/crybapp.github.io](https://github.com/crybapp/crybapp.github.io) | — | text~spec (+2 spec/docs); lang=None (+1 spec/docs) | API Reference for Cryb |
| 1 | [Ferror/asyncapi-event-catalog](https://github.com/Ferror/asyncapi-event-catalog) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) | Event Catalog generated from Async API |
| 1 | [metricq/metricq-rpc-docs](https://github.com/metricq/metricq-rpc-docs) | — | text~tool (+2 tooling/library); text~demo (+2 demo/fixtur... | 🗎 MetricQ RPC interface documentation |
| 1 | [noodlensk/task-tracker](https://github.com/noodlensk/task-tracker) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product) |  |
| 1 | [qconn-io/api-guidelines](https://github.com/qconn-io/api-guidelines) | — | text~tool (+2 tooling/library); text~product (+2 product)... | API Guidelines Portal |
| 1 | [SAP/asyncapi-specification](https://github.com/SAP/asyncapi-specification) | — | text~spec (+2 spec/docs); name~spec (+1 spec/docs); spec-... | The AsyncAPI specification for SAP ecosystem describes events that ... |
| 1 | [wbelguidoum/docapi](https://github.com/wbelguidoum/docapi) | — | text~spec (+2 spec/docs); spec-only-in-fixtures (+1 tooli... | API Documentation Hub |
| 0 | [AlayaCare/alayamarket-external-docs](https://github.com/AlayaCare/alayamarket-external-docs) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | External documentation for AlayaCare Marketplace APIs |
| 0 | [Aser-Osama/Arch-Project-Async-Docs](https://github.com/Aser-Osama/Arch-Project-Async-Docs) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... |  |
| 0 | [ConvergeIoT/convergeiot-mqtt-spec](https://github.com/ConvergeIoT/convergeiot-mqtt-spec) | — | text~product (+2 product); text~spec (+2 spec/docs); name... |  |
| 0 | [dili91/events-based-api-specs](https://github.com/dili91/events-based-api-specs) | — | text~demo (+2 demo/fixture); text~spec (+2 spec/docs); na... | A playground to try out standard specs for Events based API |
| 0 | [genesisAI4/genesis-docs](https://github.com/genesisAI4/genesis-docs) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... |  |
| 0 | [gosyuliya/docs](https://github.com/gosyuliya/docs) | — | name~spec (+1 spec/docs); lang=HTML (+1 spec/docs) |  |
| 0 | [kayalshan/Enterprise-API-Integration-Platform](https://github.com/kayalshan/Enterprise-API-Integration-Platform) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... | A high-performance, resilient integration backbone featuring API-fi... |
| 0 | [kurtrisley/DemoEventDrivenService](https://github.com/kurtrisley/DemoEventDrivenService) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) |  |
| 0 | [kurtrisley/EventDrivenServices](https://github.com/kurtrisley/EventDrivenServices) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) |  |
| 0 | [lauksas/sync-beat](https://github.com/lauksas/sync-beat) | — | text~product (+2 product); text~demo (+2 demo/fixture); t... |  |
| 0 | [Leandroyyy/async-api-translator](https://github.com/Leandroyyy/async-api-translator) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product);... | Translator for async api specification |
| 0 | [magazino/api-docs](https://github.com/magazino/api-docs) | — | name~spec (+1 spec/docs); lang=None (+1 spec/docs) |  |
| 0 | [markusahlstrand/sss](https://github.com/markusahlstrand/sss) | — | text~product (+2 product); text~spec (+2 spec/docs); spec... | Service Standard Spec |
| 0 | [MasterVentures/cea-docs](https://github.com/MasterVentures/cea-docs) | — | text~spec (+2 spec/docs); name~spec (+1 spec/docs); spec-... | Exchange Test Plan Documentation for Crypto Exchange Alliance Order... |
| 0 | [Minister2405/manifest-docs](https://github.com/Minister2405/manifest-docs) | — | name~spec (+1 spec/docs); lang=MDX (+1 spec/docs) |  |
| 0 | [msaleme/SmartMeterAsyncAPI](https://github.com/msaleme/SmartMeterAsyncAPI) | — | topic=event-driven,iot,messaging (+3 product); topic=api-... | AsyncAPI specification for real-time smart meter telemetry data con... |
| 0 | [nicolasard/async-api-stuff](https://github.com/nicolasard/async-api-stuff) | — | topic=asyncapi-specification (+3 spec/docs); text~tool (+... | Personal notes about AsyncApi project ( https://www.asyncapi.com/ ) |
| 0 | [Pakisan/IDEA-331646](https://github.com/Pakisan/IDEA-331646) | — | text~tool (+2 tooling/library); text~spec (+2 spec/docs);... | Reproduces IDEA-331646 - https://youtrack.jetbrains.com/issue/IDEA-... |
| 0 | [paulCormierProgressive/EventDrivenServices](https://github.com/paulCormierProgressive/EventDrivenServices) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs) |  |
| 0 | [Phoenix-Assassins/ac4-docs](https://github.com/Phoenix-Assassins/ac4-docs) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Online service docs for Assassin's Creed IV Black Flag |
| 0 | [sunnyhealthai/docs](https://github.com/sunnyhealthai/docs) | — | text~tool (+2 tooling/library); text~product(weak) (+1 pr... | Documentation for Sunny Health AI |
| 0 | [thake/backstage-specs-test](https://github.com/thake/backstage-specs-test) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... |  |
| 0 | [trakx/canton-api-client](https://github.com/trakx/canton-api-client) | — | text~spec (+2 spec/docs) | .Net Api Clients for Canton services |
| 0 | [verona-interfaces/player](https://github.com/verona-interfaces/player) | — | text~product(weak) (+1 product); text~spec (+2 spec/docs)... | module "player" is used to present a unit in assessment |
| 0 | [verona-interfaces/verona-module-metadata](https://github.com/verona-interfaces/verona-module-metadata) | — | text~spec (+2 spec/docs); lang=CSS (+1 spec/docs) | All modules specified here must provide metadata: name, version, ap... |
| 0 | [voidly-ai/openapi-specs](https://github.com/voidly-ai/openapi-specs) | — | topic=api-specification,openapi-spec (+3 spec/docs); text... | OpenAPI 3.1 + AsyncAPI 2.6 specifications for the Voidly platform (... |
| 0 | [xtm-group/XTRFCloudInternalEventBus](https://github.com/xtm-group/XTRFCloudInternalEventBus) | — | text~spec (+2 spec/docs); spec-at-root/docs (+1 product);... | XTRF Cloud Internal Event Bus |
| 0 | [zettai-seigi/helix-docs](https://github.com/zettai-seigi/helix-docs) | — | text~product (+2 product); text~spec (+2 spec/docs); name... | Documentation for Helix - Federated MCP Server System for the Casca... |
| 0 | [zqTheDesigner/QComponentLib-docs](https://github.com/zqTheDesigner/QComponentLib-docs) | — | name~spec (+1 spec/docs); spec-at-root/docs (+1 product);... |  |

## tangential (11)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 69 | [deivid11/tide-commander](https://github.com/deivid11/tide-commander) | — | AI coding-skill / agent repo (excluded): claude-code | Tide Commander - Visual orchestrator for multiple Claude Code, Open... |
| 15 | [diktahq/edikt](https://github.com/diktahq/edikt) | — | AI coding-skill / agent repo (excluded): claude-code | The governance layer for agentic engineering — governs your archite... |
| 15 | [frankbria/codeframe](https://github.com/frankbria/codeframe) | — | AI coding-skill / agent repo (excluded): claude-code | Think → Build → Prove → Ship. The project delivery system that turn... |
| 7 | [ammario/kalshi-docs](https://github.com/ammario/kalshi-docs) | — | AI coding-skill repo (excluded): strong text marker | LLM-friendly, auto-updating markdown repository of the Kalshi API docs |
| 6 | [KentoShimizu/sw-agent-skills](https://github.com/KentoShimizu/sw-agent-skills) | — | AI coding-skill repo (excluded): strong text marker | Software Development Agent Skills |
| 4 | [0xHoneyJar/loa-hounfour](https://github.com/0xHoneyJar/loa-hounfour) | — | AI coding-skill / agent repo (excluded): agent-coordinati... | a schema-only protocol library defining the wire format for service... |
| 3 | [zircote/documentation-review](https://github.com/zircote/documentation-review) | — | AI coding-skill / agent repo (excluded): claude-code | Claude Code plugin for comprehensive documentation management — rev... |
| 2 | [nimbus-agent/Nimbus](https://github.com/nimbus-agent/Nimbus) | — | AI coding-skill / agent repo (excluded): agentic | On-call intelligence for DevOps and platform teams. Local-first AI ... |
| 2 | [withakay/ito](https://github.com/withakay/ito) | — | AI coding-skill/agent markers in text (excluded) | AI Assisted Engineering Workflow Tools |
| 1 | [victorrentea/ai-central](https://github.com/victorrentea/ai-central) | — | AI coding-skill/agent markers in text (excluded) |  |
| 0 | [slusset/intention-driven-design](https://github.com/slusset/intention-driven-design) | — | AI coding-skill/agent markers in text (excluded) |  |

## uncategorized (302)

| ★ | Repo | Features | Why | Description |
|---:|---|---|---|---|
| 1280 | [wpilibsuite/allwpilib](https://github.com/wpilibsuite/allwpilib) | — |  | Official Repository of WPILibJ and WPILibC |
| 336 | [cardano-scaling/hydra](https://github.com/cardano-scaling/hydra) | — |  | Implementation of the Hydra Head protocol |
| 121 | [digital-asset/canton](https://github.com/digital-asset/canton) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Global Workflow Composition that is Scalable, Secure, and GDPR-comp... |
| 111 | [jeffmikels/ProPresenter-API](https://github.com/jeffmikels/ProPresenter-API) | — |  | Documenting RenewedVision's undocumented Remote Control protocol wi... |
| 103 | [ballerina-platform/asyncapi-triggers](https://github.com/ballerina-platform/asyncapi-triggers) | — | spec-at-root/docs (+1 product) | This repo will contain the trigger source code generated through ba... |
| 94 | [canton-network/splice](https://github.com/canton-network/splice) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Splice repository |
| 82 | [FreeTAKTeam/Reticulum-Community-Hub](https://github.com/FreeTAKTeam/Reticulum-Community-Hub) | — | spec-at-root/docs (+1 product) | Reticulum Community Hub for groups, mission data, and emergency-man... |
| 49 | [NiaExperience/PearlOS](https://github.com/NiaExperience/PearlOS) | — | text~product(weak) (+1 product) | Your Interface to Intelligence |
| 34 | [christianrowlands/network-survey-messaging](https://github.com/christianrowlands/network-survey-messaging) | — |  | Defines the messages that are sent from the Network Survey Android App |
| 29 | [APIs-guru/asyncapi-directory](https://github.com/APIs-guru/asyncapi-directory) | — | spec-at-root/docs (+1 product) | ⇄ Directory of asynchronous API specifications in AsyncAPI format |
| 25 | [btc-vision/opnet-node](https://github.com/btc-vision/opnet-node) | — |  | OP_NET is a decentralized system that leverages Taproot/SegWit/Lega... |
| 22 | [bang-olufsen/beoremote-halo](https://github.com/bang-olufsen/beoremote-halo) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | Beoremote Halo Open API |
| 22 | [ldynia/learning-api-styles](https://github.com/ldynia/learning-api-styles) | — | text~product(weak) (+1 product) |  |
| 17 | [opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems) | — | spec-at-root/docs (+1 product) | Public Repository for the Connected Systems SWG |
| 17 | [rpicanco/livro-eda](https://github.com/rpicanco/livro-eda) | — |  |  |
| 13 | [codex-k8s/kodex](https://github.com/codex-k8s/kodex) | — |  | 🧠 Your personal IT company in the cloud powered by Codex AI agents |
| 12 | [obot-platform/mcp-catalog](https://github.com/obot-platform/mcp-catalog) | — | spec-at-root/docs (+1 product) |  |
| 9 | [Labdata-FIA/Engenharia-Dados](https://github.com/Labdata-FIA/Engenharia-Dados) | — | lang=Jupyter Notebook (+1 spec/docs) |  |
| 9 | [Magpie-Monitor/magpie-monitor](https://github.com/Magpie-Monitor/magpie-monitor) | — | spec-at-root/docs (+1 product) | Reading logs is for the frogs, let's derive insights from them |
| 8 | [apache/eventmesh-catalog](https://github.com/apache/eventmesh-catalog) | — |  | EventMesh catalog |
| 8 | [tyntec/api-collection](https://github.com/tyntec/api-collection) | — | lang=None (+1 spec/docs) | Collection of tyntecs available API specifications in OpenAPI Spec 3.0 |
| 7 | [C7-Digital/c7_ledger](https://github.com/C7-Digital/c7_ledger) | — |  | TypeScript wrapper around Canton V2 JSON API |
| 7 | [it-incubator/nestjs](https://github.com/it-incubator/nestjs) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Examples |
| 6 | [VitorSVNascimento/Truco-SD](https://github.com/VitorSVNascimento/Truco-SD) | — | spec-at-root/docs (+1 product) | Jogo de truco criado como trabalho final em equipe da disciplina de... |
| 5 | [adevinta/vulcan-api](https://github.com/adevinta/vulcan-api) | — | spec-at-root/docs (+1 product) | Vulcan api |
| 5 | [kaaaaakun/ft_transcendence](https://github.com/kaaaaakun/ft_transcendence) | — | spec-at-root/docs (+1 product) |  |
| 5 | [kidoneself/DockPilot](https://github.com/kidoneself/DockPilot) | — |  |  |
| 5 | [stackus/eda-with-golang](https://github.com/stackus/eda-with-golang) | — |  |  |
| 4 | [RedHatInsights/event-schemas](https://github.com/RedHatInsights/event-schemas) | — | spec-at-root/docs (+1 product) | WIP consoledot CloudEvents schemas |
| 3 | [bian-official/staging](https://github.com/bian-official/staging) | — | lang=None (+1 spec/docs) |  |
| 3 | [MatthewSnelgrove/chefswap](https://github.com/MatthewSnelgrove/chefswap) | — |  |  |
| 3 | [OS2mo/os2mo](https://github.com/OS2mo/os2mo) | — |  | Docs: https://rammearkitektur.docs.magenta.dk/os2mo/ |
| 3 | [pb33f/libasyncapi](https://github.com/pb33f/libasyncapi) | — |  |  |
| 3 | [ravecat/songy](https://github.com/ravecat/songy) | — |  | 🎵 Feel the beats? Multiplayer music game. Challenge friends. Rank t... |
| 3 | [Sinrez/analytic](https://github.com/Sinrez/analytic) | — | lang=Jupyter Notebook (+1 spec/docs) | Примеры ТЗ, схем, BRD, ФТ |
| 3 | [solace-cto-labs/solace-axway-agent](https://github.com/solace-cto-labs/solace-axway-agent) | — |  | Axway-Solace-AsyncAPI Agent |
| 3 | [zahash/jsoncodegen](https://github.com/zahash/jsoncodegen) | — |  |  |
| 2 | [aklivity/todo-service](https://github.com/aklivity/todo-service) | — |  |  |
| 2 | [apiaddicts/sonarasyncapi-rules](https://github.com/apiaddicts/sonarasyncapi-rules) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | A set of rules to analize AsyncAPI documents |
| 2 | [ayumu203/poke-clone-v4](https://github.com/ayumu203/poke-clone-v4) | — | text~product(weak) (+1 product) | Pokemon Battle Web Application made with DDD. |
| 2 | [chathushkaayash/GraphQL-Over-WebSocket-Protocol](https://github.com/chathushkaayash/GraphQL-Over-WebSocket-Protocol) | — |  |  |
| 2 | [ciel334288/ghoulies](https://github.com/ciel334288/ghoulies) | — | text~product(weak) (+1 product) |  |
| 2 | [cudy789/MAPLE](https://github.com/cudy789/MAPLE) | — |  | A multicamera optimized Apriltag pose estimator geared towards FRC ... |
| 2 | [greenthegarden/enviropluspublisher](https://github.com/greenthegarden/enviropluspublisher) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | Python based AsyncAPI project with FastAPI documentation able to be... |
| 2 | [henefisa/xfs-chat-app-backend](https://github.com/henefisa/xfs-chat-app-backend) | — | spec-at-root/docs (+1 product) |  |
| 2 | [OI4/oi4-oec-service](https://github.com/OI4/oi4-oec-service) | — | text~product(weak) (+1 product) | An OI4-compliant base service covering most of the "mandatory" func... |
| 2 | [pagopa/idpay-reward-calculator](https://github.com/pagopa/idpay-reward-calculator) | — |  |  |
| 2 | [Schreglmann/gameshow](https://github.com/Schreglmann/gameshow) | — |  |  |
| 2 | [somosphi/ts-seed-hexagonal](https://github.com/somosphi/ts-seed-hexagonal) | — | spec-at-root/docs (+1 product) | Seed hexagonal architecture with typescript |
| 2 | [tapis-project/tapis-workflows](https://github.com/tapis-project/tapis-workflows) | — |  |  |
| 2 | [TP-O/werewolf](https://github.com/TP-O/werewolf) | — |  | Role-playing game inspired by Werewolf Board Game. |
| 2 | [unibuc-cs/IoT-application-set](https://github.com/unibuc-cs/IoT-application-set) | — | text~product(weak) (+1 product) | Hub App for the IoT Dataset |
| 2 | [Velkromod/gaggimate-feature-gearpump-Modded-MPC](https://github.com/Velkromod/gaggimate-feature-gearpump-Modded-MPC) | — | spec-at-root/docs (+1 product) |  |
| 1 | [aml-org/amf-metadata](https://github.com/aml-org/amf-metadata) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 1 | [BackendFans83/Taxi](https://github.com/BackendFans83/Taxi) | — | lang=None (+1 spec/docs) |  |
| 1 | [benvdbergh/M_Suite](https://github.com/benvdbergh/M_Suite) | — |  |  |
| 1 | [bitfocus/companion-module-bmd-cameras](https://github.com/bitfocus/companion-module-bmd-cameras) | — |  |  |
| 1 | [chernoova/Purr-Stay](https://github.com/chernoova/Purr-Stay) | — |  |  |
| 1 | [Dersivative/WeeChat](https://github.com/Dersivative/WeeChat) | — |  |  |
| 1 | [dnesting/sense](https://github.com/dnesting/sense) | — |  | Sense Energy Monitor API Client (unsupported, unofficial) |
| 1 | [FranMoraton/DDD-EDA-TDD-skeleton](https://github.com/FranMoraton/DDD-EDA-TDD-skeleton) | — | spec-at-root/docs (+1 product) |  |
| 1 | [GotchaAI/BE_SOCKET](https://github.com/GotchaAI/BE_SOCKET) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 1 | [GotchaAI/was](https://github.com/GotchaAI/was) | — | lang=HTML (+1 spec/docs) |  |
| 1 | [Ikay14/Suxch](https://github.com/Ikay14/Suxch) | — |  | The Suxch API is a real-time messaging API enabling seamless commun... |
| 1 | [iuschnic/simple-messenger](https://github.com/iuschnic/simple-messenger) | — | spec-at-root/docs (+1 product) | Проект по командной разработке, простой мессенджер |
| 1 | [kevin-biot/Euro-Cloud-Substrate](https://github.com/kevin-biot/Euro-Cloud-Substrate) | — | spec-at-root/docs (+1 product) |  |
| 1 | [Kyzuma/CSD_Tariffic](https://github.com/Kyzuma/CSD_Tariffic) | — |  |  |
| 1 | [ln678090/ChatRealTime](https://github.com/ln678090/ChatRealTime) | — | text~product(weak) (+1 product) |  |
| 1 | [LucaDev/LFM-Team-Blue](https://github.com/LucaDev/LFM-Team-Blue) | — | lang=TeX (+1 spec/docs) |  |
| 1 | [MehdiMaachi/tp-xml-meteo](https://github.com/MehdiMaachi/tp-xml-meteo) | — | lang=HTML (+1 spec/docs) | TP XML - Relevés de températures avec DTD, XSD, XSLT |
| 1 | [o-ran-sc/smo-teiv](https://github.com/o-ran-sc/smo-teiv) | — |  | Mirror of the smo/teiv repo |
| 1 | [pagopa/idpay-onboarding-workflow](https://github.com/pagopa/idpay-onboarding-workflow) | — |  |  |
| 1 | [poojapkamath/Building-Integrations-with-MuleSoft](https://github.com/poojapkamath/Building-Integrations-with-MuleSoft) | — |  | Integrating systems and unifying data |
| 1 | [Sergei8888/Uniscope](https://github.com/Sergei8888/Uniscope) | — |  | Код стартап-проекта "Uniscope - система удаленных астрономических н... |
| 1 | [SolaceLabs/ep-asyncapi-importer](https://github.com/SolaceLabs/ep-asyncapi-importer) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... |  |
| 1 | [SolaceLabs/sol-ep-asyncapi-importer](https://github.com/SolaceLabs/sol-ep-asyncapi-importer) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... |  |
| 1 | [supermodel/formats](https://github.com/supermodel/formats) | — | lang=None (+1 spec/docs) | Repository of popular format schemas |
| 1 | [underpass-ai/rehydration-kernel](https://github.com/underpass-ai/rehydration-kernel) | — | spec-at-root/docs (+1 product) | Kernel Memory Protocol for temporal, multidimensional, auditable AI... |
| 1 | [WaleedAshraf/asyncapi-test-gh-action](https://github.com/WaleedAshraf/asyncapi-test-gh-action) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Test Github action for asyncapi |
| 1 | [zz-plant/ethotechnics.org](https://github.com/zz-plant/ethotechnics.org) | — |  |  |
| 0 | [999iQ/networking](https://github.com/999iQ/networking) | — | spec-at-root/docs (+1 product) | Микросервис для Networking части стартапа.  |
| 0 | [AccelByte/accelbyte-api-proto](https://github.com/AccelByte/accelbyte-api-proto) | — | spec-at-root/docs (+1 product) |  |
| 0 | [acdgbrasil/contracts](https://github.com/acdgbrasil/contracts) | — | text~product(weak) (+1 product); lang=None (+1 spec/docs) | Repositório central de contratos da organização, com especificações... |
| 0 | [AceMegaSchool/evanston](https://github.com/AceMegaSchool/evanston) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [AceTheCreator/simple-commerce](https://github.com/AceTheCreator/simple-commerce) | — |  |  |
| 0 | [agarkoff/Bonds](https://github.com/agarkoff/Bonds) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [ahmad-khatib0/go](https://github.com/ahmad-khatib0/go) | — |  |  |
| 0 | [Ahmadjarad47/CRM.Medical](https://github.com/Ahmadjarad47/CRM.Medical) | — | spec-at-root/docs (+1 product) |  |
| 0 | [aklivity/todo-app](https://github.com/aklivity/todo-app) | — | spec-at-root/docs (+1 product) | Todo App |
| 0 | [alexeadem/qbo-asyncapi](https://github.com/alexeadem/qbo-asyncapi) | — | spec-at-root/docs (+1 product) |  |
| 0 | [ambansod-tibco/-Test6](https://github.com/ambansod-tibco/-Test6) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [ambansod-tibco/Test](https://github.com/ambansod-tibco/Test) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | For testing |
| 0 | [ambansod-tibco/test4](https://github.com/ambansod-tibco/test4) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [andreevcode/01_ya-arch-warmhouse](https://github.com/andreevcode/01_ya-arch-warmhouse) | — |  |  |
| 0 | [Archi-Lab-FAE/fae-team-2-service](https://github.com/Archi-Lab-FAE/fae-team-2-service) | — | text~product(weak) (+1 product) |  |
| 0 | [arjungarg07/cupidDemo](https://github.com/arjungarg07/cupidDemo) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [arjungarg07/relation-finder-prototype](https://github.com/arjungarg07/relation-finder-prototype) | — | text~product(weak) (+1 product) | Prototype for Application Relations Finder |
| 0 | [arnaldoprado74/backstage](https://github.com/arnaldoprado74/backstage) | — |  |  |
| 0 | [arnold-keyvalue/slack-bot-test](https://github.com/arnold-keyvalue/slack-bot-test) | — | lang=None (+1 spec/docs) |  |
| 0 | [arpoma16/multiuav_gui_doc](https://github.com/arpoma16/multiuav_gui_doc) | — | text~product(weak) (+1 product) |  |
| 0 | [baldimir/kie-cloud](https://github.com/baldimir/kie-cloud) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | All the cloud related code for the Apache KIE project (testing repo... |
| 0 | [baldimir/kie-frontend](https://github.com/baldimir/kie-frontend) | — |  | All the frontend code for the Apache KIE project (testing repositor... |
| 0 | [BarminGeorge/ShuKnow](https://github.com/BarminGeorge/ShuKnow) | — | spec-at-root/docs (+1 product) | ИИ-агент для автоматической организации файлов и заметок. Отправьте... |
| 0 | [BaukovGK/esp32s3_main_controller](https://github.com/BaukovGK/esp32s3_main_controller) | — | spec-at-root/docs (+1 product) |  |
| 0 | [bitsy-ai/printnanny-swupdate](https://github.com/bitsy-ai/printnanny-swupdate) | — |  | PrintNanny OS software update services |
| 0 | [bjuvensjo/backstage-slask](https://github.com/bjuvensjo/backstage-slask) | — | lang=None (+1 spec/docs) | A repository for testing Backstage discovery |
| 0 | [brajsing/newrepo](https://github.com/brajsing/newrepo) | — | lang=None (+1 spec/docs) |  |
| 0 | [brasseld/gravitee-bootcamp-june2022](https://github.com/brasseld/gravitee-bootcamp-june2022) | — | lang=None (+1 spec/docs) | EDA Bootcamp June 2022 |
| 0 | [brndngln/PLACE-HOLDER---OQEACS](https://github.com/brndngln/PLACE-HOLDER---OQEACS) | — | text~product(weak) (+1 product) | coding system |
| 0 | [carlosquintino/realtime-iot-decisioning](https://github.com/carlosquintino/realtime-iot-decisioning) | — |  |  |
| 0 | [carlosvillanua/apidefinitions](https://github.com/carlosvillanua/apidefinitions) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [ccastromar/asyncapi](https://github.com/ccastromar/asyncapi) | — | spec-at-root/docs (+1 product) | Some Node.js utitilies for asyncapi and Kafka |
| 0 | [ChiragSethi-1153/ECommerce](https://github.com/ChiragSethi-1153/ECommerce) | — |  |  |
| 0 | [chris-regnier/gavel](https://github.com/chris-regnier/gavel) | — | spec-at-root/docs (+1 product) | AI-powered content review that delivers a verdict: accept, reject, ... |
| 0 | [chugaynov/optistairs-architecture](https://github.com/chugaynov/optistairs-architecture) | — | spec-at-root/docs (+1 product) |  |
| 0 | [CodeBeast357/webosapi-asyncapi](https://github.com/CodeBeast357/webosapi-asyncapi) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [CROprogrammer/microcks](https://github.com/CROprogrammer/microcks) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Microcks |
| 0 | [danilosoarescardoso/orders-repository](https://github.com/danilosoarescardoso/orders-repository) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [David-Sousa-Web/joystick-server](https://github.com/David-Sousa-Web/joystick-server) | — | spec-at-root/docs (+1 product) |  |
| 0 | [DemoBackstage/mysecondrepopublic](https://github.com/DemoBackstage/mysecondrepopublic) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [DimitriosSpanos1998/AsyncAPI-](https://github.com/DimitriosSpanos1998/AsyncAPI-) | — | spec-at-root/docs (+1 product) |  |
| 0 | [DimitriosSpanos1998/My_version](https://github.com/DimitriosSpanos1998/My_version) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [DocHubTeam/dochub-manual](https://github.com/DocHubTeam/dochub-manual) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Manual of DocHub |
| 0 | [Dolgikh17/dolgikh_docs](https://github.com/Dolgikh17/dolgikh_docs) | — |  |  |
| 0 | [Dream-Wood/api-security-analyzer-hack](https://github.com/Dream-Wood/api-security-analyzer-hack) | — |  |  |
| 0 | [easyformal/easyformal-site](https://github.com/easyformal/easyformal-site) | — | spec-at-root/docs (+1 product); lang=CSS (+1 spec/docs) |  |
| 0 | [eda-ecommerce/asyncapi](https://github.com/eda-ecommerce/asyncapi) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [edulucca/api-autenticacao](https://github.com/edulucca/api-autenticacao) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | api-autenticacao [backstage] |
| 0 | [edulucca/github-runners-manager](https://github.com/edulucca/github-runners-manager) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | github-runners-manager [backstage] |
| 0 | [edulucca/worker-notificacoes](https://github.com/edulucca/worker-notificacoes) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | worker-notificacoes [backstage] |
| 0 | [egomez11/SmartEdify-Planner](https://github.com/egomez11/SmartEdify-Planner) | — | lang=None (+1 spec/docs) |  |
| 0 | [eharishgit/test3](https://github.com/eharishgit/test3) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [Eiritel/system_for_blood_donors_doc](https://github.com/Eiritel/system_for_blood_donors_doc) | — |  |  |
| 0 | [Elgcopilot/ISUZU-MOCK](https://github.com/Elgcopilot/ISUZU-MOCK) | — | spec-at-root/docs (+1 product) |  |
| 0 | [entente-dev/entente](https://github.com/entente-dev/entente) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... | Schema-first contract testing with centralised management service |
| 0 | [Er-kidus/Mafia-Deception-and-Survival](https://github.com/Er-kidus/Mafia-Deception-and-Survival) | — |  | Mafia is a social deduction game where players take on secret roles... |
| 0 | [Ferror/asyncapi-event-catalog-v2](https://github.com/Ferror/asyncapi-event-catalog-v2) | — |  | Event Catalog V2 Setup with Github Actions |
| 0 | [feytox/ShuKnow](https://github.com/feytox/ShuKnow) | — | spec-at-root/docs (+1 product) | ИИ-агент для автоматической организации файлов и заметок. |
| 0 | [filatkinen/socialnet](https://github.com/filatkinen/socialnet) | — | spec-at-root/docs (+1 product) |  |
| 0 | [FjordMaritimeAS/FjordControlSwagger](https://github.com/FjordMaritimeAS/FjordControlSwagger) | — | lang=None (+1 spec/docs) | Swagger specifications for Fjord Control (pushed from SwaggerHub) |
| 0 | [Flissel/requirements-engineer](https://github.com/Flissel/requirements-engineer) | — |  | Tool for engineering and managing software requirements. |
| 0 | [fluximus-prime/fluximus-prime.github.io](https://github.com/fluximus-prime/fluximus-prime.github.io) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | Github Pages Public Profile (Auto Generated - Do Not Edit) |
| 0 | [fsedano/openapiexamples](https://github.com/fsedano/openapiexamples) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [funny-bunny-corp/payment-executor](https://github.com/funny-bunny-corp/payment-executor) | — | text~product(weak) (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [funny-bunny-corp/wallet](https://github.com/funny-bunny-corp/wallet) | — |  |  |
| 0 | [GabrielAderaldo/Merma_a_musica](https://github.com/GabrielAderaldo/Merma_a_musica) | — |  |  |
| 0 | [gbsoftwaresolution/monas-ros.com](https://github.com/gbsoftwaresolution/monas-ros.com) | — |  |  |
| 0 | [gerasimov-d/flow-ops](https://github.com/gerasimov-d/flow-ops) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [gitjpk/snapquiz](https://github.com/gitjpk/snapquiz) | — |  |  |
| 0 | [gmnielsen/wpilib](https://github.com/gmnielsen/wpilib) | — |  |  |
| 0 | [gsjurseth/apigee-kafka](https://github.com/gsjurseth/apigee-kafka) | — | spec-at-root/docs (+1 product) |  |
| 0 | [h-p-b/claude-freetime](https://github.com/h-p-b/claude-freetime) | — |  |  |
| 0 | [hbtrack/official](https://github.com/hbtrack/official) | — | spec-at-root/docs (+1 product) |  |
| 0 | [hekonsek/pieronek](https://github.com/hekonsek/pieronek) | — | lang=None (+1 spec/docs) |  |
| 0 | [HexRohit/cardano](https://github.com/HexRohit/cardano) | — | spec-at-root/docs (+1 product) |  |
| 0 | [hirneagabriel/SnakeDevs](https://github.com/hirneagabriel/SnakeDevs) | — |  |  |
| 0 | [huy21it/ChatAppBackEnd](https://github.com/huy21it/ChatAppBackEnd) | — | spec-at-root/docs (+1 product) |  |
| 0 | [HyPolDev/CEPMA_Engine](https://github.com/HyPolDev/CEPMA_Engine) | — | text~product(weak) (+1 product) | CEPMA Engine |
| 0 | [iain-b/backstage-test-entities](https://github.com/iain-b/backstage-test-entities) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [ibm-cloudintegration/CP4I-PoT-Public](https://github.com/ibm-cloudintegration/CP4I-PoT-Public) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [ibrahimt2/exampleAPI](https://github.com/ibrahimt2/exampleAPI) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) | OpenAPI Prototype |
| 0 | [icegreg/chat-smpl](https://github.com/icegreg/chat-smpl) | — | spec-at-root/docs (+1 product) |  |
| 0 | [ifox777/seaf-archtool-core](https://github.com/ifox777/seaf-archtool-core) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [ifox777/test_repo_gf](https://github.com/ifox777/test_repo_gf) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [INSPIDE/DGT3.0Workshop_usecase_12](https://github.com/INSPIDE/DGT3.0Workshop_usecase_12) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [INSPIDE/DGT3.0Workshop_usecase_13](https://github.com/INSPIDE/DGT3.0Workshop_usecase_13) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [INSPIDE/DGT3.0Workshop_usecase_5](https://github.com/INSPIDE/DGT3.0Workshop_usecase_5) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Caso de uso 5 de la plataforma DGT3.0 |
| 0 | [INSPIDE/DGT3.0Workshop_usecase_9](https://github.com/INSPIDE/DGT3.0Workshop_usecase_9) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [iqb-berlin/item-table](https://github.com/iqb-berlin/item-table) | — | lang=HTML (+1 spec/docs) | Specifications and services about metadata of items in VERA project |
| 0 | [isala404/choreo-tests](https://github.com/isala404/choreo-tests) | — |  | List of components used to test out Choreo's various test suite   |
| 0 | [Ishan662/User_Management_System-Go-](https://github.com/Ishan662/User_Management_System-Go-) | — |  | A User_Management_System written in Go Language |
| 0 | [Ishou/wordsparrow](https://github.com/Ishou/wordsparrow) | — | text~product(weak) (+1 product) |  |
| 0 | [iwaag/agcode-worker](https://github.com/iwaag/agcode-worker) | — |  | worker for agcode |
| 0 | [iwaag/agoffice](https://github.com/iwaag/agoffice) | — |  | to standardize coding process |
| 0 | [jbrannst/async](https://github.com/jbrannst/async) | — | spec-at-root/docs (+1 product); lang=HTML (+1 spec/docs) |  |
| 0 | [jhoncastro28/saga-choreography](https://github.com/jhoncastro28/saga-choreography) | — |  |  |
| 0 | [jhumci/MECH-M-3-IIoT](https://github.com/jhumci/MECH-M-3-IIoT) | — | spec-at-root/docs (+1 product) |  |
| 0 | [jonnekaunisto/Murdle](https://github.com/jonnekaunisto/Murdle) | — |  |  |
| 0 | [jrevillard/edulift](https://github.com/jrevillard/edulift) | — |  |  |
| 0 | [kakabisht/AsyncAPITemplate](https://github.com/kakabisht/AsyncAPITemplate) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [Kanastra-Tech/microcks](https://github.com/Kanastra-Tech/microcks) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [KeertiPusarlaa/idp-platform](https://github.com/KeertiPusarlaa/idp-platform) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [keithralphs/DiscoveryTest](https://github.com/keithralphs/DiscoveryTest) | — | lang=None (+1 spec/docs) |  |
| 0 | [konoec/itaxcix-api](https://github.com/konoec/itaxcix-api) | — |  |  |
| 0 | [kranthikarthan/PE](https://github.com/kranthikarthan/PE) | — | text~product(weak) (+1 product) | Next Gen PE |
| 0 | [kwyn/go-axofuego](https://github.com/kwyn/go-axofuego) | — | spec-at-root/docs (+1 product) |  |
| 0 | [latp9/Test-QA](https://github.com/latp9/Test-QA) | — |  |  |
| 0 | [leefreemanxyz/redocly-async-api-reproduction](https://github.com/leefreemanxyz/redocly-async-api-reproduction) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [leopcaraballo/RLApp-V2](https://github.com/leopcaraballo/RLApp-V2) | — |  |  |
| 0 | [liamford/ms-cards](https://github.com/liamford/ms-cards) | — |  |  |
| 0 | [LowellObservatory/Lorax](https://github.com/LowellObservatory/Lorax) | — |  | The Lowell Observatory Robotic and Automatic eXplorers |
| 0 | [lucasheld/masterarbeit-files](https://github.com/lucasheld/masterarbeit-files) | — |  |  |
| 0 | [magenta-aps/os2mo](https://github.com/magenta-aps/os2mo) | — |  | Docs: https://rammearkitektur.docs.magenta.dk/os2mo/ |
| 0 | [malinthaprasan/choreo-my-apps](https://github.com/malinthaprasan/choreo-my-apps) | — |  |  |
| 0 | [mamonteiro-microops-pt/kafka-management](https://github.com/mamonteiro-microops-pt/kafka-management) | — |  |  |
| 0 | [MarcoChavezB/Lockity_DOC_MQTT](https://github.com/MarcoChavezB/Lockity_DOC_MQTT) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [mariacolab/einzelhandel](https://github.com/mariacolab/einzelhandel) | — |  |  |
| 0 | [Masterisk-F/Syncterra](https://github.com/Masterisk-F/Syncterra) | — | spec-at-root/docs (+1 product) | Synchronize audio files on your PC with your devices. |
| 0 | [MatsuoTakuro/eda-in-golang](https://github.com/MatsuoTakuro/eda-in-golang) | — |  |  |
| 0 | [milicaj00/SOA-II-Projekat](https://github.com/milicaj00/SOA-II-Projekat) | — | lang=HTML (+1 spec/docs) | Project for Software Oriented Architecture exam. |
| 0 | [minhhien-e/studydocs](https://github.com/minhhien-e/studydocs) | — |  |  |
| 0 | [minhnguyen102/CDTN_BE](https://github.com/minhnguyen102/CDTN_BE) | — | spec-at-root/docs (+1 product) |  |
| 0 | [minhnguyenkhac1983/ex-ai](https://github.com/minhnguyenkhac1983/ex-ai) | — |  | Exchange of AI, Open Source |
| 0 | [Mithlesh-Kumar2002/E_Commerce_Microservice](https://github.com/Mithlesh-Kumar2002/E_Commerce_Microservice) | — |  |  |
| 0 | [mohamedutopios/module2-wso2](https://github.com/mohamedutopios/module2-wso2) | — |  |  |
| 0 | [mtturner57/AsyncApiGenerator](https://github.com/mtturner57/AsyncApiGenerator) | — | spec-at-root/docs (+1 product) | Geenrate models or yaml from supplied file |
| 0 | [mzegarras/schemas-avros](https://github.com/mzegarras/schemas-avros) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [nandinimukherjeeblr/testing_dita](https://github.com/nandinimukherjeeblr/testing_dita) | — | lang=None (+1 spec/docs) |  |
| 0 | [nanoyan/response2](https://github.com/nanoyan/response2) | — |  |  |
| 0 | [nastosinka/oops_trap](https://github.com/nastosinka/oops_trap) | — | spec-at-root/docs (+1 product) |  |
| 0 | [Nauchara/Dumai-Arduino-LED-Panel](https://github.com/Nauchara/Dumai-Arduino-LED-Panel) | — | spec-at-root/docs (+1 product) |  |
| 0 | [ninkovski/bootcamp-back-util-api-contracts](https://github.com/ninkovski/bootcamp-back-util-api-contracts) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) |  |
| 0 | [pagopa/idpay-notification-manager](https://github.com/pagopa/idpay-notification-manager) | — |  |  |
| 0 | [pagopa/io-fims](https://github.com/pagopa/io-fims) | — |  | This is the repository that contains all the funcftionalities regar... |
| 0 | [pand1-ta/Programacion-Concurrente-y-Distribuida](https://github.com/pand1-ta/Programacion-Concurrente-y-Distribuida) | — |  |  |
| 0 | [pandapan-cute/TriggerGameCompose](https://github.com/pandapan-cute/TriggerGameCompose) | — | spec-at-root/docs (+1 product) |  |
| 0 | [parmendes/MessageBrokerExample](https://github.com/parmendes/MessageBrokerExample) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [practicumstudent2025/architecture-warmhouse](https://github.com/practicumstudent2025/architecture-warmhouse) | — |  |  |
| 0 | [Project-ScholarAI/ScholarAI-Docs](https://github.com/Project-ScholarAI/ScholarAI-Docs) | — | text~product(weak) (+1 product); name~spec (+1 spec/docs) |  |
| 0 | [qconn-io/stockmanagement-async-api](https://github.com/qconn-io/stockmanagement-async-api) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Testing sync of AsyncAPI spec with Confluent Kafka |
| 0 | [R3shm1thThar1ndu/HND_finalAuthService](https://github.com/R3shm1thThar1ndu/HND_finalAuthService) | — | spec-at-root/docs (+1 product) |  |
| 0 | [raulMrello/AstCalendar](https://github.com/raulMrello/AstCalendar) | — | spec-at-root/docs (+1 product) |  |
| 0 | [RoutineCloud/RoutineCloudServer](https://github.com/RoutineCloud/RoutineCloudServer) | — |  |  |
| 0 | [rpiontik/DocHubDoc](https://github.com/rpiontik/DocHubDoc) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... | Documentation of DocHub |
| 0 | [rtszh/architecture-yandex](https://github.com/rtszh/architecture-yandex) | — |  |  |
| 0 | [rvasqz86/manufacturing-mes-streaming-aggregate](https://github.com/rvasqz86/manufacturing-mes-streaming-aggregate) | — | spec-at-root/docs (+1 product) | Real-time manufacturing alarm pipeline using Kafka Streams + Spring... |
| 0 | [Savio629/testing](https://github.com/Savio629/testing) | — | spec-at-root/docs (+1 product) |  |
| 0 | [schooldevops/openapi_hub](https://github.com/schooldevops/openapi_hub) | — |  |  |
| 0 | [scopy-ll/ervi-backend](https://github.com/scopy-ll/ervi-backend) | — | spec-at-root/docs (+1 product) |  |
| 0 | [sfpostman/PokemonBrightbox](https://github.com/sfpostman/PokemonBrightbox) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [shashanksaxena-tz/munciplaityTax](https://github.com/shashanksaxena-tz/munciplaityTax) | — |  |  |
| 0 | [sjswerdloff/dicomweb_openapi](https://github.com/sjswerdloff/dicomweb_openapi) | — | spec-at-root/docs (+1 product); lang=None (+1 spec/docs) | Just the YAML for OpenAPI and AsyncAPI definitions for DICOM Web...... |
| 0 | [slairu/current](https://github.com/slairu/current) | — | text~product(weak) (+1 product) |  |
| 0 | [spaced-repetition-learner/srscs-deck-service](https://github.com/spaced-repetition-learner/srscs-deck-service) | — | spec-at-root/docs (+1 product) |  |
| 0 | [spaced-repetition-learner/srscs-user-service](https://github.com/spaced-repetition-learner/srscs-user-service) | — | spec-at-root/docs (+1 product) |  |
| 0 | [stan-dot/blue-mono-blue](https://github.com/stan-dot/blue-mono-blue) | — |  |  |
| 0 | [straylight-archive/render-api](https://github.com/straylight-archive/render-api) | — | spec-at-root/docs (+1 product); lang=CSS (+1 spec/docs) | // weyl // render // api |
| 0 | [Sushkov24/architecture](https://github.com/Sushkov24/architecture) | — | spec-at-root/docs (+1 product) |  |
| 0 | [t3hw00t/ARW](https://github.com/t3hw00t/ARW) | — | spec-at-root/docs (+1 product) |  |
| 0 | [TadiwanasheChawatama/zerodrift](https://github.com/TadiwanasheChawatama/zerodrift) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [tassosgomes/GestAuto](https://github.com/tassosgomes/GestAuto) | — |  |  |
| 0 | [tayyabfayyaz/hakathon_2](https://github.com/tayyabfayyaz/hakathon_2) | — |  | this repo cover all the phases of hakathon 2 in the seperat files a... |
| 0 | [tenacious89/open_agent_hackathon](https://github.com/tenacious89/open_agent_hackathon) | — |  | 性设计兼顾 “怼” 的效果和 “有趣不伤人” 的分寸的智能体 |
| 0 | [thealmikey/zilla-kt](https://github.com/thealmikey/zilla-kt) | — | text~product(weak) (+1 product); spec-only-in-fixtures (+... | Zilla with kotlin, custom kotlin manager with custom kotlin binding... |
| 0 | [thil4n/wso2-apim-source](https://github.com/thil4n/wso2-apim-source) | — | spec-only-in-fixtures (+1 tooling/library); spec-only-in-... |  |
| 0 | [Thushani-Jayasekera/test-data](https://github.com/Thushani-Jayasekera/test-data) | — | lang=None (+1 spec/docs) |  |
| 0 | [Thushani-Jayasekera/websocket-servers](https://github.com/Thushani-Jayasekera/websocket-servers) | — |  |  |
| 0 | [tiagoceridorio/crm-challenge](https://github.com/tiagoceridorio/crm-challenge) | — | spec-at-root/docs (+1 product) |  |
| 0 | [tomhv/piwu](https://github.com/tomhv/piwu) | — | spec-at-root/docs (+1 product) | Play it with us |
| 0 | [UNIZAR-30226-2021-13/UniTrivia_backend](https://github.com/UNIZAR-30226-2021-13/UniTrivia_backend) | — | spec-at-root/docs (+1 product) |  |
| 0 | [VALAWAI/C0_email_actuator](https://github.com/VALAWAI/C0_email_actuator) | — | spec-at-root/docs (+1 product) | Component that send emails. |
| 0 | [VALAWAI/C1_nit_protocol_manager](https://github.com/VALAWAI/C1_nit_protocol_manager) | — | spec-at-root/docs (+1 product) | This component check that a treatment follows the NIT protocol |
| 0 | [Velkromod/gaggimate-feature-gearpump](https://github.com/Velkromod/gaggimate-feature-gearpump) | — | spec-at-root/docs (+1 product) |  |
| 0 | [VersaceXcodes/build-an-online-web-application](https://github.com/VersaceXcodes/build-an-online-web-application) | — | text~product(weak) (+1 product) | Project build-an-online-web-application generated. |
| 0 | [VersaceXcodes/calender-system-basic-lpjlzi](https://github.com/VersaceXcodes/calender-system-basic-lpjlzi) | — |  | Generated project for calender-system-basic |
| 0 | [VersaceXcodes/calender-system-software-basic-9xvak1](https://github.com/VersaceXcodes/calender-system-software-basic-9xvak1) | — |  | Generated project for calender-system-software-basic |
| 0 | [VersaceXcodes/calender-system-software-basic-cie8og](https://github.com/VersaceXcodes/calender-system-software-basic-cie8og) | — |  | Generated project for calender-system-software-basic |
| 0 | [VersaceXcodes/calender-system-software-basic-hoigmu](https://github.com/VersaceXcodes/calender-system-software-basic-hoigmu) | — |  | Generated project for calender-system-software-basic |
| 0 | [VersaceXcodes/calender-system-software-basic-lkt6hq](https://github.com/VersaceXcodes/calender-system-software-basic-lkt6hq) | — |  | Generated project for calender-system-software-basic |
| 0 | [VersaceXcodes/construction-materials-supplies-markets-snmlrq](https://github.com/VersaceXcodes/construction-materials-supplies-markets-snmlrq) | — |  | Generated project for construction-materials-supplies-markets |
| 0 | [VersaceXcodes/delivery-service-within-24-hours-45vzsd](https://github.com/VersaceXcodes/delivery-service-within-24-hours-45vzsd) | — | text~product(weak) (+1 product) | Generated project for delivery-service-within-24-hours |
| 0 | [VersaceXcodes/delivery-service-within-24-hours-51mbar](https://github.com/VersaceXcodes/delivery-service-within-24-hours-51mbar) | — | text~product(weak) (+1 product) | Generated project for delivery-service-within-24-hours |
| 0 | [VersaceXcodes/make-a-task-ma-uonxvv](https://github.com/VersaceXcodes/make-a-task-ma-uonxvv) | — |  | Generated project for make-a-task-ma |
| 0 | [VersaceXcodes/make-a-task-management-app-7kdo5d](https://github.com/VersaceXcodes/make-a-task-management-app-7kdo5d) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-ad6v3v](https://github.com/VersaceXcodes/make-a-task-management-app-ad6v3v) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-c5nq9q](https://github.com/VersaceXcodes/make-a-task-management-app-c5nq9q) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-ce9fn3](https://github.com/VersaceXcodes/make-a-task-management-app-ce9fn3) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management-app-ehq8um](https://github.com/VersaceXcodes/make-a-task-management-app-ehq8um) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-g32khm](https://github.com/VersaceXcodes/make-a-task-management-app-g32khm) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-jza64k](https://github.com/VersaceXcodes/make-a-task-management-app-jza64k) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-k7weuf](https://github.com/VersaceXcodes/make-a-task-management-app-k7weuf) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-lzi7ep](https://github.com/VersaceXcodes/make-a-task-management-app-lzi7ep) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-plclb4](https://github.com/VersaceXcodes/make-a-task-management-app-plclb4) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-pvh6mg](https://github.com/VersaceXcodes/make-a-task-management-app-pvh6mg) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-rlzksr](https://github.com/VersaceXcodes/make-a-task-management-app-rlzksr) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-app-w6vg8v](https://github.com/VersaceXcodes/make-a-task-management-app-w6vg8v) | — |  | Generated project for make-a-task-management-app |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-0jjxse](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-0jjxse) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-fru29g](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-fru29g) | — |  | Project make-a-task-management-appdesfwqe3e generated by CoFounder. |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-fzt0ds](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-fzt0ds) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-jzaah4](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-jzaah4) | — |  | Generated project for make-a-task-management-appdesfwqe3e |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-kq2zyh](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-kq2zyh) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management-appdesfwqe3e-zpl292](https://github.com/VersaceXcodes/make-a-task-management-appdesfwqe3e-zpl292) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management1234-dbwz8a](https://github.com/VersaceXcodes/make-a-task-management1234-dbwz8a) | — |  |  |
| 0 | [VersaceXcodes/make-a-task-management1234-qr0d4h](https://github.com/VersaceXcodes/make-a-task-management1234-qr0d4h) | — |  |  |
| 0 | [VersaceXcodes/project-management-software-8xnw1g](https://github.com/VersaceXcodes/project-management-software-8xnw1g) | — |  | Generated project for project-management-software |
| 0 | [VersaceXcodes/project-management-software-ewjt80](https://github.com/VersaceXcodes/project-management-software-ewjt80) | — |  | Generated project for project-management-software |
| 0 | [VersaceXcodes/real-time-pickups-rvxv5p](https://github.com/VersaceXcodes/real-time-pickups-rvxv5p) | — |  | Generated project for real-time-pickups |
| 0 | [VersaceXcodes/taxi-package-delivery-same-day-6im713](https://github.com/VersaceXcodes/taxi-package-delivery-same-day-6im713) | — |  | Generated project for taxi-package-delivery-same-day |
| 0 | [VersaceXcodes/ui-design-7jcl18](https://github.com/VersaceXcodes/ui-design-7jcl18) | — |  | Generated project for ui-design |
| 0 | [VersaceXcodes/ui-design-h3glv2](https://github.com/VersaceXcodes/ui-design-h3glv2) | — |  | Generated project for ui-design |
| 0 | [VersaceXcodes/ui-design-l3w1mm](https://github.com/VersaceXcodes/ui-design-l3w1mm) | — |  | Generated project for ui-design |
| 0 | [VersaceXcodes/ui-design-tjtwx4](https://github.com/VersaceXcodes/ui-design-tjtwx4) | — |  | Generated project for ui-design |
| 0 | [VersaceXcodes/ui-design-voraox](https://github.com/VersaceXcodes/ui-design-voraox) | — |  | Generated project for ui-design |
| 0 | [VersaceXcodes/urgent-same-day-delivery-shalj7](https://github.com/VersaceXcodes/urgent-same-day-delivery-shalj7) | — |  | Generated project for urgent-same-day-delivery |
| 0 | [VolatilityGroup/volatility-ws](https://github.com/VolatilityGroup/volatility-ws) | — | spec-at-root/docs (+1 product) |  |
| 0 | [Vrock691/Whist-algebrique](https://github.com/Vrock691/Whist-algebrique) | — | text~product(weak) (+1 product) | Application pour jouer au Whist Algébrique |
| 0 | [welthee/tx-executor-client](https://github.com/welthee/tx-executor-client) | — | spec-at-root/docs (+1 product) |  |
| 0 | [yogami/agent-arena-terminal](https://github.com/yogami/agent-arena-terminal) | — | lang=HTML (+1 spec/docs) |  |
| 0 | [yswarkare/ssg-monorepo](https://github.com/yswarkare/ssg-monorepo) | — | lang=CSS (+1 spec/docs) | Static Site Generation Frameworks |
| 0 | [yutari/vieten](https://github.com/yutari/vieten) | — | spec-at-root/docs (+1 product) |  |
| 0 | [ZenRay/LarkServiceCursor](https://github.com/ZenRay/LarkServiceCursor) | — | text~product(weak) (+1 product) |  |
| 0 | [zohaib7279/django-api](https://github.com/zohaib7279/django-api) | — |  |  |
