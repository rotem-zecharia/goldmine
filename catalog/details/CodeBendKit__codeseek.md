# CodeBendKit/codeseek

Rust-powered code intelligence CLI for AI coding agents. Builds call graphs and hybrid semantic search indexes (Dense + Sparse + RRF + Reranker) across 7 languages. Ships as native MCP tools for Claud

## installation

```bash

## tools

codeseek install

## configuration

`~/.codeseek/config.json`:

```json
{
  "embedding": {
    "provider": "openai-compatible",
    "model": "Qwen/Qwen3-Embedding-4B",
    "api_token": "sk-...",
    "api_base_url": "https://api.siliconflow.cn/v1",
    "dimensions": 2560
  },
  "index": {
    "min_code_block_length": 16,
    "enable_reranker": true,
    "hybrid": {
      "enable_bm25": true,
      "bm25_top_k": 20,
      "vector_top_k": 20,
      "rrf_k": 60,
      "rrf_top_k": 20
    },
    "reranker": {
      "enabled": true,
      "model": "Qwen/Qwen3-Reranker-4B",
      "api_token": "sk-...",
      "api_base_url": "https://api.siliconflow.cn/v1/rerank",
      "top_n": 5,
      "candidate_multiplier": 5,
      "timeout_secs": 60
    }
  },
  "installed_hooks": {}
