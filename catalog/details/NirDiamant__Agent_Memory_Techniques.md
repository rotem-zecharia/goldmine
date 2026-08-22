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

## 🗺️ Taxonomy of Agent Memory Techniques

<p align="center">
  <img src="images/taxonomy.png" alt="Agent memory taxonomy: 30 techniques across 6 families (short-term, long-term, cognitive architectures, retrieval, frameworks, production)" width="720"/>
</p>

The 30 techniques fall into six families. Each family solves a different memory problem. Each technique lives in its own notebook.

| Family | What it solves | Techniques |
|---|---|---|
| **Short-term** | Keep recent turns in memory without filling up the context window. | 01 - 05 |
| **Long-term** | Save knowledge across sessions, users, and time. | 06 - 11 |
| **Cognitive architectures** | Working, hierarchical, and reflective memory systems. | 12 - 19 |
| **Retrieval & routing** | Choose what to recall and when. | 20 - 23 |
| **Frameworks** | Production-ready memory libraries (Mem0, Letta, Zep, Graphiti). | 24 - 27 |
| **Evaluation & production** | Measure, benchmark, and deploy memory. | 28 - 30 |

---

## 🧭 Which Technique Do I Need?

30 techniques grouped by what you are building. Pick the group that matches your goal, then open the technique inside it.

<p align="center">
  <img src="images/decision_tree.svg" alt="Decision tree: which agent memory technique do I need?" width="100%"/>
</p>

<!-- decision-tree-text-fallback -->
**Quick text version:**

- Need to manage the current chat? Start with **01-05** (short-term memory).
- Need to persist across sessions? Start with **06 Vector Store** or **21 Cross-Session Memory**.
- Building a cognitive architecture with multiple stores? See **12-19**.
- Using a framework? Go straight to **24 Graphiti**, **25 Mem0**, **26 Letta**, or **27 Zep**.
- Evaluating or shipping to production? See **28-30**.

**Still not sure?** Start with [01 Conversation Buffer](all_techniques/01_conversation_buffer_memory/). Almost every other technique builds on it.

---

## 📐 Compare Techniques at a Glance

Looking to filter by constraint (persistence, retrieval style, token cost, best-for use case)? See the [side-by-side comparison matrix](docs/comparison.md) covering all 30 techniques in one table.

## installation

> 💡  **Prefer not to install anything?** Every notebook renders on GitHub directly. Click a technique in the table above to read it in your browser. Or use the Colab badges to run it in the cloud.

```bash
# Clone the repository
git clone https://github.com/NirDiamant/Agent_Memory_Techniques.git
cd Agent_Memory_Techniques

## configuration

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## tools

cp .env.example .env
# Edit .env with your OPENAI_API_KEY and/or ANTHROPIC_API_KEY

# Launch Jupyter and start with the first technique
jupyter notebook all_techniques/01_conversation_buffer_memory/
```

---

## 📁 Project Structure

```
Agent_Memory_Techniques/
├── README.md                           # You are here
├── ROADMAP.md                          # Current state and what's next
├── LICENSE                             # Apache 2.0
├── CITATION.cff                        # How to cite this work
├── requirements.txt                    # Python dependencies
├── .env.example                        # API key template
├── llms.txt                            # LLM-discoverability index
│
├── all_techniques/                     # 30 technique folders, each with notebook + README
│   ├── 01_conversation_buffer_memory/
│   ├── 02_sliding_window_memory/
│   ├── ...
│   └── 30_production_memory_patterns/
│
├── docs/                               # Project documentation
│   ├── architecture.md                 # Memory system design patterns
│   ├── comparison.md                   # Side-by-side comparison of all 30 techniques
│   ├── glossary.md                     # Key terms and definitions
│   ├── learning_path.md                # Detailed learning path guide
│   ├── topics.md                       # Keyword index
│   ├── roadmap.md                      # Original planning archive
│   ├── FAQ.md                          # Frequently asked questions
│   └── CONTENT_STANDARDS.md            # Writing-style rules
│
├── .github/                            # GitHub community files
│   ├── CONTRIBUTING.md                 # How to contribute
│   ├── CODE_OF_CONDUCT.md              # Community guidelines
│   ├── SECURITY.md                     # Security policy
│   ├── FUNDING.yml                     # Sponsorship config
│   ├── ISSUE_TEMPLATE/                 # Issue templates
│   ├── pull_request_template.md        # PR template
│   └── workflows/                      # CI workflows
│
├── utils/                              # Shared helpers and validators
│   ├── helpers.py                      # Env loading, LLM clients, cosine, tokens
│   ├── validate_cells.py               # Notebook cell-structure validator
│   └── validate_style.py               # Prose-style validator
│
├── tests/                              # pytest smoke tests
├── data/                               # Small sample datasets
└── images/                             # Diagrams and visuals
```

---

## 📚 More from the same author

*Run a course, newsletter, or dev community? You can [earn 25% recommending RAG Made Simple](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=affiliate-signup&target=https%3A%2F%2Fnirdiamant.gumroad.com%2Faffiliates&retarget=0&text=affiliate-signup) to your audience.*

## 🤝 Contributing

<a href="https://github.com/NirDiamant/Agent_Memory_Techniques/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NirDiamant/Agent_Memory_Techniques" alt="Contributors" />
</a>

We welcome contributions. You can fill in a notebook, fix a bug, improve the docs, or propose a new technique. Every contribution helps the next reader.

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the details.

**Where we need help the most:**
- More techniques we haven't covered yet (propose one via an issue)
- Architecture diagrams (Mermaid or ASCII)
- More memory benchmarks and evaluation metrics
- Integration examples for new frameworks

---

## 💖 Sponsors

Supporting this project helps keep educational AI content free and open. If your company uses agent memory in production, consider sponsoring to get your logo below.

<a href="https://github.com/sponsors/NirDiamant"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4" alt="Become a Sponsor"/></a>

---

## 🔗 Related Work

This repo is part of a bigger collection of A
