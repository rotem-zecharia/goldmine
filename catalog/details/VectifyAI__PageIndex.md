# VectifyAI/PageIndex

📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG

## installation

```bash
pip install -U pageindex
```


```python
import os
from pageindex import PageIndexClient

os.environ["OPENAI_API_KEY"] = "your-openai-key"

client = PageIndexClient(                     
    index_model="gpt-5.6-luna",               # model to build the tree index
    chat_model="gpt-5.6-sol",                 # model to search the tree
)
doc_id = client.submit_document("report.pdf")["doc_id"]

answer = client.chat("What was the 2023 operating margin, and where is it stated?",
                     doc_id=doc_id)
print(answer)
```


### Model Recommendations

- **`index_model` — a basic model is sufficient.** The index model generates the document's tree index. A basic model is sufficient to produce a good tree structure.
- **`chat_model` — use the best model you can afford.** The chat model searches the tree to retrieve information. See [Query cost and accuracy](#query-cost-and-accuracy).

See the [Detailed Usage Guide](#detailed-usage-guide) to configure other models and integrate PageIndex with your own agent.


## Benchmarks

### Indexing cost

Building a tree locally runs **about $0.001 per page** with `index_model="gpt-5.6-luna"` — so a 1,000-page textbook costs a little over a dollar and a few minutes, once, and every later question reuses it. PageIndex is designed not to rely heavily on the model used at index time, so in our experiments a basic model does not hurt quality.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/index-cost-dark.png">
  <img src="assets/index-cost-light.png" alt="Indexing cost against document length, log-log, for nine PDFs from 9 to 1,098 pages. Points track a $0.0011-per-page reference line; the spread around it is text density, not length.">
</picture>



### Query cost and accuracy

[**PageIndex-OSS-Benchmark**](https://github.com/VectifyAI/PageIndex-OSS-Benchmark) measures exactly the setup in the quickstart above — `PageIndexClient()` in local mode, flash indexing, no OCR — on 62 lookup questions over 34 PDFs (1,945 pages) drawn from [MMLongBench-Doc-V2](https://github.com/VectifyAI/MMLongBench-Doc-V2). Every question's answer is a fact stated in running text, so a wrong answer is a **retrieval or reading failure**, not a reasoning one.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/results-dark.png">
  <img src="assets/results-light.png" alt="Accuracy against average cost per question. Each model forms a near-vertical reasoning-effort ladder; moving between models costs an order of magnitude a step.">
</picture>


Full results, data, and the runner are in the [benchmark repo](https://github.com/VectifyAI/PageIndex-OSS-Benchmark).




<a id="detailed-usage-guide"></a>
<details>
<summary>

## tools

</summary>

<br>

### ⚙️ Step 1: Initialize the client

Create a local client and choose the models used for indexing and retrieval:

```python
from pageindex import PageIndexClient
import os

client = PageIndexClient(
    index_model="gpt-5.6-luna",
    chat_model="gpt-5.6-sol",
    storage_path=".pageindex",
)
```

- **`index_model`** builds the tree index. A basic model is sufficient.

- **`chat_model`** searches the tree and answers questions. Use the best model you can afford.

- **`storage_path`** specifies where indexed documents are stored locally.

#### Model naming conventions

Model names follow [LiteLLM's naming convention](https://docs.litellm.ai/docs/providers). Choose the format that matches your provider:

**OpenAI** — use the model name directly and set `OPENAI_API_KEY`:

```python
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
chat_model = "gpt-5.6-sol"
```

**Anthropic** — prefix the model name with `anthropic/` and set `ANTHROPIC_API_KEY`:

```python
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-api-key"
chat_model = "anthropic/claude-sonnet-4-6"
```

**OpenRouter** — prefix the provider and model name with `openrouter/` and set `OPENROUTER_API_KEY`:

```python
os.environ["OPENROUTER_API_KEY"] = "your-openrouter-api-key"
chat_model = "openrouter/anthropic/claude-sonnet-4-6"
```

For model names and API key settings for other providers, see the [LiteLLM provider documentation](https://docs.litellm.ai/docs/providers).


<a id="step-2-build-the-tree-index"></a>

### 🌲 Step 2: Build the tree index

`submit_document` defaults to **Flash** indexing: the structure is extracted from the PDF's own layout (no LLM), and a model is called only for node summaries and the tree-optimization expansion pass. It takes seconds.

```python
doc_id = client.submit_document("report.pdf")["doc_id"]
```

Inspect what you got:

```python
tree = client.get_document_structure(doc_id)    # titles, page ranges, summaries — no text
client.list_documents()                         # everything you have indexed
```

A PageIndex tree looks like this — a table of contents optimized for LLMs and agents:

```jsonc
{
  "title": "Financial Stability",
  "node_id": "0006",
  "start_index": 21,
  "end_index": 22,
  "summary": "The Federal Reserve ...",
  "nodes": [
    {
      "title": "Monitoring Financial Vulnerabilities",
      "node_id": "0007",
      "start_index": 22,
      "end_index": 28,
      "summary": "The Federal Reserve's monitoring ..."
    },
    {
      "title": "Domestic and International Cooperation and Coordination",
      "node_id": "0008",
      "start_index": 28,
      "end_index": 31,
      "summary": "In 2023, the Federal Reserve collaborated ..."
    }
  ]
}
```

See more example [documents](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents) and generated [tree structures](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents/results).




### 💬 Step 3: Ask questions

`chat()` is the one-line surface. Underneath it is a document-QA agent, and you can talk to it over whichever protocol your stack already speaks:

**Get a simple answer with `chat()`:**

```python
client.chat("What changed in the risk factors?", doc_id=doc_id)
```

Pass a string or role/content history and get the answer back.

**Stream the answer:**

```python
client.chat(question, doc_id=doc_id, stream=True)
```

Returns the answer as text chunks.

**Use the OpenAI Chat Completions format:**

```python
client.chat_completions(messages, doc_id=doc_id)
```

Returns the full envelope, including token usage, streaming metadata, and `finish_reason`.

**Use the OpenAI Responses format:**

```python
client.responses("...", doc_id=doc_id, reasoning={"effort": "high"})
```

Returns the agent's process transcript in `items`. Append those items to the next call's `input` to preserve memory and benefit from provider prompt caching. This requires a Responses-compatible backend in local mode.

**Use the Anthropic Messages format:
