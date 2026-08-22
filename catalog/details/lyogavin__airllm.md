# lyogavin/airllm

AirLLM 70B inference with single 4GB GPU

## installation

First, install the airllm pip package.

```bash
pip install airllm
```

## configuration

When initialize the model, we support the following configurations:

* **compression**: supported options: 4bit, 8bit for 4-bit or 8-bit block-wise quantization, or by default None for no compression
* **profiling_mode**: supported options: True to output time consumptions or by default False
* **layer_shards_saving_path**: optionally another path to save the splitted model
* **hf_token**: huggingface token can be provided here if downloading gated models like: *meta-llama/Llama-2-7b-hf*
* **prefetching**: prefetching to overlap the model loading and compute. By default, turned on. For now, only AirLLMLlama2 supports this.
* **delete_original**: if you don't have too much disk space, you can set delete_original to true to delete the original downloaded hugging face model, only keep the transformed one to save half of the disk space.
