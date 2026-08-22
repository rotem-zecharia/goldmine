# CodeSoul-co/Hypha

Harness-oriented agent system framework for production-grade LLM agent applications

## features

| Area               | Included runtime capability                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime            | ReAct + FSM, durable session commands, bounded continuation, timers, leases, fencing, cancellation, recovery workers, human review, replay, audit, and regression projections.                           |
| Domain             | YAML/JSON/TypeScript Domain Packs, runtime validation, overlays, registry, deterministic compiler, dependency snapshots, and Agent patches.                                                              |
| Memory             | Hypha Native Memory, local Native Lite, self-hosted Mem0 OSS, Mem0 Platform, and Vertex AI Memory Bank adapters behind one governed contract.                                                            |
| Tools and MCP      | Local, HTTP, plugin, mock, and MCP adapters through one governed invocation path with capability snapshots and drift control.                                                                            |
| Skills and prompts | Built-in, filesystem, package, and signed remote Skill registries; progressive loading; versioned prompt references and templates.                                                                       |
| Execution          | Provider-neutral Workspace, Sandbox, Command, Artifact, Store, lease, recovery, and cache contracts with local-process, Docker, remote HTTP, SQLite, PostgreSQL, local-file, and S3-compatible adapters. |
| Cache              | Serving Cache, event-derived WorkCache, Thinking Cache, typed semantic cache trees, capability-result caches, Memory/context projections, Prefix/KV reuse, scoped validity, and invalidation.            |
| Surfaces           | Express API server and an example CLI that consume the same framework runtime.                                                                                                                           |

## requirements

- Node.js 22 or newer
- npm
- MongoDB and Redis for the bundled API server
- At least one configured model provider or a reachable local model endpoint

## installation

```bash
git clone https://github.com/CodeSoul-co/Hypha.git
cd Hypha
npm ci
cp .env.example .env
```

Keep product configuration out of tracked templates. Set `HYPHA_CONFIG_PATH` to a user-owned YAML
overlay; see [Upgrading](UPGRADING.md) for the conflict-free update layout.

For a disposable local MongoDB and Redis environment, you may use containers:

```bash
docker run -d --name hypha-mongodb -p 27017:27017 mongo:8
docker run -d --name hypha-redis -p 6379:6379 redis:7-alpine
```

You can instead set `MONGODB_URI` and `REDIS_URL` to self-hosted or managed services.

## configuration

Edit `.env`. Keep credentials out of `config.yaml` and source control.

```bash
HYPHA_OWNER_EMAIL=owner@example.com
HYPHA_OWNER_PASSWORD=replace-with-a-private-password
JWT_SECRET=replace-with-at-least-32-random-characters

HYPHA_LLM_DEFAULT_PROVIDER=openai
HYPHA_LLM_DEFAULT_MODEL=gpt-4o-mini
OPENAI_API_KEY=your-provider-key
```

The default deployment mode is single-user. Registration remains disabled and the configured owner
is created during startup. Internal data access still retains user, Session, Run, Workspace, and
tenant boundaries.

### 3. Start and verify the server

```bash
npm run dev
```

In another terminal:

```bash
curl -fsS http://127.0.0.1:3000/api/v1/health
curl -fsS http://127.0.0.1:3000/api/v1/ready
```

`/health` is process liveness. `/ready` is the traffic gate: it returns a failure status until
storage, the selected model provider, Memory, the canonical Runtime graph, and required workers are
ready. The route index is available at `http://127.0.0.1:3000/api/v1/docs`.

### 4. Use the CLI

```bash
npm run cli -- login --email owner@example.com
npm run cli -- chat "Explain the active runtime" --stream
npm run cli -- tools
npm run cli -- skills
npm run cli -- workflows
```

The CLI stores its endpoint configuration and JWT under `~/.hypha` by default. Set
`HYPHA_BASE_URL` and `HYPHA_HOME` to use another server or an isolated client profile.

## Develop an agent with a DomainPack

Domain Packs are the supported product-integration boundary. Product-specific tasks, prompts,
workflows, rules, and capability selections belong in a Domain Pack or product application—not in
`@codesoul-co/hypha-core`, `@codesoul-co/hypha-kernel`, or the generic Runtime.

For an application that consumes a versioned npm release, including separate Prompt, Skill, Tool,
policy, contract test, and HTTP Run submission, see the
[`release-agent` example](examples/release-agent/README.md).

### 1. Declare the domain

Start from [`configs/domain-packs/minimal.domain.yaml`](configs/domain-packs/minimal.domain.yaml).
A production Domain Pack normally defines:

| Declaration                              | What it controls                                                                                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taskSchemas`                            | Accepted task types, input schemas, output-contract references, and default workflows.                                                                                                                                          |
| `outputContracts`                        | Machine-verifiable final output schemas.                                                                                                                                                                                        |
| `sessionProfiles`                        | Default metadata and Memory, Context, Reasoning, Tool, MCP, Skill, and Policy profile references.                                                                                                                               |
| `workflows`                              | Product stages, guards, retry/timeout intent, human review, state-scoped capabilities, and topology evidence. ReAct Runs retain the protected Harness FSM; custom FSM Runs may use a separately validated application topology. |
| `tools`, `toolProfiles`                  | Stable Tool contracts and the profiles allowed to bind them to executable adapters.                                                                                                                                             |
| `mcpProfiles`      

## tools

- Tool definitions and trusted adapter bindings live in `config.yaml`, `configs/tools.yaml`, and the
  application composition layer.
- Local MCP servers use a command and argument vector; remote servers use an endpoint plus a Secret
  reference. Newly discovered capability revisions must satisfy trust and approval policy.
- Skills can come from built-ins, `~/.hypha/skills`, package registries, or an explicitly enabled
  signed remote registry. Required Skills fail startup or context construction when unavailable.
- Prompt templates live under `apps/server/src/prompts`; Domain Packs reference versioned prompt ids
  rather than embedding deployment-specific prompt loading logic in core.

The Server includes governed `utility.json`, `utility.text`, `utility.hash`, filesystem, search, and
real local stdio MCP paths. Use [`Tool adapters`](docs/guides/tool-adapters.md),
[`Tool and MCP security`](docs/guides/tool-mcp-security.md), and the
[`HTTP API`](docs/api/http.md) for configuration and invocation contracts.

## Runtime, execution, and recovery

The Express Server composes the canonical Event authority and durable execution graph during
startup. Session-command, ReAct continuation, timer, recovery, and reconciliation workers perform
an initial sweep before readiness. Shutdown drains workers while their providers remain available.

Long-running work progresses in bounded quanta. The next quantum is reconstructed from Events,
checkpoints, Artifacts, capability snapshots, and provider receipts. Recovery uses explicit bounded
retry, reconciliation, fallback, degradation, compensation, human review, quarantine,
cancellation, and failure states; repeatedly entering a loop is not considered progress.

Execution providers are registered explicitly. Local process, Docker, remote sandbox HTTP,
PostgreSQL execution records, and S3-compatible Artifacts are available as adapters, but a
deployment should activate only the providers it trusts and can verify. See
[`Execution architecture`](docs/architecture/execution.md) and
[`Runtime model`](docs/reference/runtime-model.md).

## Cache model

The detailed architecture is summarized in [Cache management and typed cache trees](#cache-management-and-typed-cache-trees).
Operationally:

- **Serving Cache** reuses exact, normalized model responses. Enable it with
  `HYPHA_SERVING_CACHE=memory`, `sqlite`, or `redis`.
- **WorkCache** stores bounded, event-derived projections and semantic cache trees. Use
  `HYPHA_WORKCACHE=off`, `memory`, `sqlite`, or `redis`.
- **Thinking Cache** reuses reasoning nodes, paths, and subgraphs through computation-oriented
  WorkCache projections when the current model, reasoning, prompt, tool-schema, and scope identity
  remain valid.
- **Tool result cache** is opt-in for eligible `none`/`read` calls and requires stable external-state
  evidence for reads.
- **Execution, Memory/context, Prompt-prefix, and Prefix/KV caches** remain subject to their own
  capability, dependency, revision, provenance, and scope checks; deployments may enable only the
  providers they can validate.

All caches are disposable views. A cache miss or cache-provider failure can bypass reuse; a cache hit
cannot authorize a side effect, skip Policy or Approval, fabricate a receipt, advance the FSM, or
replace Event and Artifact evidence. Cache-enabled and cache-disabled execution must preserve the same
source-of-truth semantics.

## HTTP API

The default API prefix is `/api/v1`. Protected routes use
`Authorization: Bearer <jwt>`. Primary surfaces include:

- `/chat` and `/chat/stream` for agent interaction;
- `/runtime/runs/:runId` plus `/events`, `/replay`, `/audit`, and `/regression` projections;
- `/tools`, `/tool-invocations`, `/tool-approvals`, and `/mcp` for governed capabilities;
- `/memory` and `/memory-admin` for scoped Memory operations;
- `/skills`, `/workflows`, `/models`, `/usage`, `/status`, and `/docs`.

See [`docs/api/http.md`](docs/api/http.md) for request and response contracts.

