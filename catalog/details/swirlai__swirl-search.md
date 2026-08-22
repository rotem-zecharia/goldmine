# swirlai/swirl-search

AI Search & RAG Without Moving Your Data. Get instant answers from your company's knowledge across 100+ apps while keeping data secure. Deploy in minutes, not months.

## features

Most "AI search" asks you to copy everything into a vector database first, then govern that copy forever. SWIRL skips the copy. It queries your sources live, with the user's own permissions, re-ranks the results, and optionally generates an answer with citations using the LLM of your choice.

| ❌ The usual way | ✅ With SWIRL |
| --- | --- |
| Stand up a vector database | No vector DB needed |
| Move and duplicate your data | Data stays in place |
| Build ETL pipelines | Query live, in place |
| Weeks of infrastructure work | One Docker command, about 2 minutes |
| A new copy to secure and audit | Permissions enforced at the source |

## installation

Make sure the [Docker app](https://docs.docker.com/get-docker/) is installed and running.

Download the compose file:

```
curl https://raw.githubusercontent.com/swirlai/swirl-search/main/docker-compose.yaml -o docker-compose.yaml
```

Optional, to enable real-time RAG with your own OpenAI key:

```
export MSAL_CB_PORT=8000
export MSAL_HOST=localhost
export OPENAI_API_KEY='<your-OpenAI-API-key>'
```

Start SWIRL:

```
docker-compose pull && docker-compose up
```

Then open <http://localhost:8000/galaxy>, log in with `admin` / `password`, and run a search. SWIRL comes ready to search Arxiv, European PMC and Google News out of the box.

[![SWIRL Galaxy UI: federated, ranked results across your sources](https://github.com/swirlai/swirl-search/raw/main/docs/images/swirl5_galaxy_results.png)](https://www.swirlaiconnect.com)

> Note: the Docker version does not retain data or configuration when shut down. For a persistent install, see the [Quick Start Guide](https://docs.swirlaiconnect.com/quick-start). Watch the [60-second video tutorial](https://www.youtube.com/watch?v=Ypn4XvSJfcQ) to get going.

## 🧱 What SWIRL Community gives you

Apache 2.0, free, yours to run anywhere:

- Federated search and RAG across 100+ connectors, with your data left in place.
- The Galaxy UI, the same interface that powers SWIRL Enterprise.
- Real-time RAG with citations using your own OpenAI key.
- Microsoft 365 integration with OAuth2.
- Re-ranking with cosine vector similarity (spaCy large model plus NLTK), duplicate detection, and result mixers.
- A pipelined Processor architecture for transforming queries, responses and results.
- Synchronous or asynchronous federation over a clean REST API.
- Results stored in SQLite or Postgres for post-processing and analytics.
- Easily extensible Connector and Mixer objects, so adding a source is straightforward.

### What teams build with it

- Knowledge base search across SharePoint, Confluence and Drive, with source links.
- Customer support assistants that search docs and tickets and draft grounded responses.
- Developer assistants over GitHub, Jira and documentation.
- Unified search across every tool, with results that respect existing permissions.

## 🆚 Community vs SWIRL 5 Enterprise

Community is genuinely useful and genuinely open. SWIRL 5 Enterprise is what you graduate to when search becomes infrastructure. We keep the line honest so you always know what you are running.

| Capability | Community (Apache 2.0) | SWIRL 5 Enterprise |
| --- | --- | --- |
| Federated search and RAG, no data movement | Yes | Yes |
| Galaxy UI | Yes | Yes |
| 100+ connectors | Yes | Yes, plus managed connectors |
| RAG with your own LLM key | Yes | Yes |
| Relevancy ranking | Cosine similarity (spaCy, NLTK) | Three-pass pipeline: BM25, then E5 embeddings with hybrid fusion, then a cross-encoder |
| Canonical answers and Pinned Results | Not included | Yes |
| First-class MCP server for agents | Not included | Yes |
| Hallucination warning on generated answers | Not included | Yes |
| Business console with AI-Yield analytics, semantic cache and dedup at scale | Not included | Yes |
| SOC-2 hosting, managed connectors, and support | Not included | Yes |

If you outgrow cosine ranking, want canonical answers, or need your agents to call SWIRL over MCP, that is SWIRL 5.

## When you outgrow Community

Plenty of teams run Community in production and never need more. If you do reach its edges, where you want the three-pass reranker, canonical answers, an MCP server for your agents, the hallucination warning, or managed connectors and support, that is what SWIRL Enterprise adds.

If that is where you are heading, you can [talk to us](https://swirlaiconnect.com/contact-us) for a walkthrough on your own systems. Nothing leaves your environment, and there is no obligation.

## 🔌 Connectors

The full, current list lives at [swirlaiconnect.com/connectors](https://swirlaiconnect.com/connectors). Connectors are easily extensible; see t
