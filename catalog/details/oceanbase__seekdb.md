# oceanbase/seekdb

The AI-Native Search Database. Best for agent storage, it unifies vector, text, structured, and semi-structured data into a single engine. This all-in-one database makes agents smarter, easier to run,

## features

### 🔥 Streaming Write + Concurrent Search, Without the P99 Spike

Agent workloads are continuous write + millisecond-later read. seekdb's
**async index pipeline (Change Stream)** decouples DML from index build,
and its **two-level HNSW** (incremental + snapshot) makes newly-written
vectors immediately searchable.

<div align="center">
  <img src="images/architecture.svg" alt="seekdb async index pipeline architecture" width="720" />
</div>

The write path commits and returns *without waiting* on index construction.
The Change Stream pipeline consumes the redo log asynchronously and updates
the delta HNSW. Queries hit both delta and snapshot indexes with fine-grained
read locks — **this is why P99 stays flat under concurrency.**

> **The result: 1,523 QPS with 21.7 ms concurrent P99 — 10.7× the QPS of
> Milvus, and P99 jitter of just 1.1× when concurrency rises (vs ~10×
> for ES / Milvus on the same workload).**

<sub>Source: [`src/share/change_stream/`](src/share/change_stream/) · [`src/share/vector_index/`](src/share/vector_index/)</sub>

### 🌿 Copy-on-Write Sandboxes for Agent Exploration

`FORK DATABASE` snapshots an entire database in seconds — no data copy.
Agents experiment freely (write, query, even break tables); then `MERGE TABLE`
commits the work back, or `DROP DATABASE` discards it. Kernel-level COW,
not application-layer save/restore.

```sql
-- Snapshot in seconds, no data copy
FORK DATABASE agent_state TO agent_sandbox_42;

-- Agent reads/writes freely on the sandbox...
USE agent_sandbox_42;
INSERT INTO memory (session_id, embedding, content) VALUES (...);

-- Accept the work back to mainline (strategies: FAIL / THEIRS / OURS)
MERGE TABLE agent_sandbox_42.memory INTO agent_state.memory STRATEGY THEIRS;
-- ...or throw it away:
DROP DATABASE agent_sandbox_42;
```

<sub>Source: [`tools/deploy/mysql_test/test_suite/fork_table/`](tools/deploy/mysql_test/test_suite/fork_table/)</sub>

### 🔍 Hybrid Search in a Single SQL

Vector + full-text + scalar filter pushed into one execution plan.
No N+1 client-side merging, no glue code to combine results.

```sql
SELECT id, title, l2_distance(emb, '[0.12,0.34,...]') AS dist
FROM docs
WHERE MATCH(content) AGAINST('quarterly report')
  AND author_id = 42
  AND created_at > '2026-01-01'
ORDER BY dist APPROXIMATE LIMIT 10;
```

### 🐬 MySQL-Compatible, ACID, Embeddable

Built on the proven OceanBase SQL engine. Works as an embedded library,
a single-node server, or in the OceanBase distributed cluster. Full ACID,
real-time writes, and the entire MySQL ecosystem out of the box.

---

<a id="quick-start"></a>

## installation

### Installation

Choose your platform:

<details open>
<summary><b>☁️ Cloud (Zero Install)</b></summary>

One curl, a running database — no signup, no credit card.

```bash
curl -X POST https://d0.seekdb.ai/api/v1/instances
```

Free for 7 days. [Learn more →](https://d0.seekdb.ai)

</details>

<details open>
<summary><b>🐍 Python (Recommended for AI/ML)</b></summary>

```bash
pip install -U pyseekdb
```

</details>

<details>
<summary><b>🐳 Docker (Quick Testing)</b></summary>

```bash
docker run -d \
  --name seekdb \
  -p 2881:2881 \
  -p 2886:2886 \
  -v ./data:/var/lib/oceanbase \
  oceanbase/seekdb:latest
```
Please refer to the [document](https://github.com/oceanbase/docker-images/blob/main/seekdb/README.md) of this docker image for details.

</details>

<details>
<summary><b>📦 Binary (Standalone)</b></summary>

```bash
# Linux (one-line install, may need sudo)
curl -fsSL https://obportal.s3.ap-southeast-1.amazonaws.com/download-center/opensource/seekdb/seekdb_install.sh | bash

# macOS (Homebrew)
brew tap oceanbase/seekdb
brew install seekdb
```

See [deployment docs](https://docs.seekdb.ai/seekdb/deploy-by-systemd/) for DEB/RPM offline install and configuration details.

</details>

<a id="more-examples"></a>

## tools

For the full Python SDK walkthrough — connection modes, embedding functions, metadata filters — see the [pyseekdb User Guide](https://github.com/oceanbase/pyseekdb).

<details open>
<summary><b>🤖 Agent Memory Pattern (continuous write + immediate retrieval)</b></summary>

The canonical agent loop: write an observation, retrieve relevant context
milliseconds later, repeat. seekdb's async index pipeline keeps both
sides fast under sustained concurrency.

```python
import pyseekdb

client = pyseekdb.Client(path="./agent_state.db")
memory = client.get_or_create_collection(name="episodic")

for step in agent.run():
    # Persist the observation
    memory.upsert(ids=[step.id], documents=[step.observation])

    # Retrieve relevant context — milliseconds after the write,
    # served by the incremental HNSW (no waiting on a background rebuild)
    relevant = memory.query(query_texts=step.next_query, n_results=5)

    agent.act(relevant)
```

</details>

<details>
<summary><b>🗄️ SQL — Schema + Hybrid Search</b></summary>

```sql
-- Table with vector column, full-text index, and HNSW vector index
CREATE TABLE articles (
  id        INT PRIMARY KEY,
  title     TEXT,
  content   TEXT,
  embedding VECTOR(384),
  FULLTEXT INDEX idx_fts (content) WITH PARSER ik,
  VECTOR   INDEX idx_vec (embedding) WITH (DISTANCE=l2, TYPE=hnsw, LIB=vsag)
) ORGANIZATION = HEAP;

-- Hybrid search: vector similarity + full-text match in one query
SELECT id, title,
       l2_distance(embedding, '[0.12, 0.34, ...]') AS dist
FROM articles
WHERE MATCH(content) AGAINST('quarterly report')
ORDER BY dist APPROXIMATE
LIMIT 10;
```

Python developers can access this via SQLAlchemy or any MySQL driver.

</details>


## 📚 Use Cases

<details open>
<summary><b>🎯 Agentic AI — Memory, Sandbox & State</b></summary>

Agents need a state store that handles continuous memory writes,
millisecond-later retrieval, branching for exploration, and rollback when
things go wrong. seekdb is built for exactly this:

- **Streaming-friendly storage** — write a memory, query it in the next ms
- **COW sandboxes** — `FORK DATABASE` for safe experimentation, `MERGE` to accept, `DROP` to roll back
- **Hybrid retrieval** — vector + full-text + relational in one SQL
- **MySQL protocol** — works with LangChain, LlamaIndex, Dify out of the box

Personal assistants · Enterprise automation · Vertical agents · Agent platforms

</details>

<details>
<summary><b>🧩 Other Use Cases</b></summary>

seekdb's hybrid retrieval + multi-model engine also fits classic AI workloads:

- **📖 RAG & Knowledge Retrieval** — vector + full-text + scalar filters with multi-level access control. *Enterprise QA, customer support, industry insights, personal knowledge bases.*
- **🔍 Semantic Search** — embedding-based search across text, images, and other modalities. *Product search, text-to-image, image-to-product.*
- **💻 AI-Assisted Coding** — semantic code search, multi-project isolation, time-travel queries for IDE plugins and code agents. *Local IDEs, web IDEs, design-to-web.*
- **⬆️ Enterprise Application Intelligence** — MySQL-compatible AI layer for legacy systems, with row/column hybrid storage. *Document intelligence, business insights, finance systems.*
- **📱 On-Device & Edge AI** — embedded / micro-server modes for resource-constrained devices. *In-vehicle systems, AI education, companion robots, healthcare devices.*

</details>

---

<a id="ecosystem--integrations"></a>

## 🌟 Ecosystem & Integrations

<div align="center">

<p>
    <a href="https://github.com/langchain-ai/langchain/pulls?q=is%3Apr+is%3Aclosed+oceanbase">
        <img src="https://img.shields.io/badge/LangChain-✅-00A67E?style=flat-square&logo=langchain" alt="LangChain" />
    </a>
    <a href="https://github.com/run-llama/llama_index/pulls?q=is%3Apr+is%3Aclosed+oceanbase">
        <img src="https://img.shields.io/badge/LlamaIndex-✅-00A67E?style=flat-square&logo=llama" alt="LlamaIndex" />
    </a>
    <a href="https://github.com/langgenius/dify/pu
