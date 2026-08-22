# micro/go-micro

A Go agent harness and service framework

## features

A harness is the runtime around an agent: the tools it can call, the memory it keeps, the guardrails that bound it, the workflows that trigger it, the services it depends on, and the protocols other agents use to reach it. 

Go Micro gives you the harness as Go code. Build an agent and it gets a model, memory, tools, planning, delegation, guardrails, and service discovery; it is reachable over [MCP](https://modelcontextprotocol.io/) and [A2A](https://a2a-protocol.org). Write services and every endpoint becomes an AI-callable tool. Orchestrate the deterministic parts with durable flows. Agents, services, and flows share one runtime because an agent is a distributed system, and building one is building a service.

## Sponsors

<a href="https://go-micro.dev/blog/2026/03/04/building-the-ai-native-future-of-go-micro-with-claude.html"><img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Anthropic_logo.svg" height="26" /></a>
&nbsp;&nbsp;
<a href="https://go-micro.dev/blog/2026/06/23/go-micro-joins-openai-s-codex-for-open-source.html"><img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" height="26" /></a>
&nbsp;&nbsp;
<a href="https://go-micro.dev/blog/2026/05/28/atlas-cloud-sponsors-go-micro-300-ai-models-one-integration.html"><img src="https://www.atlascloud.ai/logo.svg" height="26" /></a>

**Want to support Go Micro and see your logo here?** [Become a sponsor](https://discord.gg/G8Gk5j3uXr) — reach out on Discord.

## Community

Questions, ideas, or just want to build alongside us? [Join the Discord](https://discord.gg/G8Gk5j3uXr).

## Commercial Support

Running Go Micro in production, or building on it and want help? Paid **support, consulting, training, and retainers** are available directly from the maintainer — and they're what keep the project maintained. See [**Support**](SUPPORT.md) for the tiers, or [open a request](https://github.com/micro/go-micro/issues/new?template=commercial_support.md).

## Contents

- [Quick Start](#quick-start)
  - [First agent on-ramp](#first-agent-on-ramp)
- [Why an Agent Harness](#why-an-agent-harness)
- [Writing Services](#writing-services)
- [Building Agents](#building-agents) — [Plan & Delegate](#plan--delegate), [Pluggable](#batteries-included-pluggable), [Paid tools (x402)](#paid-tools-x402), [A2A](#reachable-by-other-agents-a2a)
- [Features](#features)
- [CLI](#cli)
- [Autonomous improvement loop](#autonomous-improvement-loop)
- [Multi-Service Projects](#multi-service-projects)
- [Data Model](#data-model)
- [AI Providers](#ai-providers)
- [Examples](#examples)
- [Commercial Support](#commercial-support)
- [Docs](#docs)

## installation

Install the CLI:

```bash
# Binary (no Go required)
curl -fsSL https://go-micro.dev/install.sh | sh

# Or with Go
go install go-micro.dev/v6/cmd/micro@latest
```

If install or `PATH` checks fail, use the [install troubleshooting guide](internal/website/docs/guides/install-troubleshooting.md) before scaffolding your first service.

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

### First agent on-ramp

After install and the first `micro new`/`micro run` smoke check, take the
walkable agent path in this order:

1. [Install troubleshooting](internal/website/docs/guides/install-troubleshooting.md) — verify the binary installer or `go install`, `PATH`, `micro --version`, and the no-secret smoke path before agent work.

Run `make docs-wayfinding` to verify the focused no-secret docs/CLI contract that keeps these README and website commands aligned with the installed CLI.

2. `micro agent demo` — print the provider-free first-agent demo command and next docs steps from the installed CLI.
3. `micro agent quickcheck` (or `micro agent debug`) — when scaffold → run → chat → inspect stalls, print the short recovery map before you dive into the full debugging guide.
4. `micro examples` — print the maintained provider-free runnable examples in copy/paste order.
5. `micro zero-to-hero` — print the maintained one-command no-secret lifecycle harness and runnable examples.
6. [Examples wayfinding index](examples/INDEX.md) — choose the smallest no-secret first-agent, maintained [0→hero support reference](examples/support/), and next interop examples from one map.
7. [Smallest first-agent example](examples/first-agent/) — run one service-backed agent with a mock model and no provider key.
8. [No-secret first-agent transcript](internal/website/docs/guides/no-secret-first-agent.md) — run the
   maintained support agent with a mock model and see services → agents → workflows succeed without a key.
9. [Your First Agent](internal/website/docs/guides/your-first-agent.md) — build a
   service-backed agent and talk to it with `micro chat`.
10. [Debugging your agent](internal/website/docs/guides/debugging-agents.md) — use
   `micro agent preflight` before `micro run`, `micro agent doctor` after `micro run`,
   then `micro chat` and `micro inspect agent <name>` to recover run history, memory,
   and provider checks when the first conversation does something unexpected.
11. [0→hero Reference](internal/website/docs/guides/zero-to-hero.md) — complete the
   services → agents → workflows loop with scaffold, run, chat, inspect, flow
   history, and deploy dry-run commands that match the maintained harness.

### Autonomous improvement loop

Want the same services → agents → workflows lifecycle applied to your
repository? `micro loop` scaffolds the autonomous improvement loop used by Go
Micro itself: a North Star, ranked issue queue, role prompts, GitHub Actions
workflows, and verification for CI-gated PRs.

```bash
micro loop init --roles all
micro loop verify
```

Before turning on the schedule, configure a dispatch token such as
`CODEX_

## configuration

micro mcp serve --x402_config x402.json
```

See the [Payments (x402) guide](internal/website/docs/guides/x402-payments.md).

### Reachable by other agents (A2A)

Within a Go Micro system, agents reach each other over RPC. To make them reachable by agents on *other* frameworks, Go Micro speaks the [Agent2Agent (A2A) protocol](https://a2a-protocol.org). The A2A gateway discovers your agents from the registry, generates an Agent Card for each from its metadata — the same way the MCP gateway derives tools from service endpoints — and translates incoming A2A tasks to the agent's `Agent.Chat` RPC. No per-agent code: register an agent and it's reachable over A2A.

```bash
micro a2a serve --address :4000    # gateway: expose every registered agent over A2A
micro a2a list                     # agents and their Agent Card URLs
```

Or skip the gateway entirely — an agent can serve its own A2A endpoint directly, handling tasks in-process:

```go
micro.NewAgent("task-mgr", micro.AgentServices("task"), micro.AgentA2A(":4000"))
```

It works both ways. To call an agent on another framework, an `a2a.Client` is wired into the two places that hand off work: `flow.A2A(url)` as a workflow step (the cross-framework `Dispatch`), and `delegate` to an `http(s)` URL from inside an agent.

MCP exposes your services as tools; A2A exposes your agents as agents. See the [A2A guide](internal/website/docs/guides/a2a-protocol.md).
