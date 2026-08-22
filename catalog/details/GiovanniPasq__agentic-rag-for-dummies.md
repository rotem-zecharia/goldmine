# GiovanniPasq/agentic-rag-for-dummies

A modular Agentic RAG built with LangGraph — learn Retrieval-Augmented Generation Agents in minutes.

## features

This repository demonstrates how to build an **Agentic RAG (Retrieval-Augmented Generation)** system using LangGraph with minimal code. Most RAG tutorials show basic concepts but lack guidance on building modular, agent-driven systems — this project bridges that gap by providing **both learning materials and an extensible architecture**.

## configuration

This system is provider-agnostic: the runnable app uses Ollama by default, and the chat model initialization can be adapted to any LLM provider available in [LangChain](https://python.langchain.com/docs/integrations/chat/). The examples below cover the most common options, but the same pattern applies to any other supported provider.

> **Note:** Model names change frequently. Always check the official documentation for the latest available models and their identifiers before deploying.

## installation

ollama pull granite4.1:8b
```

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="granite4.1:8b", temperature=0, seed=42)
```
> ⚠️ For reliable tool calling and instruction following, prefer models **8B+**. Smaller models may ignore retrieval instructions or hallucinate. See [Troubleshooting](#troubleshooting).

---

## tools

Create the retrieval tools the agent will use.

```python
import json
from typing import List
from langchain_core.tools import tool

RETRIEVAL_SCORE_THRESHOLD = 0.4

@tool
def search_child_chunks(query: str, limit: int = DEFAULT_RETRIEVAL_K) -> str:
    """Search document excerpts for evidence related to the user question.

    Use this as the first retrieval step. Results include parent IDs, file
    names, and short child-chunk excerpts. If excerpts are relevant but too
    fragmented to answer confidently, call retrieve_parent_chunks with the
    returned parent_id.

    Args:
        query: Focused search query with concrete keywords from the question.
        limit: Maximum number of child chunks to return.
    """
    try:
        results = child_vector_store.similarity_search(
            query,
            k=limit,
            score_threshold=RETRIEVAL_SCORE_THRESHOLD,
        )
        if not results:
            return "NO_RELEVANT_CHUNKS"

        return CHILD_CHUNK_SEPARATOR.join([
            f"Parent ID: {doc.metadata.get('parent_id', '')}\n"
            f"File Name: {doc.metadata.get('source', '')}\n"
            f"Content: {doc.page_content.strip()}"
            for doc in results
        ])

    except Exception as e:
        return f"RETRIEVAL_ERROR: {str(e)}"

@tool
def retrieve_parent_chunks(parent_id: str) -> str:
    """Retrieve the full parent chunk for a relevant child search result.

    Use this only after search_child_chunks returns a relevant parent_id and
    the child excerpt needs more surrounding context. Do not call this for
    parent IDs already available in compressed context.
    
    Args:
        parent_id: Parent chunk ID returned by search_child_chunks.
    """
    file_name = parent_id if parent_id.lower().endswith(".json") else f"{parent_id}.json"
    path = os.path.join(PARENT_STORE_PATH, file_name)

    if not os.path.exists(path):
        return "NO_PARENT_DOCUMENT"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return (
        f"Parent ID: {parent_id}\n"
        f"File Name: {data.get('metadata', {}).get('source', 'unknown')}\n"
        f"Content: {data.get('page_content', '').strip()}"
    )

llm_with_tools = llm.bind_tools([search_child_chunks, retrieve_parent_chunks])
```

---
