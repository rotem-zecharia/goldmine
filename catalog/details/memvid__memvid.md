# memvid/memvid

Memory layer for AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. Give your agents instant retrieval and long-term memory.

## requirements

-   **Rust 1.85.0+** — Install from [rustup.rs](https://rustup.rs)

## features

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `lex`               | Full-text search with BM25 ranking (Tantivy)                     |
| `pdf_extract`       | Pure Rust PDF text extraction                                    |
| `vec`               | Vector similarity search (HNSW + local text embeddings via ONNX) |
| `clip`              | CLIP visual embeddings for image search                          |
| `whisper`           | Audio transcription with Whisper                                 |
| `api_embed`         | Cloud API embeddings (OpenAI)                                    |
| `temporal_track`    | Natural language date parsing ("last Tuesday")                   |
| `parallel_segments` | Multi-threaded ingestion                                         |
| `encryption`        | Password-based encryption capsules (.mv2e)                       |
| `symspell_cleanup`  | Robust PDF text repair (fixes "emp lo yee" -> "employee")        |

Enable features as needed:

```toml
[dependencies]
memvid-core = { version = "2.0", features = ["lex", "vec", "temporal_track"] }
```

## installation

```rust
use memvid_core::{Memvid, PutOptions, SearchRequest};

fn main() -> memvid_core::Result<()> {
    // Create a new memory file
    let mut mem = Memvid::create("knowledge.mv2")?;

    // Add documents with metadata
    let opts = PutOptions::builder()
        .title("Meeting Notes")
        .uri("mv2://meetings/2024-01-15")
        .tag("project", "alpha")
        .build();
    mem.put_bytes_with_options(b"Q4 planning discussion...", opts)?;
    mem.commit()?;

    // Search
    let response = mem.search(SearchRequest {
        query: "planning".into(),
        top_k: 10,
        snippet_chars: 200,
        ..Default::default()
    })?;

    for hit in response.hits {
        println!("{}: {}", hit.title.unwrap_or_default(), hit.text);
    }

    Ok(())

## tools

The `examples/` directory contains working examples:
