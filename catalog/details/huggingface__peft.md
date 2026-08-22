# huggingface/peft

🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning.

## installation

Install PEFT from pip:

```bash
pip install peft
```

Prepare a model for training with a PEFT method such as LoRA by wrapping the base model and PEFT configuration with `get_peft_model`. For the bigscience/mt0-large model, you're only training 0.19% of the parameters!

```python
import torch
from transformers import AutoModelForCausalLM
from peft import LoraConfig, TaskType, get_peft_model

device = torch.accelerator.current_accelerator().type if hasattr(torch, "accelerator") else "cuda"
model_id = "Qwen/Qwen2.5-3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map=device)
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    task_type=TaskType.CAUSAL_LM,
    # target_modules=["q_proj", "v_proj", ...]  # optionally indicate target modules
)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()

## features

There are many benefits of using PEFT but the main one is the huge savings in compute and storage, making PEFT applicable to many different use cases.
