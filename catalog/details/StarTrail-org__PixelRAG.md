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

## features

curl -X POST http://localhost:30001/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "Overview of PixelRAG and the diagram"}], "n_docs": 1}'
```

</details>

## tools

Each stage runs independently, without the orchestrator:

```bash
pip install 'pixelrag[embed]'

pixelrag chunk --tiles-dir ./tiles
pixelrag embed --shard-dir ./tiles --output-dir ./embeddings --gpu-ids 0,1
pixelrag build-index --embeddings-dir ./embeddings --output-dir ./index
```
