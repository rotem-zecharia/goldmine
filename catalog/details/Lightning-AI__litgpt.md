# Lightning-AI/litgpt

20+ high-performance LLMs with recipes to pretrain, finetune and deploy at scale.

## installation

Install LitGPT
```
pip install 'litgpt[extra]'
```

Load and use any of the [20+ LLMs](#choose-from-20-llms):
```python
from litgpt import LLM

llm = LLM.load("microsoft/phi-2")
text = llm.generate("Fix the spelling: Every fall, the family goes to the mountains.")
print(text)
# Corrected Sentence: Every fall, the family goes to the mountains.
```

&nbsp;

✅ Optimized for fast inference</br>
✅ Quantization</br>
✅ Runs on low-memory GPUs</br>
✅ No layers of internal abstractions</br>
✅ Optimized for production scale</br>

<details>
  <summary>Advanced install options</summary>

Install from source:

```bash
git clone https://github.com/Lightning-AI/litgpt
cd litgpt
# if using uv
uv sync --all-extras
# if using pip
pip install -e ".[extra,compiler,test]"
```
</details>

[Explore the full Python API docs](tutorials/python-api.md).

&nbsp;

---
# Choose from 20+ LLMs
Every model is written from scratch to maximize performance and remove layers of abstraction:

| Model | Model size | Author | Reference |
|----|----|----|----|
| Llama 3, 3.1, 3.2, 3.3 | 1B, 3B, 8B, 70B, 405B | Meta AI | [Meta AI 2024](https://github.com/meta-llama/llama3)                                           |
| Code Llama | 7B, 13B, 34B, 70B | Meta AI | [Rozière et al. 2023](https://arxiv.org/abs/2308.12950)                                       |
| CodeGemma | 7B | Google | [Google Team, Google Deepmind](https://ai.google.dev/gemma/docs/codegemma)                                     |
| Gemma 2 | 2B, 9B, 27B | Google | [Google Team, Google Deepmind](https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf)  |
| Phi 4 | 14B | Microsoft Research | [Abdin et al. 2024](https://arxiv.org/abs/2412.08905)                                                                            |
| Qwen2.5 | 0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B | Alibaba Group | [Qwen Team 2024](https://qwenlm.github.io/blog/qwen2.5/)                                               |
| Qwen2.5 Coder | 0.5B, 1.5B, 3B, 7B, 14B, 32B | Alibaba Group | [Hui, Binyuan et al. 2024](https://arxiv.org/abs/2409.12186)                                          |
| R1 Distill Llama | 8B, 70B | DeepSeek AI | [DeepSeek AI 2025](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)                                                                                 |
| ... | ... | ... | ...   |

<details>
  <summary>See full list of 20+ LLMs</summary>

&nbsp;

#### All models

| Model | Model size | Author | Reference |
|----|----|----|----|
| CodeGemma | 7B | Google | [Google Team, Google Deepmind](https://ai.google.dev/gemma/docs/codegemma)                                                                 |
| Code Llama | 7B, 13B, 34B, 70B | Meta AI | [Rozière et al. 2023](https://arxiv.org/abs/2308.12950)                                                                   |
| Falcon | 7B, 40B, 180B | TII UAE | [TII 2023](https://falconllm.tii.ae)                                                                                              |
| Falcon 3 | 1B, 3B, 7B, 10B | TII UAE | [TII 2024](https://huggingface.co/blog/falcon3)                                                                                              |
| FreeWilly2 (Stable Beluga 2) | 70B | Stability AI | [Stability AI 2023](https://stability.ai/blog/stable-beluga-large-instruction-fine-tuned-models)                 |
| Function Calling Llama 2 | 7B | Trelis | [Trelis et al. 2023](https://huggingface.co/Trelis/Llama-2-7b-chat-hf-function-calling-v2)                                  |
| Gemma | 2B, 7B | Google | [Google Team, Google Deepmind](https://storage.googleapis.com/deepmind-media/gemma/gemma-report.pdf)                                       |
| Gemma 2 | 9B, 27B | Google | [Google Team, Google Deepmind](https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf)                                  |
| Gemma 3 | 1B, 4B, 12B, 27B | Google | [Google Team, Google Deepmind](https://arxiv.org/pdf/2503.19786)            

## features

✅ State-of-the-art optimizations: Flash Attention v2, multi-GPU support via fully-sharded data parallelism, [optional CPU offloading](tutorials/oom.md#do-sharding-across-multiple-gpus), and [TPU and XLA support](extensions/xla).</br>
✅ [Pretrain](tutorials/pretrain.md), [finetune](tutorials/finetune.md), and [deploy](tutorials/inference.md)</br>
✅ Reduce compute requirements with low-precision settings: FP16, BF16, and FP16/FP32 mixed.</br>
✅ Lower memory requirements with [quantization](tutorials/quantize.md): 4-bit floats, 8-bit integers, and double quantization.</br>
✅ [Configuration files](config_hub) for great out-of-the-box performance.</br>
✅ Parameter-efficient finetuning: [LoRA](tutorials/finetune_lora.md), [QLoRA](tutorials/finetune_lora.md), [Adapter](tutorials/finetune_adapter.md), and [Adapter v2](tutorials/finetune_adapter.md).</br>
✅ [Exporting](tutorials/convert_lit_models.md) to other popular model weight formats.</br>
✅ Many popular datasets for [pretraining](tutorials/pretrain.md) and [finetuning](tutorials/prepare_dataset.md), and [support for custom datasets](tutorials/prepare_dataset.md#preparing-custom-datasets-for-instruction-finetuning).</br>
✅ Readable and easy-to-modify code to experiment with the latest research ideas.</br>

&nbsp;

---

# Training recipes

LitGPT comes with validated recipes (YAML configs) to train models under different conditions.  We've generated these recipes based on the parameters we found to perform the best for different training conditions.

Browse all training recipes [here](config_hub).

### Example

```bash
litgpt finetune \
  --config https://raw.githubusercontent.com/Lightning-AI/litgpt/main/config_hub/finetune/llama-2-7b/lora.yaml
```
<details>
  <summary>✅ Use configs to customize training</summary>

Configs let you customize training for all granular parameters like:

```yaml
# The path to the base model's checkpoint directory to load for finetuning. (type: <class 'Path'>, default: checkpoints/stabilityai/stablelm-base-alpha-3b)
checkpoint_dir: checkpoints/meta-llama/Llama-2-7b-hf

# Directory in which to save checkpoints and logs. (type: <class 'Path'>, default: out/lora)
out_dir: out/finetune/qlora-llama2-7b

# The precision to use for finetuning. Possible choices: "bf16-true", "bf16-mixed", "32-true". (type: Optional[str], default: null)
precision: bf16-true

...
```
</details>

<details>
  <summary>✅ Example: LoRA finetuning config</summary>

&nbsp;

```yaml
# The path to the base model's checkpoint directory to load for finetuning. (type: <class 'Path'>, default: checkpoints/stabilityai/stablelm-base-alpha-3b)
checkpoint_dir: checkpoints/meta-llama/Llama-2-7b-hf

# Directory in which to save checkpoints and logs. (type: <class 'Path'>, default: out/lora)
out_dir: out/finetune/qlora-llama2-7b

# The precision to use for finetuning. Possible choices: "bf16-true", "bf16-mixed", "32-true". (type: Optional[str], default: null)
precision: bf16-true

# If set, quantize the model with this algorithm. See ``tutorials/quantize.md`` for more information. (type: Optional[Literal['nf4', 'nf4-dq', 'fp4', 'fp4-dq', 'int8-training']], default: null)
quantize: bnb.nf4

# How many devices/GPUs to use. (type: Union[int, str], default: 1)
devices: 1

# How many nodes to use. (type: int, default: 1)
num_nodes: 1

# The LoRA rank. (type: int, default: 8)
lora_r: 32

# The LoRA alpha. (type: int, default: 16)
lora_alpha: 16

# The LoRA dropout value. (type: float, default: 0.05)
lora_dropout: 0.05

# Whether to apply LoRA to the query weights in attention. (type: bool, default: True)
lora_query: true

# Whether to apply LoRA to the key weights in attention. (type: bool, default: False)
lora_key: false

# Whether to apply LoRA to the value weights in attention. (type: bool, default: True)
lora_value: true

# Whether to apply LoRA to the output projection in the attention block. (type: bool, default: False)
lora_projection: false

# Whether to apply LoRA to the weights of the MLP in t
