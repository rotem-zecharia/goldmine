# heymrun/heym

Build agentic systems. Run them with confidence. Orchestrate agents, automate business processes, inspect every execution, and keep humans in control. Deploy Heym on your own infrastructure.

## features

<div align="center">

<img src="./docs/readme-assets/key-capabilities.svg" width="100%" alt="Animated Heym key capabilities grid"/>

</div>

- **Visual Workflow Editor** — Drag-and-drop canvas powered by Vue Flow with a broad node library
- **AI Assistant** — Describe what you want in natural language (or voice) and the assistant generates and wires nodes on the canvas automatically
- **Chat with Docs** — Ask context-aware questions directly from the documentation header while the current article path is prioritized in the prompt
- **AI Skill Builder** — Create new Agent skills or revise existing ones from a modal chat with live `SKILL.md` and Python file previews
- **LLM & Agent Nodes** — First-class LLM node and a full Agent node with tool calling, canvas node tools, sandboxed Python tools, MCP connections, skills, optional persistent memory (per-node knowledge graph with background extraction), and LLM Batch API mode with live status branches for supported providers
- **Multi-Agent Orchestration** — One agent orchestrates named sub-agents and sub-workflows, all wired visually
- **Human-in-the-Loop (HITL)** — Pause agent execution to request user approval or input before proceeding
- **Guardrails** — Content filtering, NSFW protection, and multilingual safety checks on LLM and Agent nodes
- **Built-In RAG** — Insert documents and run semantic search against managed vector stores (Qdrant or built-in Postgres/pgvector) in two nodes
- **MCP Support** — Connect Agent nodes to any MCP server as a client; expose your workflows as an MCP server for Claude, Cursor, and other clients
- **Portal** — Turn any workflow into a public chat UI at `/chat/{slug}` with streaming responses and file uploads
- **Webhook SSE Streaming** — Generate ready-to-run cURL commands for `/execute` or `/execute/stream`, with per-node start messages and live node event output in the terminal
- **Live Execution Canvas** — Open any running production execution from History or a Kanban card and watch the existing run continue node by node on the animated canvas with incremental Debug logs
- **Data Tables** — Manage structured data directly in the dashboard and reference it from workflows
- **Workflow Analyzer** — Run-aware AI feedback that generates a shared Markdown report with improvement areas, purpose, and step-by-step behavior
- **Workflow-Powered Dashboards** — Build custom chart dashboards where every widget is backed by its own hidden Heym workflow
- **Agentic Kanban Board** — Cards are persistent agentic jobs; moving a card into a column runs that column's ordered workflow chain with the card's full context (content, comments, history, previous outputs), and results are written back to the card
- **Templates** — Start from pre-built workflow templates to get up and running quickly
- **Parallel Execution** — Independent nodes run concurrently based on the graph structure, no configuration needed
- **Auto Heal** — Playwright selectors break? AI automatically detects and fixes them at runtime
- **LLM Fallback** — Automatic model fallback when the primary LLM fails or is unavailable
- **Reasoning Support** — Configure reasoning effort and temperature per Agent node for fine-grained control
- **Command Palette** — Ctrl+K for instant search, navigation, and workflow actions
- **Evals** — Define test suites and run them against any workflow with one click
- **LLM Traces** — Full observability for every agent call: requests, responses, tool calls, and timing
- **Alerts** — Threshold rules over a time window on error count, run duration, LLM spend, and execution count, built in an AI-fillable wizard that backtests the condition before you save it and can run any workflow when it fires
- **LLM Cost Tracking** — Per-trace token counts (input / output) with real-time USD cost calculation, historical analytics with time-range filtering, and a synced pricing table covering all major models
- **Self-Hosted** — Your data, your infrastructure

---

## Full Feature Set

## installation

Prefer to watch it first? **[Set Up Heym Locally in Under 2 Minutes](https://www.youtube.com/watch?v=P6YvlupUboU)** walks the whole path: clone the repository, start PostgreSQL and create your account on a local instance.

```bash
git clone https://github.com/heymrun/heym.git
cd heym
./run.sh

# OR — with .env file (run.sh auto-generates SECRET_KEY and ENCRYPTION_KEY)
git clone https://github.com/heymrun/heym.git
cd heym
cp .env.example .env
./run.sh

# OR — Docker with .env file
git clone https://github.com/heymrun/heym.git
cd heym
cp .env.example .env
# Generate required keys and write them into the placeholder lines copied from
# .env.example (replace in place — appending with >> would create duplicate entries):
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
ENCRYPTION_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
sed -i.bak "s|^SECRET_KEY=.*|SECRET_KEY=${SECRET_KEY}|; s|^ENCRYPTION_KEY=.*|ENCRYPTION_KEY=${ENCRYPTION_KEY}|" .env && rm -f .env.bak
docker run --env-file .env \
  -p 4017:4017 \
  -e FILE_STORAGE_DIR=/app/data/files \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$(pwd)/data/files:/app/data/files" \
  -v heym-codex-workspaces:/app/data/codex-workspaces \
  -v heym-opencode-workspaces:/app/data/opencode-workspaces \
  ghcr.io/heymrun/heym:latest

# OR — minimal, no .env file
docker run \
  -e ENCRYPTION_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))") \
  -e SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))") \
  -e DATABASE_URL=postgresql+asyncpg://postgres:postgres@host.docker.internal:6543/heym \
  -e FILE_STORAGE_DIR=/app/data/files \
  -p 4017:4017 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$(pwd)/data/files:/app/data/files" \
  -v heym-codex-workspaces:/app/data/codex-workspaces \
  -v heym-opencode-workspaces:/app/data/opencode-workspaces \
  ghcr.io/heymrun/heym:latest
```

Open the editor on port `4017`. See [ENVIRONMENT-VARIABLES.md](ENVIRONMENT-VARIABLES.md) for every setting and its default.

Three things about the `docker run` setup are worth knowing:

- **`FILE_STORAGE_DIR=/app/data/files` is load-bearing.** The release image runs the backend from `/app/backend`, so the default relative path would land inside the container instead of your mount and Drive uploads would vanish on restart. `./run.sh` and `./deploy.sh` are unaffected.
- **Keep `heym-codex-workspaces` mounted.** Python skills and the Codex node run there in a hardened sibling container; without it, skill execution fails closed. Per-run isolation needs Docker Engine 25.0+.
- **Keep `heym-opencode-workspaces` mounted** if you use the OpenCode Go node. The sibling runner shares that volume; without it the wrapper fails closed.
- **The Docker socket grants broad host control.** MCP `stdio` servers need it, because the caller-supplied command runs in a throwaway container rather than on the host. Docker log access stays off unless you set `DOCKER_LOGS_ENABLED=true` and `DOCKER_LOGS_ALLOWED_EMAILS`. Create that admin account first, or keep `ALLOW_REGISTER=false`, so nobody can self-register into an allow-listed email.

## Deploy & Call Workflows

Heym workflows are not limited to the editor. Run them from the canvas, call them through `/execute`, stream progress through `/execute/stream`, expose them as MCP tools at `/api/mcp/sse`, or publish them as Portal chat apps at `/chat/{slug}`. The same workflow can serve people, backend services, and AI clients without rebuilding the automation.

## Production Readiness

Heym is built to be inspected and operated in your own infrastructure. Docker deployment, JWT auth, team controls, shared credentials, `SECURITY.md`, execution history, logs, LLM traces, OpenTelemetry export, evals, and per-model USD cost tracking all live in the core self-hostable product.

Every pull request runs the [PR checks](https://github.com/heymrun/heym/actions/workflows/pr-checks.yml) workflow: a file line-limit check,

## configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Optional database connection string override | auto-built from `POSTGRES_*` |
| `POSTGRES_HOST` | Database host used when `DATABASE_URL` is empty | `localhost` |
| `POSTGRES_PORT` | Database port used when `DATABASE_URL` is empty | `6543` |
| `SECRET_KEY` | JWT signing key | — |
| `ENCRYPTION_KEY` | Encrypts stored credentials at rest. Required at startup; generate with `python -c "import secrets; print(secrets.token_hex(32))"` | — |
| `BACKEND_PORT` | Backend server port | `10105` |
| `FRONTEND_PORT` | Frontend server port | `4017` |
| `ALLOW_REGISTER` | Enable user registration | `true` |
| `REQUEST_BODY_MAX_SIZE_MB` | Maximum backend HTTP request body size; defaults to `100`, one MB above `FILE_MAX_SIZE_MB` to allow multipart overhead | `100` |
| `HEYM_OTEL_ENABLED` | Enable OpenTelemetry tracing for workflow, node, and Agent tool executions | `false` |
| `HEYM_OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP/HTTP base endpoint, e.g. `http://collector:4318` (spans posted to `/v1/traces`) | — |
| `HEYM_OTEL_EXPORTER_OTLP_HEADERS` | Comma-separated `key=value` exporter headers for auth | — |
| `HEYM_OTEL_SERVICE_NAME` | `service.name` resource attribute | `heym` |
| `HEYM_OTEL_TRACES_SAMPLER_RATIO` | Parent-based head sampling ratio (`0.0`–`1.0`) | `1.0` |
| `HEYM_OTEL_CAPTURE_NODE_IO` | Attach truncated node input/output to node spans | `false` |
| `HEYM_MCP_ALLOW_PRIVATE_URLS` | Allow MCP HTTP/SSE servers on private/loopback/metadata addresses (SSRF guard off). Keep `false` on hosted/multi-tenant | `false` |

See [ENVIRONMENT-VARIABLES.md](ENVIRONMENT-VARIABLES.md) for the complete reference.

---

## 🛠️ Development

**Prerequisites:** [Bun](https://bun.sh/) ≥ 1.0 · [Python](https://python.org/) ≥ 3.11 · [UV](https://github.com/astral-sh/uv) · [Docker](https://docker.com/)

```bash
# Start all services (recommended)
./run.sh
./run.sh --no-debug    # INFO logging instead of DEBUG
```

Or start each service manually:

```bash
# Start database only
docker-compose up -d postgres

# Backend
cd backend && uv sync && uv run alembic upgrade head
uv run uvicorn app.main:app --reload --port 10105

# Frontend (separate terminal)
cd frontend && bun install && bun run dev
```

**Validation (lint + typecheck + tests):**
```bash
./check.sh    # Run all checks — required before pushing
```

Or run individually:
```bash
cd frontend && bun run lint && bun run typecheck && bun run test
cd backend  && uv run ruff check . && uv run ruff format .
```

---

## 📄 License

This project is licensed under the **[MIT License](LICENSE)** with the **[Commons Clause](COMMONS-CLAUSE.md)** condition applied. In other words, Heym is **source-available** rather than OSI-open-source. See both files for details.

**TL;DR:** You are free to use, modify, distribute, and self-host this software — but you may **not sell** it or offer it as a paid service. Commercial licensing is available for teams that need those rights.

---

## Watch Heym Tutorials

<div align="center">

<a href="https://www.youtube.com/playlist?list=PLPXd_ZbA4wgEHP5PXoaRqbsDJdat7OSd4">
  <img src="./docs/readme-assets/tutorial-videos-playlist.png" width="100%" alt="Watch Heym tutorial videos on YouTube"/>
</a>

</div>

---

## 💬 Community

Join our Discord to connect with the community, ask questions, share workflows, and stay up to date:

[![Discord](https://img.shields.io/badge/Discord-Join%20us-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/T2wXvuVdMX )

---

## 🧩 Share a Template

Want to publish a workflow template for the community? You can now submit it directly from the **[Templates page](https://heym.run/submit)** — open the dialog, paste your workflow DSL, and send it for review. No pull request needed.

If you'd rather contribute through code, please **[start a Discussion](https://github.com/heymrun/heym/discussions)** so we can talk it through together **before** opening a pu
