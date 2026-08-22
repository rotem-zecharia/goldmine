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

## configuration

uv venv --python 3.12
source .venv/bin/activate

uv pip install torch==2.12.0 torchvision
uv pip install --no-build-isolation axolotl[deepspeed]

## tools

axolotl fetch examples
