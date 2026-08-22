# InternLM/lmdeploy

LMDeploy is a toolkit for compressing, deploying, and serving LLMs.

## installation

## Installation

It is recommended installing lmdeploy using pip in a conda environment (python 3.10 - 3.13):

```shell
conda create -n lmdeploy python=3.12 -y
conda activate lmdeploy
pip install lmdeploy
```

Starting from **v0.13.0**, the default prebuilt wheels published on **PyPI** are built against **CUDA 12.8**, so `pip install lmdeploy` is sufficient for typical setups including GeForce RTX 50 series.

## Offline Batch Inference

```python
import lmdeploy
with lmdeploy.pipeline("internlm/internlm3-8b-instruct") as pipe:
    response = pipe(["Hi, pls intro yourself", "Shanghai is"])
    print(response)
```

> \[!NOTE\]
> By default, LMDeploy downloads model from HuggingFace. If you would like to use models from ModelScope, please install ModelScope by `pip install modelscope` and set the environment variable:
>
> `export LMDEPLOY_USE_MODELSCOPE=True`
>
> If you would like to use models from openMind Hub, please install openMind Hub by `pip install openmind_hub` and set the environment variable:
>
> `export LMDEPLOY_USE_OPENMIND_HUB=True`

For more information about inference pipeline, please refer to [here](docs/en/llm/pipeline.md).

# Tutorials

Please review [getting_started](docs/en/get_started/get_started.md) section for the basic usage of LMDeploy.

For detailed user guides and advanced guides, please refer to our [tutorials](https://lmdeploy.readthedocs.io/en/latest/):

- User Guide
  - [LLM Inference pipeline](docs/en/llm/pipeline.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Dh-YlSwg78ZO3AlleO441NF_QP2shs95#scrollTo=YALmXnwCG1pQ)
  - [VLM Inference pipeline](docs/en/multi_modal/vl_pipeline.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nKLfnPeDA3p-FMNw2NhI-KOpk7-nlNjF?usp=sharing)
  - [LLM Serving](docs/en/llm/api_server.md)
  - [VLM Serving](docs/en/multi_modal/api_server_vl.md)
  - [Quantization](docs/en/quantization)
- Advance Guide
  - [Inference Engine - TurboMind](docs/en/inference/turbomind.md)
  - [Inference Engine - PyTorch](docs/en/inference/pytorch.md)
  - [Customize chat templates](docs/en/advance/chat_template.md)
  - [Add a new model](docs/en/advance/pytorch_new_model.md)
  - gemm tuning
  - [Long context inference](docs/en/advance/long_context.md)
  - [Multi-model inference service](docs/en/llm/proxy_server.md)

# Third-party projects

- Deploying LLMs offline on the NVIDIA Jetson platform by LMDeploy: [LMDeploy-Jetson](https://github.com/BestAnHongjun/LMDeploy-Jetson)

- Example project for deploying LLMs using LMDeploy and BentoML: [BentoLMDeploy](https://github.com/bentoml/BentoLMDeploy)

# Contributing

We appreciate all contributions to LMDeploy. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.

# Acknowledgement

- [FasterTransformer](https://github.com/NVIDIA/FasterTransformer)
- [llm-awq](https://github.com/mit-han-lab/llm-awq)
- [vLLM](https://github.com/vllm-project/vllm)
- [DeepSpeed-MII](https://github.com/microsoft/DeepSpeed-MII)

# Citation

```bibtex
@misc{2023lmdeploy,
    title={LMDeploy: A Toolkit for Compressing, Deploying, and Serving LLM},
    author={LMDeploy Contributors},
    howpublished = {\url{https://github.com/InternLM/lmdeploy}},
    year={2023}
}
```

```bibtex
@article{zhang2025lmdeploy,
  title={LMDeploy Accelerates Mixed-Precision LLM Inference with TurboMind},
  author={Zhang, Li and Jiang, Youhe and He, Guoliang and Chen, Xin and Lv, Han and Yao, Qian and Ma, Ningsheng and Fu, Fangcheng and Chen, Kai},
  journal={arXiv preprint arXiv:2508.15601},
  year={2025}
}
```

# License

This project is released under the [Apache 2.0 license](LICENSE).
