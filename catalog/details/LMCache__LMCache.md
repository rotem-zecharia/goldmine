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

## Contributing
We welcome and value contributions and collaborations. Join us in improving LMCache. Check out the [Contributing Guide](https://docs.lmcache.ai/developer_guide/contributing.html) or join our [Slack community](https://join.slack.com/t/lmcacheworkspace/shared_invite/zt-3zxjao8h0-lRfBfnLqbALOtLsWn2ITxA) to get started.

## Adoption and Partnerships
LMCache has a growing community of developers, researchers, industry adopters, and partners building the next generation of efficient LLM inference systems.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="asset/partner_dark.png">
    <source media="(prefers-color-scheme: light)" srcset="asset/partner_light.png">
    <img alt="LMCache Adoption and Partnerships" src="asset/partner_light.png">
  </picture>
</p>

As an independent open-source project, LMCache is becoming the de-facto standard for KV Cache management in LLM inference. Its continued development and community work are supported in part by [Tensormesh](https://www.tensormesh.ai/).

## Citation

LMCache builds on research in KV cache management, including cache reuse, offloading, compression, and serving optimization. If you use LMCache in your research, please cite the LMCache paper and related work.

~~~bibtex
@article{cheng2025lmcache,
  title={LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference},
  author={Cheng, Yihua and Liu, Yuhan and Yao, Jiayi and An, Yuwei and Chen, Xiaokun and Feng, Shaoting and Huang, Yuyang and Shen, Samuel and Du, Kuntai and Jiang, Junchen},
  journal={arXiv preprint arXiv:2510.09665},
  year={2025}
}
~~~

<details>
<summary>Related papers</summary>

~~~bibtex
@inproceedings{liu2024cachegen,
  title={Cachegen: Kv cache compression and streaming for fast large language model serving},
  author={Liu, Yuhan and Li, Hanchen and Cheng, Yihua and Ray, Siddhant and Huang, Yuyang and Zhang, Qizheng and Du, Kuntai and Yao, Jiayi and Lu, Shan and Ananthanarayanan, Ganesh and others},
  booktitle={Proceedings of the ACM SIGCOMM 2024 Conference},
  pages={38--56},
  year={2024}
}

@inproceedings{yao2025cacheblend,
  title={Cacheblend: Fast large language model serving for rag with cached knowledge fusion},
  author={Yao, Jiayi and Li, Hanchen and Liu, Yuhan and Ray, Siddhant and Cheng, Yihua and Zhang, Qizheng and Du, Kuntai and Lu, Shan and Jiang, Junchen},
  booktitle={Proceedings of the twentieth European conference on computer systems},
  pages={94--109},
  year={2025}
}
~~~

</details>

## License

The LMCache codebase is licensed under Apache License 2.0. See the [LICENSE](LICENSE) file for details.
