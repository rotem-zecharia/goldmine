# micro/go-micro

A Go agent harness and service framework

## features

A harness is the runtime around an agent: the tools it can call, the memory it keeps, the guardrails that bound it, the workflows that trigger it, the services it depends on, and the protocols other agents use to reach it. 

Go Micro gives you the harness as Go code. Build an agent and it gets a model, memory, tools, planning, delegation, guardrails, and service discovery; it is reachable over [MCP](https://modelcontextprotocol.io/) and [A2A](https://a2a-protocol.org). Write services and every endpoint becomes an AI-callable tool. Orchestrate the deterministic parts with durable flows. Agents, services, and flows share one runtime because an agent is a distributed system, and building one is building a service.

## installation

Install the CLI:

```bash

## tools

Scaffold a service, run it, call it:

```bash
micro new helloworld
cd helloworld
micro run
```

Prefer Docker? The `micro` image (Docker Hub `micro/micro` or GitHub Container Registry `ghcr.io/micro/go-micro`) bundles the CLI and its runtime dependencies:

```bash
docker pull micro/micro:latest          # or ghcr.io/micro/go-micro:latest
docker run --rm -it micro/micro new helloworld
docker run --rm -it --network host -v "$(pwd)":/micro/helloworld micro/micro run
```

Then in another terminal:

```bash
curl -X POST http://localhost:8080/api/helloworld/Helloworld.Call \
  -H 'Content-Type: application/json' -d '{"name":"World"}'
```

This install → scaffold → run → call path is covered by no-secret CI harnesses. To
verify just the local installer and first-run CLI boundaries without network
access or provider keys, use:

```bash
make install-smoke
```

To verify the focused CLI inner-loop contract — scaffold → run/chat/inspect → deploy dry-run — use:

```bash
make inner-loop
```

To run only the ordered [0→hero services → agents → workflows transcript](internal/website/docs/guides/zero-to-hero.md) that CI guards, use:

```bash
make zero-to-hero-transcript
```

To run the broader local contract (including that transcript, chat/inspect CLI boundaries, and deploy dry-run), use:

```bash
make harness
```

## configuration

micro mcp serve --x402_config x402.json
```

See the [Payments (x402) guide](internal/website/docs/guides/x402-payments.md).
