# LMCache/LMCache

LMCache: Supercharge Your LLM with the Fastest KV Cache Layer

## features

- **Engine-independent deployment**: LMCache, as a standalone daemon process, manages KV cache independently from the inference engine process, so that KV cache will not be lost even if the inference engine crashes (i.e., no fate-sharing with engines).

- **Persistent, tiered KV cache offloading and reuse**: Move KV caches out of GPU memory into a tiered storage hierarchy spanning CPU memory, local storage, and remote backends, enabling reuse across requests, sessions, and engine instances to reduce repeated prefill computation and improve TTFT.

- **Production-level KV cache observability**: LMCache provides a rich set of KV cache observability metrics, including typical Kubernetes metrics (health monitoring, performance diagnostics), KV-cache-specific metrics (request-level and token-level prefix cache hits, lifecycle, request-level KV cache performance), management metrics (user-specific usage), and more.

- **Pluggable storage and transport backends**: Easily integrate remote storage and KV transfer backends through a unified interface, enabling KV cache offloading and sharing across storage providers. Through this interface, LMCache supports storage backends including CPU RAM, local disk (SSD), Redis/Valkey, Mooncake, InfiniStore, S3-compatible object storage, NIXL, and GDS.

- **Non-prefix KV reuse**: Extend KV reuse beyond prefix caching by reusing cached KV blocks at any position in the prompt. This leverages CacheBlend to selectively recompute tokens for quality recovery.

- **PD disaggregation and KV transfer**: Support KV cache transfer from prefill workers to decode workers over NVLink, RDMA, or TCP through transport layers such as NIXL.

- **Pluggable KV transformation**: A simple interface for researchers to write compression, token dropping, and custom serialization through a flexible SERDE interface.

LMCache is becoming an integral layer in the LLM inference *ecosystem*, with *community*-driven integration with serving engines, inference frameworks, hardware vendors, storage systems, and infrastructure providers:

<p align="center">
  <img src="asset/ecosystem.png" alt="LMCache ecosystem">
</p>

## installation

To use LMCache, simply install `lmcache` from your package manager, e.g. pip:
```bash
pip install lmcache
```

For more setup options and examples, see:
- [Installation](https://docs.lmcache.ai/getting_started/installation.html)
- [Quickstart](https://docs.lmcache.ai/getting_started/quickstart.html)
- [LMCache Recipes](https://docs.lmcache.ai/recipes/index.html)
- [CLI Reference](https://docs.lmcache.ai/cli/index.html)
- [Benchmarking Guide](https://docs.lmcache.ai/getting_started/benchmarking.html)
- [Production Deployment](https://docs.lmcache.ai/mp/deployment.html)
