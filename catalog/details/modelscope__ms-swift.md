# modelscope/ms-swift

Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.6, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM4.5v, Gemma4, Llava, Phi

## installation

To install using pip:
```shell
pip install ms-swift -U

## tools

Here is a minimal example of training to deployment using ms-swift. For more details, you can check the [examples](https://github.com/modelscope/ms-swift/tree/main/examples).

- If you want to use other models or datasets (including multimodal models and datasets), you only need to modify `--model` to specify the corresponding model's ID or path, and modify `--dataset` to specify the corresponding dataset's ID or path.
- By default, ModelScope is used for downloading models and datasets. If you want to use HuggingFace, simply specify `--use_hf true`.

|   Useful Links |
| ------ |
|   [🔥Command Line Parameters](https://swift.readthedocs.io/en/latest/Instruction/Command-line-parameters.html)   |
|   [Megatron-SWIFT](https://swift.readthedocs.io/en/latest/Megatron-SWIFT/Quick-start.html)   |
|   [GRPO](https://swift.readthedocs.io/en/latest/Instruction/GRPO/GetStarted/GRPO.html)   |
|   [Supported Models and Datasets](https://swift.readthedocs.io/en/latest/Instruction/Supported-models-and-datasets.html)   |
|   [Custom Models](https://swift.readthedocs.io/en/latest/Customization/Custom-model.html), [🔥Custom Datasets](https://swift.readthedocs.io/en/latest/Customization/Custom-dataset.html)   |
|   [LLM Tutorial](https://github.com/modelscope/modelscope-classroom/tree/main/LLM-tutorial)   |
