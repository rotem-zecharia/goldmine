# qdrant/qdrant

Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/

## features

* **Faceting** - aggregate search results by payload values.
* **Recommendation** - use positive and negative examples to find similar points.
* **Discovery** - constrain search to a specific region of the vector space.
* **Search Relevance Tuning** - tools for adjusting search results, such as Maximal Marginal Relevance (MMR) and the Relevance Feedback Query.
* **Multitenancy** - scalable partitioning of data for multi-user environments.
* **Observability** - comprehensive metrics, telemetry, and audit logging for monitoring and debugging.
* **Query Planning and Payload Indexes** - leverages stored payload information to optimize query execution strategy.
* **SIMD Hardware Acceleration** - utilizes modern CPU x86-x64 and Neon architectures to deliver better performance.
* **GPU Support** - for accelerated indexing, with support for NVIDIA and AMD GPUs.
* **Async I/O** - uses `io_uring` to maximize disk throughput utilization even on network-attached storage.
* **Write-Ahead Logging** - ensures data persistence with update confirmation, even during power outages.
