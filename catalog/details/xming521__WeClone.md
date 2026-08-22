# xming521/WeClone

🚀 One-stop solution for creating your AI twin from chat history 💡 Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life.

## features

- 💫 Complete end-to-end solution for creating digital avatars, including chat data export, preprocessing, model training, and deployment
- 💬 Fine-tune LLM using chat history with support for image modal data, infusing it with that authentic "flavor"
- 🔗 Integrate with Telegram, WhatsApp (coming soon) to create your own digital avatar
- 🛡️ Privacy information filtering with localized fine-tuning and deployment for secure and controllable data

## requirements

The project uses Qwen2.5-VL-7B-Instruct model by default with LoRA method for SFT stage fine-tuning. You can also use other models and methods supported by [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory/tree/main#supported-models).

Estimated VRAM requirements: 
| Method                          | Precision |   7B  |  14B  |  30B  |   70B  |   `x`B  |
| ------------------------------- | --------- | ----- | ----- | ----- | ------ | ------- |
| Full (`bf16` or `fp16`)         |    32     | 120GB | 240GB | 600GB | 1200GB | `18x`GB |
| Full (`pure_bf16`)              |    16     |  60GB | 120GB | 300GB |  600GB |  `8x`GB |
| Freeze/LoRA/GaLore/APOLLO/BAdam |    16     |  16GB |  32GB |  64GB |  160GB |  `2x`GB |
| QLoRA                           |     8     |  10GB |  20GB |  40GB |   80GB |   `x`GB |
| QLoRA                           |     4     |   6GB |  12GB |  24GB |   48GB | `x/2`GB |
| QLoRA                           |     2     |   4GB |   8GB |  16GB |   24GB | `x/4`GB |

## installation

1. CUDA installation (skip if already installed, **requires version 12.6 or above**)

2. It is recommended to use [uv](https://docs.astral.sh/uv/) to install dependencies, which is a very fast Python environment manager. After installing uv, you can use the following commands to create a new Python environment and install dependencies. 
```bash
git clone https://github.com/xming521/WeClone.git && cd WeClone
uv venv .venv --python=3.12
source .venv/bin/activate # windows .venv\Scripts\activate
uv pip install --group main -e . 
```

3. Copy the configuration file template and rename it to `settings.jsonc`, and make subsequent configuration changes in this file:

```bash
cp examples/tg.template.jsonc settings.jsonc
```

> [!NOTE]
> Training and inference related configurations are unified in the file `settings.jsonc`

4. Use the following command to test whether the CUDA environment is correctly configured and can be recognized by PyTorch (not needed for Mac):
```bash
  python -c "import torch; print('CUDA Available:', torch.cuda.is_available());"
```

5. (Optional) Install FlashAttention to accelerate training and inference: `uv pip install flash-attn --no-build-isolation`.

## configuration

- (Optional) Modify `model_name_or_path`, `template`, `lora_target` in `settings.jsonc` to select other locally downloaded models.   
- Modify `per_device_train_batch_size` and `gradient_accumulation_steps` to adjust VRAM usage.  
- You can modify parameters like `num_train_epochs`, `lora_rank`, `lora_dropout` in `train_sft_args` based on your dataset's quantity and quality.

## tools

```bash
weclone-cli server
```

## limitations

- [ ] Support more data sources
- [ ] Richer context: including contextual conversations, chat participant information, time, etc.
- [ ] Memory support
- [ ] Multimodal support: image support already implemented
- [ ] Data augmentation
- [ ] GUI support
- [ ] COT (Chain of Thought) thinking support
