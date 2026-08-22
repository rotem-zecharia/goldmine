# StarTrail-org/PixelRAG

The end of web parsing. The beginning of scalable pixel-native search. link: https://pixelrag.ai/

## installation

curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'
```

> **Live, hosted endpoint** — [`https://api.pixelrag.ai`](https://api.pixelrag.ai/status) serves a
> pre-built index of **8.28M Wikipedia pages**. No setup, no API key. It even takes an image as the query
> ([visual search](https://pixelrag.ai/docs#search)) — see the **[API reference →](https://pixelrag.ai/docs)**.

Or try it in the browser at **[pixelrag.ai](https://pixelrag.ai)**, or run the demo notebook in
Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/StarTrail-org/PixelRAG/blob/main/demos/quickstart.ipynb) — it
renders a page and searches the hosted index, with the images inline.

## What it is

PixelRAG renders documents — web pages, PDFs, images — as screenshots and retrieves over the
images directly. Visual structure that HTML parsing throws away — tables, charts, layout,
infographics — stays intact, so the reader model can actually answer questions about it.
Wikipedia's 8.28M articles ship as a pre-built index; the pipeline itself is general-purpose.

## Give Claude eyes

The renderer also ships as a Claude Code plugin — the **pixelbrowse** skill. Instead of fetching
raw HTML, Claude screenshots a page with `pixelshot` and _reads the image_, so it sees
charts, diagrams, tables, and layout the way a person does.

Install it — no clone needed. Install the `pixelshot` CLI so it's on your `PATH`
(use `uv tool` or `pipx` to keep it isolated yet always available to Claude — a
plain `pip install` into a project venv may leave `pixelshot` off `PATH`):

```bash
uv tool install pixelrag                            # pixelshot on PATH (or: pipx install pixelrag)
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```

Then just ask Claude to look at a page:

```bash
claude -p "screenshot https://news.ycombinator.com and summarize the top stories"
claude -p "screenshot https://arxiv.org/abs/2404.12387 and explain the key findings"
```

Or use the slash command in an interactive session: `/screenshot https://example.com`.
No MCP server, no backend: the skill just calls `pixelshot` (Playwright/CDP) on your machine.

## How it works

<p align="center">
  <img src="docs/assets/pipeline.png" alt="Text-based RAG parses to text and loses the table; PixelRAG renders to screenshot tiles and keeps it" width="100%">
</p>

Text-based RAG parses the page to text chunks and **loses the table** — the reader can't find the
answer. PixelRAG renders the page to **screenshot tiles**, retrieves the right tile, and the reader
reads the number straight off the image.

Two pieces make this work: (1) rendering documents to images instead of parsing them to text, and
(2) a `Qwen3-VL-Embedding` model, LoRA-fine-tuned on screenshot data, that embeds page images into
a space where visual content is retrievable.

## Pipelines

Capture is the standalone `pixelshot` command; the rest of the pipeline runs through the
`pixelrag` umbrella — `pixelrag <stage>`. Install only the stages you need:

| Command                                    | What it does                                                    | Install                         |
| ------------------------------------------ | --------------------------------------------------------------- | ------------------------------- |
| `pixelshot`                                | Document → image tiles (Playwright CDP, PDF)                    | `pip install pixelrag`          |
| `pixelrag chunk` · `embed` · `build-index` | Tiles → vectors → FAISS index                                   | `pip install 'pixelrag[embed]'` |
| `pixelrag index`                           | Orchestrates the full pipeline: source → ingest → embed → index | `pip install 'pixelrag[index]'` |
| `pixelrag serve`                           | FAISS sea

## configuration

cat > pixelrag.yaml << 'EOF'
source:
  type: local
  path: ./paper.pdf

embed:
  model: Qwen/Qwen3-VL-Embedding-2B
  device: auto

output: ./paper_index
EOF

# 3. Build the index (~3 min on Apple M-series, ~1 min on GPU)
pixelrag index build

# 4. Serve it
pixelrag serve --index-dir ./paper_index --port 30001

## features

curl -X POST http://localhost:30001/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "Overview of PixelRAG and the diagram"}], "n_docs": 1}'
```

</details>

### Render a page programmatically

```python
from pixelrag_render import render_url

# render a single page to tiles — e.g. for an agent to read
tiles = render_url("https://en.wikipedia.org/wiki/Python", "./tiles")
```

The same rendering is available as a CLI — `pixelshot` ships with `pip install pixelrag`:

```bash
# Web page → tiles (headless Chromium via CDP)
pixelshot https://en.wikipedia.org/wiki/Python -o ./tiles

## tools

Each stage runs independently, without the orchestrator:

```bash
pip install 'pixelrag[embed]'

pixelrag chunk --tiles-dir ./tiles
pixelrag embed --shard-dir ./tiles --output-dir ./embeddings --gpu-ids 0,1
pixelrag build-index --embeddings-dir ./embeddings --output-dir ./index
```

### Qdrant backend

[Qdrant](https://qdrant.tech) is an open-source vector search engine for high-performance and massive scale. [FAISS](https://ai.meta.com/tools/faiss/) remains the default for local indexes. Use Qdrant for configurable quantization, disk-backed vectors, payload filtering, and one collection shared by multiple PixelRAG servers.

Quantization compresses vectors to reduce memory use and speed up search, with a recall tradeoff that depends on the method and settings.

To configure quantization, pass any Qdrant `quantization_config` object in a JSON file.
See Qdrant's [quantization guide](https://qdrant.tech/documentation/manage-data/quantization/#setting-up-quantization-in-qdrant) for supported methods and parameters.

```json
{
  "scalar": {
    "type": "int8",
    "quantile": 0.99,
    "always_ram": true
  }
}
```

```bash
pip install 'pixelrag[serve,qdrant]'   # or 'pixelrag[index,qdrant]'

# Build against a Qdrant server.
# Start one locally with: docker run -p 6333:6333 qdrant/qdrant
pixelrag build-index --embeddings-dir ./embeddings --output-dir ./index \
    --backend qdrant --qdrant-url http://localhost:6333 --collection pixelrag \
    --qdrant-quantization-config ./quantization.json

# Add documents to an existing collection.
pixelrag build-index --embeddings-dir ./more --output-dir ./index \
    --backend qdrant --qdrant-url http://localhost:6333 --collection pixelrag --append
