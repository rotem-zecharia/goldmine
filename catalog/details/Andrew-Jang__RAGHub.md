# Andrew-Jang/RAGHub

A community-driven collection of RAG (Retrieval-Augmented Generation) frameworks, projects, and resources. Contribute and explore the evolving RAG ecosystem.

## tools

Welcome to **RAGHub**, a living collection of **new and emerging frameworks, projects, and resources** in the **Retrieval-Augmented Generation (RAG)** ecosystem. This is a **community-driven project for [r/RAG](https://www.reddit.com/r/Rag/)**, where we aim to catalog the rapid growth of RAG tools and projects that are pushing the boundaries of the field.

Each day, it feels like a new tool or framework emerges, and choosing the right one is becoming more of an art than a science. Is the framework from three months ago still relevant? Or was it just hype, rehashing old concepts with a fresh look? **RAGHub exists to help you stay ahead of these changes**, providing a platform for the latest innovations in RAG.

## How to Contribute

This is a community project, and **we welcome contributions from everyone**! If you’d like to add a new framework, project, or resource, please check out our [Contribution Guidelines](CONTRIBUTING.md) for details on how to get started.

## Table of Contents

- [RAGHub: A Directory of Tools for Retrieval-Augmented Generation (RAG)](#raghub-a-directory-of-tools-for-retrieval-augmented-generation-rag)
  - [How to Contribute](#how-to-contribute)
  - [Table of Contents](#table-of-contents)
  - [RAG Frameworks](#rag-frameworks)
  - [RAG Evaluation and Optimization Frameworks](#rag-evaluation-and-optimization-frameworks)
  - [RAG Engines](#rag-engines)
  - [FAQ](#faq)
  - [RAG Resources and Sites](#rag-resources-and-sites)
  - [Model LeaderBoards](#model-leaderboards)
  - [License](#license)
  - [Join the Conversation](#join-the-conversation)


## FAQ

### What is RAG (Retrieval-Augmented Generation)?

**RAG** is a technique that enhances Large Language Model (LLM) responses by retrieving relevant information from external knowledge sources before generating answers. This approach reduces hallucinations and provides more accurate, contextually relevant responses based on actual data.

### How do I choose the right RAG framework?

Consider these factors when selecting a framework:

| Factor | Consideration |
|--------|--------------|
| **Use Case** | Chatbot, search engine, or document QA? |
| **Scale** | Enterprise-scale needs vs. prototyping |
| **Complexity** | LangChain/LlamaIndex (full-featured) vs. LightRAG (simple) |
| **Integration** | Does it support your vector DB and LLM provider? |
| **Language** | Python (LangChain/LlamaIndex) vs. TypeScript vs. Rust |

### What's the difference between RAG Frameworks and RAG Engines?

- **Frameworks** (e.g., LangChain, LlamaIndex): Libraries you integrate into your code to build custom RAG pipelines
- **Engines** (e.g., RAGFlow, Dify): Standalone platforms providing ready-to-use RAG functionality

### Do I need a vector database for RAG?

Yes, vector databases store document embeddings for semantic search. Popular options:

| Database | Best For |
|----------|---------|
| **ChromaDB** | Prototyping, easy setup |
| **Qdrant** | Production, high performance |
| **Pinecone** | Enterprise, managed service |
| **Weaviate** | Hybrid search, GraphQL |

### How do I evaluate my RAG system?

Use evaluation frameworks listed in this directory:

- **ragas**: Measures faithfulness, answer relevancy, context precision
- **Trulens**: Feedback functions for quality assessment
- **Phoenix**: Observability and troubleshooting tools
- **Deepchecks**: Continuous validation and drift detection

### What are common RAG challenges and solutions?

| Challenge | Solution |
|-----------|----------|
| **Poor retrieval quality** | Optimize chunking strategy and embeddings |
| **Context window limits** | Use reranking to reduce retrieved content |
| **Hallucinations** | Ensure retrieved context is properly used by LLM |
| **Latency** | Optimize retrieval indexing, use streaming |

### Can I use RAG with local/self-hosted models?

Yes! Many frameworks support local LLMs:

| Method | Description |
|--------|------------|
| **Ollama** | Easy local model deployment |
| **vLLM** | High-perfor
