# sandbaseai/sandbase-harness

Local-first AI agent runtime with sandboxed sessions, MCP tools, memory, credentials, audit/replay, and a built-in console. Run OpenAI, Anthropic, MiniMax, DeepSeek V4, and OpenAI-compatible models on

## features

- Claude Managed Agents-style `/v1` API and local Console
- SQLite-backed agents, sessions, environments, credential vaults, memory
  stores, files, skills, and API keys — SQLite metadata by default
- local file/skill bytes stored in the workspace state directory
- Resumable Server-Sent Events for session replay and debugging
- One active model provider boundary configured through Settings V2
- Sandbox backends: local process, Docker (per-session containers), Kubernetes
  (kubectl exec/cp), self-hosted worker queue
- Settings V2: one workspace model vendor, loop engine, storage, memory,
  sandbox — with validation, form/JSON modes, and restart flow
- MCP toolsets, permission policies, built-in tools, and skill packages
- DeepSeek Harness bridge over MCP stdio for agents, sessions, streamed turns,
  artifacts, and cancellation
- TypeScript SDK at `managed-agents/sdk`
- Release gate: `npm run release:check`

## requirements

- Node.js 22+
- npm 10+
- A model provider API key (OpenAI, Anthropic, MiniMax, or an OpenAI-compatible endpoint)
- Docker (optional, for Docker-backed sandboxes)

## installation

```bash
git clone --branch v0.3.7 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build
mkdir ../my-agents && cd ../my-agents
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

Open `http://127.0.0.1:3000/dashboard`, go to **Settings > Models**, paste your
API key, and you're running.

The unscoped `managed-agents` name on npm is not this project. Until an
official scoped package is announced in this repository, install only from the
tagged GitHub source release shown above. Do not run `npx managed-agents` or
`npm install managed-agents`.

The six-tool MCP bridge is published as a multi-architecture OCI image. Start
the Harness API, then add this stdio command to an MCP client:

```bash
docker pull ghcr.io/sandbaseai/sandbase-harness-mcp:0.3.7
docker run --rm -i \
  -e MANAGED_AGENTS_URL=http://host.docker.internal:3000 \
  ghcr.io/sandbaseai/sandbase-harness-mcp:0.3.7
```

For an authenticated remote runtime, also pass `MANAGED_AGENTS_API_KEY`. The
container image contains only the MCP bridge; agent sessions and sandbox work
remain in the connected Harness runtime. Every release image is built from the
matching Git tag for `linux/amd64` and `linux/arm64`, includes OCI source and
MCP ownership metadata, and receives a GitHub build-provenance attestation.

## configuration

`.managed-agents/config.yaml`:

```yaml
model:
  provider: openai
  api_key: ${OPENAI_API_KEY}

storage:
  metadata: { provider: sqlite, options: {} }
  artifacts: { provider: local, options: { base_path: files } }
```

Agents pick concrete model IDs (`gpt-4o`, `claude-sonnet-4-20250514`,
`openai/gpt-5.5`). The workspace config only says how to reach the model
service.

For DeepSeek V4 Pro/Flash configuration, including maximum reasoning effort,
see [DeepSeek V4](docs/deepseek-v4.md).

For first-class MiniMax configuration, regional endpoints, and the supported
MiniMax-M3 and MiniMax-M2.7 model IDs, see [MiniMax](docs/minimax.md).

## tools

Create an agent:

```bash
curl -X POST http://127.0.0.1:3000/v1/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Incident commander",
    "model": "gpt-4o",
    "system": "You are an on-call incident commander.",
    "tools": [{ "type": "agent_toolset_20260401" }]
  }'
```

Create an environment (local sandbox):

```bash
curl -X POST http://127.0.0.1:3000/v1/environments \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Default local",
    "config": { "hosting_type": "local", "sandbox_provider": "local" }
  }'
```

Create a Docker-isolated environment:

```bash
curl -X POST http://127.0.0.1:3000/v1/environments \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Docker sandbox",
    "config": {
      "sandbox_provider": "docker",
      "image": "node:22-slim",
      "resources": { "memory": "1g", "cpu": 1 }
    }
  }'
```

Start a session:

```bash
curl -X POST http://127.0.0.1:3000/v1/sessions \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "agent_...",
    "environment_id": "env_...",
    "title": "Triage SENTRY-123"
  }'
```

Send a message:

```bash
curl -X POST http://127.0.0.1:3000/v1/sessions/SESSION_ID/messages \
  -H "Content-Type: application/json" \
  -d '{ "content": "Investigate the alert." }'
```

Resume the event stream:

```bash
curl -N http://127.0.0.1:3000/v1/sessions/SESSION_ID/events/stream \
  -H "Last-Event-ID: 42"
```
