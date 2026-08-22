# MemTensor/MemOS

Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

## features

- **Unified Memory API**: A single API to add, retrieve, edit, and delete memory—structured as a graph, inspectable and editable by design, not a black-box embedding store.
- **Multi-Modal Memory**: Natively supports text, images, tool traces, and personas, retrieved and reasoned together in one memory system.
- **Multi-Cube Knowledge Base Management**: Manage multiple knowledge bases as composable memory cubes, enabling isolation, controlled sharing, and dynamic composition across users, projects, and agents.
- **Asynchronous Ingestion via MemScheduler**: Run memory operations asynchronously with millisecond-level latency for production stability under high concurrency.
- **Memory Feedback & Correction**: Refine memory with natural-language feedback—correcting, supplementing, or replacing existing memories over time.

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
