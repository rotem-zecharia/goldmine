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
