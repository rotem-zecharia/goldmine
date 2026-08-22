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
# 1. Start MockServer
docker run -d --rm -p 1080:1080 mockserver/mockserver

# 2. Mock an endpoint: GET /hello -> 200 "Hello World"
#    (MockServer exposes a REST control plane on the same port)
curl -X PUT http://localhost:1080/mockserver/expectation \
  -H 'Content-Type: application/json' \
  -d '{
        "httpRequest":  { "method": "GET", "path": "/hello" },
        "httpResponse": { "statusCode": 200, "body": "Hello World" }
      }'

# 3. Call your mock
curl http://localhost:1080/hello
# -> Hello World
```

…or, on macOS / Linux, install it with [Homebrew](https://brew.sh/) and run the `mockserver` command directly:

```bash
brew install mockserver
mockserver run --port 1080
```

#### One-command recipes

For common end-to-end setups, the [`examples/docker-compose`](examples/docker-compose) recipes are a single `docker compose up` each — mock from an OpenAPI spec, a record/replay proxy, a contract-validating proxy, or a chaos proxy:

```bash
cd examples/docker-compose/mock-from-openapi
docker compose up
curl http://localhost:1080/pets
```

The same can be done from any client library or the dashboard at <http://localhost:1080/mockserver/dashboard>. For more configuration options see the [Docker documentation](https://www.mock-server.com/where/docker.html).

For every way to run MockServer yourself — Docker, docker-compose recipes, the `mockserver` CLI, the JVM-less binary bundle, Helm/Kubernetes, the JAR, and Testcontainers — see the [Self-Hosting MockServer guide](https://www.mock-server.com/mock_server/self_hosting_mockserver.html).

#### Drive it from Postman or Bruno

Explore MockServer's REST control plane from an API client — create expectations, verify requests, and inspect recorded traffic:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/3256712-63a2d67a-46d6-41fd-a544-0535e7393e7d?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D3256712-63a2d67a-46d6-41fd-a544-0535e7393e7d%26entityType%3Dcollection%26workspaceId%3D1739eeee-5da1-4112-86a7-b6c094f2b527)

- **Postman** — click the button above, or import [`examples/postman`](examples/postman) ([guide](https://www.mock-server.com/where/postman.html)).
- **Bruno** (open-source, git-native) — open [`examples/bruno`](examples/bruno) in [Bruno](https://www.usebruno.com/) via **Open Collection** ([guide](https://www.mock-server.com/where/bruno.html)).

### Documentation

For usage guide please see: [www.mock-server.com](https://www.mock-server.com/)

### Developer Documentation

Architecture, code structure, infrastructure, and operations documentation is available in the [docs/](docs/README.md) directory.

### AI Integration

MockServer includes a built-in [MCP](https://modelcontextprotocol.io) server for AI coding assistant integration at `/mockserver/mcp`. See [llms.txt](https://www.mock-server.com/llms.txt) and [AI Integration docs](https://www.mock-server.com/mock_server/ai_mcp_setup.html).

### Change Log

Please see: [Change Log](https://github.com/mock-server/mockserver-monorepo/blob/master/changelog.md)

### Community

<table>
    <tr>
        <td>Discussions</td>
        <td><a href="https://github.com/mock-server/mockserver-monorepo/discussions"><img height="20px" src="https://mock-server.com/images/GitHub_Logo-md.png" alt="GitHub Discussions"></a></td>
    </tr>
    <tr>
        <td>Issues, Bugs &amp; Feature Requests</td>
        <td><a href="https://github.com/mock-server/mockserver-monorepo/issues"><img height="20px" src="https://mock-server.com/images/GitHub_Logo-md.png" alt="GitHub Issues"></a></td>
    </tr>
    <tr>
        <td>Roadmap</td>
        <td><a href="https://github.com/orgs/mock-server/projects/1"><img height="20px" src="https://mock-server.com/images/GitHub_Logo-md.png" alt="GitHub Project"></a></td>
    </tr>
    <tr>
        <td>Security</td>
        <td><a href="https://github.com/mock-server/mock

## requirements

**Runtime:** MockServer 6.x requires **Java 17+**. The minimum was raised from Java 11 as part of the Jakarta EE 10 / Spring 7 platform modernisation — see the [Java 17 / Jakarta upgrade guide](docs/operations/migration-java17-jakarta.md). If you are still on Java 11, pin to the `5.15.x` line (no longer receiving security updates). The official Docker image already bundles a Java 17 runtime.

**Building from source:** requires **JDK 17+**; the produced bytecode targets Java 17.

**Security Note:** MockServer is a **development and testing tool only**. See [SECURITY.md](SECURITY.md) for important security considerations.

### Versions

##### Maven Central [![mockserver](https://img.shields.io/maven-central/v/org.mock-server/mockserver-netty.svg)](https://central.sonatype.com/search?q=g:org.mock-server)

Maven Central contains the following MockServer artifacts under the `org.mock-server` groupId. Every artifact ships in two forms — `-no-dependencies` (shaded, zero transitive deps, **recommended**) and the plain form (transitive deps declared in the POM, for the rare case where you need to override versions yourself).

**Server:**
* [mockserver-netty-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-netty-no-dependencies) / [mockserver-netty](https://central.sonatype.com/artifact/org.mock-server/mockserver-netty) — Netty-based HTTP(S) mock + proxy server (embed in tests or run standalone)
* [mockserver-war](https://central.sonatype.com/artifact/org.mock-server/mockserver-war) — deployable WAR for hosting MockServer in a servlet container (mock mode)
* [mockserver-proxy-war](https://central.sonatype.com/artifact/org.mock-server/mockserver-proxy-war) — deployable WAR for hosting MockServer in a servlet container (proxy mode)

**Java client:**
* [mockserver-client-java-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-client-java-no-dependencies) / [mockserver-client-java](https://central.sonatype.com/artifact/org.mock-server/mockserver-client-java) — Java client for the MockServer REST API

**Test framework integrations:**
* [mockserver-junit-rule-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-junit-rule-no-dependencies) / [mockserver-junit-rule](https://central.sonatype.com/artifact/org.mock-server/mockserver-junit-rule) — JUnit 4 `@Rule`
* [mockserver-junit-jupiter-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-junit-jupiter-no-dependencies) / [mockserver-junit-jupiter](https://central.sonatype.com/artifact/org.mock-server/mockserver-junit-jupiter) — JUnit 5 extension (`@MockServerSettings`, `@MockServerTest`)
* [mockserver-spring-test-listener-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-spring-test-listener-no-dependencies) / [mockserver-spring-test-listener](https://central.sonatype.com/artifact/org.mock-server/mockserver-spring-test-listener) — Spring `TestExecutionListener`
* [mockserver-spring-boot-starter](https://central.sonatype.com/artifact/org.mock-server/mockserver-spring-boot-starter) — Spring Boot auto-configuration; set `mockserver.enabled=true` to start MockServer and expose a `MockServerClient` bean (dev/test)
* [mockserver-integration-testing-no-dependencies](https://central.sonatype.com/artifact/org.mock-server/mockserver-integration-testing-no-dependencies) / [mockserver-integration-testing](https://central.sonatype.com/artifact/org.mock-server/mockserver-integration-testing) — shared integration-test helpers

**Build-tool plugin:**
* [mockserver-maven-plugin](https://central.sonatype.com/artifact/org.mock-server/mockserver-maven-plugin) — Maven plugin to start, stop, and fork MockServer during the build lifecycle

> **Tip:** The `-no-dependencies` artifacts bundle all dependencies into a single JAR with packages relocated under `shaded_package.*`, so they declare zero transitive dependencies. This avoids classpath conflicts with versions of
