# GiovanniPasq/agentic-rag-for-dummies

A modular Agentic RAG built with LangGraph — learn Retrieval-Augmented Generation Agents in minutes.

## features

This repository demonstrates how to build an **Agentic RAG (Retrieval-Augmented Generation)** system using LangGraph with minimal code. Most RAG tutorials show basic concepts but lack guidance on building modular, agent-driven systems — this project bridges that gap by providing **both learning materials and an extensible architecture**.

### What's inside

| Feature | Description |
|---|---|
| 🗂️ **Hierarchical Indexing** | Search small chunks for precision, retrieve large Parent chunks for context |
| 🧠 **Conversation Memory** | Maintains context across questions for natural dialogue |
| ❓ **Query Clarification** | Rewrites ambiguous queries or pauses to ask the user for details |
| 🤖 **Agent Orchestration** | LangGraph coordinates the full retrieval and reasoning workflow |
| 🔀 **Multi-Agent Map-Reduce** | Decomposes complex queries into parallel sub-queries |
| ✅ **Self-Correction** | Re-queries automatically if initial results are insufficient |
| 🗜️ **Context Compression** | Keeps working memory lean across long retrieval loops |
| 🔍 **Observability** | Track LLM calls, tool usage, and graph execution with Langfuse |
| 📊 **Evaluation** | Evaluate retrieval and answer quality with RAGAS metrics |

### 🎯 Two Ways to Use This Repo

**1️⃣ Learning Path: Interactive Notebook**

Step-by-step tutorial perfect for understanding core concepts. Start here if you're new to Agentic RAG or want to experiment quickly.

**2️⃣ Building Path: Modular Project**

Flexible architecture where each component can be independently adapted — LLM provider, embedding model, PDF converter, and agent workflow. The runnable app is Ollama-first, and it can be adapted to any chat model provider supported by LangChain. Examples are included for Anthropic, OpenAI, and Google.

See [Modular Architecture](#modular-architecture) and [Installation & Usage](#installation--usage) to get started.

## How It Works

### Document Preparation: Hierarchical Indexing

Before queries can be processed, documents are split twice for optimal retrieval:

- **Parent Chunks**: Bounded large sections based on Markdown headers (H1, H2, H3)
- **Child Chunks**: Small, fixed-size pieces derived from parents

> Optional: 🐿️ [**Chunky**](https://github.com/GiovanniPasq/chunky) is an open-source toolkit for reliable RAG pipelines: convert PDFs to Markdown, clean documents, inspect chunks, compare chunking strategies, and enrich metadata before building the vector store.

This combines the **precision of small chunks** for search with the **contextual richness of large chunks** for answer generation.

---

### Query Processing: Four-Stage Intelligent Workflow
```
User Query → Conversation Summary → Query Rewriting → Query Clarification →
Parallel Agent Reasoning → Aggregation → Final Response
```

**Stage 1 — Conversation Understanding:** Maintains a rolling summary and recent conversation history to preserve continuity without indefinitely increasing context size.

**Stage 2 — Query Clarification:** Resolves references ("How do I update it?" → "How do I update SQL?"), splits multi-part questions into focused sub-queries, detects unclear inputs, and rewrites queries for optimal retrieval. Pauses for human input when clarification is needed.

**Stage 3 — Intelligent Retrieval (Multi-Agent Map-Reduce):** Spawns parallel agent subgraphs — one per sub-query. Each agent searches child chunks, fetches parent chunks for context, self-corrects if results are insufficient, compresses context to avoid redundant fetches, and falls back gracefully if the search budget is exhausted.

> **Example:** *"What is JavaScript? What is Python?"* → 2 parallel agents execute simultaneously.

**Stage 4 — Response Generation:** Aggregates all agent responses into a single coherent answer.

---

## configuration

This system is provider-agnostic: the runnable app uses Ollama by default, and the chat model initialization can be adapted to any LLM provider available in [LangChain](https://python.langchain.com/docs/integrations/chat/). The examples below cover the most common options, but the same pattern applies to any other supported provider.

> **Note:** Model names change frequently. Always check the official documentation for the latest available models and their identifiers before deploying.

### Ollama (Local)

```bash

## installation

ollama pull granite4.1:8b
```

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="granite4.1:8b", temperature=0, seed=42)
```
> ⚠️ For reliable tool calling and instruction following, prefer models **8B+**. Smaller models may ignore retrieval instructions or hallucinate. See [Troubleshooting](#troubleshooting).

---

### Cloud Providers

<details>
<summary>Click to expand</summary>

**OpenAI GPT:**
```bash
pip install -qU langchain-openai
```
```python
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "your-api-key-here"
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

**Anthropic Claude:**
```bash
pip install -qU langchain-anthropic
```
```python
from langchain_anthropic import ChatAnthropic
import os

os.environ["ANTHROPIC_API_KEY"] = "your-api-key-here"
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
```

**Google Gemini**
```bash
pip install -qU langchain-google-genai
```
```python
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
```
</details>

---

## Implementation

Additional details, extended explanations, and Langfuse observability are available in the **[notebook](notebooks/agentic_rag.ipynb)** and full project. The companion **[evaluation notebook](notebooks/evaluation.ipynb)** scores the final answers and the actual child/parent tool outputs used by the agent with direct RAGAS metric calls.

| Step | Description |
|------|-------------|
| 1 | [Initial Setup and Configuration](#step-1-initial-setup-and-configuration) |
| 2 | [Configure Vector Database](#step-2-configure-vector-database) |
| 3 | [PDFs to Markdown](#step-3-pdfs-to-markdown) |
| 4 | [Hierarchical Document Indexing](#step-4-hierarchical-document-indexing) |
| 5 | [Define Agent Tools](#step-5-define-agent-tools) |
| 6 | [Define System Prompts](#step-6-define-system-prompts) |
| 7 | [Define State and Data Models](#step-7-define-state-and-data-models) |
| 8 | [Agent Configuration](#step-8-agent-configuration) |
| 9 | [Build Graph Node and Edge Functions](#step-9-build-graph-node-and-edge-functions) |
| 10 | [Build the LangGraph Graphs](#step-10-build-the-langgraph-graphs) |
| 11 | [Create Chat Interface](#step-11-create-chat-interface) |

### Step 1: Initial Setup and Configuration

Define paths and initialize core components.

```python
import os
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant.fastembed_sparse import FastEmbedSparse
from qdrant_client import QdrantClient

DOCS_DIR = "docs"  # Directory containing your pdf files
MARKDOWN_DIR = "markdown_docs" # Directory containing the pdfs converted to markdown
PARENT_STORE_PATH = "parent_store"  # Directory for parent chunk JSON files
CHILD_COLLECTION = "document_child_chunks"
DEFAULT_RETRIEVAL_K = 7
CHILD_CHUNK_SEPARATOR = "\n\n<CHILD_CHUNK_BOUNDARY>\n\n"

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(MARKDOWN_DIR, exist_ok=True)
os.makedirs(PARENT_STORE_PATH, exist_ok=True)

from langchain_ollama import ChatOllama
llm = ChatOllama(model="granite4.1:8b", temperature=0, seed=42)

dense_embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")
sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

client = QdrantClient(path="qdrant_db")
```

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

### Step 6: Define System Prompts

Define the system prompts for conversation summarization, query rewriting, agent orchestration, context compression, fallback response, and answer aggregation.

<details>
<summary>Conversation Summary Prompt</summary>

```python
def get_conversation_summary_prompt() -> str:
    return """## Role
You are a compact memory manager for a retrieval-augmented chat assistant.

## Context
The input contains an existing rolling summary plus older user/assistant messages that will be removed from raw chat history.

## Instructions
- Merge the existing summary with the new older messages.
- Preserve context needed for future follow-up questions: topics, user preferences, important facts, unresolved questions, and referenced source file names.
- Discard greetings, tool calls, tool outputs, formatting chatter, duplicate details, and resolved misunderstandings.
- Keep the summary compact: 30-70 words unless more detail is essential.

## Output
Return exactly one merged summary and nothing else.
Do not include labels such as "Updated summary:", "Previous summary:", or "New messages:".
Do not include both old and new summaries.
If there is no meaningful context, return an empty string.
"""
```

</details>

<details>
<summary>Query Rewrite Prompt</summary>

```python
def get_rewrite_query_prompt() -> str:
    return """## Role
You are a query rewriting specialist for document retrieval in a RAG system.

## Instructions
- Rewrite the current query so it is clear, self-contained, and useful for retrieval.
- Use the conversation summary and recent conversation only to resolve vague follow-ups that refer to prior context.
- When an unresolved query and o
