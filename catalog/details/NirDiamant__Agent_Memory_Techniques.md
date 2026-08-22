# NirDiamant/Agent_Memory_Techniques

Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks

## features

> ### 💡 Quick Answer (for search engines and skimmers)
>
> **Agent memory** is the set of techniques that let an LLM-based agent (a system built around a Large Language Model) remember information across turns, sessions, and tasks. Without memory, an agent re-derives context every time and cannot personalize, learn, or maintain coherence over long interactions. This repository documents 30 distinct memory techniques, grouped into six families: short-term context management, long-term storage, cognitive architectures, retrieval and multi-agent patterns, batteries-included frameworks, and production deployment patterns.

Think about a friend who forgets every conversation you've ever had. Every morning you're strangers again. That's what most AI agents are like today.

Every AI agent eventually hits the same wall: **it forgets**.

In 2026, AI agents are everywhere. But most of them still forget what you told them yesterday. Without strong memory, an agent can't keep context across conversations. It can't learn from past chats. It can't build a lasting relationship with you.

The landscape is shifting fast:

- **Anthropic's 7 Layers of Memory** (March 2026): from conversation context to cross-project knowledge, defining the memory hierarchy for Claude Code
- **Mem0**: managed memory layer gaining rapid adoption for personalized AI
- **Letta (MemGPT)**: self-editing memory with inner/outer monologue architecture
- **Zep**: temporal knowledge graphs for long-term agent memory
- **Graphiti**: episodic-to-semantic knowledge graph extraction
- **MemOS & Memori**: memory-as-infrastructure platforms for production agents

But there's no single hands-on guide that teaches you **how each technique works, when to use it, and how to build it yourself**.

That's why this repository exists. **30 techniques. Runnable notebooks. Real code you can use today.**

---

## installation

> 💡  **Prefer not to install anything?** Every notebook renders on GitHub directly. Click a technique in the table above to read it in your browser. Or use the Colab badges to run it in the cloud.

```bash

## configuration

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## tools

cp .env.example .env
