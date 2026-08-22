# hiyouga/LlamaFactory

Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

## installation

![GitHub Trend](https://trendshift.io/api/badge/repositories/17371)

</div>

👋 Join our [WeChat](https://github.com/hiyouga/llamafactory-community/blob/main/wechat/main.jpg) and [NPU](https://github.com/hiyouga/llamafactory-community/blob/main/wechat/npu.jpg) user groups.

\[ English | [中文](README_zh.md) \]

**Fine-tuning a large language model can be easy as...**

https://github.com/user-attachments/assets/3991a3a8-4276-4d30-9cab-4cb0c4b9b99e

Start local training:
- Please refer to [usage](#getting-started)

Start cloud training:
- **Colab (free)**: https://colab.research.google.com/drive/1eRTPn37ltBbYsISy9Aw2NuI2Aq5CQrD9?usp=sharing
- **PAI-DSW (free trial)**: https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory
- **AMD GPU Cloud (free credits)**: https://github.com/AMD-AIM/AMD_Developers_Notebooks/blob/main/en/AMD_developer_LLaMAFactory_note_en.md

Read technical notes:
- **Documentation (WIP)**: https://llamafactory.readthedocs.io/en/latest/
- **Documentation (AMD GPU)**: https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/llama_factory_llama3.html
- **Documentation (ASCEND NPU)**: https://llamafactory.readthedocs.io/en/latest/multibackend/npu/index.html
- **Official Blog**: https://blog.llamafactory.net/en/

> [!NOTE]
> Except for the above links, all other websites are unauthorized third-party websites. Please carefully use them.

## features

- **Various models**: LLaMA, LLaVA, Mistral, Mixtral-MoE, Qwen3, Qwen3-VL, DeepSeek, Gemma, GLM, Phi, etc.
- **Integrated methods**: (Continuous) pre-training, (multimodal) supervised fine-tuning, reward modeling, PPO, DPO, KTO, ORPO, etc.
- **Scalable resources**: 16-bit full-tuning, freeze-tuning, LoRA and 2/3/4/5/6/8-bit QLoRA via AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ.
- **Advanced algorithms**: [GaLore](https://github.com/jiaweizzhao/GaLore), [BAdam](https://github.com/Ledzy/BAdam), [APOLLO](https://github.com/zhuhanqing/APOLLO), [Adam-mini](https://github.com/zyushun/Adam-mini), [Muon](https://github.com/KellerJordan/Muon), [OFT](https://github.com/huggingface/peft/tree/main/src/peft/tuners/oft), DoRA, LongLoRA, LLaMA Pro, Mixture-of-Depths, LoRA+, LoftQ and PiSSA.
- **Practical tricks**: [FlashAttention-2](https://github.com/Dao-AILab/flash-attention), [Unsloth](https://github.com/unslothai/unsloth), [Liger Kernel](https://github.com/linkedin/Liger-Kernel), [KTransformers](https://github.com/kvcache-ai/ktransformers/), RoPE scaling, NEFTune and rsLoRA.
- **Wide tasks**: Multi-turn dialogue, tool using, image understanding, visual grounding, video recognition, audio understanding, etc.
- **Experiment monitors**: LlamaBoard, TensorBoard, Wandb, MLflow, [SwanLab](https://github.com/SwanHubX/SwanLab), etc.
- **Faster inference**: OpenAI-style API, Gradio UI and CLI with [vLLM worker](https://github.com/vllm-project/vllm) or [SGLang worker](https://github.com/sgl-project/sglang).

## requirements

| Mandatory    | Minimum | Recommend |
| ------------ | ------- | --------- |
| python       | 3.11     | >=3.11   |
| torch        | 2.0.0   | 2.6.0     |
| torchvision  | 0.15.0  | 0.21.0    |
| transformers | 4.49.0  | 4.50.0    |
| datasets     | 2.16.0  | 3.2.0     |
| accelerate   | 0.34.0  | 1.2.1     |
| peft         | 0.14.0  | 0.15.1    |
| trl          | 0.8.6   | 0.9.6     |

| Optional     | Minimum | Recommend |
| ------------ | ------- | --------- |
| CUDA         | 11.6    | 12.2      |
| deepspeed    | 0.10.0  | 0.16.4    |
| bitsandbytes | 0.39.0  | 0.43.1    |
| vllm         | 0.4.3   | 0.8.2     |
| flash-attn   | 2.5.6   | 2.7.2     |

## tools

```bash
API_PORT=8000 llamafactory-cli api examples/inference/qwen3.yaml infer_backend=vllm vllm_enforce_eager=true
```

> [!TIP]
> Visit [this page](https://platform.openai.com/docs/api-reference/chat/create) for API document.
>
> Examples: [Image understanding](scripts/api_example/test_image.py) | [Function calling](scripts/api_example/test_toolcall.py)
