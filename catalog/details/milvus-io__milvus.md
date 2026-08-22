# milvus-io/milvus

Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

## installation

```python
$ pip install -U pymilvus
```
This installs `pymilvus`, the Python SDK for Milvus. Use `MilvusClient` to create a client:
```python
from pymilvus import MilvusClient
```

* You can also try Milvus Lite for quickstart by installing `pymilvus[milvus-lite]`. To create a local vector database, simply instantiate a client with a local file name for persisting data:

  ```python
  client = MilvusClient("milvus_demo.db")
  ```

* You can also specify the credentials to connect to your deployed [Milvus server](https://milvus.io/docs/authenticate.md?tab=docker) or [Zilliz Cloud](https://docs.zilliz.com/docs/quick-start):

  ```python
  client = MilvusClient(
    uri="<endpoint_of_self_hosted_milvus_or_zilliz_cloud>",
    token="<username_and_password_or_zilliz_cloud_api_key>")
  ```

With the client, you can create collection:
```python
client.create_collection(
    collection_name="demo_collection",
    dimension=768,  # The vectors we will use in this demo have 768 dimensions

## features

Milvus is designed to handle vector search at scale. It stores vectors, which are learned representations of unstructured data, together with other scalar data types such as integers, strings, and JSON objects. Users can conduct efficient vector search with metadata filtering or hybrid search. Here are why developers choose Milvus as the vector database for AI applications:

**High Performance at Scale and High Availability**  
  * Milvus features a [distributed architecture](https://milvus.io/docs/architecture_overview.md ) that separates [compute](https://milvus.io/docs/data_processing.md#Data-query) and [storage](https://milvus.io/docs/data_processing.md#Data-insertion). Milvus can horizontally scale and adapt to diverse traffic patterns, achieving optimal performance by independently increasing query nodes for read-heavy workload and data node for write-heavy workload. The stateless microservices on K8s allow [quick recovery](https://milvus.io/docs/coordinator_ha.md#Coordinator-HA) from failure, ensuring high availability. The support for [replicas](https://milvus.io/docs/replica.md) further enhances fault tolerance and throughput by loading data segments on multiple query nodes. See [benchmark](https://zilliz.com/vector-database-benchmark-tool) for performance comparison.


**Support for Various Vector Index Types and Hardware Acceleration**  
  * Milvus separates the system and core vector search engine, allowing it to support all major vector index types that are optimized for different scenarios, including HNSW, IVF, FLAT (brute-force), SCANN, and DiskANN, with [quantization-based](https://milvus.io/docs/index.md?tab=floating#IVFPQ) variations and [mmap](https://milvus.io/docs/mmap.md). Milvus optimizes vector search for advanced features such as [metadata filtering](https://milvus.io/docs/scalar_index.md#Scalar-Index) and [range search](https://milvus.io/docs/single-vector-search.md#Range-search). Additionally, Milvus implements hardware acceleration to enhance vector search performance and supports GPU indexing, such as NVIDIA's [CAGRA](https://github.com/rapidsai/cuvs).


**Flexible Multi-tenancy and Hot/Cold Storage**
  * Milvus supports [multi-tenancy](https://milvus.io/docs/multi_tenancy.md#Multi-tenancy-strategies) through isolation at database, collection, partition, or partition key level. The flexible strategies allow a single cluster to handle hundreds to millions of tenants, also ensures optimized search performance and flexible access control. Milvus enhances cost-effectiveness with hot/cold storage. Frequently accessed hot data can be stored in memory or on SSDs for better performance, while less-accessed cold data is kept on slower, cost-effective storage. This mechanism can significantly reduce costs while maintaining high performance for critical tasks.

**Sparse Vector for Full Text Search and Hybrid Search**
  * In addition to semantic search through dense vector, Milvus also natively supports [full text search](https://milvus.io/docs/full-text-search.md) with BM25 as well as learned sparse embeddings such as SPLADE and BGE-M3. Users can store sparse vectors and dense vectors in the same collection, and define functions to rerank results from multiple search requests. See examples of [Hybrid Search with semantic search + full text search](https://milvus.io/docs/full_text_search_with_milvus.md).

**Data Security and Fine-grain Access Control**
  * Milvus ensures data security by implementing mandatory user authentication, TLS encryption, and Role-Based Access Control (RBAC). User authentication ensures that only authorized users with valid credentials can access the database, while TLS encryption secures all communications within the network. Additionally, RBAC allows for fine-grained access control by assigning specific permissions to users based on their roles. These features make Milvus a robust and secure choice for enterprise applications, protecting sensitive data from unauthorized access and po
