# alibaba/zvec

A lightweight, lightning-fast, in-process vector database

## features

- **Blazing Fast**: Searches billions of vectors in milliseconds.
- **Simple, Just Works**: [Install](#-installation) and start searching in seconds. Pure local, no servers, no config, no fuss.
- **Dense + Sparse Vectors**: Support dense and sparse embeddings, multi-vector queries, and a rich selection of [vector index types](https://zvec.org/en/docs/db/concepts/vector-index/#vector-index-types) that scale from memory to disk.
- **Full-Text Search (FTS)**: Native keyword-based full-text search — query string fields with natural-language or structured expressions.
- **Hybrid Search**: Fuse vector similarity, full-text search, and structured filters in a single query for precise results.
- **Durable Storage**: Write-ahead logging (WAL) guarantees persistence — data is never lost, even on process crash or power failure.
- **Concurrent Access**: Multiple processes can read the same collection simultaneously; writes are single-process exclusive.
- **Runs Anywhere**: As an in-process library, Zvec runs wherever your code runs — notebooks, servers, CLI tools, or even edge devices.

## installation

Zvec offers official SDKs across multiple languages:

- **[Python](https://pypi.org/project/zvec/)**: `pip install zvec` (requires 64-bit Python 3.10–3.14)
- **[Node.js](https://www.npmjs.com/package/@zvec/zvec)**: `npm install @zvec/zvec`
- **[Go](https://github.com/zvec-ai/zvec-go)**: High-performance Go bindings.
- **[Rust](https://crates.io/crates/zvec-rust)**: `cargo add zvec-rust`
- **[Dart/Flutter](https://pub.dev/packages/zvec)**: `flutter pub add zvec`

Prefer a visual tool? Try **[Zvec Studio](https://github.com/zvec-ai/zvec-studio)** to browse data and debug queries — no code required.
