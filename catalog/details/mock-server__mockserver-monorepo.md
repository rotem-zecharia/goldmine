# mock-server/mockserver-monorepo

MockServer is an HTTP(S) mock server and proxy for testing that lets you mock APIs, inspect and modify live traffic, and inject failures. It supports HTTP/1.1, HTTP/2, gRPC, WebSockets, TCP and more o

## features

- **Mock any API** — HTTP/1.1, HTTPS, HTTP/2, HTTP/3, gRPC, gRPC-Web, JSON-RPC, WebSockets, raw TCP, and message brokers (Kafka, MQTT). Match requests on method, path, query, headers, cookies and body (JSON, XML, JSONPath, XPath, regex, OpenAPI) and return configured responses.
- **Proxy & record** — port forwarding, web (HTTP) proxy, HTTPS tunneling (CONNECT) and SOCKS, with full visibility of even TLS-encrypted traffic.
- **Dynamic responses** — response templating (Velocity, Mustache, JavaScript), class/closure callbacks and webhooks.
- **OpenAPI** — generate expectations directly from an OpenAPI/Swagger specification.
- **Verification** — assert which requests were received, in what order, and how many times.
- **Chaos & resilience testing** — inject latency, dropped/slow connections and failures to test how your system copes with a misbehaving dependency.
- **LLM / AI mocking** — mock chat-completion APIs for OpenAI, Anthropic, Gemini, Bedrock, Azure OpenAI and Ollama (including streaming), plus a built-in MCP server for AI coding assistants.
- **Live dashboard** — watch requests, expectations and logs in real time at `/mockserver/dashboard`.
- **Clients & integrations** — Java, JavaScript/Node, Python and Ruby clients, plus JUnit and Spring support.
- **Run anywhere** — Docker, Helm/Kubernetes, JAR or WAR, with optional clustered state for multi-instance deployments.

See the [changelog](changelog.md) for what has shipped in each version.

## installation

Run MockServer with Docker, then mock an endpoint and call it:

```bash

## requirements

**Runtime:** MockServer 6.x requires **Java 17+**. The minimum was raised from Java 11 as part of the Jakarta EE 10 / Spring 7 platform modernisation — see the [Java 17 / Jakarta upgrade guide](docs/operations/migration-java17-jakarta.md). If you are still on Java 11, pin to the `5.15.x` line (no longer receiving security updates). The official Docker image already bundles a Java 17 runtime.

**Building from source:** requires **JDK 17+**; the produced bytecode targets Java 17.

**Security Note:** MockServer is a **development and testing tool only**. See [SECURITY.md](SECURITY.md) for important security considerations.
