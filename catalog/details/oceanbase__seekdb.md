# oceanbase/seekdb

The AI-Native Search Database. Best for agent storage, it unifies vector, text, structured, and semi-structured data into a single engine. This all-in-one database makes agents smarter, easier to run,

## installation

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
