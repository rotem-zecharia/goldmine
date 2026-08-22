# memvid/memvid

Memory layer for AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. Give your agents instant retrieval and long-term memory.

## requirements

-   **Rust 1.85.0+** — Install from [rustup.rs](https://rustup.rs)

### Add to Your Project

```toml
[dependencies]
memvid-core = "2.0"
```

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
}
```

---

## Build

Clone the repository:

```bash
git clone https://github.com/memvid/memvid.git
cd memvid
```

Build in debug mode:

```bash
cargo build
```

Build in release mode (optimized):

```bash
cargo build --release
```

Build with specific features:

```bash
cargo build --release --features "lex,vec,temporal_track"
```

---

## Run Tests

Run all tests:

```bash
cargo test
```

Run tests with output:

```bash
cargo test -- --nocapture
```

Run a specific test:

```bash
cargo test test_name
```

Run integration tests only:

```bash
cargo test --test lifecycle
cargo test --test search
cargo test --test mutation
```

---

## tools

The `examples/` directory contains working examples:

### Basic Usage

Demonstrates create, put, search, and timeline operations:

```bash
cargo run --example basic_usage
```

### PDF Ingestion

Ingest and search PDF documents (uses the "Attention Is All You Need" paper):

```bash
cargo run --example pdf_ingestion
```

### CLIP Visual Search

Image search using CLIP embeddings (requires `clip` feature):

```bash
cargo run --example clip_visual_search --features clip
```

### Whisper Transcription

Audio transcription (requires `whisper` feature):

```bash
cargo run --example test_whisper --features whisper -- /path/to/audio.mp3
```

**Available Models:**

| Model                 | Size   | Speed   | Use Case                            |
| --------------------- | ------ | ------- | ----------------------------------- |
| `whisper-small-en`    | 244 MB | Slowest | Best accuracy (default)             |
| `whisper-tiny-en`     | 75 MB  | Fast    | Balanced                            |
| `whisper-tiny-en-q8k` | 19 MB  | Fastest | Quick testing, resource-constrained |

**Model Selection:**

```bash
# Default (FP32 small, highest accuracy)
cargo run --example test_whisper --features whisper -- audio.mp3

# Quantized tiny (75% smaller, faster)
MEMVID_WHISPER_MODEL=whisper-tiny-en-q8k cargo run --example test_whisper --features whisper -- audio.mp3
```

**Programmatic Configuration:**

```rust
use memvid_core::{WhisperConfig, WhisperTranscriber};

// Default FP32 small model
let config = WhisperConfig::default();

// Quantized tiny model (faster, smaller)
let config = WhisperConfig::with_quantization();

// Specific model
let config = WhisperConfig::with_model("whisper-tiny-en-q8k");

let transcriber = WhisperTranscriber::new(&config)?;
let result = transcriber.transcribe_file("audio.mp3")?;
println!("{}", result.text);
```


## Text Embedding Models

The `vec` feature includes local text embedding support using ONNX models. Before using local text embeddings, you need to download the model files manually.
