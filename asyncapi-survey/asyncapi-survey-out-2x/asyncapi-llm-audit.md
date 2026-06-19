# LLM audit of the rule-based classifier

Full LLM re-pass (`claude --model sonnet`) over every repo with readable text, compared to the rule-based bucket. **No buckets were changed** — disagreements are listed for review.


Agreement on rule-assigned SUT buckets (product/tooling/demo/spec): **456/769 = 59%**


## Confusion matrix (rows = rule bucket, cols = LLM verdict)

| rule \\ llm | product | tooling/library | demo/fixture | spec/docs | tangential | uncategorized | total |
|---|---|---|---|---|---|---|---|
| product | 164 | 18 | 76 | 15 | 18 | 2 | 293 |
| tooling/library | 27 | 123 | 33 | 14 | 24 | 2 | 223 |
| demo/fixture | 20 | 16 | 145 | 11 | 7 | 3 | 202 |
| spec/docs | 3 | 10 | 12 | 24 | 2 | 0 | 51 |
| catalog | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tangential | 0 | 0 | 0 | 0 | 11 | 0 | 11 |
| uncategorized | 62 | 14 | 45 | 20 | 56 | 8 | 205 |

## Disagreements for review (313)

Sorted by rule bucket, then LLM confidence. High-confidence rows are the likeliest rule errors.


### rule = demo/fixture (57)

- **WaleedAshraf/asyncapi-github-action** (11★) → llm=**tooling/library** (c=0.99) — GitHub Action that validates AsyncAPI schema files
  `GitHub action to validate if AsyncAPI schema file is valid or not.`
- **Mermade/openapi-filter** (172★) → llm=**tooling/library** (c=0.97) — Tool filtering AsyncAPI/OpenAPI/Swagger definitions
  `Filter internal paths, operations, parameters, schemas etc from OpenAPI/Swagger/AsyncAPI definitions`
- **eharishgit/hello-world** (0★) → llm=**tangential** (c=0.97) — GitHub tutorial hello-world repo, no real AsyncAPI use
  `Welcome to GitHub Welcome to GitHub—where millions of developers work together on software. Ready to get started? Let’s learn how this all w`
- **kanekoshoyu/asyncapi-rust-ws-template** (2★) → llm=**tooling/library** (c=0.97) — AsyncAPI code generator template producing Rust WebSocket clients
  `AsyncAPI Template for Generating Rust WebSocket Client`
- **actions-marketplace-validations/WaleedAshraf_asyncapi-github-action** (0★) → llm=**tooling/library** (c=0.95) — GitHub Action that validates AsyncAPI schema files
  `AsyncAPI Github Action This action validates if the AsyncAPI schema file is valid or not. Inputs filepath Required Path of the AsyncAPI sche`
- **event-catalog/eventcatalog** (2734★) → llm=**tooling/library** (c=0.95) — Discovery and governance tool for event-driven systems with AsyncAPI support
  `The discovery and governance layer for event-driven systems. Document your domains, services, events and schemas — for your teams and your A`
- **kevinswiber/spectral-function-past-tense** (1★) → llm=**tooling/library** (c=0.95) — Spectral custom function for linting AsyncAPI message names
  `Test values in Spectral to ensure the text is in past-tense.  Good for ensuring events in AsyncAPI and other use cases.`
- **weidmueller/u-os-hub-api** (8★) → llm=**spec/docs** (c=0.95) — API specifications for the u-OS Data Hub product
  `API specifications of the u-OS Data Hub`
- **api-components/amf-components** (0★) → llm=**tooling/library** (c=0.93) — Web components for visualizing AMF graph model
  `A set of web components based on LitElement that creates the visualization layer on top of the AMF's graph model.`
- **Raiffeisen-DGTL/rest-api-guide** (21★) → llm=**spec/docs** (c=0.92) — Bank-internal REST API best practices guidelines site
  `В этом репозитории находится REST API Best Practices.`
- **SDA-SE/sda-spring-boot-commons** (19★) → llm=**tooling/library** (c=0.92) — Library set to bootstrap Spring Boot services
  `A set of libraries to bootstrap spring boot services easily that follow the patterns and specifications promoted by the SDA SE`
- **open-data-fabric/open-data-fabric** (144★) → llm=**spec/docs** (c=0.92) — Open protocol specification for decentralized data exchange
  `Open protocol for decentralized exchange and transformation of data`
- **NASA-AMMOS/anms** (2★) → llm=**product** (c=0.9) — Real deployable network management system from NASA/JHU
  `Asynchronous Network Management System (ANMS)`
- **afmancilla/poc-submodule** (0★) → llm=**uncategorized** (c=0.9) — No readme or description to determine purpose
  `poc-submodule`
- **afmancilla/poc-subtree** (0★) → llm=**uncategorized** (c=0.9) — No meaningful content to determine purpose
  `poc-subtree`
- **ibm-cloud-architecture/vaccine-freezer-mgr** (0★) → llm=**product** (c=0.9) — Quarkus microservice for vaccine cold-chain management
  `Vaccine Freezer manager service This is a basic Quarkus reactive messaging app to listen to Alerts on freezer and also manage the life cycle`
- **CZSK-MicroHacks/MicroHack-GitHub-engineering-constitution** (0★) → llm=**spec/docs** (c=0.88) — Engineering governance constitution and standards documentation
  `My GitHub Copilot demo constitution This repository is the shared source of truth for engineering governance across all MicroHack projects. `
- **RidgeRun/ridgerun-immersive-teleoperation** (0★) → llm=**product** (c=0.88) — Real robot teleoperation platform with live video streaming
  `RidgeRun Immersive Teleoperation is a platform for remotely controlling robots with low-latency video streaming and reliable command channel`
- **call-sofia/callsofia-webhooks-docs** (0★) → llm=**spec/docs** (c=0.88) — Webhook event catalog and documentation for CallSofia service
  `CallSofia Webhooks v2 Real time event notifications for your CallSofia voice AI intake pipeline. Subscribe to call lifecycle events, lead qu`
- **kiransth77/aionmcp** (2★) → llm=**tooling/library** (c=0.88) — MCP server that imports and exposes AsyncAPI specs as agent tools
  `Autonomous Go MCP Server - Dynamic API specification importer with self-learning capabilities`
- **online-bridge-hackathon/data-formats** (0★) → llm=**spec/docs** (c=0.88) — Repository is specifications and example JSON payloads only
  `Specifications and Example JSONs`
- **Fortellis/example-spec** (0★) → llm=**spec/docs** (c=0.85) — Explicitly example specs for Fortellis platform APIs
  `Example Fortellis Specification`
- **Kong/developer.konghq.com** (23★) → llm=**spec/docs** (c=0.85) — Source code for Kong's developer documentation website
  `🦍 Source code for developer.konghq.com website.`
- **SebastianBorchardt1984/incubator-kie-kogito-runtimes** (0★) → llm=**product** (c=0.82) — Apache Kogito cloud-native business automation runtime platform
  `Kogito Kogito is the next generation of business automation platform focused on cloud native development, deployment and execution. Quick Li`
- **bike4life-organization/bike4life** (3★) → llm=**product** (c=0.82) — Real app with PubSub, MongoDB, Redis local dev stack
  `Bike4Life APIs Local dev instructions In order to start developing within the local environment you must first execute this command: bash do`
- **razvanguta/SmartLight** (3★) → llm=**product** (c=0.82) — Deployable smart home/office lighting IoT API
  `SmartLight API Table of Contents About The Project Built With Getting Started Installation Usage Roadmap License Contact Acknowledgments Abo`
- **yaraPB/RICER-project** (1★) → llm=**product** (c=0.82) — Production forest fire management platform with GIS and AI
  `RICER (Resilient Infrastructures and Coordinated Emergency Response) is a production-ready forest fire management platform designed specific`
- **BakangMonei/PolyGlot-Demo-Examples** (0★) → llm=**spec/docs** (c=0.8) — Architecture documentation for builders, not runnable software
  `Enterprise-Grade MySQL + MongoDB Implementation for Financial Services`
- **Mik-Grzeg/krewetka** (2★) → llm=**product** (c=0.8) — Real-time AI-based network intrusion detection system
  `krewetka What's that This project presents a real time intrusion detection system based on an artificial intelligence model. The purpose of `
- **Ravip2006/Demo** (0★) → llm=**spec/docs** (c=0.8) — Central contract repo for OpenAPI, GraphQL, gRPC, AsyncAPI specs
  `Central Contract Repository for the Order API What is Central Contract Repository? Please see Documentation This repository serves as the Ce`
- **fern-demo/stress-test** (0★) → llm=**tangential** (c=0.8) — Fern docs stress test; no genuine AsyncAPI usage
  `Stress Test of Fern Docs`
- **fkatsaras/functionality-dsl** (1★) → llm=**tooling/library** (c=0.8) — DSL and code generator for REST and WebSocket APIs
  `A DSL for creating low code backend applications`
- **tkubica12/gh-copilot-constitution** (1★) → llm=**tangential** (c=0.8) — GitHub Copilot governance template; AsyncAPI incidental standard
  `My GitHub Copilot demo constitution This repository is the shared source of truth for engineering governance across all MicroHack projects. `
- **sjarmak/CodeContextBench_Dashboard** (0★) → llm=**tangential** (c=0.78) — Benchmark platform for coding agents; AsyncAPI incidental
  `CodeContextBench Benchmark adapter generation, verification, and result analysis platform. CodeContextBench generates benchmark task adapter`
- **tiagobento/kie-monorepo** (1★) → llm=**tooling/library** (c=0.78) — KIE tooling applications and libraries monorepo
  `Apache KIE :: Monorepo PoC`
- **twimprine/GitWorkflow** (0★) → llm=**tangential** (c=0.78) — AI agent orchestrator design repo; no genuine AsyncAPI use
  `Autonomous PRP Batch Orchestrator Status : Design & Reference Implementation This repository contains the design documentation and reference`
- **victorbahl/mulequiz** (2★) → llm=**product** (c=0.78) — Deployed MuleSoft quiz app with WebSocket event API
  `MuleQuiz allows you to play with your friends / colleagues and improve your knowledge about MuleSoft.`
- **Nordic-MVP-GitOps-Repos/hypersonic-lightweight-cp4i** (9★) → llm=**tangential** (c=0.75) — GitOps deployment config for CP4I; AsyncAPI incidental
  `GitOps resources for IBM Cloud Pak for Integration`
- **RuiEusebio/confluent-selfservice** (2★) → llm=**product** (c=0.75) — Deployable Confluent/Kafka self-service management platform
  `Confluent Selfservice Requirements docker kind make helm provision local cluster The completion of the setup typically requires approximatel`
- **VALAWAI/C1_llm_email_replier** (0★) → llm=**product** (c=0.75) — Deployable AI processing component in VALAWAI framework
  `Reply automatically any received mail using a large language model (LLM) .`
- **starnold-redhat/rhdh-install** (0★) → llm=**tangential** (c=0.75) — Ansible demo-environment setup; AsyncAPI incidental
  `Ansible Developer Self Service This playbook will setup a demo environment to show the ansible self service demo. This demo has the followin`
- **sonra44/QIKI_DTMP** (0★) → llm=**product** (c=0.73) — Space simulation platform with operator console and telemetry pipeline
  `Truth-first space-simulation game with ORION operator surface and simulation-truth telemetry pipeline.`
- **gsperim/account-engine-lab** (0★) → llm=**product** (c=0.72) — Financial posting engine with concrete NFRs; two real services
  `Core engine focused on debit and credit postings with daily balance calculation and consolidation.`
- **leynos/bournemouth** (0★) → llm=**product** (c=0.72) — Experimental deployable chat app with RAG and knowledge graph
  `Raggy Graph Chat`
- **manuschillerdev/esphome-elero** (2★) → llm=**product** (c=0.72) — Deployable IoT firmware component for Elero RF devices
  `An ESPHome component to control Devices with the bidirectional Elero protocol (Covers and Lights)`
- **zuevrs/yanote** (0★) → llm=**tooling/library** (c=0.72) — HTTP contract coverage tool for API spec validation
  `yanote Yanote показывает не абстрактное «тесты прошли», а доказуемое покрытие HTTP контракта по живым вызовам: рекордер пишет events.jsonl ,`
- **innovatrics/smartface-integrations** (1★) → llm=**product** (c=0.68) — Real-world SmartFace integrations with deployed production code
  `SmartFace Integrations This repository contains integrations of Innovatrics SmartFace with various products or technologies. Repository is a`
- **nekofar/warpcast** (2★) → llm=**tooling/library** (c=0.65) — TypeScript client library for Warpcast APIs
  `TypeScript client for interacting with Warpcast APIs`
- **specdojo/specdojo** (0★) → llm=**spec/docs** (c=0.65) — Documentation framework with templates and guidelines, not runnable software
  `SpecDojo SpecDojoは、 仕様駆動開発のためのドキュメントフレームワーク です。 プロダクトの構築・改修に必要なドキュメントを体系化し、 記述規約、サンプル、生成AI向け指示テンプレート、ツールを通じて、 プロダクトのライフサイクル全体を一貫して支援します。 仕様駆`
- **mx-kshitij/filedropper** (0★) → llm=**tooling/library** (c=0.62) — NPM package React component with demo project link
  `Filedropper [Filedropper for react client] Features [feature highlights] Usage [step by step instructions] Demo project [link to sandbox] Is`
- **HenderOrlando/booklyapp** (0★) → llm=**product** (c=0.6) — Institutional booking platform with microservices architecture
  `Plataforma diseñada para la gestión eficiente de reservas`
- **genelaz/blue_viper_pro** (0★) → llm=**uncategorized** (c=0.6) — Flutter starter with minimal description; purpose unclear
  `BlueViper — saha haritası ve atış araçları gibi.`
- **invivo-digital-factory/openapi-compiler-ts** (0★) → llm=**tooling/library** (c=0.6) — Compiles OpenAPI/AsyncAPI docs to TypeScript types and validation
  `A project to compile openapi doc to ts type and joi validation`
- **umdloop/umdloop_gui** (0★) → llm=**product** (c=0.58) — Real ROS2 web GUI application with WebSocket backend
  `Getting Started Prerequisites uv (Python package manager) Node.js and npm ROS2 Humble Setup Navigate into the web gui folder: bash cd umdloo`
- **varunaditya27/sentinel-orchestrator-network** (0★) → llm=**product** (c=0.52) — AI-powered security and governance platform for Cardano
  `🛡️ Sentinel Orchestrator Network (S.O.N.) AI Powered Security & Governance Platform for Cardano 🔒 Fork Detection • ⚖️ Governance Autopilot •`
- **paulus85/companion** (0★) → llm=**product** (c=0.5) — Office application monorepo, minimal info available
  `Monorepo for the Companion project, the app for your office`
- **skunkforce/node-agnostic-datastream-interface** (3★) → llm=**tooling/library** (c=0.5) — C++23 datastream library with message schemas; AsyncAPI likely incidental
  `NADI: Node Agnostic Datastream Interface Table of Contents Introduction Core Concepts Message Schemas C++ Example Python Example Related Pro`

### rule = product (129)

- **ajgarciaparadigma/asyncapi-publisher** (0★) → llm=**demo/fixture** (c=0.98) — Explicitly illustrates AsyncAPI generator with Spring Boot
  `Hello Kafka API Example to ilustrate AsycAPI generator From AsynApi spec i've created a springboot project Steps done 1 Create asyncapi spec`
- **BitKa-Exchange/bitka-exchange** (1★) → llm=**demo/fixture** (c=0.97) — Explicitly educational clone, not intended for production
  `Bitkub Clone project for learning`
- **caochun/tollgate** (3★) → llm=**demo/fixture** (c=0.97) — Readme explicitly states project is for demonstrating microservice design
  `Tollgate 本项目为事件驱动的微服务系统设计演示之用。系统包括若干独立服务（SpringBoot应用）相互协同完成车辆的收费放行业务。 具体请见架构说明 运行 shell mvn clean install 启动MQ ./start server.sh 启动车道服务 cd `
- **cibanezb95STG/quoteAssessmentCIB** (0★) → llm=**demo/fixture** (c=0.97) — Job application assessment project, not production software
  `Assessment for backend position. Project for financial quotes.`
- **event-catalog/generators** (14★) → llm=**tooling/library** (c=0.97) — Plugin integrations/generators for EventCatalog including AsyncAPI
  `Plugin integrations for EventCatalog`
- **microcks/microcks** (1963★) → llm=**tooling/library** (c=0.97) — Cloud-native API mocking and testing platform tool
  `The open source, cloud native tool for API Mocking and Testing. Microcks is a Cloud Native Computing Foundation incubating project 🚀`
- **pfarkya/asyncApi_AccountManagerEDA** (2★) → llm=**demo/fixture** (c=0.97) — Explicitly demonstrates EDA creation using AsyncAPI codegen
  `This is an Account Management Application in Event Driven Architecture.`
- **prafulrana/asyncAPIExamples** (1★) → llm=**spec/docs** (c=0.97) — Collection of AsyncAPI specs for real-world broker channels
  `Collection of AsyncAPI specs with real world broker channels.`
- **thushalya/asyncapi-tools** (0★) → llm=**tooling/library** (c=0.97) — Ballerina WebSocket service to AsyncAPI generator tool
  `Source code for Ballerina WebSocket service to AsyncAPI generator cmd tool`
- **ClearEyesFullHearts/asyncapi-pub-middleware** (0★) → llm=**tooling/library** (c=0.96) — Express middleware library that reads AsyncAPI files to validate
  `Add a validating publisher object, from an AsyncAPI file description, to your request`
- **ClearEyesFullHearts/asyncapi-sub-middleware** (0★) → llm=**tooling/library** (c=0.96) — Express middleware library generating routes from AsyncAPI spec
  `Create routes and validation for an express-like async server`
- **aml-org/als** (32★) → llm=**tooling/library** (c=0.96) — Language Server Protocol implementation for API specs
  `Language Server implementation for AML and AML-defined metadata`
- **delano/postman-mcp-server** (154★) → llm=**tangential** (c=0.96) — Postman MCP server; no AsyncAPI relevance
  `An MCP server that provides access to Postman.`
- **microcks/microcks-testcontainers-go** (10★) → llm=**tooling/library** (c=0.96) — Go library embedding Microcks into unit tests
  `Go lib for Testcontainers that enables embedding Microcks into your unit tests with lightweight, throwaway instance thanks to containers.`
- **Chinitsu-Challenge/chinitsu-demo** (4★) → llm=**demo/fixture** (c=0.95) — Demo mahjong game, name and readme confirm demo purpose
  `Chinitsu Showdown 清一色对战 两人实时麻将对战游戏，专注于 清一色（Chinitsu） 玩法。 目录 快速开始 功能模块 服务端 前端 WebSocket 接口 连接地址 客户端发送消息格式 服务端响应消息格式 Action 详细说明 错误码 游戏流程 配置说明`
- **GUR-ok/otus-microservice-architecture** (0★) → llm=**demo/fixture** (c=0.95) — Explicitly homework for OTUS 2022 course
  `Домашние задания по курсу "OTUS 2022. Микросервисная Архитектура". Автор: Горелов Юрий.`
- **Kuestenlogik/Bowire** (4★) → llm=**tooling/library** (c=0.95) — Multi-protocol API workbench supporting AsyncAPI among others
  `Multi-protocol API workbench for .NET — discover, invoke, record, mock, replay across gRPC, REST, GraphQL, MQTT, SignalR, WebSocket, SSE, MC`
- **atharvagadkari05/template_EDA_API** (3★) → llm=**demo/fixture** (c=0.95) — Streetlights canonical AsyncAPI example reimplemented
  `API developed by the use of AsyncAPI tool which helps to document and write code for Event-driven-architecture APIs.`
- **btravers/amqp-contract** (18★) → llm=**tooling/library** (c=0.95) — Library providing type-safe AMQP/RabbitMQ contracts for TypeScript
  `Type-safe contracts for AMQP/RabbitMQ messaging with TypeScript`
- **kyleczhang/cits5506-iot-parkreserve-group29** (0★) → llm=**demo/fixture** (c=0.95) — CITS5506 university course IoT project
  `ParkReserve ParkReserve is a multi tier IoT parking reservation system built for CITS5506 Group 29. It combines: a cloud backend for account`
- **ngscheurich/elixirconf-eu-2024** (0★) → llm=**demo/fixture** (c=0.95) — Conference talk source code, collaborative game demo
  `🗺️ “Let’s Go on an Adventure” (ElixirConf EU 2024)`
- **anonymousc/ft_transcendance-42** (1★) → llm=**demo/fixture** (c=0.94) — Explicitly created as part of 42 school curriculum
  `digitalyzing travel planning stuff`
- **Ramonjrtan/event-driven-order-platform-qa** (0★) → llm=**demo/fixture** (c=0.93) — Recruiter portfolio simulating QA, not production system
  `QA portfolio simulating testing of an event-driven microservices platform, covering asynchronous workflows, event validation, idempotency, f`
- **SynapticFour/sc-specs** (0★) → llm=**spec/docs** (c=0.93) — Repository of API specifications and schemas for compute fabric
  `Synaptic Core API Specifications API specifications for the Synaptic Core scientific compute fabric — a domain agnostic set of primitives fo`
- **bb-frc-workshops/wpilib-ws-schema** (2★) → llm=**spec/docs** (c=0.93) — AsyncAPI schema defining WPILib WebSocket protocol, not runnable software
  `Schema for the WPILib WebSocket extension`
- **cyberlytics/Conversphere** (0★) → llm=**demo/fixture** (c=0.93) — University course project (WAE at OTH Amberg Weiden)
  `WaeProjektarbeit Conversphere This is the Conversphere project for the WAE course at OTH Amberg Weiden. Start PLS NOTE: You need to run 'npm`
- **ewanvidal/SimuMarty** (2★) → llm=**demo/fixture** (c=0.93) — End-of-studies school project, educational robotics simulator
  `SimuMarty est une application web moderne de simulation robotique éducative permettant aux étudiants d'apprendre la programmation robotique `
- **jean0313/k2a** (0★) → llm=**tooling/library** (c=0.93) — CLI tool that generates AsyncAPI specs from a Kafka cluster
  `k2a`
- **olaviolacerda/notification** (1★) → llm=**demo/fixture** (c=0.93) — Explicitly a template/seed repo for bootstrapping new projects
  `Typescript Seed Backend Description This is a template repository to serve as seed for new projects developed @somosphi. This repo uses Type`
- **postman-cs/postman-aws-spec-discovery-action** (0★) → llm=**tooling/library** (c=0.93) — GitHub Action that discovers and exports API specs from AWS
  `Public customer preview GitHub Action that discovers and exports API specs from AWS services (API Gateway, AppSync, EventBridge, SNS, and mo`
- **vincenzocorso/car-sharing** (3★) → llm=**demo/fixture** (c=0.93) — Explicitly a practice project for learning microservice patterns
  `A microservice application developed to practise implementing some of the most common patterns.`
- **way-platform/mbz-go** (2★) → llm=**tooling/library** (c=0.93) — Go SDK and CLI for Mercedes-Benz Fleet API
  `Go SDK for the Mercedes-Benz Fleet API`
- **ziyashaw/backstage_demo2** (0★) → llm=**demo/fixture** (c=0.93) — Second Backstage demo repo, same pattern
  `Backstage What is Backstage? Backstage is an open platform for building developer portals. Powered by a centralized software catalog, Backst`
- **Alex009/architecture-sprint-3** (0★) → llm=**demo/fixture** (c=0.92) — Microservices course practical assignment
  `Практическое задание по разделению на микросервисы`
- **SolaceLabs/solace-tools-typescript** (5★) → llm=**tooling/library** (c=0.92) — Libraries and CLI tools for Solace platform including AsyncAPI importer
  `This repository contains tools to enable interaction with the Solace PubSub+ Platform including an AsyncAPI Importer`
- **SourceOS-Linux/sourceos-spec** (1★) → llm=**spec/docs** (c=0.92) — Machine-readable contract layer of JSON Schemas and API fragments
  `sourceos-spec`
- **Veriflite/portal-api** (0★) → llm=**spec/docs** (c=0.92) — Repository content is the Portal API specification document
  `Veriflite Portal API Specification`
- **d1m1tur/PGJ-2026** (0★) → llm=**demo/fixture** (c=0.92) — Game jam prototype server, not production
  `Plovdiv Game Jam 2026 project`
- **danilfg/bank-test-platform** (6★) → llm=**demo/fixture** (c=0.91) — Educational banking platform for QA learning
  `EasyITLab Bank EasyBank is an open source educational banking platform designed for learning QA automation, API testing, DevTools debugging,`
- **Ashish8951/poker-docs** (0★) → llm=**spec/docs** (c=0.9) — Single HTML page serving Swagger and AsyncAPI API docs
  `API Documentation Single HTML page that serves all REST (Swagger UI) and WebSocket (AsyncAPI) documentation. Prerequisites Node.js 18+ (for `
- **Lynda1423/gestion-vehicules** (0★) → llm=**demo/fixture** (c=0.9) — Master 1 university microservices course project
  `SGFV Système Global de Gestion de Flotte de Véhicules 🏎️📡 🎓 Projet Master 1 Architecture Micro Services & Cloud Native Bienvenue dans le pro`
- **MaxwellGBrown/aws_websockets_eventbus** (0★) → llm=**demo/fixture** (c=0.9) — Explicitly an example eventbus with AWS CloudFormation
  `Example Eventbus with a WebSocket API Gateway`
- **Sriramanenivikas/Intelligent-Warehouse-Orchestration-System** (1★) → llm=**spec/docs** (c=0.9) — Documentation-first skeleton explicitly without application code
  `IWOS  is a unified fulfillment platform that combines quick commerce (dark stores, rapid picking), large-scale e-commerce fulfillment (pick-`
- **gravitee-io/gravitee-apim-mcp-server** (2★) → llm=**tooling/library** (c=0.9) — MCP server tool wrapping Gravitee APIM for AI assistants
  `Gravitee API Management (APIM) MCP Server This repository contains a Model Context Protocol (MCP) server for the Gravitee.io API Management `
- **krittamark/incident-tracking-service** (0★) → llm=**demo/fixture** (c=0.9) — CS366 course project microservice
  `Microservice for the source of truth for fundamental incident data. Part of the CS366 Microservices and Serverless Architectures course proj`
- **mcrawfo2/go-msx** (3★) → llm=**tooling/library** (c=0.9) — Go library for building Cisco MSX microservices
  `Go library for building MSX microservices`
- **mindsmiths/docs** (2★) → llm=**spec/docs** (c=0.9) — Documentation site for Mindsmiths Platform
  `Mindsmiths Platform Docs`
- **snatalija/IOT** (0★) → llm=**demo/fixture** (c=0.9) — Explicitly an end-to-end demo system for IoT microservices
  `IoT Amazon Delivery — Mikroservisi (REST + gRPC + MQTT + NATS + ML) End‑to‑end demo sistem za isporuke koji: prima događaje sa “senzora” (si`
- **wallaceespindola/contract-first-integrations** (0★) → llm=**demo/fixture** (c=0.9) — Reference implementation demonstrating contract-first patterns
  `Contract First Integrations`
- **ChunPingWang/saga-kafka** (0★) → llm=**demo/fixture** (c=0.88) — Learning/demo project for Kafka Saga orchestration pattern
  `Saga Kafka 分散式交易系統 使用 Saga 編排模式 (Orchestration Pattern) 實作的分散式交易系統，透過 Apache Kafka 進行微服務間的非同步通訊。 目錄 系統架構 Saga 編排模式 Clean Architecture 領域驅動設計`
- **MCI-MS-WS2025-Advanced-Project/crazy-labyrinth-gameserver** (0★) → llm=**demo/fixture** (c=0.88) — Winter-semester 2025 course/workshop project
  `The Amazing Labyrinth - Game Server`
- **SayReal-US/API-designs---Software-Engineer-Thesis-K22** (0★) → llm=**spec/docs** (c=0.88) — Thesis API design specifications for microservice rental service
  `API design for a microservice-based driver rental service with REST endpoints and real-time tracking.`
- **axvg/store-microservices** (0★) → llm=**demo/fixture** (c=0.88) — Self-described sample store application, no readme
  `Sample store application using microservices`
- **bfl-ajay/AsyncApi-Example** (0★) → llm=**demo/fixture** (c=0.88) — Repo named 'Example', demonstrates AsyncAPI with WebSocket API
  `This is a secure, production-ready WebSocket-based API built using Node.js, MySQL, and AsyncAPI specification. It supports user registration`
- **dataGriff/dog.rescue.api** (0★) → llm=**spec/docs** (c=0.88) — Primarily an OpenAPI contract for a dog adoption platform
  `Dog Rescue Adoption API An OpenAPI 3.0 contract for a multi rescue dog adoption platform. Rescue organisations can register themselves and a`
- **kaaaaakun/AsyncAPI-mock-server** (0★) → llm=**tooling/library** (c=0.88) — Tool that generates WebSocket mock servers from AsyncAPI specs
  `WebSocket Mock Server using AsyncAPI Generator このプロジェクトは、AsyncAPI Generator を使用して WebSocket モックサーバーを作成する方法を示します。 サーバーは、AsyncAPI 仕様に基づいて WebS`
- **somosphi/ts-seed-jest** (5★) → llm=**demo/fixture** (c=0.88) — Explicitly a seed/template repo for new TypeScript projects
  `Typescript backend template with Jest`
- **danieldan0/microservice-store** (1★) → llm=**spec/docs** (c=0.87) — C4 architecture documentation for online shop system
  `C4 Architecture Documentation – Online Shop System Online Shop System Context Diagram This diagram shows the high level view of the Online S`
- **djoleant/IoTS-Smart-building** (0★) → llm=**demo/fixture** (c=0.87) — Student IoT microservices project with named student IDs
  `Internet of Things and Services project for Smart buildings`
- **The-All-Knowing/cosmiccpp** (3★) → llm=**demo/fixture** (c=0.85) — Book companion code reimplementing Python architecture book in C++
  `Сервис управления распределением позиций заказов в партиях.`
- **UNIZAR-30226-2025-05/adrenalux-backend** (0★) → llm=**demo/fixture** (c=0.85) — University course project for collectible card game
  `⚽️ ADRENALUX ⚽️ Backend Adrenalux es un juego de cartas coleccionables basado en la liga española, donde los jugadores pueden coleccionar, i`
- **Unizar-30226-2026-11/Backend** (0★) → llm=**demo/fixture** (c=0.85) — University course project (Unizar group 11, 2026) backend
  `Repositorio para el backend del proyecto Tale of Recognition.`
- **Unizar-30226-2026-11/Movil** (0★) → llm=**demo/fixture** (c=0.85) — University course project mobile frontend, same cohort
  `Repositorio para el frontend móvil del proyecto Tale of Recognition.`
- **allenheltondev/gopher-holes-unlimited** (61★) → llm=**tangential** (c=0.85) — OpenAPI spec for fictional site, not AsyncAPI
  `Example OpenAPI Spec for fictional website: Gopher Holes Unlimited`
- **EduRS14/sistema-recomendacion-distribuido-peliculas** (0★) → llm=**demo/fixture** (c=0.82) — Academic distributed system project, no production indicators
  `Sistema de Recomendación Distribuido hecho con Go para el Backend y React para el Frontend, levantado bajo una orquestación de contenedores `
- **Owen-Richards/ai-nutritionist** (0★) → llm=**tangential** (c=0.82) — AWS/WhatsApp bot; no AsyncAPI connection evident
  `� Serverless AI Nutritionist Assistant - WhatsApp/SMS bot powered by AWS Bedrock for personalized, budget-friendly meal planning`
- **RidaNaz/Agentic-Todo** (1★) → llm=**demo/fixture** (c=0.82) — Progressive 6-phase learning project, not production service
  `Naz Todo — Agentic Todo App A full stack AI powered todo application built across 6 progressive phases, from a console app to a cloud deploy`
- **Xen0Xys/N2I-2024-API** (0★) → llm=**demo/fixture** (c=0.82) — NestJS starter for N2I-2024 coding competition
  `[circleci image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token abc123def456 [circleci url]: https://circleci.com/gh`
- **andreitudose2000/ingineria-programarii** (0★) → llm=**demo/fixture** (c=0.82) — Student IoT project for programming engineering course
  `Smart deskchair IoT app`
- **ayointegral/cloud-sandbox-backstage** (1★) → llm=**demo/fixture** (c=0.82) — Backstage sandbox/template portal, not a production service
  `Cloud Sandbox - Backstage Developer Portal with custom catalog and templates`
- **baldimir/kie-backend** (0★) → llm=**demo/fixture** (c=0.82) — Explicitly a testing repo for alternative repository structure
  `All the backend code for the Apache KIE project (testing repository for an alternative repository structure)`
- **devmentors/Mikroserwisy-Revisited** (2★) → llm=**demo/fixture** (c=0.82) — Companion code for a Polish microservices course
  `[PL] Mikroserwisy 6 lat później czyli... jak nie utonąć 😉`
- **funny-bunny-corp/payment-service** (0★) → llm=**demo/fixture** (c=0.82) — Demo org name; generic payment service sample
  `Payment Service In a payment gateway context, a payment service that handles both payment and refund requests would be designed to facilitat`
- **ivankahl/asyncapi-food-delivery** (0★) → llm=**demo/fixture** (c=0.82) — Food delivery demo API, archetypal AsyncAPI example pattern
  `Food Delivery API Real time API that lets you place orders for food at resutarants and track the progress of the meal. Running the server 1.`
- **jsa4000/Internal-Development-Platform** (2★) → llm=**demo/fixture** (c=0.82) — Backstage IDP demo/showcase setup, not a deployed product
  `Backstage as Internal Developer Platform (IDP)`
- **robev2252060/2247107_MAP** (3★) → llm=**demo/fixture** (c=0.82) — Numbered course-ID name indicates student project
  `Mars Automation Platform (MAP) is an event-driven system that ingests heterogeneous Mars habitat sensor data, normalizes it into a unified e`
- **LordMoMA/Intelli-Mall** (63★) → llm=**demo/fixture** (c=0.8) — Explicitly simulates retail; showcase of distributed patterns
  `A distributed system that simulates a retail experience coupled with some futuristic shopping robots.`
- **Minister2405/my-docs** (0★) → llm=**spec/docs** (c=0.8) — Docusaurus-based documentation website
  `Website This website is built using Docusaurus, a modern static website generator. Installation bash yarn Local Development bash yarn start `
- **The-Microservice-Dungeon/game** (0★) → llm=**demo/fixture** (c=0.8) — Educational game project teaching microservice architecture
  `Test Coverage Report Code Quality Report game This README file should be adapted to include the following information: (1) How can the servi`
- **The-Microservice-Dungeon/gamelog** (1★) → llm=**demo/fixture** (c=0.8) — Educational game log service for microservices course
  `gamelog Running this service Prerequisites To run this service and its dependencies, the following things need to be installed: Docker and D`
- **The-Microservice-Dungeon/trading** (1★) → llm=**demo/fixture** (c=0.8) — Educational trading service for microservices course
  `trading Setup for local testing 1. install a local apache client like laragon or xampp 2. create a local mysql database for the project 3. c`
- **Yodata/real-estate** (4★) → llm=**spec/docs** (c=0.8) — Shared event data standards catalog for real estate
  `standard events for real estate software and data integration`
- **kanekoshoyu/exchange-collection** (23★) → llm=**spec/docs** (c=0.8) — Collection of machine-readable crypto exchange API specifications
  `Collection of Crypto Exchange OpenAPI and Generated Clients`
- **PikPakPik/T-JSF-600** (0★) → llm=**demo/fixture** (c=0.78) — Course-code named IRC chat school project
  `IRC Chat IRC Chat est une application de messagerie en temps réel avec la possiblité de créer des cannaux et d'envoyer des messages privées `
- **SoftwareEngineerUB/SmartEnergy** (2★) → llm=**demo/fixture** (c=0.78) — Romanian university IoT student project for home energy
  `SmartEnergy este o aplicatie IoT al cărei scop este de a interacționa cu device-urile smart dintr-o locuință pentru a eficientiza energia co`
- **joass1/ESD-Ticket-booking** (0★) → llm=**demo/fixture** (c=0.78) — IS213 course code; school group project (G3T1)
  `Event Ticketing Platform IS213 Enterprise Solution Development G3T1 A microservices based event ticketing system that allows users to browse`
- **marcgr9/ptbox-assignment** (0★) → llm=**demo/fixture** (c=0.78) — School assignment server project
  `PTBOX Assignment server How to run 1. Clone this repository, including the theHarvester submodule (you can use recurse submodules ) 2. Run f`
- **springwolf/springwolf-app** (0★) → llm=**tooling/library** (c=0.78) — Service for viewing and publishing to multiple AsyncAPI docs
  `Springwolf App Table Of Contents About Usage Examples Limitations Future Plans About Springwolf App is a service that allows the user to vie`
- **Brico87/seed-kafka** (0★) → llm=**demo/fixture** (c=0.75) — Kafka infrastructure seed/starter project
  `Lancement infra C:\Projects\seed kafka docker compose up d [+] Running 5/6 Volume "seed kafka klaw data" Created 3.3s ✔ Container klaw core `
- **ChiragSethi-1153/RMHA** (0★) → llm=**demo/fixture** (c=0.75) — Stock NestJS starter template with no custom product logic
  `[circleci image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token abc123def456 [circleci url]: https://circleci.com/gh`
- **SEP4Y-2025/SEP4** (0★) → llm=**demo/fixture** (c=0.75) — School semester engineering project with generic Docker setup
  `SEP4 Installation Prerequisites Docker Docker Compose Steps 1. Clone the repository: sh git clone https://github.com/yourusername/your repo.`
- **blagoySimandov/takgo** (0★) → llm=**demo/fixture** (c=0.75) — Personal multiplayer tic-tac-toe project with spec generated demo
  `TakGo Multiplayer tic tac toe. Go HTTP/WebSocket server with a terminal UI client. REST API Echo + Huma, OpenAPI spec and Swagger UI served `
- **dataGriff/dog-walking** (0★) → llm=**spec/docs** (c=0.75) — Product spec and contract with only a reference implementation
  `dog walking A product specification, OpenAPI contract, and reference API implementation for the Stardogwalker dog walking management platfor`
- **dgnsrekt/gexbot-faker-api** (4★) → llm=**demo/fixture** (c=0.75) — Mock/faker API replaying historical market data for testing
  `GEX Faker API Mock API server that replays historical GexBot market data with per API key sequential playback. Includes REST API, WebSocket `
- **masechkacat/tic-tac-toe-server** (2★) → llm=**demo/fixture** (c=0.75) — Game server demo using WebSockets
  `This API allows real-time interaction in a Tic Tac Toe game via WebSockets.`
- **nesaa-a/SPDD-EventSystem** (0★) → llm=**demo/fixture** (c=0.75) — Student project path in OneDrive Desktop, course assignment
  `SPDD EventSystem — Run instructions Recommended: run the full stack using Docker Compose (infra + services). From PowerShell: powershell cd `
- **opengeospatial/developer-website** (7★) → llm=**tangential** (c=0.75) — OGC standards documentation site; AsyncAPI likely incidental
  `OGC Developer Website`
- **sohailhaider/backstage-search-github-issues-plugin** (0★) → llm=**tangential** (c=0.75) — Backstage plugin for GitHub issues; AsyncAPI only incidental
  `Backstage What is Backstage? Backstage is an open platform for building developer portals. Powered by a centralized software catalog, Backst`
- **yukihito-jokyu/postman-mcp-server** (0★) → llm=**tangential** (c=0.75) — MCP server AI agent tool, AsyncAPI incidental
  `Postman MCP Server Version: v0.2.0 An MCP server that provides access to the Postman API. Functionality is based on the official OpenAPI spe`
- **zynax-io/zynax** (1★) → llm=**tangential** (c=0.75) — AI agent workflow control plane, AsyncAPI incidental
  `Declarative, cloud-native, engine-agnostic control plane for AI agent workflows`
- **j-alonso-guerra/open-api-public** (0★) → llm=**tangential** (c=0.73) — OpenAPI-only ecommerce spec repo; AsyncAPI only incidental
  `Ecommerce Platform API Documentation This repository contains OpenAPI 3.0 specifications for the microservices of the Ecommerce Platform, wr`
- **Navdeep-12/Backstage** (0★) → llm=**tangential** (c=0.72) — Standard Backstage fork, no AsyncAPI-specific purpose evident
  `Backstage English \ 한국어 \ 中文版 What is Backstage? Backstage is an open platform for building developer portals. Powered by a centralized soft`
- **dataGriff/pet.insurance.domain.app.v1** (0★) → llm=**demo/fixture** (c=0.72) — Spec-driven example API, educational pattern demonstration
  `pet.insurance.domain.app.v1 A spec driven, contract first Pet Insurance REST API built with Python/FastAPI. Pet owners can register their pe`
- **isehuetdk/backstage** (0★) → llm=**demo/fixture** (c=0.72) — Test deployment of Backstage developer portal, not production
  `Test deployment of Backstage for Azure Self-service`
- **josebusv/enterprise-integration-platform** (0★) → llm=**demo/fixture** (c=0.72) — Academic-style project describing enterprise integration patterns
  `Enterprise Integration Platform 1. Contexto Las organizaciones modernas operan sobre múltiples sistemas críticos como ERPs, plataformas de c`
- **kishoretvk/AgentAI** (1★) → llm=**tangential** (c=0.72) — AI agent collection; AsyncAPI mentioned only incidentally
  `this is a collection of AI agents which can indpdently work with any LLM to help create tasks and get tasks easier by helping LLM  as extend`
- **mattlat21/homeassistant** (0★) → llm=**tangential** (c=0.72) — Home Assistant config directory, AsyncAPI incidental
  `Anything Home Assistant Related`
- **phalanxduel/phalanxduel** (1★) → llm=**tangential** (c=0.72) — Card game application; no AsyncAPI mention in readme
  `Arm yourself for battle with spades and clubs and shields against your opponent. Phalanx is a head-to-head combat card game for two or more `
- **project-ascend-io/intracom-backend** (0★) → llm=**demo/fixture** (c=0.72) — Express TypeScript boilerplate template, not a specific product
  `Intracom's backend uses ExpressJS with Typescript, MongoDB`
- **vhurryharry/OOT** (0★) → llm=**tangential** (c=0.72) — E-learning web app, no meaningful AsyncAPI usage visible
  `Olive Oil Times`
- **zdmooc/TradeOps-GenAI-Integration** (0★) → llm=**demo/fixture** (c=0.72) — Portfolio project showcasing trading integration patterns
  `TradeOps GenAI Integration Hub Trading · Integration IA/GenAI · API/Event/Workflow · Agentic AI · MCP · RAG · Run Projet portfolio "Consulta`
- **DevOpsMadDog/Fixops** (5★) → llm=**tangential** (c=0.7) — Security platform; AsyncAPI not mentioned, incidental at best
  `ALdeci — AI-powered Decision Intelligence for Security Teams. Multi-LLM consensus (GPT-4 + Claude + Gemini), built-in pentest engine, signed`
- **DevOpsMadDog/aldeci-core** (0★) → llm=**tangential** (c=0.7) — Same ALDECI security platform; no AsyncAPI usage described
  `ALDECI ASPM + CTEM + CSPM unified security platform — self hosted, AI native, multi LLM consensus. Replace your $500K security stack (Snyk +`
- **SoldierrBoy/EventTicketBookingSystem** (1★) → llm=**demo/fixture** (c=0.7) — Personal portfolio project with full-stack boilerplate structure
  `Event Ticket Booking System A comprehensive event ticket booking system built with .NET Core backend, React frontend, PostgreSQL database, a`
- **bshongwe/fintech-api** (1★) → llm=**demo/fixture** (c=0.7) — Single-dev portfolio showcase of fintech API patterns
  `fintech api — Secure Financial Services Platform A production ready fintech API platform with OAuth2 authorization, account management, and `
- **decker757/Smart-Clinic-Queue-ESD** (1★) → llm=**demo/fixture** (c=0.68) — ESD likely school course; event-driven microservices project
  `Smart Clinic Queue ESD Smart Clinic Queue is a polyclinic queue management platform built on an event driven microservices architecture. The`
- **BalaNarvar/BackStage1** (0★) → llm=**tangential** (c=0.65) — Appears to be an upstream Backstage fork with no AsyncAPI focus
  `Backstage What is Backstage? Backstage is an open platform for building developer portals. Powered by a centralized service catalog, Backsta`
- **EdithRW/rw-backend-dashboard** (0★) → llm=**demo/fixture** (c=0.65) — Described as backend test; minimal info, not production
  `backend test for rw dashboard`
- **Sakshamjain98/skillforge-meet** (0★) → llm=**demo/fixture** (c=0.65) — Personal portfolio video conferencing app, no production indicators
  `SkillForge Meet — Full Stack Video Conferencing Project Structure skillforge meet/ ├── apps/ │ ├── backend/ Node.js + Express + Socket.IO + `
- **SmartSleepIoT/SmartSleepCoding** (0★) → llm=**demo/fixture** (c=0.65) — IoT student project with standard template README structure
  `SmartSleep - an API for an IoT bed device`
- **fenix-hub/cns-project-backend** (0★) → llm=**tangential** (c=0.65) — OpenAPI-focused backend; AsyncAPI not mentioned in readme
  `CNS Server OpenAPI specs This project was created using node (typescript), express and mongodb. The following list of commands illustrates h`
- **naomesh/naomesh-web-api** (0★) → llm=**demo/fixture** (c=0.65) — REST API explicitly built for a demonstrator webapp
  `REST api for the demonstator webapp`
- **newsukarun/async-api** (0★) → llm=**tooling/library** (c=0.65) — Server providing AsyncAPI tools, pre-1.0 under development
  `Server API Server API providing official AsyncAPI tools :loudspeaker: ATTENTION: This package is still under development and has not publish`
- **davidosantos/backstage** (0★) → llm=**tangential** (c=0.62) — Backstage fork with no clear AsyncAPI-specific purpose
  `Backstage 🏖️ The week beginning the 26th of June, some of the maintainers will be taking a well earned Summer Holiday break. We will be slow`
- **FlorinaMt/SEP4** (0★) → llm=**demo/fixture** (c=0.6) — SEP4 suggests 4th-semester school project
  `SEP4 Installation Prerequisites Docker Docker Compose Steps 1. Clone the repository: sh git clone https://github.com/yourusername/your repo.`
- **EthanSheehan/Grid-Sentinel** (0★) → llm=**demo/fixture** (c=0.58) — POC C2 system; fantastical scope reads as demo/prototype
  `tags: [grid sentinel] Grid Sentinel C2 — Multi Agent Decision Centric Command & Control Overview Grid Sentinel C2 is a high fidelity Command`
- **FrackiewiczP/info_bubbles** (1★) → llm=**demo/fixture** (c=0.55) — Multiple student authors, minimal project description
  `Authors Paweł Frąckiewicz Jan Janiszewski Ignacy Sujecki How to run To run the app run docker compose up from the project root. Web app will`
- **dlcastra/WABToDo-back-end-** (0★) → llm=**uncategorized** (c=0.55) — Minimal Django ToDo backend; AsyncAPI role unclear
  `Python version: 3.12.5 To run 1. Install dependencies: pip install r requirements.txt 2. Configure and test connection to PostgresSQL databa`
- **edulucca/gateway-stripe-adapter** (0★) → llm=**uncategorized** (c=0.3) — Minimal readme; insufficient info beyond Backstage tag
  `gateway-stripe-adapter [backstage]`

### rule = spec/docs (27)

- **albertnadal/asyncapi-schema-pydantic** (14★) → llm=**tooling/library** (c=0.97) — Pydantic library for parsing AsyncAPI spec schemas
  `Pydantic model for the AsyncAPI (v2) specification schema`
- **asynq-io/pydantic-asyncapi** (9★) → llm=**tooling/library** (c=0.97) — Python library providing Pydantic models for AsyncAPI documents
  `Pydantic models for AsyncAPI schema`
- **daveshanley/asyncapi-tutorials** (7★) → llm=**demo/fixture** (c=0.97) — Tutorials with code and specs, accompanies blog articles
  `Looking to get started with AsyncAPI, React, WebSockets and Go? This set of code, specs and guides should get you started`
- **paulCormierProgressive/EventDrivenServices** (0★) → llm=**demo/fixture** (c=0.97) — Explicitly a Hypertheory course repository
  `Event Driven Services This repo is for the Hypertheory course Event Driven Services . Repositories Docs This is an ASP.NET MVC Application t`
- **dedoussis/asynction** (51★) → llm=**tooling/library** (c=0.96) — SocketIO Python framework driven by AsyncAPI spec
  `SocketIO python framework driven by the AsyncAPI specification. Built on top of Flask-SocketIO. Inspired by Connexion.`
- **Kong/spec-renderer** (33★) → llm=**tooling/library** (c=0.95) — Pluggable API spec renderer tool for documentation experiences
  `A lightweight, pluggable spec renderer built by Kong. Designed to power fast, customizable API documentation experiences.`
- **Pakisan/IDEA-331646** (0★) → llm=**demo/fixture** (c=0.95) — AsyncAPI spec fixture reproducing a JetBrains IDE bug
  `Reproduces IDEA-331646 - https://youtrack.jetbrains.com/issue/IDEA-331646/AsyncAPI-Preview-panel-cant-render-references-outside-given-specif`
- **PcComponentes/open-api-messaging-context** (10★) → llm=**tooling/library** (c=0.95) — Behat library validating messages against AsyncAPI specs
  `Little context in behat for validate published messages according to an OpenApi and AsyncApi specification.`
- **kurtrisley/DemoEventDrivenService** (0★) → llm=**demo/fixture** (c=0.95) — Hypertheory course demo event-driven services
  `Event Driven Services This repo is for the Hypertheory course Event Driven Services . Repositories Docs This is an ASP.NET MVC Application t`
- **kurtrisley/EventDrivenServices** (0★) → llm=**demo/fixture** (c=0.95) — Hypertheory course event-driven services repo
  `Event Driven Services This repo is for the Hypertheory course Event Driven Services . Repositories Docs This is an ASP.NET MVC Application t`
- **nicolasard/async-api-stuff** (0★) → llm=**demo/fixture** (c=0.95) — Explicitly personal notes and examples about AsyncAPI
  `Personal notes about AsyncApi project ( https://www.asyncapi.com/ )`
- **wbelguidoum/docapi** (1★) → llm=**tooling/library** (c=0.95) — Tool that discovers and renders OpenAPI/AsyncAPI specs
  `API Documentation Hub`
- **alexandramartinez/asyncapis-accounts-email** (1★) → llm=**demo/fixture** (c=0.92) — Tutorial resources based on AsyncAPI example article
  `All the resources you need to implement a functional simple architecture with an Accounts and an Email services using AsyncAPI, Anypoint Cod`
- **xtm-group/XTRFCloudInternalEventBus** (0★) → llm=**product** (c=0.92) — Internal event bus using AsyncAPI to describe its API
  `XTRF Cloud Internal Event Bus`
- **noodlensk/task-tracker** (1★) → llm=**demo/fixture** (c=0.9) — Course homework repo with AsyncAPI spec added as exercise
  `task tracker A repo for home task for the course https://education.borshev.com/architecture. Changelog Week 0 DRAFT Added C4 model diagram d`
- **golemfactory/ya-client** (8★) → llm=**tooling/library** (c=0.88) — REST API client binding and spec for Yagna/Golem
  `Specification for REST API in yagna`
- **lauksas/sync-beat** (0★) → llm=**demo/fixture** (c=0.88) — Multi-stack learning implementations of one specification
  `📺 SyncBeat: The Ultimate YouTube Watch Party SyncBeat is a "TV first" collaborative music video player. Open it on a big screen, scan the QR`
- **thake/backstage-specs-test** (0★) → llm=**demo/fixture** (c=0.88) — Specs and catalogs to test out Backstage, not production
  `This repo contains some specs and catalogs to test out backstage.io`
- **asyncapi/tck** (12★) → llm=**tooling/library** (c=0.87) — Test compatibility kit for AsyncAPI processor compliance testing
  `(WIP) Test Compatibility Suite for AsyncAPI`
- **kayalshan/Enterprise-API-Integration-Platform** (0★) → llm=**product** (c=0.85) — Deployable enterprise integration backbone with Kafka and AWS
  `A high-performance, resilient integration backbone featuring API-first governance, event-driven orchestration (Kafka/SQS), and automated par`
- **apideck-io/api-registry** (11★) → llm=**tangential** (c=0.83) — API specifications directory/catalog indexing many formats
  `The API registry is an API specifications registry that indexes specs like OpenAPI, Swagger, API Blueprint, Apache Avro, Protocol buffers, J`
- **Leandroyyy/async-api-translator** (0★) → llm=**tooling/library** (c=0.82) — Tool that translates/processes AsyncAPI specifications
  `Translator for async api specification`
- **Phoenix-Assassins/ac4-docs** (0★) → llm=**tangential** (c=0.8) — Reverse-engineering game protocol docs; no AsyncAPI use
  `Online service docs for Assassin's Creed IV Black Flag`
- **Ferror/asyncapi-event-catalog** (1★) → llm=**demo/fixture** (c=0.78) — POC showing catalog generation from AsyncAPI specs
  `Event Catalog generated from Async API`
- **dili91/events-based-api-specs** (0★) → llm=**demo/fixture** (c=0.75) — Self-described playground for event-based API specs
  `A playground to try out standard specs for Events based API`
- **trakx/canton-api-client** (0★) → llm=**product** (c=0.62) — Generated .Net API client SDK for Canton blockchain services
  `.Net Api Clients for Canton services`
- **jgazeau/shadocs** (59★) → llm=**tooling/library** (c=0.55) — Hugo documentation theme; likely renders or demos AsyncAPI docs
  `Shadocs Theme for Hugo`

### rule = tooling/library (100)

- **Mrc0113/asyncapi-codegen-scst** (3★) → llm=**demo/fixture** (c=0.97) — Code artifacts for an AsyncAPI code generation blog/video
  `Code Artifacts used for AsyncAPI Code Generation Blog + Video`
- **Pakisan/jasyncapi-idea-plugin-demo** (0★) → llm=**demo/fixture** (c=0.97) — Demo specs showcasing AsyncAPI JetBrains plugin
  `Repository to show how AsyncAPI specification works in JetBrains IDE`
- **coiouhkc/asyncapi-generator-examples** (0★) → llm=**demo/fixture** (c=0.97) — Examples and configurations for asyncapi-generator tool
  `AsyncAPI Generator Examples Examples and different configurations utilizing https://github.com/coiouhkc/asyncapi generator to generate the c`
- **jonaslagoni/asyncapi-miniseries** (2★) → llm=**demo/fixture** (c=0.97) — Explicitly a mini series with blog posts teaching AsyncAPI codegen
  `This repository contains all resources related to the mini series about utilizing AsyncAPI code generation to your advantage`
- **meteatamel/asyncapi-basics** (3★) → llm=**demo/fixture** (c=0.97) — Explicitly a samples and reference repo about AsyncAPI
  `This repository contains information, references, and samples about AsyncAPI`
- **ripple/rippled-api-spec** (2★) → llm=**spec/docs** (c=0.97) — Repository of OpenAPI/AsyncAPI specs for XRP Ledger
  `A repository for OpenAPI / AsyncAPI specifications. This ideally eventually can be used to automatically generate code and docs to simplify `
- **DEFRA/ffc-pay-request-editor** (0★) → llm=**product** (c=0.95) — Production web microservice for debt enrichment overrides
  `Edit payment requests`
- **Sofie-Automation/sofie-core** (341★) → llm=**product** (c=0.95) — Real deployed TV broadcast studio automation system by NRK
  `Sofie Core: A Part of the Sofie TV Studio Automation System`
- **arih1299/solacedemo-kafkasummitapac2021** (3★) → llm=**demo/fixture** (c=0.95) — Conference demo for Kafka Summit APAC 2021
  `solacedemo kafkasummitapac2021 Setting Up on Local Environment 1. Register with Solace Cloud at https://console.solace.cloud/ 2. Run a local`
- **asyncapi-actions-testing/website** (0★) → llm=**demo/fixture** (c=0.95) — Explicit test clone of AsyncAPI website, not production
  `clone of website for testing`
- **canton-network/cf-docs** (2★) → llm=**spec/docs** (c=0.95) — Documentation website repo for Canton Foundation
  `home for the new unified Canton Foundation docs`
- **edwmurph/api-docs** (0★) → llm=**demo/fixture** (c=0.95) — Demo React app showcasing Swagger and AsyncAPI integrations
  `api docs client side rendered react app demoing standalone swagger and asyncapi integrations with hosted api definitions TODO custom rendere`
- **hasathcharu/ballerina-websockets-test** (0★) → llm=**demo/fixture** (c=0.95) — Explicit test examples demonstrating AsyncAPI tooling usage
  `Ballerina WebSockets Test Examples Overview This is a set of Ballerina WebSocket test examples. The examples demonstrates how to use the Asy`
- **sroigmas/asyncapi** (0★) → llm=**demo/fixture** (c=0.95) — Explicitly a small practice of AsyncAPI definition and code gen
  `Small practice of AsyncAPI definition and Spring code generation`
- **viruskizz/42bangkok_ft-transcendence** (0★) → llm=**demo/fixture** (c=0.95) — Final project for 42 school, not production software
  `ft trancendence The final project in 42 common core. Docker To run to project on local environment sh make to run only Frontend NextJS sh ma`
- **David-DAM/kafka-cero-a-experto** (3★) → llm=**demo/fixture** (c=0.93) — Explicitly a course final project for learning Kafka
  `Proyecto final del curso Spring Boot Async de cero a Experto`
- **deltaeight/ma2-websocket-api** (4★) → llm=**spec/docs** (c=0.93) — AsyncAPI documentation of GrandMA2 WebSocket API only
  `A documentation of the GrandMA 2 websocket API`
- **Jacksonspencerd/tcss559-project** (1★) → llm=**demo/fixture** (c=0.92) — Course project (TCSS 559) full-stack observability platform
  `☁️ TCSS 559 Project: Eye in the Sky A full stack observability platform featuring a React frontend, Node.js/Go backend services, Cloud Funct`
- **durable-workflow/durable-workflow.github.io** (2★) → llm=**spec/docs** (c=0.92) — Docusaurus documentation website for Durable Workflow product
  `Documentation website for Durable Workflow, built with Docusaurus and published at durable-workflow.com. Hosts versioned product docs, guide`
- **hazamashoken/ft_trancendence** (3★) → llm=**demo/fixture** (c=0.92) — 42 school final project, not production software
  `ft trancendence The final project in 42 common core. Docker To run to project on local environment sh make to run only Frontend NextJS sh ma`
- **iqb-specifications/response** (0★) → llm=**spec/docs** (c=0.92) — Data specification repo with JSON Schema and AsyncAPI-generated types
  `Data output of assessments`
- **jpxcz/websocket_template_nodejs** (0★) → llm=**demo/fixture** (c=0.92) — Explicitly a template/boilerplate for WebSocket with AsyncAPI docs
  `NodeJs + Fastify + AsyncApi for documentation generator`
- **qmg-vgalcenco/asyncapi-validator** (0★) → llm=**demo/fixture** (c=0.92) — Created to test and experiment with asyncapi-validator library
  `async validator This repo was created to test / experiment a bit with the https://www.npmjs.com/package/asyncapi validator library. Specific`
- **rakeshmani35/springboot-openAPI** (0★) → llm=**tangential** (c=0.92) — OpenAPI-focused Spring Boot demo, not AsyncAPI
  `Spring Boot3 openAPI In API first design, create API first and than generate the generate the stub code by using openAPI generator. Useful l`
- **verona-interfaces/editor** (0★) → llm=**spec/docs** (c=0.92) — Specification for async host-editor iframe communication
  `Interface for task/unit authoring applications`
- **hschaffner/AsyncAPI_Test** (0★) → llm=**demo/fixture** (c=0.91) — Explicit test of AsyncAPI Solace code generation
  `Test to use AsyncAPI and Solace code generator to create Spring Cloud Streams application`
- **ChunPingWang/saga-axon** (0★) → llm=**demo/fixture** (c=0.9) — Explicitly demonstrates Axon Saga pattern, not production use
  `Saga 訂單交易系統 基於 Axon Framework 實作的分散式交易協調系統，採用 Saga 模式 處理跨服務的訂單、付款、庫存交易。 專案概述 本專案展示如何使用 Axon Framework 實作 Choreography based Saga 模式，協調三個微服務之`
- **SolaceLabs/solace-jenkins-plugin** (0★) → llm=**demo/fixture** (c=0.9) — Repo explicitly contains AsyncAPI sample files for testing
  `Contains AsyncAPI sample files to use for testing with AWX/Ansible Tower and Jenkins`
- **Verdenroz/finance-query** (36★) → llm=**product** (c=0.9) — Hosted open-source financial data API with real endpoints
  `Open-source API for financial data. Get quotes, historical data, technical indicators, and more.`
- **ZiyamSanthosh/AsyncApiAmf** (0★) → llm=**demo/fixture** (c=0.9) — PoC experimenting with AsyncAPI and AMF parser combination
  `A project to try the combination of AsyncAPI and AMF parser`
- **bitsy-ai/printnanny-webapp** (3★) → llm=**product** (c=0.9) — Real webapp and API for OctoPrint Print Nanny plugin
  `Print Nanny Webapp API and webapp for Octoprint Print Nanny plugin by Bitsy.ai .. image:: https://img.shields.io/badge/built%20with Cookiecu`
- **gedeondt/reatilerworkflow-charla** (0★) → llm=**demo/fixture** (c=0.9) — 'charla' = talk/presentation; retail workflow simulation demo
  `Reatiler Workflow Monorepo Monorepo orientado a la simulación de orquestaciones retail siguiendo la filosofía Spec as Source . Todo el compo`
- **imaginestudio-ai/golang-ninja** (1★) → llm=**demo/fixture** (c=0.9) — Collection of Go tutorials and hands-on learning projects
  `This repository contains a collection of tutorials and hands-on projects for learning Go (Golang).`
- **panand13/backstage** (0★) → llm=**product** (c=0.9) — Backstage open-source developer portal platform
  `Backstage During the month of July the majority of the maintainers will be on summer vacation 🏖️ Development will continue as usual, but exp`
- **rahulmehta25/Smart-Legal-Contracts** (0★) → llm=**tangential** (c=0.9) — Legal contract AI tool, no AsyncAPI mention
  `Smart Legal Contracts Upload a contract. Get a classified risk breakdown. Ask GPT 4 to rewrite the hostile clauses without losing legal inte`
- **servaasvdc/whatstack** (2★) → llm=**tangential** (c=0.9) — Tech stack detector; AsyncAPI just one detectable technology
  `whatstack detects the tech stack of a project. Built for humans and clankers.`
- **solace-cto-labs/solace-amplify-discovery-agent** (1★) → llm=**product** (c=0.9) — Deployable agent syncing Solace AsyncAPIs with Axway Amplify platform
  `Solace-Amplify-Discovery-Agent for synchronizing Solace AsyncAPIs with Axway Amplify Platform`
- **specmesh/getting-started-apachekafka** (1★) → llm=**demo/fixture** (c=0.9) — Getting-started tutorial and HelloWorld guide for SpecMesh
  `Getting started: SpecMesh with Apache Kafka Without security or ACLs Introduction This guide provides the simplest way to understand how to `
- **MEF-GIT/MEF-LSO-Legato-SDK** (3★) → llm=**spec/docs** (c=0.88) — Telecom standards API spec bundle, not runnable software
  `The SDK includes APIs for Service Catalog, Service Order, Service Inventory and Service Notification functions of the Service Orchestration `
- **derberg/shrekapp-asyncapi-designed** (4★) → llm=**demo/fixture** (c=0.88) — Fun chatbot demo designed to explore AsyncAPI and WebSocket
  `This repository stores a WebSocket project designed with AsyncAPI. It exposes an interface to talk to a chatbot trained on Wit.ai`
- **openxapi/openxapi** (9★) → llm=**spec/docs** (c=0.88) — Repository is standardized OpenAPI/AsyncAPI specs for exchanges
  `OpenAPI and AsyncAPI specifications for cryptocurrency exchanges and DeFi protocols`
- **MEF-GIT/MEF-LSO-Allegro-SDK** (1★) → llm=**spec/docs** (c=0.87) — Telecom standards body API specification bundle
  `This repository contains the MEF LSO Allegro SDK.`
- **MEF-GIT/MEF-LSO-Interlude-SDK** (0★) → llm=**spec/docs** (c=0.87) — Telecom standards body API specification bundle
  `Mplify LSO Interlude SDK Kylie Release Download Link Download the entire repository by clicking here Introduction All references to 'MEF For`
- **CardanoSolutions/ogmios** (327★) → llm=**product** (c=0.85) — Production WebSocket/JSON-RPC bridge service for Cardano node
  `❇️ A WebSocket JSON/RPC bridge for Cardano`
- **Chief-Strategist-J/llm-observability-platform** (3★) → llm=**product** (c=0.85) — Deployable LLM observability platform with real instrumentation
  `High-performance LLM observability and evaluation platform with automated instrumentation, stateful chat orchestration, semantic vector memo`
- **Leonardo-Santos-oficial/jose-diego** (0★) → llm=**tangential** (c=0.85) — Crash game demo; AsyncAPI not mentioned or relevant
  `Aviator – Crash Game Demo Sistema completo de crash game no estilo Aviator, com autenticação Supabase, realtime via Node service e frontend `
- **TemplateMechanics/tilt** (2★) → llm=**demo/fixture** (c=0.85) — Example Kubernetes environment demonstrating deployment patterns
  `Tilt File Examples`
- **christian-photo/ninaAPI** (46★) → llm=**product** (c=0.85) — Real deployed plugin providing WebSocket/REST API for astronomy software
  `A webapi (and websocket) to control N.I.N.A.`
- **prichelle/prichelle.github.io** (0★) → llm=**tangential** (c=0.85) — Jekyll personal blog theme, no substantive AsyncAPI usage
  `Minimal Mistakes Jekyll theme Minimal Mistakes is a flexible two column Jekyll theme, perfect for building personal sites, blogs, and portfo`
- **DEFRA/ahwr-message-generator-backend** (0★) → llm=**product** (c=0.82) — Real backend service on Core delivery platform
  `Git repository for service ahwr-message-generator-backend`
- **GeniaV/stellar-burgers-backend** (0★) → llm=**demo/fixture** (c=0.82) — Self-described pet project, frontend built for education
  `:dog: :hamburger: Backend for Stellar Burgers Project (pet project)`
- **deathbycaptcha/deathbycaptcha-agent-api-metadata** (0★) → llm=**spec/docs** (c=0.82) — API spec/metadata for AI agents, not runnable software
  `Deathbycaptcha main http and sockets api IA agent metadata`
- **fulmenhq/goneat** (0★) → llm=**tangential** (c=0.82) — Polyglot code-quality CLI; no AsyncAPI focus
  `All about smoothly delivering neat code at scale`
- **gregoriocarranza/APPS-II-Core-Backend** (0★) → llm=**demo/fixture** (c=0.82) — 'APPS-II' course starter backend generated from CLI
  `Sundays Framework Project This directory contains the starter backend generated by the CLI. Quick start 1. Install dependencies: bash npm in`
- **holstein13/mcp-config-manager** (28★) → llm=**tangential** (c=0.82) — MCP config tool for AI systems; AsyncAPI only incidental
  `Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sy`
- **mulesoft/api-console** (907★) → llm=**tangential** (c=0.82) — RAML/OAS console tool; no AsyncAPI involvement
  `An interactive REST console based on RAML/OAS files`
- **n1md7/IoT-Device-Manager** (1★) → llm=**product** (c=0.82) — Deployable IoT device manager with Arduino/ESP32 clients
  `IoT device manager with microcontroller clients such as Arduino(uno/mega), ESP32 and ESP8622`
- **8cH9azbsFifZ/hangboard** (12★) → llm=**product** (c=0.8) — Deployable IoT hangboard training device service
  `A universal force and velocity sensing hangboard mount with exercise timers for all hangboards.`
- **Lap-Platform/LAP** (339★) → llm=**tangential** (c=0.8) — AI-agent API catalog/directory; AsyncAPI is one of many incidental formats
  `Your agents are guessing at APIs. Give them the actual Agent-Native spec. 1500+ API's Ready To-Use skills,  Compile any API spec into a lean`
- **SolaceLabs/solace-ansible-plugin** (0★) → llm=**demo/fixture** (c=0.8) — Sample AsyncAPI files bundled with CICD demo/test playbooks
  `Test Ansible Playbooks using Solace Ansible Galaxy`
- **SolaceLabs/solace-tryme-cli-mcp-server** (0★) → llm=**demo/fixture** (c=0.8) — Explicitly a proof-of-concept MCP server wrapping CLI
  `MCP server for solace-tryme-cli`
- **ThomasWimprine/LangChangeWorkflows** (1★) → llm=**tangential** (c=0.8) — LangGraph/LLM workflow tool, AsyncAPI mentioned incidentally
  `LangGraph-based PRP workflow orchestration with multi-agent coordination, cost optimization, and quality gates`
- **Zenika/kafka-schema-registry-publish** (0★) → llm=**demo/fixture** (c=0.8) — Explicitly shows best practices via demo docker-compose setup
  `Publish schemas to your schemas registry using CI-CD`
- **advanced-rest-client/api-headers-document** (0★) → llm=**tangential** (c=0.8) — AMF-based REST API docs component, not AsyncAPI-specific
  `⛔️ DEPRECATED This component is being deprecated. Use `api-documentation` instead.`
- **advanced-rest-client/api-method-documentation** (0★) → llm=**tangential** (c=0.8) — HTTP method documentation renderer, AMF/REST focus
  `⛔️ DEPRECATED This component is being deprecated. Use `api-documentation` instead.`
- **advanced-rest-client/api-request** (1★) → llm=**tangential** (c=0.8) — HTTP request editor component, not AsyncAPI tooling
  `⛔️ DEPRECATED This component is being deprecated. Use `@api-components/amf-components` instead.`
- **funny-bunny-corp/ledger** (0★) → llm=**demo/fixture** (c=0.8) — Demo org name; Quarkus ledger sample service
  `ledger This project uses Quarkus, the Supersonic Subatomic Java Framework. If you want to learn more about Quarkus, please visit its website`
- **kdcube/kdcube-ai-app** (10★) → llm=**product** (c=0.8) — Self-hosted AI control plane with tenancy and RBAC
  `Ship customer-facing AI with isolation, spend controls, and provenance.`
- **nikolay-e/diffctx** (1★) → llm=**tangential** (c=0.8) — LLM diff context tool; AsyncAPI only one of many formats
  `Smart git diff context for LLMs - selects the minimal code fragments needed to understand a change. Also exports full codebase in YAML/JSON/`
- **obedito-lab/document-services-s** (0★) → llm=**product** (c=0.8) — Production document-signing System API service
  `Document Services S (System Layer) Servicio System API para la gestion de firmas de documentos. Implementa el sistema en el nivel System Lay`
- **pproenca/agent-tui** (95★) → llm=**tangential** (c=0.8) — AI agent TUI automation tool; AsyncAPI not mentioned
  `TUI automation for AI agents. Control any terminal app from code.`
- **ArshdevSinghji/iffy-backend** (0★) → llm=**product** (c=0.78) — Location-based dating app modular monolith backend
  `Iffy is a location-based dating app built with a modular monolith backend and a Next.js frontend.`
- **BidnessForB/postman-sdk** (0★) → llm=**tangential** (c=0.78) — Postman API SDK built as a Cursor learning exercise
  `SDK for Postman API in NodeJS`
- **canton-network/wallet** (39★) → llm=**product** (c=0.78) — Deployable Wallet Gateway server plus dApp/Wallet SDKs
  `Wallet Gateway`
- **climateandtech/report-analyst** (35★) → llm=**product** (c=0.78) — Real versioned open-core framework for sustainability report analysis
  `OpenSustainabilityAnalyst ReportAnalyst is an open-source / open-core framework for customizable research-driven end-to-end sustainability r`
- **omiga-group/omiga** (0★) → llm=**product** (c=0.78) — Multi-domain platform with codegen, DB migrations, multiple services
  `Omiga`
- **pascal-audio/px-api** (0★) → llm=**spec/docs** (c=0.78) — Official API spec and docs for hardware audio amplifiers
  `Public JSON-RPC based API for PX-Series`
- **Flissel/Coding_engine** (0★) → llm=**tangential** (c=0.75) — AI code-generation agent; AsyncAPI incidental if present
  `Society of Mind autonomous code generation platform — 37+ AI agents generating production-ready projects from JSON requirements`
- **Flissel/DaveFelix-Coding-Engine** (0★) → llm=**tangential** (c=0.75) — AI code-generation engine; AsyncAPI incidental if present
  `Engine for generating code snippets and templates.`
- **arielril/hexagonal-architecture** (11★) → llm=**demo/fixture** (c=0.75) — Architectural demo project illustrating hexagonal design patterns
  `Repository that contains some project that have been designed following the hexagonal architecture`
- **kweaver-ai/kweaver-core** (817★) → llm=**tangential** (c=0.75) — AI decision-agent harness platform, AsyncAPI incidental
  `KWeaver Core is a harness-first foundation for enterprise decision agents. It turns fragmented data, knowledge, tools, and policies into gov`
- **CoolSpy3/CSPackets** (0★) → llm=**product** (c=0.72) — Real Minecraft packet library generated via AsyncAPI Generator
  `An implementation of most 1.8.9 Minecraft packets for use with CSModLoader.`
- **encypher-studio/newsware-docs** (0★) → llm=**spec/docs** (c=0.72) — Documentation site frontend for Newsware API clients
  `Frontend for user documentation of the Newsware clients to interact with the API`
- **openagents-org/openagents** (3784★) → llm=**product** (c=0.72) — Deployable AI agent collaboration workspace with CLI
  `OpenAgents - AI Agent Networks for Open Collaboration`
- **DevOpsMadDog/aldeci_core** (0★) → llm=**tangential** (c=0.7) — Cleaned mirror of ALDECI; no AsyncAPI usage described
  `ALDECI core — cleaned source snapshot (no legacy docs/contexts). AI-native security decision intelligence platform. ASPM + CTEM + CSPM, mult`
- **conversales/convai-widget-embed** (0★) → llm=**tangential** (c=0.65) — Voice/text SDK; AsyncAPI mention appears incidental
  `Conversales SDK Build multimodal voice and text experiences with Conversales. This workspace contains client libraries, widgets, shared type`
- **yankeeinlondon/rusty-biscuit** (3★) → llm=**tangential** (c=0.65) — AI research automation tools, AsyncAPI role unclear
  `A monorepo for AI-powered research and automation tools`
- **claudioed/equipment-metadata** (0★) → llm=**product** (c=0.63) — Quarkus microservice for equipment metadata management
  `equipment metadata This project uses Quarkus, the Supersonic Subatomic Java Framework. If you want to learn more about Quarkus, please visit`
- **ArabotHXL/BTC_project** (1★) → llm=**product** (c=0.62) — Bitcoin mining SaaS with microservice APIs
  `BTC Project Repository for https://replit.com/@hxl1992hao/BitcoinMiningCalculator. What This Contains Flask/SQLAlchemy HashInsight mining ca`
- **Arkhe-Network/Arkhe-OS** (1★) → llm=**tangential** (c=0.62) — Quantum genomics research project, AsyncAPI tangential
  `ASI`
- **arc-framework/arc-platform** (0★) → llm=**tangential** (c=0.62) — AI agent orchestration platform; AsyncAPI likely incidental
  `The official production monorepo for A.R.C. Houses the "Brain" (Python/LangGraph), Voice services, and OCI-compliant Docker infrastructure. `
- **junjiepro/mango** (0★) → llm=**product** (c=0.62) — AI agent dialogue platform; AsyncAPI likely incidental
  `Mango 智能Agent对话平台 一个支持多模态对话、后台任务执行、小应用生态和持续学习的智能Agent平台。 技术栈 前端框架 : Next.js 14+ (App Router), React 18+ 样式 : TailwindCSS 3.4, shadcn/ui, Rad`
- **ashtanko/log4fit-api** (0★) → llm=**product** (c=0.6) — Real exercise-tracking backend with JWT auth and workout features
  `Log4Fit is a backend application for an exercise tracking platform, built with Kotlin and Ktor. It provides a simple and robust foundation f`
- **nanoyan/metadata-store** (0★) → llm=**spec/docs** (c=0.6) — Schema/metadata definitions using AsyncAPI type definitions for TypeScript
  `Data interface for defining metadata for objects based on vocabularies of IQB. JSON Schema (see metadata store.schema.json ) Schema document`
- **yuvraj-chouhan-dev/ready-now-server** (0★) → llm=**product** (c=0.6) — SDK backend server, real deployable service
  `ready now SDK Backend server`
- **H1lp0p/fins-web** (0★) → llm=**product** (c=0.55) — Monorepo with BFF, multiple packages, real structure
  `Fins Monorepo: React (Vite), пакеты @fins/ui kit , @fins/api , @fins/entities , BFF (FastAPI), OpenAPI контракты. Требования Node LTS, pnpm `
- **chvanam/fdp-rust-manifest** (0★) → llm=**demo/fixture** (c=0.55) — Benchmarking project using AsyncAPI CLI as tooling dependency
  `Benchmarking bash Install asyncapi cli npm install g @asyncapi/cli Install hyperfine apt install hyperfine brew install hyperfine Install da`
- **kaje94/choreo-connect-test** (0★) → llm=**product** (c=0.55) — Deployable bridge service connecting local dev to Choreo environment
  `Choreo Local Bridge Service This service bridges your local development environment with your deployed Choreo project. This bridge enables y`
- **Matusko/flea** (0★) → llm=**uncategorized** (c=0.5) — Nx workspace with no AsyncAPI context visible
  `Flea ✨ This workspace has been generated by Nx, a Smart, fast and extensible build system. ✨ Generate code If you happen to use Nx plugins, `
- **joefrancisGA/ArchLucid** (0★) → llm=**uncategorized** (c=0.45) — Readme unclear; purpose and AsyncAPI role indeterminate
  `ArchLucid Full repository overview (documentation spine, local install path, APIs, CLI, tests): docs/REPOSITORY README.md . Buyers / evaluat`