# topoteretes/cognee

Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.

## features

- Easily Build Company Brain - unify data from various sources in one place and enable Agents with your domain knowledge
- Knowledge infrastructure — unified ingestion, graph/vector search, runs locally, ontology grounding, multimodal
- Persistent and Learning Agents - learn from feedback, context management, cross-agent knowledge sharing
- Reliable and Trustworthy Agents - agentic user/tenant isolation, traceability, OTEL collector, audit traits

### How it Works

<p align="center">
  <img src="assets/remember.svg" alt="Cognee Products" width="80%" />
</p>

<p align="center">
  <img src="assets/recall.svg" alt="Cognee Recall" width="80%" />
</p>

## Basic Usage & Feature Guide

To learn more, [check out this short, end-to-end Colab walkthrough](https://colab.research.google.com/drive/1HRrzIvzcbwrESVfX76wJLKmtIg00SUga?usp=sharing) of Cognee's core features.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HRrzIvzcbwrESVfX76wJLKmtIg00SUga?usp=sharing)

## installation

Let’s try Cognee in just a few lines of code.

## requirements

- Python 3.10 to 3.14

## configuration

```python
import os
os.environ["LLM_API_KEY"] = "YOUR OPENAI_API_KEY"
```
Alternatively, create a `.env` file using our [template](https://github.com/topoteretes/cognee/blob/main/.env.template).

To integrate other LLM providers, see our [LLM Provider Documentation](https://docs.cognee.ai/setup-configuration/llm-providers).

### Step 3: Run the Pipeline

Cognee's API gives you four operations — `remember`, `recall`, `forget`, and `improve`:

```python
import cognee
import asyncio


async def main():
    # Store permanently in the knowledge graph (runs add + cognify + improve)
    await cognee.remember("Cognee turns documents into AI memory.")

    # Store in session memory (fast cache, syncs to graph in background)
    await cognee.remember("User prefers detailed explanations.", session_id="chat_1")

    # Query with auto-routing (picks best search strategy automatically)
    results = await cognee.recall("What does Cognee do?")
    for result in results:
        print(result)

    # Query session memory first, fall through to graph if needed
    results = await cognee.recall("What does the user prefer?", session_id="chat_1")
    for result in results:
        print(result)

    # Delete when done
    await cognee.forget(dataset="main_dataset")


if __name__ == '__main__':
    asyncio.run(main())

```

### Use the Cognee CLI

```bash
cognee-cli remember "Cognee turns documents into AI memory."

cognee-cli recall "What does Cognee do?"

cognee-cli forget --all
```

To open the local UI, run:
```bash
cognee-cli -ui
```

> **Note:** The MCP server launched by `cognee-cli -ui` runs inside a Docker container.
> Docker Desktop, Colima, or any OCI-compatible runtime with a working `docker` CLI is
> required. See [Docker & Colima Setup](docs/docker-colima-setup.md) for details.

### Performance tuning

Cognee's defaults favor memory quality over raw latency. Two knobs matter:

- **`AUTO_FEEDBACK=false`** removes the one LLM call cognee makes after each answered
  query to self-tune its memory. Reads get faster and cheaper; session memory itself
  keeps working. Turn it back on when you want memory that improves from conversation
  signals.
- **`CACHING=false`** disables session memory entirely — `remember(session_id=...)`
  stops working and `recall()` loses conversation context. Only set this if you don't
  use session memory at all. **If you're benchmarking cognee, leave it on** — turning
  it off benchmarks cognee with its memory layer removed.

A third flag, `DATASET_QUEUE_ENABLED=false`, removes the per-process concurrency guard
on datasets; it saves a little latency but risks file-lock leaks and resource
exhaustion when multiple datasets run in parallel — leave it on for servers.

## Run with Docker

Prefer containers? Cognee publishes prebuilt images to Docker Hub on every push to `main`:
[`cognee/cognee`](https://hub.docker.com/r/cognee/cognee) (the API server) and
[`cognee/cognee-mcp`](https://hub.docker.com/r/cognee/cognee-mcp) (the MCP server).

> **Just want to try it?** Follow the
> [minimal docker-compose try-out](docs/minimal-docker-compose.md) — a single
> copy-pasteable compose file that runs the prebuilt image, no clone or build needed.

### Option A — Docker Compose (build from source)

Clone the repo, create a `.env` with at least `LLM_API_KEY`, then:

```bash
cp .env.template .env   # then edit .env and set LLM_API_KEY

## tools

docker compose up

# Optional profiles (combine as needed):
docker compose --profile ui up        # + frontend on http://localhost:3000
docker compose --profile mcp up       # + MCP server on http://localhost:8001
docker compose --profile postgres up  # + Postgres/PGVector
docker compose --profile neo4j up     # + Neo4j
```

> The `cognee` and `cognee-mcp` services publish different host ports (`8000` vs `8001`),
> so you can run both at once.

### Option B — Pull the prebuilt image (no clone required)

```bash
# Create a minimal .env in the current directory
echo 'LLM_API_KEY="YOUR_OPENAI_API_KEY"' > .env

# API server
docker run --env-file ./.env -p 8000:8000 --rm -it cognee/cognee:main

# MCP server (HTTP transport)
docker pull cognee/cognee-mcp:main
docker run -e TRANSPORT_MODE=http --env-file ./.env -p 8000:8000 --rm -it cognee/cognee-mcp:main
```

See the [MCP server README](cognee-mcp/README.md) for SSE/stdio transports, optional
extras, and MCP client configuration.

## Use with AI Agents

### Claude Code

Install the [Cognee memory plugin](https://github.com/topoteretes/cognee-integrations/tree/main/integrations/claude-code) to give Claude Code persistent memory across sessions. The plugin captures prompts, tool traces, and assistant responses into session memory, injects relevant context on every prompt, and syncs session memory into the permanent knowledge graph at session end.

**Install** from the Claude Code marketplace. The recommended way is from your shell, *before* launching Claude Code, so the first `claude` launch is a clean session that bootstraps memory automatically:

```bash
