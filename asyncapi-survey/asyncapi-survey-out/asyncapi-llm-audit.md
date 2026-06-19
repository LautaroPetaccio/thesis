# LLM audit of the rule-based classifier

Full LLM re-pass (`claude --model sonnet`) over every repo with readable text, compared to the rule-based bucket. **No buckets were changed** — disagreements are listed for review.


Agreement on rule-assigned SUT buckets (product/tooling/demo/spec): **404/677 = 60%**


## Confusion matrix (rows = rule bucket, cols = LLM verdict)

| rule \\ llm | product | tooling/library | demo/fixture | spec/docs | tangential | uncategorized | total |
|---|---|---|---|---|---|---|---|
| product | 151 | 11 | 58 | 13 | 21 | 3 | 257 |
| tooling/library | 37 | 113 | 27 | 19 | 16 | 2 | 214 |
| demo/fixture | 18 | 7 | 102 | 9 | 12 | 0 | 148 |
| spec/docs | 2 | 8 | 8 | 38 | 2 | 0 | 58 |
| catalog | 0 | 0 | 0 | 0 | 48 | 0 | 48 |
| tangential | 1 | 0 | 0 | 2 | 10 | 0 | 13 |
| uncategorized | 57 | 14 | 50 | 18 | 18 | 5 | 162 |

## Disagreements for review (273)

Sorted by rule bucket, then LLM confidence. High-confidence rows are the likeliest rule errors.


### rule = demo/fixture (46)

- **kanekoshoyu/asyncapi-rust-ws-template** (2★) → llm=**tooling/library** (c=0.99) — AsyncAPI template/generator for Rust WebSocket clients
  `AsyncAPI Template for Generating Rust WebSocket Client`
- **ONSdigital/dp-search-data-importer** (0★) → llm=**product** (c=0.95) — Real microservice consuming Kafka messages to populate Elasticsearch
  `Service to store searchable content into elasticsearch`
- **tewhatuora/api-standards** (13★) → llm=**spec/docs** (c=0.94) — Official API development and security standards documentation site
  `Health New Zealand | Te Whatu Ora API Development and Security Standards`
- **ArieGoldkin/ai-agent-hub** (10★) → llm=**tangential** (c=0.93) — AI agent skills repo for Claude; not an AsyncAPI user
  `🚀 AI Agent Hub ✨ Transform Claude into 10 Context Aware AI Agents Working in Parallel ✨ 🧠 Intelligent Orchestration + 79% Faster with Squad `
- **Ravip2006/Demo** (0★) → llm=**spec/docs** (c=0.93) — Central contract repository housing multiple API specs
  `Central Contract Repository for the Order API What is Central Contract Repository? Please see Documentation This repository serves as the Ce`
- **specmatic/labs-contracts** (0★) → llm=**spec/docs** (c=0.93) — Central repository of canonical OpenAPI/AsyncAPI contract specs
  `Central Contracts Repo for projects inside Labs`
- **specmatic/specmatic-order-contracts** (6★) → llm=**spec/docs** (c=0.93) — Central contract repository holding API specs for sample projects
  `Contracts for sample projects that use Specmatic to do contract driven development`
- **ScrKiddie/AtoiTalkAPI** (0★) → llm=**product** (c=0.92) — Deployable real-time chat backend with WebSocket events
  `RESTful API for real-time chat applications with WebSocket events, media uploads, and automated cleanup.`
- **Vellum-IO/keeper-api-contracts** (0★) → llm=**spec/docs** (c=0.92) — OpenAPI spec files for internal DBaaS service, no runnable code
  `The openAPI contracts for back and frontends.`
- **call-sofia/callsofia-webhooks-docs** (0★) → llm=**spec/docs** (c=0.9) — Webhook event catalog and documentation, not runnable software
  `CallSofia Webhooks v2 Real time event notifications for your CallSofia voice AI intake pipeline. Subscribe to call lifecycle events, lead qu`
- **microcks/microcks.io** (24★) → llm=**spec/docs** (c=0.9) — Public website resources and templates for Microcks
  `Public website resources and templates`
- **qoretechnologies/qore** (63★) → llm=**tangential** (c=0.9) — General-purpose programming language; AsyncAPI incidental
  `Qore Programming Language`
- **openshift-hyperfleet/architecture** (2★) → llm=**spec/docs** (c=0.88) — Architecture documents and engineering standards repository
  `Status: Active Owner: Architecture Team Last Updated: 2025 11 07 HyperFleet Architecture Repository Table of Contents Overview Repository Ac`
- **Emiltzav/asyncapi-iot-examples** (0★) → llm=**spec/docs** (c=0.87) — Catalog of AsyncAPI 3.0 descriptions for IoT devices, thesis artifact
  `A catalog of AsyncAPI 3.0 descriptions for asynchronous APIs of IoT devices.`
- **icanbwell/fhir-server** (47★) → llm=**product** (c=0.87) — Production-grade open-source FHIR server with streaming
  `Open Source FHIR Server backed by MongoDB`
- **ministryofjustice/hmpps-locations-inside-prison-api** (2★) → llm=**product** (c=0.85) — Production API managing locations inside prisons
  `HMPPS Location Inside Prison Service API`
- **socrateasehq/autoproctor-mintlify-docs** (0★) → llm=**tangential** (c=0.85) — Mintlify docs starter kit; no AsyncAPI content visible
  `Mintlify Starter Kit Use the starter kit to get your docs deployed and ready to customize. Click the green Use this template button at the t`
- **yourbourse/trade-server-trading-view-js** (0★) → llm=**product** (c=0.85) — Production-ready trading terminal with real-time market data
  `Public Repository for Trading View integration with Trade Server`
- **DataDog/stickerlandia** (7★) → llm=**product** (c=0.78) — Real deployed community engagement platform for Datadog events
  `Stickerlandia Overview Stickerlandia lets you collect Datadog stickers by completing Datadog certifications, trading with others, and throug`
- **WebFuzzing/Dataset** (50★) → llm=**tangential** (c=0.78) — Test dataset of REST/GraphQL apps; AsyncAPI only incidental
  `Web Fuzzing Dataset (WFD): a set of web/enterprise applications for experimentation in automated system testing`
- **adimail/rocket-landing-rl** (1★) → llm=**tangential** (c=0.78) — RL simulation for rocket landing; no AsyncAPI relevance visible
  `reinforcement learning simulation to land a spacex rocket booster vertically`
- **factory-x-contributions/async-aas-helm** (2★) → llm=**tooling/library** (c=0.78) — Helm charts wiring AAS implementations to MQTT broker
  `A helm chart to spin up various AAS implementations and connect them to an MQTT broker.`
- **manosmax/Smart-Waste-Bin** (1★) → llm=**product** (c=0.78) — IoT pipeline with AsyncAPI docs for real deployment
  `Final Project for Advanced Programming Techniques`
- **nekofar/warpcast** (2★) → llm=**tooling/library** (c=0.78) — TypeScript client SDK for Warpcast APIs
  `TypeScript client for interacting with Warpcast APIs`
- **up1/workshop-js-testing-202507** (1★) → llm=**tangential** (c=0.78) — JS testing workshop; AsyncAPI only incidental
  `Full stack testing workshop with JavaScript`
- **tanishy7777/Joined_Words** (1★) → llm=**product** (c=0.76) — Real-time multiplayer game with rooms and live leaderboards
  `This repo adds multiplayer functionality to the Joined Words Game`
- **HyPolDev/Bot** (0★) → llm=**product** (c=0.75) — Automated cross-exchange prediction market arbitrage trading engine
  `Cross Exchange Prediction Market Arbitrage Engine A fully automated, market neutral trading system designed to identify and execute statisti`
- **ambihome-gmbh/asyncapi** (0★) → llm=**tooling/library** (c=0.75) — Middleware validating and routing AsyncAPI messages over MQTT
  `EXPERIMENTAL. Receive and send valid asyncapi messages over MQTT.`
- **clecioantao/platform-state-repo** (0★) → llm=**tangential** (c=0.75) — GitOps state repo; AsyncAPI not mentioned
  `platform state repo Fonte única da verdade (GitOps) para a PoC de IDP com: Backstage (local, fora do cluster) → gera conteúdo GitOps Argo CD`
- **dotnet/maui-labs** (166★) → llm=**tangential** (c=0.75) — .NET MAUI mobile tooling; AsyncAPI only incidental
  `Experimental and pre-release tools for .NET MAUI`
- **nashspence/pyspec** (0★) → llm=**tooling/library** (c=0.75) — Spec-to-artifact code generation tool, not a deployable app
  `pyspec contract pyspec contract is a Python first, spec to artifact tool for whole app product specifications. It turns a sparse human autho`
- **specmatic/specmatic-studio-playwright-ts-tests** (0★) → llm=**tangential** (c=0.75) — E2E test suite for Specmatic Studio; no direct AsyncAPI usage
  `Automated tests for Specmatic Studio`
- **zuevrs/yanote** (0★) → llm=**tooling/library** (c=0.75) — Tool recording live calls and validating API contract coverage
  `yanote Yanote показывает не абстрактное «тесты прошли», а доказуемое покрытие HTTP контракта по живым вызовам: рекордер пишет events.jsonl ,`
- **CruelAddict/ori** (1★) → llm=**tangential** (c=0.72) — TUI database explorer; no evident AsyncAPI usage
  `TUI DB Explorer`
- **inputlayer/inputlayer** (26★) → llm=**product** (c=0.72) — Deployable streaming reasoning layer for AI systems
  `Streaming reasoning layer for AI. Incremental rules engine with vector search, graph traversal, and explainable derivation traces.`
- **lufyxz7/xpogo** (0★) → llm=**product** (c=0.72) — Real AI-powered export platform backend service
  `Backend Detail : https://xpogo-backend.vercel.app`
- **taonaben/grupus-frontend** (0★) → llm=**tangential** (c=0.72) — Flutter boilerplate starter with no meaningful AsyncAPI usage
  `grupus A new Flutter project. Getting Started This project is a starting point for a Flutter application. A few resources to get you started`
- **TykTechnologies/exp** (0★) → llm=**tooling/library** (c=0.7) — Experimental dev tooling and schema generators from API vendor
  `This repository holds experimental and deprecated tooling`
- **AndreiBacs/EchipaMea** (1★) → llm=**tangential** (c=0.65) — Flutter contractor app; no AsyncAPI mention in readme
  `EchipaMea Mobile app for small contractor teams, built with Flutter. What it does Supports two roles: Foreman and Worker Foreman area includ`
- **Ihor-Mykytiuk/software-architecture** (0★) → llm=**product** (c=0.65) — Web application for finding teams and project collaborators
  `Web application for finding teams and projects Online web application that helps people find like minded collaborators for informal projects`
- **manuschillerdev/esphome-elero** (2★) → llm=**product** (c=0.65) — Real ESPHome IoT firmware component for RF blinds
  `An ESPHome component to control Devices with the bidirectional Elero protocol (Covers and Lights)`
- **nba-amtgroup/4424rr-2** (0★) → llm=**product** (c=0.65) — Real railroad maintenance application using CV and ML
  `trackbot2`
- **BenediktusG/task-manager** (0★) → llm=**product** (c=0.6) — Functional multi-tenant task manager with real-time notifications
  `Multi Tenant Task Manager with real-time notification`
- **jijingkun-commits/fastapi** (0★) → llm=**product** (c=0.6) — AI conversational assistant application with FastAPI backend
  `ai agent`
- **andreaseger/homelab-tools** (0★) → llm=**product** (c=0.58) — Real monorepo of containerized homelab infrastructure utilities
  `Homelab Tools A monorepo of containerized applications and utilities for homelab infrastructure management. Getting Started This workspace u`
- **jhekasoft/e-backend** (0★) → llm=**product** (c=0.52) — Generic personal backend service with HTTP server and DB
  `e-backend is a backend for all the projects`

### rule = product (106)

- **microcks/microcks** (1956★) → llm=**tooling/library** (c=0.99) — API mocking and testing platform consuming AsyncAPI specs
  `The open source, cloud native tool for API Mocking and Testing. Microcks is a Cloud Native Computing Foundation incubating project 🚀`
- **EcoHub-AG/Api-Specs** (0★) → llm=**spec/docs** (c=0.97) — Repository purpose is storing API specifications only
  `Specifications for all our APIs`
- **Souvikns/greet-bot** (0★) → llm=**demo/fixture** (c=0.97) — Simple WebSocket example app using Glee framework
  `A simple websocket API example using glee.`
- **VisioLab/cash-register-api** (1★) → llm=**spec/docs** (c=0.97) — AsyncAPI spec describing WebSocket API, no runnable software
  `Specification of VisioLab's cash register API`
- **bpbpublications/Spring-Boot-3-API-Mastery** (12★) → llm=**demo/fixture** (c=0.97) — Book companion repository by BPB Publications
  `Spring Boot 3 API Mastery, by BPB Publications`
- **event-catalog/generators** (14★) → llm=**tooling/library** (c=0.97) — AsyncAPI and OpenAPI generator plugins for EventCatalog
  `Plugin integrations for EventCatalog`
- **fraunhoferfokus/dredger-todos** (0★) → llm=**demo/fixture** (c=0.97) — Demo and test fixture for the dredger generator
  `dredger todos async dredger todos dient zum Demonstrieren und Testen von dredger . dredger generiert aus OpenAPI und AsyncAPI Spezifikatione`
- **omnai-project/OmnAIScope_DataServer_API_Doc** (0★) → llm=**spec/docs** (c=0.97) — Repo explicitly documents WebSocket API with AsyncAPI spec
  `Async API description for the OmnAIView Backend`
- **specmatic/specmatic** (381★) → llm=**tooling/library** (c=0.97) — Contract testing and service virtualization tool for AsyncAPI/OpenAPI
  `Eliminate API integration headaches with Specmatic's no-code AI-powered API development suite. Teams ship APIs 10x faster by transforming sp`
- **specmatic/studio-demo** (2★) → llm=**demo/fixture** (c=0.97) — Explicitly a demo project for Specmatic Studio features
  `Demo project showcasing how to use Specmatic Studio for API contract testing, mocking, resiliency, and more, with hands-on video guidance.`
- **takeruun/ws-ts-gen** (0★) → llm=**tooling/library** (c=0.97) — CLI code generator from AsyncAPI 3.0 schemas to TypeScript
  `ws ts gen AsyncAPIスキーマ（YAML/JSON）からTypeScriptコードを自動生成するCLIツールです。 特徴 WebSocketサーバー・クライアント両対応 : サーバー側とクライアント側のコードを生成 型安全なメッセージハンドリング : TypeScr`
- **aml-org/als** (32★) → llm=**tooling/library** (c=0.96) — Language server providing IDE support for AsyncAPI and RAML
  `Language Server implementation for AML and AML-defined metadata`
- **ngscheurich/elixirconf-eu-2024** (0★) → llm=**demo/fixture** (c=0.96) — Conference talk companion source code, not production
  `🗺️ “Let’s Go on an Adventure” (ElixirConf EU 2024)`
- **specmatic/specmatic-arazzo-openapi-asyncapi-sample** (0★) → llm=**demo/fixture** (c=0.96) — Sample project demonstrating API workflow testing with Arazzo
  `From REST to Events: API Workflow Testing and Mocking with a Single Arazzo Spec`
- **CALLlA-74/bauman-poker** (0★) → llm=**demo/fixture** (c=0.95) — University coursework: online poker protocol prototype
  `Курсовая работа по протоколам вычислительных сетей В ходе выполнения данной работы были разработаны протокол онлайн игры "ПОКЕР" и программн`
- **Kuestenlogik/Bowire** (4★) → llm=**tooling/library** (c=0.95) — Multi-protocol API workbench supporting AsyncAPI among many protocols
  `Multi-protocol API workbench for .NET — discover, invoke, record, mock, replay across gRPC, REST, GraphQL, MQTT, SignalR, WebSocket, SSE, MC`
- **LouisSappey/tp-nest-web-socket** (0★) → llm=**demo/fixture** (c=0.95) — 'TP' is French for school practical assignment
  `TP Nest Chat WebSocket Backend NestJS pour un chat temps reel avec authentification JWT, chat general, salons prives, reactions emojis et in`
- **ahelme/mcp-claude-code-browser-tools** (2★) → llm=**tangential** (c=0.95) — AI coding agent MCP server, no AsyncAPI usage
  `An browser-tools mcp server for claude code`
- **btravers/amqp-contract** (18★) → llm=**tooling/library** (c=0.95) — TypeScript library for type-safe AMQP/RabbitMQ contracts
  `Type-safe contracts for AMQP/RabbitMQ messaging with TypeScript`
- **calvinlee999/AI-Platform-for-FinTech-Evolution** (0★) → llm=**spec/docs** (c=0.95) — Executive documentation and architecture diagrams only
  `AI Platform for FinTech Evolution 🎯 Executive Summary This repository provides executive level documentation and high level architecture for`
- **foxminchan/BookWorm** (502★) → llm=**demo/fixture** (c=0.95) — Explicitly demo-only, not production ready
  `The practical implementation of Aspire using Microservices, AI-Agents`
- **kingak4/ft_transcendence** (4★) → llm=**demo/fixture** (c=0.95) — 42 school curriculum final project
  `ft_transcendence is a team-based web application built as part of the final 42 project. Our web application includes a login system, interac`
- **pingxin403/platform-console** (0★) → llm=**demo/fixture** (c=0.95) — Personal learning project with explicitly fictional scenario
  `Personal learning project: Backstage IDP reference implementation. Scenario (50-person SaaS) is fictional.`
- **tornado80/collaborative-whiteboard** (1★) → llm=**demo/fixture** (c=0.95) — University course project, Internet Protocols at Aalto
  `Collaborative Whiteboard written in Erlang and React over Websocket protocol. Share the URL with your team mates to start doodling your awes`
- **StepanNazar/city-report-ai-assistance-service** (0★) → llm=**demo/fixture** (c=0.93) — Explicitly described as university software architecture labs
  `university labs for software architecture`
- **UNIZAR-30226-2026-07/BombaVa-Backend** (1★) → llm=**demo/fixture** (c=0.93) — University of Zaragoza course project with academic numbering
  `Backend del juego de Bomba Va`
- **ai-digital-architect/asyncapi_discovery** (0★) → llm=**tooling/library** (c=0.93) — Tool that scans code and generates AsyncAPI specs
  `Scan repositories for event producers regardless of the broker and create asynapi catalog specifications for those.`
- **piedraprog/unified-personal-skills** (2★) → llm=**tangential** (c=0.93) — AI coding-agent skills registry, AsyncAPI only incidental
  `skills que voy acumulando que me funcionen para el desarrollo`
- **rlarin/it-crowd-pixel-agents** (1★) → llm=**tangential** (c=0.93) — AI coding-agent visualization plugin, not an AsyncAPI user
  `Pixel art office where your Claude Code agents come to life — with JetBrains (PyCharm/WebStorm) support. Fork of pixel-agents by Pablo De Lu`
- **LeonidasGarcia/puchamon** (0★) → llm=**demo/fixture** (c=0.92) — Explicitly a university project, Pokemon Showdown clone
  `Proyecto universitario de clon de Pokemon Showdown con un bot IA para simulación de batallas 3v3 o 4v4`
- **Remake1/GrokOA** (0★) → llm=**tangential** (c=0.92) — Interview cheat tool; AsyncAPI not mentioned at all
  `Stealth coding Online Assessment and Interview cheat tool.`
- **StableCoinTF/StableCoinBC_Adapter_Docs** (0★) → llm=**spec/docs** (c=0.92) — AsyncAPI YAML spec repo generating Kafka API documentation
  `StableCoinBC_Adapter_Docs`
- **Thomas-More-Digital-Innovation/2526-DI-004-GoStrategy** (0★) → llm=**demo/fixture** (c=0.92) — University course project at Thomas More institution
  `Project 2025-2026 DI-004: GoStrategy`
- **V-ivek/workflow-engine** (0★) → llm=**demo/fixture** (c=0.92) — Explicitly a coding challenge submission, not production software
  `An Event-Driven workflow orchestration engine`
- **aniccname/Q-Game** (0★) → llm=**demo/fixture** (c=0.92) — School project from Fall 2023 Software Development course
  `A Qwirkle inspired game using a Client-Server architecture. A browser-based client is hosted at the linked website.`
- **igmrrf/ecommerce_services** (1★) → llm=**demo/fixture** (c=0.92) — Self-described demonstration of microservices architecture
  `E commerce Microservices This project is a demonstration of a microservices architecture for an e commerce platform. It involves four main s`
- **jhamill34/disney-gen-ai-takehome** (0★) → llm=**demo/fixture** (c=0.92) — Take-home interview/exercise project, not production software
  `Disney GenAI Take home This project ingests different web pages and stores them in a vector database (I chose to use the PgVector extension `
- **miltonabdon/ecommerce-scalable-platform** (0★) → llm=**demo/fixture** (c=0.92) — Explicitly a practical demonstration of architectural patterns
  `E-Commerce platform demonstrating scalable architecture for Black Friday — Java 21, Spring Boot 3.3, Kafka, Redis, MongoDB, Elasticsearch, O`
- **nandorsilva/eda-fia-th** (0★) → llm=**demo/fixture** (c=0.92) — Explicitly a lab for local development and study purposes
  `Lab Eda Kafka Connect Disclaimer As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos Pré requisitos? `
- **MALIEV-Co-Ltd/Maliev.MessagingContracts** (0★) → llm=**spec/docs** (c=0.9) — Contract-first schema registry and AsyncAPI specs only
  `Messaging contracts for all Maliev microservices — events, commands, RPC messages, schemas, AsyncAPI specs, and RabbitMQ topology.`
- **facundo1220/asyncapi-eda-ecommerce** (0★) → llm=**demo/fixture** (c=0.9) — Demonstrates EDA microservices pattern with RabbitMQ
  `EDA Ecommerce Microservices Este proyecto implementa una arquitectura orientada a eventos (EDA) para un sistema de ecommerce, utilizando mic`
- **jordancrombie/bsim** (0★) → llm=**demo/fixture** (c=0.9) — Banking simulator, educational or demo application
  `A Banking Simulator`
- **metalalive/e_commerce** (1★) → llm=**demo/fixture** (c=0.9) — Readme explicitly states not production ready, learning purpose
  `E-commerce backend platform implemented in Python / C / Rust`
- **rabbytesoftware/quiver.core** (6★) → llm=**tangential** (c=0.9) — Cross-platform package manager; no AsyncAPI relevance
  `Quiver is a multi-platform package manager - probably the only one you'll ever need! It's designed to make complex installation processes qu`
- **CodingFlow/rating-service-dotnet** (1★) → llm=**demo/fixture** (c=0.88) — Explicit prototype showcasing architectural best practices
  `Prototype full-stack C#, Preact web app deployed on Azure AKS using modern tools, developer experience, architectural design for enterprise-`
- **Integration-Project-2026-Groep-2/CRM** (2★) → llm=**demo/fixture** (c=0.88) — Academic integration project microservice for school platform
  `CRM — Integration Project 2025/2026 Salesforce integration for the Desideriushogeschool event management platform (Groep 2). CRM is the mast`
- **Integration-Project-2026-Groep-2/Planning** (0★) → llm=**demo/fixture** (c=0.88) — Academic integration project planning microservice, Groep 2
  `Planning Service Microservice voor het beheren van sessies, locaties en sprekers. Onderdeel van het Integratieproject 2026 — Groep 2. Vereis`
- **Kambolo/Picksy** (0★) → llm=**demo/fixture** (c=0.88) — Engineering thesis web app, not production software
  `Picksy – Real Time Group Voting Application Picksy is a web based application designed to facilitate real time group voting. The system allo`
- **MathTrail/contracts** (0★) → llm=**spec/docs** (c=0.88) — Schema registry with AsyncAPI spec and event contracts
  `Schema Registry for MathTrail: Type-safe contracts and event definitions to ensure cross-service compatibility across the EDA stack.`
- **ProsusAI/agentic-services-protocol** (12★) → llm=**spec/docs** (c=0.88) — Open protocol/spec definition for agentic service lifecycle
  `Agentic Services Protocol (ASP) - an open protocol for the complete agentic service lifecycle: discovery, catalog, fulfillment, order tracki`
- **bicatu/event-catalog** (5★) → llm=**demo/fixture** (c=0.88) — Companion repo for an article, starter/example purpose
  `Event Catalog starter repository`
- **devmentors/Mikroserwisy-Revisited** (2★) → llm=**demo/fixture** (c=0.88) — Polish microservices course companion code, educational
  `[PL] Mikroserwisy 6 lat później czyli... jak nie utonąć 😉`
- **ivanztz/sandbox** (2★) → llm=**demo/fixture** (c=0.88) — Explicitly educational or project accelerator purposes
  `Sandbox project`
- **kaucrow/mqtt-rest-bridge** (0★) → llm=**demo/fixture** (c=0.88) — Explicitly described as a demo SCADA system
  `MQTT broker & REST API for a demo SCADA system which bridges two microcontrollers with a real-time dashboard and an SQLite database.`
- **maxime-aube/ollama** (0★) → llm=**demo/fixture** (c=0.88) — Node/TypeScript starter template boilerplate
  `node ts starter template This is a starter repository for nodejs projects in Typescript made in node v20.11. You'll find: Typescript and esl`
- **xingyug/service2mcp** (0★) → llm=**tooling/library** (c=0.88) — Compiles AsyncAPI and other specs into MCP tool servers
  `Compile any API (OpenAPI, GraphQL, gRPC, REST, SOAP, SQL, AsyncAPI, JSONRPC) into a governed, observable MCP tool server — detect → extract `
- **Harmelodic/init-microservice** (3★) → llm=**demo/fixture** (c=0.87) — Bootstrapping template and reference implementation for microservices
  `How I build microservices (in Java).`
- **Insightpulseai/agents** (0★) → llm=**tangential** (c=0.87) — AI agent personas and prompt contracts registry, not AsyncAPI user
  `Agent personas, skills, judges, evals, metadata, registries, and prompt contracts`
- **Malmo-Skyttegille-Pistolsektionen/rotation_target_backend_resources** (0★) → llm=**spec/docs** (c=0.87) — Resources and AsyncAPI/OpenAPI documentation, not runnable software
  `Resources used by the Rotation Target Backend`
- **DarkflameUniverse/DarkflameServer** (738★) → llm=**tangential** (c=0.85) — Game server emulator; AsyncAPI not central to its purpose
  `The main repository for the Darkflame Universe Server Emulator project.`
- **DevashishBoini/attendanceSystem** (0★) → llm=**demo/fixture** (c=0.85) — Explicitly based on a Harkirat Singh course assignment
  `Attendance System A real time classroom attendance marking system built with Node.js, Express, WebSocket, and MongoDB. Teachers can mark stu`
- **event-catalog/eventcatalog** (2724★) → llm=**tooling/library** (c=0.85) — Tooling platform to catalog and govern event-driven APIs
  `The discovery and governance layer for event-driven systems. Document your domains, services, events and schemas — for your teams and your A`
- **rainbow-mobile/web_robot_server** (2★) → llm=**demo/fixture** (c=0.85) — NestJS starter repository template, not a real service
  `[circleci image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token abc123def456 [circleci url]: https://circleci.com/gh`
- **Devathon-2024-team5/Preguntonic-backend** (0★) → llm=**demo/fixture** (c=0.82) — Hackathon (Devathon-2024) team project, not production software
  `Preguntonic-Backend es el núcleo inteligente y robusto que impulsa la experiencia de juego de Preguntonic. Diseñado para proporcionar una ge`
- **IATI/iati-message-queue-service** (0★) → llm=**spec/docs** (c=0.82) — Repo is the specification for an internal message queue service
  `IATI Message Queue Service Summary Product IATI Message Queue Service Description The specification for the internal message queue service t`
- **codeboltai/codeboltjs** (0★) → llm=**tangential** (c=0.82) — AI agent SDK; no AsyncAPI focus
  `Js Library for Codebolt`
- **cycleplatform/api-spec** (5★) → llm=**spec/docs** (c=0.82) — Dedicated API spec repo for Cycle platform APIs
  `OpenAPI spec files for Cycle APIs`
- **kanekoshoyu/exchange-collection** (23★) → llm=**spec/docs** (c=0.82) — Collection of crypto exchange OpenAPI/AsyncAPI spec documents
  `Collection of Crypto Exchange OpenAPI and Generated Clients`
- **makeevolution/SimplePizzaWinkel** (0★) → llm=**demo/fixture** (c=0.82) — Personal learning project applying microservices knowledge
  `Simple Pizza Winkel Description This is my personal project, to apply my learnings about microservices that I have seen and worked with in m`
- **znsio/specmatic-async-order-api-kotlin** (0★) → llm=**demo/fixture** (c=0.82) — Sample app demonstrating Specmatic async contract testing
  `Order API accepts request for an order which is created asynchronously.`
- **LaurenCattoor/st-microservice-ticketing** (0★) → llm=**demo/fixture** (c=0.8) — Student project with deliverables language; thesis-style setup
  `Microservices Ticketing Before proceeding, make sure to follow the Project Build and Deploy document for proper setup and deployment instruc`
- **Xen0Xys/N2I-2024-API** (0★) → llm=**demo/fixture** (c=0.8) — NestJS starter for N2I 2024 competition, not production service
  `[circleci image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token abc123def456 [circleci url]: https://circleci.com/gh`
- **briossant/BotAmoungUs** (0★) → llm=**demo/fixture** (c=0.8) — Hackathon proof-of-concept game, not production
  `Bot Among Us A real time multiplayer social deduction game where humans try to identify AI controlled players — and an AI benchmarking platf`
- **motor-screwdriver/mts-true-tech-hack-26** (4★) → llm=**demo/fixture** (c=0.8) — Hackathon project indicated by -hack-26 in repo name
  `WikiLive is a real-time document collaboration platform. The project combines an editor with CRDT synchronization, a backend API for busines`
- **owasp-noir/noir** (1320★) → llm=**tooling/library** (c=0.8) — SAST tool parsing API specs including AsyncAPI to extract endpoints
  `Hunt every Endpoint in your code, expose Shadow APIs, map the Attack Surface.`
- **Binit-Dhakal/Saarathi** (0★) → llm=**demo/fixture** (c=0.78) — "Simulates" ride lifecycle; portfolio/demo project
  `Ride-sharing App built with Golang and NextJS in event-driven architecture`
- **CDFmmgr9fLkRH453kRC33TrEp/matching-engine** (2★) → llm=**demo/fixture** (c=0.78) — Self-described simplistic exchange simulator, not production
  `Rust Matching Engine, Limit Order Book, and Exchange Simulator Simplistic exchange simulator with in memory order book and multi asset credi`
- **cjjohansen/drone-web** (2★) → llm=**demo/fixture** (c=0.78) — API design example using ADDR/Event Modeling methodology
  `drone ecommerce website using ADDR Design process`
- **delano/postman-mcp-server** (150★) → llm=**tangential** (c=0.78) — MCP server for Postman API; no AsyncAPI connection visible
  `An MCP server that provides access to Postman.`
- **openwop/openwop** (1★) → llm=**spec/docs** (c=0.78) — Wire-level protocol specification for multi-agent orchestration
  `openwop — Open Workflow Orchestration Protocol`
- **Lulexs/iots-1** (0★) → llm=**demo/fixture** (c=0.75) — Uses university dataset, student IoT gateway project
  `O dataset u: Izvor: https://zenodo.org/records/13808085 Dataset sadrzi sirok skup podataka (1.6 gb) o razlicitim parametrima sistema za snab`
- **TristanDeLil/ms-microservice-ticketing** (0★) → llm=**demo/fixture** (c=0.75) — Student microservices project at Howest university
  `Microservices Ticketing bash docker compose f config/ticketing howestprime dev/docker compose.yml up d remove orphans Infrastructure 📘 Mongo`
- **prajwalaher33/feeshr** (1★) → llm=**tangential** (c=0.75) — AI agent collaboration platform; AsyncAPI use incidental
  `Feeshr — Operating Engine for AI Agents`
- **thomascarter613/aic-smb-copilot-codebase** (0★) → llm=**demo/fixture** (c=0.74) — Skeleton/boilerplate microservices architecture with K8s manifests
  `Orders Vertical Slice (Skeleton) Gateway → Orders → Payments → Projector with K8s manifests ( canary , KEDA ) and Sigstore admission policy.`
- **Brico87/seed-kafka** (0★) → llm=**demo/fixture** (c=0.72) — Kafka infrastructure seed/starter setup, not a deployable product
  `Lancement infra C:\Projects\seed kafka docker compose up d [+] Running 5/6 Volume "seed kafka klaw data" Created 3.3s ✔ Container klaw core `
- **Kiloforge/kiloforge** (17★) → llm=**tangential** (c=0.72) — AI coding-agent orchestration platform; AsyncAPI incidental
  `1,000x Productivity. Command AI agent swarms and ship code at the speed of thought.`
- **ManuMarcos/mind-battle-backend** (0★) → llm=**demo/fixture** (c=0.72) — Kahoot-inspired learning project, no production indicators
  `Backend for a real-time multiplayer quiz game inspired by Kahoot. Built with a microservices architecture using Spring Boot, MongoDB, WebSoc`
- **Sriramanenivikas/Intelligent-Warehouse-Orchestration-System** (1★) → llm=**demo/fixture** (c=0.72) — Explicitly a planning skeleton without implementation code
  `IWOS  is a unified fulfillment platform that combines quick commerce (dark stores, rapid picking), large-scale e-commerce fulfillment (pick-`
- **ZuzannaTabisz/snp-app** (0★) → llm=**tangential** (c=0.72) — RNA structural analysis tool; no meaningful AsyncAPI usage
  `SNPsniper leverages state of the art computational methods to predict, compare, and visualize structural changes in RNA sequences, offering `
- **ZuzannaTabisz/snpapptests** (0★) → llm=**tangential** (c=0.72) — Test suite for RNA app; no meaningful AsyncAPI usage
  `snp app Włączenie aplikacji docker compose up build Włączenie aplikacji z zapisywaiem logów docker compose up build 2 &1 tee build log.txt B`
- **ayointegral/cloud-sandbox-backstage** (1★) → llm=**tangential** (c=0.72) — Backstage portal; AsyncAPI only incidental in catalog templates
  `Cloud Sandbox - Backstage Developer Portal with custom catalog and templates`
- **davidtgillard/fits** (0★) → llm=**tangential** (c=0.72) — Zig repo engine; no AsyncAPI connection visible
  `One eighth of an agony`
- **hungvo2010/free-note-service** (0★) → llm=**demo/fixture** (c=0.72) — Basic learning project with checklist-style incomplete features
  `free note service Simple web socket server built with Java Core Supports: [ ] WebSocket handshaking [ ] HTTPS support [ ] Fragmentation [ ] `
- **murithigeo/ogc-edr-api** (0★) → llm=**demo/fixture** (c=0.72) — Reference implementation for OGC standard, work in progress
  `A reference implementation for OGC EDR API`
- **seanchatmangpt/dslmodel** (27★) → llm=**tangential** (c=0.72) — AI dev platform; AsyncAPI mentioned incidentally, not core purpose
  `Structured outputs from DSPy and Jinja2`
- **yukihito-jokyu/postman-mcp-server** (0★) → llm=**tangential** (c=0.72) — MCP server wrapping Postman API, AsyncAPI incidental
  `Postman MCP Server Version: v0.2.0 An MCP server that provides access to the Postman API. Functionality is based on the official OpenAPI spe`
- **Anomaliszt/Conquest** (1★) → llm=**tangential** (c=0.7) — C2 framework; no AsyncAPI mention in readme
  `Conquest Command & Control (C2) framework with Flask/Socket.IO server, PyInstaller based payload builder, and operator CLI. Prerequisites Py`
- **pt9912/geodata-native-suite** (0★) → llm=**tangential** (c=0.7) — Helm/Kubernetes monorepo; no clear AsyncAPI role
  `geodata native suite (monorepo) Vereint Charts , Values (base→platform→env), RKE2 Deployment und DevContainer in einem Repo. Struktur .devco`
- **nguyenvinhhuy/microservice-platform** (0★) → llm=**demo/fixture** (c=0.68) — Reference architecture demo showcasing full enterprise stack
  `Microservice Platform Complete Stack 🚀 Enterprise grade microservice platform với 8 Spring Boot services + Angular 21 Frontend + Keycloak Id`
- **ChargeAndTrack/backend-spe** (0★) → llm=**demo/fixture** (c=0.65) — Academic SPE project backend with documentation site
  `Backend for the SPE project.`
- **pseudotop/maekon-client** (0★) → llm=**tangential** (c=0.65) — Local desktop agent; AsyncAPI presence not evident from text
  `Open-source desktop intelligence client that turns local work signals into a real-time focus timeline and actionable suggestions.`
- **apakhbari/backstage** (0★) → llm=**demo/fixture** (c=0.6) — Personal notes and tips about a Backstage deployment setup
  `Backstage 🦾`
- **loulou123546/kenshiata-shared** (0★) → llm=**tangential** (c=0.55) — Shared types library; AsyncAPI likely incidental
  `Shared files between server and clients, like types or some pure function`
- **yuvraj-chouhan-dev/ready-now-server** (0★) → llm=**uncategorized** (c=0.5) — Sparse readme, insufficient information to classify
  `ready now SDK Backend server`
- **aescanero/dago** (0★) → llm=**uncategorized** (c=0.45) — No readme; DA Orchestrator purpose too vague to classify
  `DA Orchestrator core repository`
- **itamm15/sync-async-docs** (0★) → llm=**uncategorized** (c=0.35) — Only Phoenix boilerplate in readme; purpose unclear
  `SyncAsyncDocs To start your Phoenix server: Run mix setup to install and setup dependencies Start Phoenix endpoint with mix phx.server or in`

### rule = spec/docs (20)

- **ByteBardOrg/AsyncAPI.NET** (13★) → llm=**tooling/library** (c=0.99) — .NET SDK and object model for AsyncAPI specification
  `The official continuation of LEGO.AsyncAPI.NET from the original author and maintainer. The SDK contains a useful object model for AsyncAPI `
- **bdragon300/go-asyncapi** (11★) → llm=**tooling/library** (c=0.99) — AsyncAPI codegen, CLI, diagram, and web UI toolchain
  `AsyncAPI tool: codegen, no-code CLI app, server definitions, diagrams, web UI`
- **asynq-io/pydantic-asyncapi** (9★) → llm=**tooling/library** (c=0.98) — Pydantic models for validating and generating AsyncAPI docs
  `Pydantic models for AsyncAPI schema`
- **dghilardi/asyncapiv3** (3★) → llm=**tooling/library** (c=0.98) — Rust library parsing and serializing AsyncAPI v3 specs
  `Asyncapi v3 Representation of the AsyncAPI v3 specification. AsyncAPI is a standard inspired by OpenAPI/Swagger targetting asynchronous and `
- **RobinTail/zod-sockets** (116★) → llm=**tooling/library** (c=0.97) — Library that generates AsyncAPI specs from Socket.IO schemas
  `Socket.IO solution with I/O validation and the ability to generate AsyncAPI specification and a contract for consumers.`
- **asyncapi/tck** (12★) → llm=**demo/fixture** (c=0.97) — Test Compatibility Kit with AsyncAPI fixture documents
  `(WIP) Test Compatibility Suite for AsyncAPI`
- **joserprieto/ai-skills** (2★) → llm=**tangential** (c=0.97) — AI coding-agent skills collection, not an AsyncAPI user
  `Reusable AI agent skills for Claude Code and other AI tools`
- **Leandroyyy/async-api-translator** (0★) → llm=**tooling/library** (c=0.95) — Translator tool for AsyncAPI specifications
  `Translator for async api specification`
- **wirenboard/wb-device-manager** (0★) → llm=**product** (c=0.95) — Real IoT Modbus device manager with MQTT/AsyncAPI spec
  `Wiren Board modbus devices manager`
- **fern-api/docs-starter** (39★) → llm=**demo/fixture** (c=0.93) — Starter template for publishing docs from OpenAPI
  `Publish beautiful documentation from OpenAPI and markdown (MDX)`
- **Kong/spec-renderer** (33★) → llm=**tooling/library** (c=0.92) — Pluggable API spec renderer powering documentation experiences
  `A lightweight, pluggable spec renderer built by Kong. Designed to power fast, customizable API documentation experiences.`
- **belgif/openapi-cloudevents** (0★) → llm=**tangential** (c=0.92) — OpenAPI CloudEvents definitions; no AsyncAPI usage
  `OpenAPI definitions for CloudEvents`
- **fern-demo/postman-quickstart** (0★) → llm=**demo/fixture** (c=0.91) — Demo quickstart template identical to docs-starter
  `Docs starter Create beautiful documentation in under 5 minutes using your OpenAPI specification. Customer showcase Get inspired by API docum`
- **Scott-HW-OU/shw-616172** (0★) → llm=**demo/fixture** (c=0.9) — Docs starter template with sample API for onboarding
  `Documentation for shw-616172`
- **fern-support/universal-shuttle-348791** (0★) → llm=**demo/fixture** (c=0.9) — Docs starter template boilerplate
  `Documentation for universal-shuttle-348791`
- **heikkilamarko/todo-app** (20★) → llm=**demo/fixture** (c=0.9) — Explicitly a hobby playground for experimenting with technologies
  `Todo App`
- **DocHubTeam/DocHub** (375★) → llm=**tooling/library** (c=0.88) — Architecture-as-code tool that renders AsyncAPI among other formats
  `Управление архитектурой как кодом`
- **eclipse-canought/can-translator** (0★) → llm=**product** (c=0.87) — Deployable automotive MQTT-to-CAN translator service
  `can-translator`
- **maciekpapiez/redocly-1** (0★) → llm=**demo/fixture** (c=0.85) — Starter template for Redocly API docs project
  `Reunite Redoc Starter Project [!IMPORTANT] This project is a starter template for use with Redocly's Reunite product suite. For open source `
- **Koh0920/webapp_specs** (0★) → llm=**demo/fixture** (c=0.8) — Template/boilerplate repo for web app design specifications
  `webapp specs 現代のWebアプリ開発に必要な設計仕様書を、業界標準の書式で管理するテンプレートリポジトリ。 特徴 業界標準準拠 : OpenAPI、DBML、AsyncAPI等を採用 3段階テンプレート : minimal/standard/enterprise 自動`

### rule = tooling/library (101)

- **smoya/asyncapi-parser-example** (0★) → llm=**demo/fixture** (c=0.99) — Minimal example showing how to validate AsyncAPI documents
  `This small and simple repository shows how to validate an AsyncAPI document from your code using the @asyncapi/parser`
- **Pakisan/jasyncapi-idea-plugin-demo** (0★) → llm=**demo/fixture** (c=0.97) — Explicitly a demo repo for JetBrains AsyncAPI plugin
  `Repository to show how AsyncAPI specification works in JetBrains IDE`
- **jonathan-prout/tic-tac-toe** (0★) → llm=**demo/fixture** (c=0.97) — Explicitly a demo project for WebSocket and REST API
  `Demo project for websocket and rest api`
- **kondoumh/asyncapi-study** (0★) → llm=**demo/fixture** (c=0.97) — Explicitly named study repo for learning AsyncAPI
  `asyncapi study AsyncAPI Initiative for event driven APIs AsyncAPI Studio install CLI shell npm install g @asyncapi/cli`
- **laat/asyncapi-generator-repro** (0★) → llm=**demo/fixture** (c=0.97) — Bug reproduction case for asyncapi-generator issue
  `repro sh npm ci npx asyncapi generator force write output dist asyncapi.yaml @asyncapi/html template Something went wrong: Error: This templ`
- **meteatamel/asyncapi-basics** (3★) → llm=**demo/fixture** (c=0.97) — Educational samples and references about AsyncAPI
  `This repository contains information, references, and samples about AsyncAPI`
- **openxapi/openxapi** (9★) → llm=**spec/docs** (c=0.97) — Collection of AsyncAPI/OpenAPI specs for crypto exchanges
  `OpenAPI and AsyncAPI specifications for cryptocurrency exchanges and DeFi protocols`
- **s-menne-inovex/async_api_pages** (1★) → llm=**demo/fixture** (c=0.97) — Explicitly testing asyncapi generator with GitHub Pages
  `Testing the asyncapi generator with github pages`
- **ripple/rippled-api-spec** (2★) → llm=**spec/docs** (c=0.96) — Repository of OpenAPI/AsyncAPI specs for XRP Ledger
  `A repository for OpenAPI / AsyncAPI specifications. This ideally eventually can be used to automatically generate code and docs to simplify `
- **sarkr72/practice** (0★) → llm=**demo/fixture** (c=0.96) — Explicitly described as a learning project for enterprise patterns
  `EMS — Employee Management System Spring Boot 3.3 reference service. Built as a learning project for enterprise patterns: layered config, Fly`
- **viktorSrk/quartogether** (0★) → llm=**demo/fixture** (c=0.96) — TU Delft CSE2000 course project, academic year
  `Full-stack collaborative online text editor using the Quarto engine for rendering. The editor supports real-time collaboration through WebSo`
- **EVerest/EVerest** (207★) → llm=**product** (c=0.95) — Linux Foundation Energy-backed EV charging software stack
  `Main Repository of EVerest - an EV charging software stack`
- **PolyAI-LDN/polyai-mintlify-doc** (0★) → llm=**spec/docs** (c=0.95) — Documentation site source for PolyAI Agent Studio
  `This is the source code of the PolyAI Agent Studio documentation`
- **juliangracin/community-docs** (0★) → llm=**spec/docs** (c=0.95) — Repository contains AsyncAPI spec file for community API
  `Community Docs Community API The asyncAPI spec in api/ws community api.yml file. To preview the file, copy it's contents into the AsyncAPI S`
- **openfoodfacts/openfoodfacts-server** (1047★) → llm=**product** (c=0.95) — Main food database API server and web interface
  `Open Food Facts database, API server and web interface - 🐪🦋 Perl, CSS and JS coders welcome 😊 For helping in Python, see Robotoff or taxonom`
- **roldaiateam/apis-especifications** (0★) → llm=**spec/docs** (c=0.95) — API contract specifications published as Maven artifacts
  `Este repositorio contiene las definiciones y especificaciones de las APIs del sistema`
- **Pinit-Scheduler/pinit-task** (0★) → llm=**product** (c=0.93) — Real task-management microservice backend
  `일정 관리/실행 서비스 Pinit의 일정 관리/실행 기능을 담당하는 마이크로서비스`
- **Benzinga/benzinga-docs** (2★) → llm=**spec/docs** (c=0.92) — Mintlify-powered documentation site for Benzinga APIs
  `Benzinga Docs Powered by Mintlify Live at https://benzinga 2.mintlify.app Click on Use this template to copy the Mintlify starter kit. The s`
- **CardanoSolutions/ogmios** (327★) → llm=**product** (c=0.92) — Real deployable WebSocket/JSON-RPC bridge for Cardano node
  `❇️ A WebSocket JSON/RPC bridge for Cardano`
- **EDALearn/EDA-TransactionalOutbox-Modulith-JPA** (5★) → llm=**demo/fixture** (c=0.92) — Tutorial implementing Transactional Outbox pattern with ZenWaveSDK
  `Implementing a Transactional OutBox With AsyncAPI, SpringModulith and ZenWaveSDK`
- **Grinseteddy/DomainDrivenApiDesign** (5★) → llm=**demo/fixture** (c=0.92) — Training resources with demo online library interfaces
  `Repository for ressources for trainings`
- **bian-official/public** (194★) → llm=**tangential** (c=0.92) — Banking Swagger/OpenAPI APIs; no AsyncAPI usage
  `This is a repository of BIAN artefacts, currently the BIAN Semantic APIs`
- **exploding-CATs-42/ft_transcendence** (0★) → llm=**demo/fixture** (c=0.92) — 42 school capstone project, not production software
  `ft transcendence This project is run and developed via Docker Compose and Makefile . Below is the working command sequence for developers, i`
- **lg-labs/blank-service** (4★) → llm=**demo/fixture** (c=0.92) — Explicitly a template; readme says replace blank with domain
  `👋 Management the blank service for the blanksystem as template.`
- **ministryofjustice/hmpps-accredited-programmes-manage-and-deliver-api** (3★) → llm=**product** (c=0.92) — Production Spring Boot API for HMPPS accredited programmes
  `HMPPS Manage and Deliver Accredited Programmes API Layer (bootstrapped 2025-06-10)`
- **specmatic/aws-lambda-kafka-with-localstack** (0★) → llm=**demo/fixture** (c=0.92) — Demo showing Lambda/Kafka contract testing with AsyncAPI 3.0
  `Run Specmatic Kafka Contract Test on AWS Lambda with Amazon MSK on LocalStack using AsyncAPI 3.0 This project demonstrates below aspects Set`
- **ministryofjustice/hmpps-find-and-refer-an-intervention-service** (2★) → llm=**product** (c=0.91) — Production service for finding and referring interventions
  `Business/domain interface for providing Find and Refer an Intervention Service`
- **TemplateMechanics/tilt** (2★) → llm=**demo/fixture** (c=0.9) — Tilt file examples demonstrating deployment patterns
  `Tilt File Examples`
- **bitsy-ai/printnanny-webapp** (3★) → llm=**product** (c=0.9) — Real IoT webapp and API for 3D printer monitoring plugin
  `Print Nanny Webapp API and webapp for Octoprint Print Nanny plugin by Bitsy.ai .. image:: https://img.shields.io/badge/built%20with Cookiecu`
- **deepgram/starter-contracts** (0★) → llm=**spec/docs** (c=0.9) — Collection of OpenAPI and AsyncAPI specs for Deepgram services
  `Quickly build Deepgram Starter Apps from API specifications and Interface contracts`
- **encypher-studio/newsware-docs** (0★) → llm=**spec/docs** (c=0.9) — Frontend documentation site for Newsware API clients
  `Frontend for user documentation of the Newsware clients to interact with the API`
- **DEFRA/ffc-doc-statement-generator** (0★) → llm=**product** (c=0.88) — Production statement generator service with Azure Service Bus
  `FFC Payment Statement Generator Prerequisites Docker Docker Compose Optional: Kubernetes Helm Azure Service Bus This service depends on a va`
- **Jacksonspencerd/tcss559-project** (1★) → llm=**demo/fixture** (c=0.88) — University course project (TCSS 559) observability platform
  `☁️ TCSS 559 Project: Eye in the Sky A full stack observability platform featuring a React frontend, Node.js/Go backend services, Cloud Funct`
- **RossBugginsNHS/notify-asyncapi** (1★) → llm=**spec/docs** (c=0.88) — Builds and publishes AsyncAPI schema pages for NHS Notify
  `Notify Async Events Schema Setup bash make config Build bash make build Preview View build schema pages in /docs folder Setup github pages, `
- **forepath/agenstra** (1★) → llm=**product** (c=0.88) — Deployable platform for managing AI agent infrastructure
  `Centralized management platform for distributed AI agent infrastructure with real-time interaction, code editing, and automated provisioning`
- **l3wi/docs** (0★) → llm=**spec/docs** (c=0.88) — Documentation site using Mintlify starter kit
  `Mintlify Starter Kit Use the starter kit to get your docs deployed and ready to customize. Click the green Use this template button at the t`
- **samovers/OFARM** (0★) → llm=**spec/docs** (c=0.88) — Open semantic reference model and governance framework, not runnable software
  `Open semantic reference model and governance framework for traceable, interoperable crop-farming platforms.`
- **simliai/docs** (1★) → llm=**spec/docs** (c=0.88) — Documentation site using Mintlify, no runnable application
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **acidtango/ollert-backend** (2★) → llm=**product** (c=0.87) — API-first backend using asyncapi.yml to generate TypeScript types
  `Generate Schemas First, you need to install @asyncapi/cli globally , installing it as dev dependencies doesn't work: npm install g @asyncapi`
- **Caldis/frameworks** (8★) → llm=**tangential** (c=0.85) — Curated design-frameworks catalog; AsyncAPI incidental
  `Software Design Frameworks | A curated collection for engineers, architects, and AI agents`
- **Opzet/EFDesignerExamples** (0★) → llm=**tangential** (c=0.85) — Entity Framework code-gen examples; no AsyncAPI relevance
  `EF Visual Designer Examples Model and generate code for Database Examples for both Entity Framework v6.x (Dot Net 4.x) and Entity Framework `
- **bakabala27-svg/NAAS-Agentic-Core** (2★) → llm=**tangential** (c=0.85) — AI tutoring framework; no AsyncAPI usage evident
  `🛡️ North African AI Safety Lab (NAAS Lab) Project: EL NUKHBA (The Elite) NAAS Agentic Core 0b7285?style for the badge) The "Elite" Verify th`
- **pascal-audio/px-api** (0★) → llm=**spec/docs** (c=0.85) — API documentation and spec for hardware audio amplifiers
  `Public JSON-RPC based API for PX-Series`
- **pv-udpv/dual-publish-platform** (0★) → llm=**demo/fixture** (c=0.85) — Reference scaffold template for publishing OpenAPI/AsyncAPI specs
  `Reference scaffold: dual-publish OpenAPI/AsyncAPI specs as both UTCP manuals and MCP server surfaces from one source of truth, with codegen `
- **solace-cto-labs/solace-amplify-discovery-agent** (1★) → llm=**product** (c=0.85) — Deployable agent synchronizing AsyncAPIs between Solace and Amplify
  `Solace-Amplify-Discovery-Agent for synchronizing Solace AsyncAPIs with Axway Amplify Platform`
- **DigKick/DigKick** (4★) → llm=**product** (c=0.83) — Real table-soccer goal-detection system with MQTT hardware integration
  `DigKick is a system that detects goals and tracks players elo for table soccer.`
- **AlexandrePh/flywheel-starter-kit** (0★) → llm=**demo/fixture** (c=0.82) — Starter kit template for AI-driven application development
  `Flywheel Starter Kit A comprehensive starter kit for building modern, AI driven applications following Flywheel principles. This repository `
- **Tomeku-Development/AgentMesh** (0★) → llm=**demo/fixture** (c=0.82) — Hackathon competition entry for Vertex Swarm Challenge 2026
  `MESH is a fully decentralized multi-agent system where autonomous agents negotiate, trade, ship, inspect, and settle supply chain orders -- `
- **cipher982/longhouse** (0★) → llm=**tangential** (c=0.82) — AI agent session manager; no AsyncAPI usage
  `centralized location for managing ai agents`
- **gocobalt/mintlify-docs** (1★) → llm=**spec/docs** (c=0.82) — Mintlify docs starter kit, documentation only
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including. This is a sam`
- **klurvio/sukko** (0★) → llm=**product** (c=0.82) — Real-time trading data WebSocket infrastructure platform
  `Sukko Multi tenant WebSocket infrastructure platform for real time data distribution. Built for trading and market data — delivers messages `
- **mayankshouche/docs** (0★) → llm=**tangential** (c=0.82) — Mintlify docs starter kit, no AsyncAPI content evident
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **mayankshouche/docs-ally** (0★) → llm=**tangential** (c=0.82) — Mintlify docs starter kit, no AsyncAPI content evident
  `Mintlify Starter Kit Use the starter kit to get your docs deployed and ready to customize. Click the green Use this template button at the t`
- **paddypawprints/VLMChat** (1★) → llm=**product** (c=0.82) — Deployable edge AI platform for vision language models on hardware
  `VLMChat An edge AI platform for deploying vision language models (VLMs) on devices like Raspberry Pi and NVIDIA Jetson, with a web based man`
- **David-Parry/server-agents** (3★) → llm=**product** (c=0.8) — Deployable AI agent orchestration platform with governance
  `Server Agents Platform The server side backbone of this AI agent infrastructure. It orchestrates LLM interactions, enforces governance polic`
- **NHSDigital/nhs-notify-supplier-api** (3★) → llm=**spec/docs** (c=0.8) — Primary content is API definitions, sandbox, and SDK for external suppliers
  `API Definitions, Sandbox and SDK for the NHS Notify Supplier API`
- **NeatGuyCoding/spring-io** (1★) → llm=**tangential** (c=0.8) — Conference notes and summaries, not an actual service or spec
  `spring io conference`
- **OpenDonationAssistant/docs** (0★) → llm=**spec/docs** (c=0.8) — Documentation site using Mintlify, not runnable software
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **hahnbeelee/docs-michal** (1★) → llm=**spec/docs** (c=0.8) — Mintlify starter kit, documentation only
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **ppzxc/relaybox** (0★) → llm=**product** (c=0.8) — Deployable relay hub with protocol parsing and message routing
  `English 한국어 relaybox A generic relay hub: receives any inbound protocol/format, applies CEL/Expr expression based filter, transform, and rou`
- **AbhishekCS3459/URL-Shortner-using-GRPC** (0★) → llm=**demo/fixture** (c=0.78) — Student project documenting AsyncAPI 3.0.0 spec for URL shortener
  `This is a url service which uses grpc  for communicating to the url generator service which I have deployed over aws`
- **E2RD0/digital-resources-transcription-service** (0★) → llm=**product** (c=0.78) — Live Whisper-as-a-Service with email delivery and editor UI
  `WaaS Whisper as a Service GUI and API for OpenAI Whisper No video support What is Jojo? Jojo is a GUI for upload and transcribe a audio or v`
- **GopiR17/backstage-prod** (0★) → llm=**product** (c=0.78) — Production Backstage developer portal deployment
  `Backstage English \ 한국어 \ 中文版 What is Backstage? Backstage is an open source framework for building developer portals. Powered by a centrali`
- **Zenika/kafka-schema-registry-publish** (0★) → llm=**demo/fixture** (c=0.78) — Best-practices demo for publishing schemas via CI/CD
  `Publish schemas to your schemas registry using CI-CD`
- **arc-framework/arc-platform** (0★) → llm=**product** (c=0.78) — Production AI agent orchestration platform with event-driven services
  `The official production monorepo for A.R.C. Houses the "Brain" (Python/LangGraph), Voice services, and OCI-compliant Docker infrastructure. `
- **davidB/sandbox_cdevents_spec** (0★) → llm=**demo/fixture** (c=0.78) — Sandbox exploration of cdevents spec formats
  `exploration of other way to define cdevents (and to generate doc, sdk,...)`
- **ff-fab/cosalette-apps** (1★) → llm=**product** (c=0.78) — Deployable smart home IoT bridge applications
  `Monorepo for cosalette based smart home apps.`
- **AcidicSoil/lms-llmsTxt** (1★) → llm=**tangential** (c=0.75) — LM Studio llms.txt generator, unrelated to AsyncAPI
  `LM-Studio llms.txt generator using DSPy framework`
- **BidnessForB/oas-converter-lambda** (0★) → llm=**tangential** (c=0.75) — OAS 2→3 converter lambda; AsyncAPI not its focus
  `Lambda function to convert API Definitions (schemas) from OAS 2.0 -> OAS 3.0`
- **OKArc/backstage** (0★) → llm=**product** (c=0.75) — Fork of Backstage, a real deployable developer portal platform
  `Backstage English \ 한국어 \ 中文版 What is Backstage? Backstage is an open source framework for building developer portals. Powered by a centrali`
- **Sovereign-Labs/sovereign-sdk** (476★) → llm=**tangential** (c=0.75) — Blockchain rollup SDK; AsyncAPI mention likely incidental
  `A flexible toolkit for building real-time blockchains`
- **saujasn/accelerator** (0★) → llm=**product** (c=0.75) — Deployable multi-service application generating code from AsyncAPI spec
  `Accelerator Project Overview & Architecture 📋 See PIPELINE.md for the data flow architecture and payload schemas. Available Commands task ve`
- **worried-networking/uptrakit** (0★) → llm=**product** (c=0.75) — Self-hosted deployable update-tracking service for homelabs
  `Your homelab’s little helper for tracking and applying updates.`
- **AcidicSoil/DSPyTeach** (1★) → llm=**tangential** (c=0.72) — DSPy CLI analyzer tool, no meaningful AsyncAPI usage
  `dspyteach – DSPy File Teaching Analyzer What it does dspyteach is a Python CLI with two top level workflows: dspyteach analyze ... for file `
- **IMAGINARY/track-n-truck** (0★) → llm=**product** (c=0.72) — Deployable game application with event-driven communication
  `A game about Communication & Coordination.`
- **cidverse/repoanalyzer** (1★) → llm=**tangential** (c=0.72) — Repo scanner library; AsyncAPI detection incidental
  `a go library to analyze a project directory to determinate all modules / languages / build-systems used`
- **dcSpark/sovereign-sdk** (1★) → llm=**tangential** (c=0.72) — Blockchain rollup toolkit; no AsyncAPI connection visible
  `A flexible toolkit for building real-time blockchains`
- **ekidenfi/ekiden-docs** (2★) → llm=**spec/docs** (c=0.72) — Documentation site for ekiden platform using Mintlify
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **gonewton/newton** (0★) → llm=**product** (c=0.72) — Deployable CLI for workflow automation and orchestration
  `Newton`
- **hotcode-dev/zerohub** (0★) → llm=**product** (c=0.72) — Deployable open-source WebRTC signaling server
  `An open-source WebRTC signaling server`
- **jacekzwpl/docueye** (18★) → llm=**product** (c=0.72) — Deployable architecture visualization tool with product page
  `DocuEye is a tool that lets You visualize views and documentation created using Structurizr DSL`
- **neosun100/VibeVoice** (2★) → llm=**product** (c=0.72) — Deployable real-time TTS streaming application framework
  `Open-Source Frontier Voice AI - Real-time Text-to-Speech with Docker support`
- **rbaxim/MOP** (0★) → llm=**product** (c=0.72) — Deployable stdio-to-HTTP bridge service with session management
  `A stdio ↔ HTTP(s) bridge`
- **vivekjava/Spring-Boot-Rest** (0★) → llm=**product** (c=0.72) — Deployable Spring Boot reporting service using AsyncAPI
  `Standard service with low code and no code`
- **daksh0702/first-backstage-app** (0★) → llm=**demo/fixture** (c=0.7) — 'first-backstage-app' name signals learning/demo project
  `Backstage English \ 한국어 \ 中文版 What is Backstage? Backstage is an open source framework for building developer portals. Powered by a centrali`
- **knowmadmood-poc-rhdevhub/backstage** (0★) → llm=**demo/fixture** (c=0.7) — POC org name; Backstage proof-of-concept deployment
  `Backstage English \ 한국어 \ 中文版 What is Backstage? Backstage is an open source framework for building developer portals. Powered by a centrali`
- **maxkrv/uchat** (4★) → llm=**product** (c=0.68) — Chat application in C with WebSocket and SQLite
  `Chat application`
- **certifieddata/certifieddata-agent-commerce-public** (1★) → llm=**spec/docs** (c=0.67) — Public API contracts, event schemas, and SDK for payments service
  `Public API, SDKs, schemas, event contracts, and examples for CertifiedData Payments — a machine-readable payments and provenance layer for A`
- **RafaelAlmeida00/Plant-Simulador-Huggy** (0★) → llm=**demo/fixture** (c=0.65) — Simulator on HuggingFace, minimal info suggests demo
  `license: mit title: Simulator Plant sdk: docker emoji: 🚀 colorFrom: blue colorTo: green short description: Simulator Plant`
- **aperim/production-city-web** (0★) → llm=**product** (c=0.65) — Production City web application monorepo foundation
  `Production City web application`
- **dalsgaard/account-service** (0★) → llm=**demo/fixture** (c=0.65) — Described as blank CDK template project
  `Welcome to your CDK TypeScript project This is a blank project for CDK development with TypeScript. The cdk.json file tells the CDK Toolkit `
- **donbagger/documentation** (0★) → llm=**demo/fixture** (c=0.65) — Mintlify starter kit boilerplate, not a real service
  `Mintlify Starter Kit Click on Use this template to copy the Mintlify starter kit. The starter kit contains examples including Guide pages Na`
- **allofmeng/streamline_project** (9★) → llm=**product** (c=0.62) — Real web UI application for Decent Espresso DE1 IoT device
  `Streamline.js A modern web UI skin for the Decent Espresso DE1, built on top of Streamline Bridge (reaprime). This is a full rewrite of the `
- **fredabila/oahl** (6★) → llm=**product** (c=0.62) — Deployable framework exposing hardware APIs to AI agents
  `Open Agent Hardware Layer is an open-source framework for exposing real hardware capabilities to AI agents through standardized APIs.`
- **openagents-org/openagents** (3737★) → llm=**product** (c=0.62) — Deployable AI agent collaboration platform/workspace
  `OpenAgents - AI Agent Networks for Open Collaboration`
- **JannikAlx/kafkaProducer** (0★) → llm=**tangential** (c=0.6) — Kafka producer app; no AsyncAPI mention in available text
  `Kafka Producer with Bundled Map Configuration Overview This project now supports both bundled and custom map configurations: 1. Bundled Map `
- **jason931225/oyatie** (0★) → llm=**tangential** (c=0.6) — AI agent-oriented repo; AsyncAPI mentioned incidentally in specs
  `Oyatie WIP`
- **chem-gl/chemistry-apps** (0★) → llm=**product** (c=0.58) — Real Django-based chemistry apps with async job orchestration
  `Apps de quimica de uso general`
- **Itshalffull/Concept-Oriented-Programming-Framework** (0★) → llm=**uncategorized** (c=0.55) — No readme; description too vague to classify
  `A concept first, spec first, multi language programming framework`
- **acvigue/casa-bonita** (0★) → llm=**product** (c=0.55) — Likely smart-home Nuxt app; AsyncAPI role unclear from readme
  `Nuxt Minimal Starter Look at the Nuxt documentation to learn more. Setup Make sure to install dependencies: bash npm npm install pnpm pnpm i`
- **Matusko/flea** (0★) → llm=**uncategorized** (c=0.5) — Only Nx workspace boilerplate readme, no domain context
  `Flea ✨ This workspace has been generated by Nx, a Smart, fast and extensible build system. ✨ Generate code If you happen to use Nx plugins, `