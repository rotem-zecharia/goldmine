# qualcomm/GenieX

Run frontier LLMs and VLMs locally on Qualcomm devices across NPU, GPU, and CPU with a few lines of code

## installation

Pick your interface below. Each one follows the same three steps — **Install**, **Run**, and **Docs** — and shows both runtimes: a **GGUF** model from Hugging Face (`llama_cpp`) and a **pre-compiled bundle** from Qualcomm AI Hub (`qairt`, NPU).

### CLI

![Windows ARM64](https://img.shields.io/badge/Windows%20ARM64-0078D6?style=flat-square&logo=windows&logoColor=white) ![Linux ARM64](https://img.shields.io/badge/Linux%20ARM64-FCC624?style=flat-square&logo=linux&logoColor=black)

**Install**

- **Windows ARM64** — [download the installer](https://github.com/qualcomm/GenieX/releases), run it, then open a new terminal.
- **Linux ARM64** — one line, no `sudo`:
  ```bash
  curl -fsSL https://qaihub-public-assets.s3.us-west-2.amazonaws.com/qai-hub-geniex/install.sh | sh
  ```

**Run** — chat with any model in one line (drag in an image for VLMs):

```bash
# GGUF from Hugging Face → llama.cpp (NPU / GPU / CPU)
geniex infer google/gemma-4-E4B-it-qat-q4_0-gguf

# Pre-compiled bundle from Qualcomm AI Hub → Qualcomm AI Engine Direct (NPU)
geniex infer ai-hub-models/Qwen2.5-VL-7B-Instruct

# GGUF from Docker Hub (https://hub.docker.com/u/ai) → llama.cpp (NPU / GPU / CPU)
geniex infer docker.io/ai/gemma3
```

📖 **Docs** — [Install](https://geniex.aihub.qualcomm.com/en/run/cli/install) · [Quickstart](https://geniex.aihub.qualcomm.com/en/run/cli/quickstart) · [Command reference](https://geniex.aihub.qualcomm.com/en/run/cli/reference)

### Python

![Windows ARM64](https://img.shields.io/badge/Windows%20ARM64-0078D6?style=flat-square&logo=windows&logoColor=white) ![Linux ARM64](https://img.shields.io/badge/Linux%20ARM64-FCC624?style=flat-square&logo=linux&logoColor=black)

**Install**

```bash
pip install geniex
```

**Run** — mirrors Hugging Face `transformers` (`from_pretrained()` → `.generate()`):

```python
# GGUF from Hugging Face → llama.cpp
from geniex import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("unsloth/Qwen3.5-2B-GGUF", precision="Q4_0")

messages = [{"role": "user", "content": "What is 2+2?"}]
prompt = model.tokenizer.apply_chat_template(messages, add_generation_prompt=True)

for chunk in model.generate(prompt, max_new_tokens=256, stream=True):
    print(chunk, end="", flush=True)

model.close()
```

```python
# Pre-compiled bundle from Qualcomm AI Hub → Qualcomm AI Engine Direct (NPU)
from geniex import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("ai-hub-models/Qwen3-4B")

messages = [{"role": "user", "content": "What is 2+2?"}]
prompt = model.tokenizer.apply_chat_template(messages, add_generation_prompt=True)

for chunk in model.generate(prompt, max_new_tokens=256, stream=True):
    print(chunk, end="", flush=True)

model.close()
```

📖 **Docs** — [Install](https://geniex.aihub.qualcomm.com/en/run/python/install) · [Quickstart](https://geniex.aihub.qualcomm.com/en/run/python/quickstart) · [API reference](https://geniex.aihub.qualcomm.com/en/run/python/api-reference)

### OpenAI-compatible server

![Windows ARM64](https://img.shields.io/badge/Windows%20ARM64-0078D6?style=flat-square&logo=windows&logoColor=white) ![Linux ARM64](https://img.shields.io/badge/Linux%20ARM64-FCC624?style=flat-square&logo=linux&logoColor=black)

**Install** — ships with the CLI ([install above](#cli)).

**Run** — pull any model (GGUF or Qualcomm AI Hub bundle), then serve an OpenAI-compatible API:

```bash
geniex pull ai-hub-models/Qwen3-4B-Instruct-2507
geniex serve   # serves http://127.0.0.1:18181/v1
```

```bash
curl http://127.0.0.1:18181/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ai-hub-models/Qwen3-4B-Instruct-2507",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Point any OpenAI client at `http://127.0.0.1:18181/v1` — no code changes.

📖 **Docs** — [Local server guide](https://geniex.aihub.qualcomm.com/en/run/cli/local-server)

### Android (Kotlin / Java)

![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=andr
