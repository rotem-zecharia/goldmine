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
