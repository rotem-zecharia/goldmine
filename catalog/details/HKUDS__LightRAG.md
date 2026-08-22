# HKUDS/LightRAG

[EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation

## installation

**💡 Using uv for Package Management**: This project uses [uv](https://docs.astral.sh/uv/) for fast and reliable Python package management. Install uv first: `curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix/macOS) or `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` (Windows)

> **Note**: You can also use pip if you prefer, but uv is recommended for better performance and more reliable dependency management.
>
> **📦 Offline Deployment**: For offline or air-gapped environments, see the [Offline Deployment Guide](./docs/OfflineDeployment.md) for instructions on pre-installing all dependencies and cache files.

## configuration

make dev
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)

## tools

lightrag-server
```

* Launching the LightRAG Server with Docker Compose

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
cp env.example .env  # Update the .env with your LLM and embedding configurations

## features

- **Deep Contextual Understanding:** Through graph-structured indexing, LightRAG captures complex semantic dependencies between entities, overcoming the fragmented context limitations typical of traditional chunk-based retrieval methods. Its generation quality and context awareness are particularly outstanding in vertical domains (e.g., legal, financial) that require global comprehension or logical reasoning.
- **Exceptional Comprehensiveness & Diversity:** LightRAG’s dual-level retrieval mechanism allows it to integrate detailed facts and abstract concepts concurrently. This enables the system to achieve remarkable performance in query result comprehensiveness and diversity, making it highly effective at handling complex, cross-document queries.
- **Extreme Retrieval Efficiency & Low Cost:** LightRAG does not rely on inefficient community reports or multi-hop reasoning for complex queries. This drastically reduces the number of LLM calls required during both the indexing and querying phases, significantly lowering response latency and LLM computational costs.
- **Incremental Updates & Selective Deletion:** LightRAG addresses the challenges of incrementally updating and selectively deleting content from graph-based knowledge bases, keeping them current in dynamic data environments. When a document is deleted, the system can use the LLM cache created during indexing to quickly rebuild the affected entities and relationships, substantially improving update efficiency.
- **Multiple Document Parsing Engines:** LightRAG's document processing pipeline supports MinerU, Docling, and Native and can be extended with third-party parsers. LightRAG's Native engine efficiently parses images, tables, and formulas in Word and Markdown documents, making it especially suitable for documents rich in multimodal content. The Native engine also automatically detects and corrects section headings in Word documents, improving content extraction from documents with inconsistent outlines and laying the foundation for section-aware text chunking.
- **Multiple Text Chunking Strategies:** LightRAG supports four text chunking strategies: `Fixed-length (F)`, `Recursive character (R)`, `Vector semantic (V)`, and `Paragraph semantic (P)`. The LightRAG-native `Paragraph semantic (P)` strategy **aligns chunk boundaries with the document's native semantic boundaries**—headings, paragraphs, and tables—as closely as possible. This reduces problems such as mismatched headings and content or missing header rows when long tables are split.
- **Multiple Storage Backends:** LightRAG's default KV, vector, and graph stores use in-memory databases with local file persistence, making them well suited for quickly evaluating the project. LightRAG also supports a wide range of commonly used storage backends for production deployments with large datasets.
