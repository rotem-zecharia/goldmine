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

## Screenshots

| Console overview | Settings | API reference |
| --- | --- | --- |
| ![overview](docs/assets/dashboard-overview.png) | ![settings](docs/assets/dashboard-settings-models.png) | ![api-ref](docs/assets/dashboard-api-reference.png) |

## requirements

- Node.js 22+
- npm 10+
- A model provider API key (OpenAI, Anthropic, MiniMax, or an OpenAI-compatible endpoint)
- Docker (optional, for Docker-backed sandboxes)

## DeepSeek Harness

Run this project as a DSH plugin instead of treating `dsh-plugin` as discovery
metadata only. Install the bundle into a DSH profile, start `managed-agents`,
then boot that profile:

```bash
export MANAGED_AGENTS_URL=http://127.0.0.1:3000
# Run from the sibling my-agents workspace created above.
dsh plugin --profile web add -w ../sandbase-harness
dsh web
```

The profile installs the verified source checkout directly; it does not resolve
the unrelated unscoped npm package. The patch starts the bundled MCP entry over
stdio. DSH can then list agents,
create and run sessions, inspect results and artifacts, and stop work through
native `mcp__sandbase__*` tools. See
[`examples/deepseek-harness`](examples/deepseek-harness/README.md) for the full
tool list and authenticated-runtime configuration.

For a walkthrough that starts with DSH and adds this runtime as a real
third-party plugin, read the
[DeepSeek Harness developer guide](https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/#add-a-real-third-party-runtime-plugin).

Pair the plugin with SandBase Skills to give the same DSH project a portable,
source-verifiable research workflow:

```bash
npx --yes github:sandbaseai/sandbase-skills add multi-source-search
dsh web
```

This installs the complete Skill into `.dsh/skills/multi-source-search`, DSH's
project-scoped discovery directory. It runs from GitHub source and needs no
SandBase account when DSH already provides web/search tools.

For a complete, reproducible workflow that combines the evidence ledger with
sandboxed execution, credentials, audit, and replay, read
[Build an Auditable Research Agent](https://blog.sandbase.ai/auditable-research-agent-evidence-ledger-sandbox-replay/).

New to DSH profiles, plugin composition, tool policy, or session semantics? The
independent [DeepSeek Harness Handbook](https://github.com/sandbaseai/deepseek-harness-handbook)
provides source-backed quickstarts, architecture maps, and troubleshooting for
the runtime layers used by this integration. Start with the local-browser
[Install Doctor](https://sandbaseai.github.io/deepseek-harness-handbook/install-doctor.html)
for installation evidence, or use the
[Failure Router](https://sandbaseai.github.io/deepseek-harness-handbook/diagnose.html)
to identify the first broken runtime boundary.

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

### Portable Agent Plugin

Copilot CLI, VS Code, and other Agent Plugins 1.0 clients can install the same
OCI-backed MCP bridge directly from this repository. Start the Harness API and
Docker first, then expose its URL to the plugin process:

```bash
export MANAGED_AGENTS_URL=http://host.docker.internal:3000
# Optional when the runtime requires authentication:
export MANAGED_AGENTS_API_KEY=your-runtime-key

copilot plugin install sandbaseai/sandbase-harness:agent-plugin
```

The plugin passes these environment variables through to the pinned
`ghcr.io/sandbaseai/sandbase-harness-mcp:0.3.7` image. It does not store a key
in `plugin.json`, `mcp.json`, or the installed plugin files. On Linux, the
plugin's Docker command maps `host.docker.internal` through `host-gateway`.

For development from the latest `main` branch:

```bash
git clone https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness && npm ci && npm run build
cd .. && mkdir my-agents-dev && cd my-agents-dev
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

## Workspace Layout

```text
my-agents/
├── agents/                  # Seed agent definitions (YAML)
│   └── assistant.yaml
├── skills/                  # Seed skill packages
│   └── example-skill/
│       └── SKILL.md
└── .managed-agents/         # Runtime state (gitignored)
    ├── config.yaml          # Workspace configuration
    ├── data.db              # SQLite metadata
    ├── logs/runtime.log
    ├── files/               # Uploaded file bytes
    ├── skills/              # Uploaded skill packages
    ├── snapshots/           # Session workspace snapshots
    └── sandbox/             # Local session sandboxes
```

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

## CLI

```bash
managed-agents init
managed-agents start [--host 127.0.0.1] [--port 3000]
managed-agents list
managed-agents reload
managed-agents chat <agent-id> --message "hello"
managed-agents template list | install <name> | create <name>
```

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

## SDK

```typescript
import { ManagedAgentsClient } from 'managed-agents/sdk';

const client = new ManagedAgentsClient({
  baseUrl: 'http://127.0.0.1:3000',
});

const session = await client.sessions.create({
  agent: 'agent_...',
  environment_id: 'env_...',
});

for await (const event of client.sessions.chat(session.id, 'Hello')) {
  if (event.type === 'agent.message_chunk') {
    process.stdout.write(event.delta ?? '');
  }
}
```

The `/v1` API follows Claude Managed Agents resource shapes, so you can also
point the Anthropic SDK at the local runtime:

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.MANAGED_AGENTS_API_KEY ?? 'local-dev-key',
  baseURL: 'http://127.0.0.1:3000',
});

const session = await client.beta.sessions.create({
  agent: 'agent_...',
  environment_id: 'env_...',
});
```

## Authentication

Open by default. Authentication activates when at least one API key exists:

```bash
