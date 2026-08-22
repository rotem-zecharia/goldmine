# axolotl-ai-cloud/axolotl

Go ahead and axolotl questions

## features

Axolotl is a free and open-source tool designed to streamline post-training and fine-tuning for the latest large language models (LLMs).

Features:

- **Multiple Model Support**: Train various models like GPT-OSS, LLaMA, Mistral, Mixtral, Pythia, and many more models available on the Hugging Face Hub.
- **Multimodal Training**: Fine-tune vision-language models (VLMs) including LLaMA-Vision, Qwen2-VL, Pixtral, LLaVA, SmolVLM2, GLM-4.6V, InternVL 3.5, Gemma 3n, PaddleOCR-VL, Muse Glimmer, and audio models like Voxtral with image, video, and audio support.
- **Training Methods**: Full fine-tuning, LoRA, QLoRA, GPTQ, QAT (int8/int4/FP8/NVFP4/MXFP4), FP8 mixed-precision training, NVFP4/MXFP4 MoE LoRA, Preference Tuning (DPO, IPO, KTO, ORPO), RL (GRPO, GDPO), and Reward Modelling (RM) / Process Reward Modelling (PRM).
- **Easy Configuration**: Re-use a single YAML configuration file across the full fine-tuning pipeline: dataset preprocessing, training, evaluation, quantization, and inference.
- **Performance Optimizations**: [Multipacking](https://docs.axolotl.ai/docs/multipack.html), [Flash Attention 2/3/4](https://docs.axolotl.ai/docs/attention.html#flash-attention), [Xformers](https://docs.axolotl.ai/docs/attention.html#xformers), [Flex Attention](https://docs.axolotl.ai/docs/attention.html#flex-attention), [SageAttention](https://docs.axolotl.ai/docs/attention.html#sageattention), [Liger Kernel](https://docs.axolotl.ai/docs/custom_integrations.html#liger-kernels), [Cut Cross Entropy](https://docs.axolotl.ai/docs/custom_integrations.html#cut-cross-entropy), [ScatterMoE](https://docs.axolotl.ai/docs/custom_integrations.html#kernels-integration), [Sequence Parallelism (SP)](https://docs.axolotl.ai/docs/sequence_parallelism.html), [LoRA optimizations](https://docs.axolotl.ai/docs/lora_optims.html), [Multi-GPU training (FSDP1, FSDP2, DeepSpeed)](https://docs.axolotl.ai/docs/multi-gpu.html), [Multi-node training (Torchrun, Ray)](https://docs.axolotl.ai/docs/multi-node.html), and many more!
- **Flexible Dataset Handling**: Load from local, HuggingFace, and cloud (S3, Azure, GCP, OCI) datasets.
- **Cloud Ready**: We ship [Docker images](https://hub.docker.com/u/axolotlai) and also [PyPI packages](https://pypi.org/project/axolotl/) for use on cloud platforms and local hardware.

## installation

**Requirements**:

- NVIDIA GPU (Ampere or newer for `bf16` and Flash Attention) or AMD GPU
- Python >=3.11 (3.12 recommended)
- PyTorch ≥2.11.0

### Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb#scrollTo=msOCO4NRmRLa)

### Installation

```bash
# install uv if you don't already have it installed (restart shell after)
curl -LsSf https://astral.sh/uv/install.sh | sh

# change depending on system
export UV_TORCH_BACKEND=cu130

## configuration

uv venv --python 3.12
source .venv/bin/activate

uv pip install torch==2.12.0 torchvision
uv pip install --no-build-isolation axolotl[deepspeed]

# Download example axolotl configs, deepspeed configs
axolotl fetch examples
axolotl fetch deepspeed_configs  # OPTIONAL
```

#### Using Docker

Installing with Docker can be less error prone than installing in your own environment.
```bash
docker run --gpus '"all"' --ipc=host --rm -it axolotlai/axolotl:main-latest
```

Other installation approaches are described [here](https://docs.axolotl.ai/docs/installation.html).

#### Cloud Providers

<details>

- [RunPod](https://runpod.io/gsc?template=v2ickqhz9s&ref=6i7fkpdz)
- [Vast.ai](https://cloud.vast.ai?ref_id=62897&template_id=bdd4a49fa8bce926defc99471864cace&utm_source=github&utm_medium=developer_community&utm_campaign=template_launch_axolotl&utm_content=readme)
- [PRIME Intellect](https://app.primeintellect.ai/dashboard/create-cluster?image=axolotl&location=Cheapest&security=Cheapest&show_spot=true)
- [Modal](https://www.modal.com?utm_source=github&utm_medium=github&utm_campaign=axolotl)
- [Novita](https://novita.ai/gpus-console?templateId=311)
- [JarvisLabs.ai](https://jarvislabs.ai/templates/axolotl)
- [Latitude.sh](https://latitude.sh/blueprint/989e0e79-3bf6-41ea-a46b-1f246e309d5c)

</details>

### Your First Fine-tune

```bash

## tools

axolotl fetch examples

# Or, specify a custom path
axolotl fetch examples --dest path/to/folder

# Train a model using LoRA
axolotl train examples/llama-3/lora-1b.yml
```

That's it! Check out our [Getting Started Guide](https://docs.axolotl.ai/docs/getting-started.html) for a more detailed walkthrough.


## 📚 Documentation

- [Installation Options](https://docs.axolotl.ai/docs/installation.html) - Detailed setup instructions for different environments
- [Support Matrix](https://docs.axolotl.ai/docs/support-matrix.html) - Feature support, compatibility, and known gaps
- [Configuration Guide](https://docs.axolotl.ai/docs/config-reference.html) - Full configuration options and examples
- [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html) - Loading datasets from various sources
- [Dataset Guide](https://docs.axolotl.ai/docs/dataset-formats/) - Supported formats and how to use them
- [Multi-GPU Training](https://docs.axolotl.ai/docs/multi-gpu.html)
- [Multi-Node Training](https://docs.axolotl.ai/docs/multi-node.html)
- [Multipacking](https://docs.axolotl.ai/docs/multipack.html)
- [API Reference](https://docs.axolotl.ai/docs/api/) - Auto-generated code documentation
- [FAQ](https://docs.axolotl.ai/docs/faq.html) - Frequently asked questions

## AI Agent Support

Axolotl ships with built-in documentation optimized for AI coding agents (Claude Code, Cursor, Copilot, etc.). These docs are bundled with the pip package, no repo clone needed.

```bash
