# modelscope/ms-swift

Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.6, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM4.5v, Gemma4, Llava, Phi

## installation

To install using pip:
```shell
pip install ms-swift -U

# Using uv
pip install uv
uv pip install ms-swift -U --torch-backend=auto
```

To install from source:
```shell
# pip install git+https://github.com/modelscope/ms-swift.git

git clone https://github.com/modelscope/ms-swift.git
cd ms-swift
# The main branch is for swift 4.x. To install swift 3.x, please run the following command:
# git checkout release/3.12
pip install -e .

# Using uv
uv pip install -e . --torch-backend=auto
```

Running Environment:

|              | Range        | Recommended         | Notes                                     |
|--------------|--------------|---------------------|-------------------------------------------|
| python       | >=3.10        | 3.12                |                                           |
| cuda         |              | cuda12.8/13.0    | No need to install if using CPU, NPU, MPS |
| torch        | >=2.0        | 2.8.0/2.11.0         |                            |
| transformers | >=4.33       | 4.57.6/5.12.1              |                          |
| modelscope   | >=1.23       |                     |                                           |
| datasets     | >=3.0,<4.8.5 | 3.6.0/4.8.4         |                    |
| peft         | >=0.11,<0.21 |                     |                                           |
| flash_attn   |              | 2.8.3/4.0.0b15 |                                           |
| trl          | >=0.15,<1.0 | 0.29.1              | RLHF                                      |
| deepspeed    | >=0.14       | 0.18.9              | Training                                  |
| vllm         | >=0.5.1      | 0.11.0/0.23.0       | Inference/Deployment                      |
| sglang       | >=0.4.6      |          | Inference/Deployment                      |
| evalscope    | >=1.0       |                     | Evaluation                                |
| gradio       |              | 5.32.1              | Web-UI/App                                |

For more optional dependencies, you can refer to [here](https://github.com/modelscope/ms-swift/blob/main/requirements/install_all.sh).


## 🚀 Quick Start

10 minutes of self-cognition fine-tuning of Qwen3-4B-Instruct-2507 on a single 3090 GPU:

### Command Line Interface (Recommended)

```shell
# 13GB
CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model Qwen/Qwen3-4B-Instruct-2507 \
    --tuner_type lora \
    --dataset 'AI-ModelScope/alpaca-gpt4-data-zh#500' \
              'AI-ModelScope/alpaca-gpt4-data-en#500' \
              'swift/self-cognition#500' \
    --torch_dtype bfloat16 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --lora_rank 8 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --gradient_accumulation_steps 16 \
    --eval_steps 50 \
    --save_steps 50 \
    --save_total_limit 2 \
    --logging_steps 5 \
    --max_length 2048 \
    --output_dir output \
    --warmup_ratio 0.05 \
    --dataloader_num_workers 4 \
    --model_author swift \
    --model_name swift-robot
```

Tips:

- If you want to train with a custom dataset, you can refer to [this guide](https://swift.readthedocs.io/en/latest/Customization/Custom-dataset.html) to organize your dataset format and specify `--dataset <dataset_path>`.
- The `--model_author` and `--model_name` parameters are only effective when the dataset includes `swift/self-cognition`.
- To train with a different model, simply modify `--model <model_id/model_path>`.
- By default, **ModelScope** is used for downloading models and datasets. If you want to use HuggingFace, simply specify `--use_hf true`.

After training is complete, use the following command to infer with the trained weights:

- Here, `--adapters` should be replaced with the last checkpoint folder generated during training. Since the adapters folder contains the training parameter file `args.json`, there is no need to specify `--model`, `--system` 

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

### Training

Supported Training Methods:

| Method                                                       | Full-Parameter                                               | LoRA | QLoRA                                                        | Deepspeed                                                    | Multi-Machine                                                | Multimodal                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Pre-training](https://github.com/modelscope/ms-swift/blob/main/examples/train/pretrain) | ✅                                                            | ✅    | ✅                                                            | ✅                                                            | ✅                                                            | ✅                                                            |
| [Supervised Fine-Tuning](https://github.com/modelscope/ms-swift/blob/main/examples/train/lora_sft.sh) | [✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/full/train.sh) | ✅    | [✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/qlora) | [✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multi-gpu/deepspeed) | [✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multi-node) | [✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multimodal) |
| [GRPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/grpo) | ✅                                                            | ✅    | ✅                                                            | ✅                                                            | ✅                                                            | ✅                                                            |
| [GKD](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/gkd) | ✅                                                            | ✅    | ✅                                                            | ✅                                                            | ✅                                                            | [✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/multimodal/rlhf/gkd) |
| [PPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/ppo) | ✅      
