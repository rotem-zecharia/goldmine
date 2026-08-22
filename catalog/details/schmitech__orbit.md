# schmitech/orbit

Self-hosted, OpenAI-compatible AI gateway for private RAG, natural-language data access, and tool-calling agents.

## features

| Capability | Included |
| :--- | :--- |
| **Model gateway** | 41 configured inference backends and providers, OpenAI-compatible APIs, per-key routing, model switching, retries, and fallbacks. |
| **Retrieval** | Vector RAG, file and multimodal RAG, SQL, MongoDB, Elasticsearch, REST, GraphQL, web search, and multi-source answers. |
| **Agents and protocols** | MCP tool calling, bounded multi-step loops, natural-language skill routing, A2A, and asynchronous RabbitMQ requests. |
| **Media** | Image, video, speech, PDF, Word, Excel, PowerPoint, CSV, and markdown generation. |
| **Security** | API keys, RBAC, Entra ID and Auth0 SSO, rate limits, quotas, moderation, file encryption, and cloud secret managers. |
| **Operations** | Admin UI, health checks, metrics, audit logs, per-request token and estimated-cost tracking, spend analytics, circuit breakers, datasource pooling, and hot adapter reloads. |

[Browse all adapters](docs/adapters/adapters.md) · [See provider configuration](config/inference.yaml) · [Read the configuration reference](install/default-config/config.yaml)

⭐ **Finding ORBIT useful?** [Star the repository](https://github.com/schmitech/orbit) to help other developers discover it and support continued investment in new model, datasource, and agent integrations.

## installation

<div align="center">
  <a href="https://orbit.schmitech.ca/?utm_source=github&utm_medium=readme&utm_campaign=try_orbit&utm_content=quick_start"><img src="https://img.shields.io/badge/TRY%20ORBIT%20LIVE-Explore%20the%20Sandbox%20%E2%86%92-7C3AED?style=for-the-badge" alt="Try ORBIT live — explore the sandbox" /></a>
  <br />
  <em>Explore the live sandbox instantly—no download, Docker, or setup required.</em>
</div>

### Install ORBIT

#### Option 1 (Preferred): Stable release tarball

**Prerequisites:** Linux or macOS, Python 3.12+, and an internet connection for downloading dependencies.

Download and install the latest stable release:

```bash
curl -L https://github.com/schmitech/orbit/releases/download/v2.15.9/orbit-2.15.9.tar.gz -o orbit-2.15.9.tar.gz
tar -xzf orbit-2.15.9.tar.gz
cd orbit-2.15.9
./install/setup.sh --profile default
./bin/orbit.sh start
```

ORBIT starts on [http://localhost:3000](http://localhost:3000). For Windows, follow the [Windows installation guide](install/windows.md).

ORBIT is highly configurable. The main server settings live in `./config/config.yaml`; inference providers, adapters, models, data sources, and other capabilities are configured in the other files under `./config/`.

See the [server management guide](docs/server.md#server-management) for commands to start, stop, restart, pause, and monitor ORBIT.

To use the optional ORBIT chatbot web interface, install and run `orbitchat` from your host machine:

```bash
npm install -g orbitchat
ORBIT_ADAPTER_KEYS='{"simple-chat":"default-key"}' orbitchat
```

Then open [http://localhost:5173](http://localhost:5173) in your browser.

See the [OrbitChat project and documentation](clients/orbitchat/README.md) for configuration, custom adapters, authentication, and advanced usage.

#### Option 2: Docker

**Prerequisites:** Docker, 4 GB of free RAM, and 3 GB of disk space.

<details>
<summary><strong>Option 1: Local / Offline (Ollama)</strong></summary>

```bash
docker pull schmitech/orbit-ollama:latest
docker run -d --name orbit -p 5173:5173 -p 3000:3000 \
  -v orbit-data:/orbit/data \
  -v orbit-models:/orbit/models \
  schmitech/orbit-ollama:latest
```

The first run downloads the local chat/vision model (`gemma4:e2b`, ~7.2 GB) inside the container and will take some time to complete startup depending on your internet connection speed. Once pulled, open [http://localhost:5173](http://localhost:5173) and start chatting — upload a PDF, a spreadsheet, or an image and ask about it. No cloud account or API key required.

| | Model |
| :--- | :--- |
| Chat | `gemma4:e2b` (Ollama) |
| Vision | `gemma4:e2b` (Ollama) |
| Embeddings | `nomic-embed-text` (Ollama) |
</details>

<details>
<summary><strong>Option 2: OpenAI Hosted Model</strong></summary>

```bash
export OPENAI_API_KEY=sk-...

docker pull schmitech/orbit-openai:latest
docker run -d --name orbit -p 5173:5173 -p 3000:3000 \
  -e OPENAI_API_KEY \
  -v orbit-data:/orbit/data \
  schmitech/orbit-openai:latest
```

| | Model |
| :--- | :--- |
| Chat | `gpt-5.4-mini` (also selectable: `gpt-5.4`, `gpt-5.4-nano`) |
| Vision | `gpt-5.5` |
| Embeddings | `text-embedding-3-small` |
</details>

<details>
<summary><strong>Option 3: Gemini Hosted Model</strong></summary>

```bash
export GOOGLE_API_KEY=...

docker pull schmitech/orbit-gemini:latest
docker run -d --name orbit -p 5173:5173 -p 3000:3000 \
  -e GOOGLE_API_KEY \
  -v orbit-data:/orbit/data \
  schmitech/orbit-gemini:latest
```

| | Model |
| :--- | :--- |
| Chat | `gemini-3.1-pro-preview` (also selectable: `gemini-3.6-flash`) |
| Vision | `gemini-3.6-flash` |
| Embeddings | `gemini-embedding-2-preview` |
</details>

</br>

Port `5173` is the chat UI, `3000` is the OpenAI-compatible API if you want to call ORBIT directly:

```bash
curl -X POST http://localhost:3000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: multimodal' \
  -H 'X-Session-ID: local-test' \
  -d '{"messages":[{"role":"user","content":"What can ORBIT conne
