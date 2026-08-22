# cactus-compute/needle

14MB foundation model for tiny devices; phones, wearables, smart home, and robots.

## installation

```sh
pip install cactus-needle
```

Needle reads your tool descriptions to decide what to call and how to fill arguments, so describing them well is the whole game.

**Simple**: decorate a function. The signature gives the argument types, the docstring is the tool description, and `run()` completes the loop: model picks the call, Needle executes your function, feeds the result back, and returns the final response with the executed tool results attached as `results`.

```python
import needle

@needle.tool
def get_weather(city: str):
    "Get the current weather for a city."
    return {"city": city, "temp_c": 27, "sky": "clear"}

agent = needle.Needle(tools=[get_weather])
print(agent.run("what's it like in Lagos right now?")["results"])
# [{'city': 'Lagos', 'temp_c': 27, 'sky': 'clear'}]
```

**Extraction**: to pull structured data out of text, declare the shape and call `extract()`. Pass a Pydantic model and you get a typed object back.

```python
from pydantic import BaseModel

class Invoice(BaseModel):
    vendor: str
    total: float
    due_date: str

invoice = needle.extract("Invoice from Acme Corp, $1,200.00, due 2026-09-01", Invoice)
print(invoice.vendor, invoice.total)   # -> Acme Corp 1200.0
```

Per argument descriptions and choices, value constraints compiled into the decode grammar, raw JSON schemas, driving the loop with `complete()`, the response contract, system facts, tool retrieval, and confidence gating are all covered in [doc/apis.md](doc/apis.md).

## Playground

Try any model in the browser: pick a preset, edit the tools or prompt, and Run. Follow-up queries continue the same conversation.

```sh
needle playground                      # base model, http://127.0.0.1:7860
needle playground --weights my.cact    # a tuned model
```

The server downloads and initializes the model before serving, so the first query is instant. The **Finetune on these tools** button runs the fine-tuning pipeline below from the UI and hands back a downloadable `.cact`.

## Fine-tuning

Needle fine-tunes with LoRA on the frozen base and merges the adapter at export, so a run is cheap and the tuned model is still a single `.cact` that runs on the same engine. The workflow is: (optionally) synthesize data, LoRA fine-tune, then build a tuned `.cact`. See [doc/finetuning.md](doc/finetuning.md) for dataset sizing, reading the loss curve, and troubleshooting.

**Data format.** A JSONL file, one example per line. `reasoning` is optional; an off-topic example has `answers: []`.

```json
{"query": "dim the kitchen to 10", "tools": [{"name": "set_lights", "parameters": {"type": "object", "properties": {"room": {"type": "string"}, "brightness": {"type": "integer"}}, "required": ["room"]}}], "answers": [{"name": "set_lights", "arguments": {"room": "kitchen", "brightness": 10}}], "reasoning": "'kitchen' -> room; 'dim to 10' -> brightness 10"}
```

**1. Synthesize data (optional).** Needs `OPENROUTER_API_KEY`. Seed from a tool schema file, or expand an existing set:

```sh
export OPENROUTER_API_KEY=sk-or-...
needle generate-data --tools my_tools.json --num-samples 500 --output data.jsonl
needle generate-data --augment data.jsonl --num-samples 500      # expand an existing JSONL
```

Set `OPENROUTER_URL` to use an OpenAI-compatible gateway instead of the default OpenRouter endpoint.

**2. LoRA fine-tune.** The base checkpoint auto-downloads from Hugging Face if you do not pass `--checkpoint`. `--generate N` first synthesizes N more examples from the tools in your data (also needs `OPENROUTER_API_KEY`).

```sh
needle finetune data.jsonl --epochs 10
needle finetune data.jsonl --epochs 10 --generate 300 --lora-rank 16 --lora-alpha 32
```

Key options: `--epochs` (default 3), `--lora-rank` (16), `--lora-alpha` (32), `--lr` (1e-4), `--batch-size` (16), `--max-len` (1024), `--val-split` (0.1), `--checkpoint <base.pkl>`, `--out <adapter.pkl>`. The adapter is written to `checkpoints/needle_lora.pkl`. A validation loss prints each epoch from the held out
