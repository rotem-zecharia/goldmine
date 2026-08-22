# microsoft/kernel-memory

Research project. A Memory solution for users, teams, and applications.

## tools

The example show the default documents ingestion pipeline:

1. Extract text: automatically recognize the file format and extract the information
2. Partition the text in small chunks, ready for search and RAG prompts
3. Extract embeddings using any LLM embedding generator
4. Save embeddings into a vector index such as
   [Azure AI Search](https://learn.microsoft.com/azure/search/vector-search-overview),
   [Qdrant](https://qdrant.tech/) or other DBs.

The example shows how to **safeguard private information** specifying who owns each document, and
how to **organize data** for search and faceted navigation, using **Tags**.
