# HKUDS/LightRAG

[EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation

## installation

**💡 Using uv for Package Management**: This project uses [uv](https://docs.astral.sh/uv/) for fast and reliable Python package management. Install uv first: `curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix/macOS) or `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` (Windows)

> **Note**: You can also use pip if you prefer, but uv is recommended for better performance and more reliable dependency management.
>
> **📦 Offline Deployment**: For offline or air-gapped environments, see the [Offline Deployment Guide](./docs/OfflineDeployment.md) for instructions on pre-installing all dependencies and cache files.

### Install LightRAG Server

* Install from PyPI

```bash
### Install LightRAG Server as tool using uv (recommended)
uv tool install "lightrag-hku[api]"

### Or using pip
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install "lightrag-hku[api]"

# Setup env file
# Obtain the env.example file by downloading it from the GitHub repository root
# or by copying it from a local source checkout.
cp env.example .env  # Update the .env with your LLM and embedding configurations
# Launch the server. It binds to all interfaces (0.0.0.0) by default.

## tools

# 127.0.0.1 for local-only access; without auth every endpoint is public.
# Note: the Ollama-compatible /api/* routes stay open by default for client
# compatibility; set WHITELIST_PATHS=/health to require auth on them too.
lightrag-server
```

* Installation from Source

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG

## configuration

make dev
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# Or on Windows: .venv\Scripts\activate

## features

- **Deep Contextual Understanding:** Through graph-structured indexing, LightRAG captures complex semantic dependencies between entities, overcoming the fragmented context limitations typical of traditional chunk-based retrieval methods. Its generation quality and context awareness are particularly outstanding in vertical domains (e.g., legal, financial) that require global comprehension or logical reasoning.
- **Exceptional Comprehensiveness & Diversity:** LightRAG’s dual-level retrieval mechanism allows it to integrate detailed facts and abstract concepts concurrently. This enables the system to achieve remarkable performance in query result comprehensiveness and diversity, making it highly effective at handling complex, cross-document queries.
- **Extreme Retrieval Efficiency & Low Cost:** LightRAG does not rely on inefficient community reports or multi-hop reasoning for complex queries. This drastically reduces the number of LLM calls required during both the indexing and querying phases, significantly lowering response latency and LLM computational costs.
- **Incremental Updates & Selective Deletion:** LightRAG addresses the challenges of incrementally updating and selectively deleting content from graph-based knowledge bases, keeping them current in dynamic data environments. When a document is deleted, the system can use the LLM cache created during indexing to quickly rebuild the affected entities and relationships, substantially improving update efficiency.
- **Multiple Document Parsing Engines:** LightRAG's document processing pipeline supports MinerU, Docling, and Native and can be extended with third-party parsers. LightRAG's Native engine efficiently parses images, tables, and formulas in Word and Markdown documents, making it especially suitable for documents rich in multimodal content. The Native engine also automatically detects and corrects section headings in Word documents, improving content extraction from documents with inconsistent outlines and laying the foundation for section-aware text chunking.
- **Multiple Text Chunking Strategies:** LightRAG supports four text chunking strategies: `Fixed-length (F)`, `Recursive character (R)`, `Vector semantic (V)`, and `Paragraph semantic (P)`. The LightRAG-native `Paragraph semantic (P)` strategy **aligns chunk boundaries with the document's native semantic boundaries**—headings, paragraphs, and tables—as closely as possible. This reduces problems such as mismatched headings and content or missing header rows when long tables are split.
- **Multiple Storage Backends:** LightRAG's default KV, vector, and graph stores use in-memory databases with local file persistence, making them well suited for quickly evaluating the project. LightRAG also supports a wide range of commonly used storage backends for production deployments with large datasets.

### Multimodal Capability Upgrades

Traditional RAG systems lack an effective way to process multimodal content such as images, formulas, and tables in documents. Starting with v1.5, LightRAG seamlessly integrates multimodal processing into its document pipeline and query flow. Through the knowledge graph, LightRAG connects multimodal content with the body text and can use that information when answering queries to produce more accurate and reliable responses. This capability can substantially improve RAG quality for documents rich in multimodal content, such as operation manuals and academic papers.
