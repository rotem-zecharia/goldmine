# weaviate/weaviate

Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance and scalability of a c

## installation

Weaviate offers multiple installation and deployment options:

- [Docker](https://docs.weaviate.io/deploy/installation-guides/docker-installation)
- [Kubernetes](https://docs.weaviate.io/deploy/installation-guides/k8s-installation)
- [Weaviate Cloud](https://console.weaviate.cloud)

See the [installation docs](https://docs.weaviate.io/deploy) for more deployment options, such as [AWS](https://docs.weaviate.io/deploy/installation-guides/aws-marketplace) and [GCP](https://docs.weaviate.io/deploy/installation-guides/gcp-marketplace).

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
