# weaviate/weaviate

Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance and scalability of a c

## installation

Weaviate offers multiple installation and deployment options:

- [Docker](https://docs.weaviate.io/deploy/installation-guides/docker-installation)
- [Kubernetes](https://docs.weaviate.io/deploy/installation-guides/k8s-installation)
- [Weaviate Cloud](https://console.weaviate.cloud)

See the [installation docs](https://docs.weaviate.io/deploy) for more deployment options, such as [AWS](https://docs.weaviate.io/deploy/installation-guides/aws-marketplace) and [GCP](https://docs.weaviate.io/deploy/installation-guides/gcp-marketplace).

## Getting started

You can easily start Weaviate and a local vector embedding model with [Docker](https://docs.docker.com/desktop/).
Create a `docker-compose.yml` file:

```yml
services:
  weaviate:
    image: cr.weaviate.io/semitechnologies/weaviate:1.36.0
    ports:
      - "8080:8080"
      - "50051:50051"
    environment:
      ENABLE_MODULES: text2vec-model2vec
      MODEL2VEC_INFERENCE_API: http://text2vec-model2vec:8080

  # A lightweight embedding model that will generate vectors from objects during import
  text2vec-model2vec:
    image: cr.weaviate.io/semitechnologies/model2vec-inference:minishlab-potion-base-32M
```

Start Weaviate and the embedding service with:

```bash
docker compose up -d
```

Install the Python client (or use another [client library](#client-libraries-and-apis)):

```bash
pip install -U weaviate-client
```

The following Python example shows how easy it is to populate a Weaviate database with data, create vector embeddings and perform semantic search:

```python
import weaviate
from weaviate.classes.config import Configure, DataType, Property

# Connect to Weaviate
client = weaviate.connect_to_local()

# Create a collection
client.collections.create(
    name="Article",
    properties=[Property(name="content", data_type=DataType.TEXT)],
    vector_config=Configure.Vectors.text2vec_model2vec(),  # Use a vectorizer to generate embeddings during import
    # vector_config=Configure.Vectors.self_provided()  # If you want to import your own pre-generated embeddings
)

# Insert objects and generate embeddings
articles = client.collections.get("Article")
articles.data.insert_many(
    [
        {"content": "Vector databases enable semantic search"},
        {"content": "Machine learning models generate embeddings"},
        {"content": "Weaviate supports hybrid search capabilities"},
    ]
)

# Perform semantic search
results = articles.query.near_text(query="Search objects by meaning", limit=1)
print(results.objects[0])

client.close()
```

This example uses the `Model2Vec` vectorizer, but you can choose any other [embedding model provider](https://docs.weaviate.io/weaviate/model-providers) or [bring your own pre-generated vectors](https://docs.weaviate.io/weaviate/starter-guides/custom-vectors).

## tools

Weaviate provides client libraries for several programming languages:

- [Python](https://docs.weaviate.io/weaviate/client-libraries/python)
- [JavaScript/TypeScript](https://docs.weaviate.io/weaviate/client-libraries/typescript)
- [Java](https://docs.weaviate.io/weaviate/client-libraries/java)
- [Go](https://docs.weaviate.io/weaviate/client-libraries/go)
- [C#/.NET](https://docs.weaviate.io/weaviate/client-libraries/csharp)

There are also additional [community-maintained libraries](https://docs.weaviate.io/weaviate/client-libraries/community).

Weaviate exposes [REST API](https://docs.weaviate.io/weaviate/api/rest), [gRPC API](https://docs.weaviate.io/weaviate/api/grpc), and [GraphQL API](https://docs.weaviate.io/weaviate/api/graphql) to communicate with the database server.

## features

These features enable you to build AI-powered applications:

- **⚡ Fast Search Performance**: Perform complex semantic [searches](https://docs.weaviate.io/weaviate/search/similarity) over billions of vectors in milliseconds. Weaviate's architecture is built in Go for speed and reliability, ensuring your AI applications are highly responsive even under heavy load. See our [ANN benchmarks](https://docs.weaviate.io/weaviate/benchmarks/ann) for more info.

- **🔌 Flexible Vectorization**: Seamlessly vectorize data at import time with [integrated vectorizers](https://docs.weaviate.io/weaviate/model-providers) from OpenAI, Cohere, HuggingFace, Google, and more. Or you can import [your own vector embeddings](https://docs.weaviate.io/weaviate/starter-guides/custom-vectors).

- **🔍 Advanced Hybrid & Image Search**: Combine the power of semantic search with traditional [keyword (BM25) search](https://docs.weaviate.io/weaviate/search/bm25), [image search](https://docs.weaviate.io/weaviate/search/image) and [advanced filtering](https://docs.weaviate.io/weaviate/search/filters) to get the best results with a single API call.

- **🤖 Integrated RAG & Reranking**: Go beyond simple retrieval with built-in [generative search (RAG)](https://docs.weaviate.io/weaviate/search/generative) and [reranking](https://docs.weaviate.io/weaviate/search/rerank) capabilities. Power sophisticated Q&A systems, chatbots, and summarizers directly from your database without additional tooling.

- **📈 Production-Ready & Scalable**: Weaviate is built for mission-critical applications. Go from rapid prototyping to production at scale with native support for [horizontal scaling](https://docs.weaviate.io/deploy/configuration/horizontal-scaling), [multi-tenancy](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy), [replication](https://docs.weaviate.io/deploy/configuration/replication), and fine-grained [role-based access control (RBAC)](https://docs.weaviate.io/weaviate/configuration/rbac).

- **💰 Cost-Efficient Operations**: Radically lower resource consumption and operational costs with built-in [vector compression](https://docs.weaviate.io/weaviate/configuration/compression). Vector quantization and multi-vector encoding reduce memory usage with minimal impact on search performance.

- **⏱️ Object TTL**: Automatically expire and remove stale data with configurable [time-to-live](https://docs.weaviate.io/weaviate/manage-collections/time-to-live) settings per collection, with full RBAC and multi-tenancy support.

For a complete list of all functionalities, visit the [official Weaviate documentation](https://docs.weaviate.io).

## Useful resources

### AI Agent Skills

[Weaviate Agent Skills](https://github.com/weaviate/agent-skills) is a collection of skills for AI coding agents (Claude Code, Cursor, GitHub Copilot, and others) that enable them to work with Weaviate more accurately and efficiently. Skills cover searching, querying, collection management, data import, and full application blueprints (RAG, agentic RAG, chatbots, and more).

Install with:

```bash
npx skills add weaviate/agent-skills
```

### Demo projects & recipes

These demos are working applications that highlight some of Weaviate's capabilities. Their source code is available on GitHub.

- [Elysia](https://elysia.weaviate.io) ([GitHub](https://github.com/weaviate/elysia)): Elysia is a decision tree based agentic system which intelligently decides what tools to use, what results have been obtained, whether it should continue the process or whether its goal has been completed.
- [Verba](https://weaviate.io/blog/verba-open-source-rag-app) ([GitHub](https://github.com/weaviate/verba)): A community-driven open-source application designed to offer an end-to-end, streamlined, and user-friendly interface for Retrieval-Augmented Generation (RAG) out of the box.
- [Healthsearch](https://weaviate.io/blog/healthsearch-demo) ([GitHub](https://github.com/weaviate/healthsearch-demo)): An open-source
