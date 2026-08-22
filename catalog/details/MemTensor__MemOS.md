# MemTensor/MemOS

Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

## features

- **Unified Memory API**: A single API to add, retrieve, edit, and delete memory—structured as a graph, inspectable and editable by design, not a black-box embedding store.
- **Multi-Modal Memory**: Natively supports text, images, tool traces, and personas, retrieved and reasoned together in one memory system.
- **Multi-Cube Knowledge Base Management**: Manage multiple knowledge bases as composable memory cubes, enabling isolation, controlled sharing, and dynamic composition across users, projects, and agents.
- **Asynchronous Ingestion via MemScheduler**: Run memory operations asynchronously with millisecond-level latency for production stability under high concurrency.
- **Memory Feedback & Correction**: Refine memory with natural-language feedback—correcting, supplementing, or replacing existing memories over time.


### News

- **2026-08-17** · 🐋 **MemOS Connects with DeepSeek Harness**
  MemOS now brings persistent memory to **DeepSeek Harness** through both local and cloud plugins. DSH can automatically recall relevant context before a task and retain new experience after a successful turn, without modifying its core.

- **2026-07-02** · 🏆 **MemOS Advances Agent and User Memory Benchmarks**
  With MemOS, **OpenClaw** improves average task completion from **36.63% to 50.87%** across five agent tasks. MemOS also achieves **88.83 on LoCoMo** and **89.20 on LongMemEval**, and leads in **OmniMemEval**, a unified evaluation of 14 commercial memory products across ten datasets.

- **2026-05-09** · 🧠 **memos-local-plugin 2.0**
  Official local memory plugin for **Hermes Agent** and **OpenClaw**. One core powers self-evolving memory across L1 traces, L2 policies, L3 world models, and crystallized Skills, with local-first storage and feedback-driven retrieval.

- **2026-04-10** · 👧🏻 **MemOS Hermes Agent Local Plugin**
  Official Hermes Agent memory plugins launched: Hybrid retrieval (FTS5 + vector), smart dedup, tiered skill evolution, multi-agent collaboration. 100% local, zero cloud dependency.
  
- **2026-03-08** · 🦞 **MemOS OpenClaw Plugin — Cloud & Local**
  Official OpenClaw memory plugins launched. **Cloud Plugin**: hosted memory service with 72% lower token usage and multi-agent memory sharing ([MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)). **Local Plugin** (`v1.0.0`): 100% on-device memory with persistent SQLite, hybrid search (FTS5 + vector), task summarization & skill evolution, multi-agent collaboration, and a full Memory Viewer dashboard.

## 📊 Performance

MemOS leads across multiple benchmarks — evaluated against mainstream commercial memory products across 5 user memory and 5 agent memory tasks.


| Benchmark       | Score |
| --------------- | ----- |
| LoCoMo          | 88.83 |
| LongMemEval     | 89.20 |
| PersonaMem v2   | 40.58 |
| HaluMem         | 80.91 |
| BEAM-10M        | 56.75 |
| GDPVal          | 62.07 |
| LiveCodeBench   | 64.96 |
| OmniMath        | 61.00 |
| SWE-Bench       | 38.46 |
| BrowseComp-Plus | 23.85 |


Evaluated via OmniMemEval — [https://github.com/MemTensor/OmniMemEval](https://github.com/MemTensor/OmniMemEval).

## 🎯 What MemOS Is For

MemOS gives AI agents long-term memory. Common uses:

- AI assistants with consistent, context-rich conversations
- Customer support that recalls past tickets and user history
- Personalized agents that adapt to individual preferences
- Multi-agent collaboration with shared or isolated memory

## installation

MemOS is built around four entry points. Pick the one that matches your scenario.


|              | Cloud API               | Self-Host          | MemOS Cloud Plugin       | Local Plugin                                     |
| ------------ | ----------------------- | ------------------ | ------------------------ | ------------------------------------------------ |
| Best for     | Your app, fully managed | Teams on own infra | OpenClaw users, zero ops | DeepSeek Harness, Hermes, or OpenClaw; on-device |
| Setup        | Get an API key          | docker compose up  | openclaw plugins install | npm install + agent-specific setup               |
| Infra needed | None (hosted)           | Neo4j + Qdrant     | None (uses MemOS Cloud)  | None (local SQLite)                              |
| Data lives   | MemOS Cloud             | Your servers       | MemOS Cloud              | Your machine                                     |

## tools

You want to add memory to your app through a fully managed service — no infrastructure to run.

**1. Get an API key:**

- Sign up on the [MemOS dashboard](https://memos-dashboard.openmem.net/cn/quickstart/?source=landing).
- Go to **API Keys** and copy your key (starts with `mpg-`). Keep it server-side.

**2. Add and search memories:**

```python
import requests

API_KEY = "mpg-..."                  # keep this server-side
base = "https://memos.memtensor.cn/api/openmem/v1"
headers = {"Authorization": f"Token {API_KEY}", "Content-Type": "application/json"}

# 1. Add a memory
requests.post(f"{base}/add/message", headers=headers, json={
    "user_id": "alice",
    "conversation_id": "conv_001",
    "messages": [{"role": "user", "content": "I like strawberry"}],
})

# 2. Search memories
res = requests.post(f"{base}/search/memory", headers=headers, json={
    "query": "What do I like?",
    "user_id": "alice",
})
print(res.json())
```

**Next steps:**

- [MemOS Cloud Getting Started](https://memos-docs.openmem.net/memos_cloud/quick_start/) — connect to MemOS Cloud and enable memory in minutes.
- [MemOS Cloud Platform](https://memos.openmem.net/?from=/quickstart/) — explore the Cloud dashboard, features, and workflows.

### 🖥️ Self-Host the MemOS Service

You want to run MemOS as a REST service on your own machine or cluster.

**Option A — Docker (recommended):**

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
cd docker
docker compose up                    # starts MemOS API + Neo4j + Qdrant
```

The API is served at `http://localhost:8000`.

**Option B — Run with uvicorn (without Docker):**

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
# Ensure Neo4j and Qdrant are running, then:
cd src
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
```

See `[docker/.env.example](./docker/.env.example)` for all configuration options (LLM provider, embedder, vector DB, graph DB, scheduler). The full deployment guide is at [https://memos-docs.openmem.net/open_source/getting_started/rest_api_server/](https://memos-docs.openmem.net/open_source/getting_started/rest_api_server/).

**Try the API:**

```python
import requests, json

headers = {"Content-Type": "application/json"}
base = "http://localhost:8000/product"

# 1. Create a memory cube
requests.post(f"{base}/create_cube", headers=headers, data=json.dumps({
    "cube_name": "Alice's memory",
    "owner_id": "alice",
    "cube_id": "alice_cube",
}))

# 2. Add a memory
requests.post(f"{base}/add", headers=headers, data=json.dumps({
    "user_id": "alice",
    "writable_cube_ids": ["alice_cube"],
    "messages": [{"role": "user", "content": "I like strawberry"}],
    "async_mode": "sync",
}))

# 3. Search memories
res = requests.post(f"{base}/search", headers=headers, data=json.dumps({
    "query": "What do I like?",
    "user_id": "alice",
    "readable_cube_ids": ["alice_cube"],
}))
print(res.json())
```

<a id="memos-plugin"></a>

### 🧠 MemOS Plugin: Persistent Memory for Your AI Agents ✨

MemOS gives OpenClaw, Hermes, and DeepSeek Harness a shared local memory core; the managed ***MemOS Cloud Plugin*** is available for OpenClaw and DeepSeek Harness 🏃🏻

| 🔌 Plugin                                                                                                     | 💡 Core Features | 🧩 Resources                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------
