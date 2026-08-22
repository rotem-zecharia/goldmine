# getzep/graphiti

Build Real-Time Knowledge Graphs for AI Agents

## features

Traditional RAG approaches often rely on batch processing and static data summarization, making them inefficient for
frequently changing data. Graphiti addresses these challenges by providing:

- **Temporal Fact Management:** Facts have validity windows. When information changes, old facts are
  invalidated — not deleted. Query what's true now, or what was true at any point in time.
- **Episodes & Provenance:** Every entity and relationship traces back to the episodes (raw data) that produced it.
  Full lineage from derived fact to source.
- **Prescribed & Learned Ontology:** Define entity and edge types upfront via Pydantic models (prescribed), or let
  structure emerge from your data (learned). Start simple, evolve as patterns appear.
- **Incremental Graph Construction:** New data integrates immediately without batch recomputation. The graph evolves
  in real-time as episodes are ingested.
- **Hybrid Retrieval:** Combines semantic embeddings, keyword (BM25), and graph traversal for low-latency,
  high-precision queries without reliance on LLM summarization.
- **Scalability:** Efficiently manages large datasets with parallel processing, pluggable graph backends, suitable
  for enterprise workloads.

<p align="center">
    <img src="/images/graphiti-intro-slides-stock-2.gif" alt="Graphiti structured + unstructured demo" width="700px">
</p>

## installation

Requirements:

- Python 3.10 or higher
- Neo4j 5.26 / FalkorDB 1.1.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon OpenSearch
  Serverless collection (serves as the full text search backend) / Kuzu 0.11.2 (**deprecated**, see below)
- OpenAI API key (Graphiti defaults to OpenAI for LLM inference and embedding)

> [!IMPORTANT]
> Graphiti works best with LLM services that support Structured Output (such as OpenAI, Anthropic, and Gemini).
> Using other services may result in incorrect output schemas and ingestion failures. This is particularly
> problematic when using smaller models.

Optional:

- Google Gemini, Anthropic, or Groq API key (for alternative LLM providers)

> [!TIP]
> The simplest way to install Neo4j is via [Neo4j Desktop](https://neo4j.com/download/). It provides a user-friendly
> interface to manage Neo4j instances and databases.
> Alternatively, you can use FalkorDB on-premises via Docker and instantly start with the quickstart example:
> ```
> docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
> ```

```bash
pip install graphiti-core
```

or

```bash
uv add graphiti-core
```

## configuration

In addition to the Neo4j and OpenAi-compatible credentials, Graphiti also has a few optional environment variables.
If you are using one of our supported models, such as Anthropic or Voyage models, the necessary environment variables
must be set.

## tools

azure_client = AsyncOpenAI(
    base_url="https://your-resource-name.openai.azure.com/openai/v1/",
    api_key="your-api-key",
)
