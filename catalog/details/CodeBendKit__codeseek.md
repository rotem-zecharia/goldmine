# CodeBendKit/codeseek

Rust-powered code intelligence CLI for AI coding agents. Builds call graphs and hybrid semantic search indexes (Dense + Sparse + RRF + Reranker) across 7 languages. Ships as native MCP tools for Claud

## installation

```bash
# Install via npm (handles setup wizard + binary download automatically)
npm install -g codeseek

# First run — interactive setup wizard configures your embedding model
codeseek

# Index your project
codeseek init

# Search code by symbol name
codeseek search main --limit 10

# Query call graph
codeseek callers main
codeseek callees process_data

## tools

codeseek install

# Check status
codeseek status

# Auto-index on git commits
codeseek install-hooks
```

Natural Language Code Search example

```bash
╰─$ codeseek search 'how the code embedding work'
1. get_embedding (0.7973)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
2. EmbeddingService (0.2855)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
3. EmbeddingData (0.1449)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
4. EmbeddingResponse (0.1304)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
5. default_model (0.0450)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/config.rs:0

```

Function Call Graph example

```bash
╰─$ codeseek callgraph apply_rerank
Call graph for 'apply_rerank' (depth=1):

== Callers (upstream, depth=1) ==
  search (/home/do/ssd/iohub/dev/codeseek/rust-core/src/services/hybrid_search.rs:210)

== Callees (downstream, depth=1) ==
  rerank (/home/do/ssd/iohub/dev/codeseek/rust-core/src/services/reranker_service.rs:331)
  config (/home/do/ssd/iohub/dev/codeseek/rust-core/src/services/hybrid_search.rs:325)

```

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
}
```

### Model Roles

| Model | Role | When |
|-------|------|------|
| `Qwen/Qwen3-Embedding-4B` | Converts code → vectors for dense search | Index building |
| `Qwen/Qwen3-Reranker-4B` | Scores (query, code) pairs for precision | Search time |

Set via the interactive wizard on first run, or create manually.

## Development

```bash
cd rust-core

# Build
cargo build
