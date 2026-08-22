# dapr/dapr

Dapr is a portable runtime for building distributed applications across cloud and edge, combining event-driven architecture with workflow orchestration.

## features

Modern applications are no longer simple request/response services. They are long-running workflows, AI agents, event-driven pipelines, multi-agent systems, and human-in-the-loop processes — and they must survive failures, maintain state, and communicate securely in production.

Building all of that reliably is hard. Dapr brings proven patterns and battle-tested building blocks together into one consistent programming model, so you don't have to reinvent durability, security, or messaging for every service you ship. You're never exposed to low-level primitives like threading, partitioning, or retry logic — and you can move seamlessly between platforms and backing infrastructure without rewriting your code. Platform teams use Dapr to provide governance and golden paths, while application teams get simple APIs that work the same everywhere.

## tools

Durable execution and AI build on the same proven building blocks that power Dapr microservices. Mix and match what you need:

| API | What it does |
|:----|:-------------|
| **Workflows** | Author long-running, durable workflows and agentic processes as code |
| **Service Invocation** | Reliable, secure service-to-service calls with built-in mTLS, retries, and observability |
| **State Management** | Persist and query state across dozens of stores without coupling to a database |
| **Pub/Sub** | Build event-driven systems on your preferred message broker with at-least-once delivery |
| **Actors** | Build stateful, virtual actor-based applications |
| **Conversation** | Call LLMs through a consistent API, with prompt caching and tool calling |
| **Bindings** | Trigger your code from, and send events to, external systems |
| **Secrets** | Retrieve secrets securely from external secret stores |
| **Configuration** | Read and subscribe to application configuration consistently |
| **Distributed Lock** | Coordinate access to shared resources safely |
| **Cryptography** | Encrypt and decrypt data without exposing keys to your application |
| **Jobs** | Schedule work to run now or in the future |

All APIs are available over HTTP and gRPC, with SDKs for Java, .NET, Go, JavaScript, Python, Rust, C++, and PHP. You benefit from built-in [observability](https://docs.dapr.io/concepts/observability-concept/), reliability, and pluggable, vendor-neutral components for state stores, message brokers, and more across Azure, AWS, and GCP.

## installation

* See the [quickstarts repository](https://github.com/dapr/quickstarts) for code examples that can help you get started with Dapr.
* Explore additional samples in the Dapr [samples repository](https://github.com/dapr/samples).
