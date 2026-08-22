# 1ay1/agentty

AI pair programming in your terminal — one static binary, sub-ms startup, any model

## features

Most terminal coding agents ship as a Node or Python app and send big chunks of your repository to the model on every turn. agentty takes the opposite approach:

- **It's one native binary.** 16.7 MB, ~3 ms cold start, zero runtime dependencies — no Node, no Python, no `npm install`, no `node_modules`. Download and run.
- **It sends only the relevant code.** Built-in retrieval (hybrid BM25 + dense embeddings, code-aware chunking, GraphRAG) fetches just the slices that matter — often cutting context by 80%+ vs. whole-repo dumping.
- **It's not locked to one vendor.** Sign in with your Claude Pro/Max, or point it at OpenAI, Groq, OpenRouter, Cerebras, or a fully local Ollama model. Switch live with `^P`.
- **It's safe by default.** Shell and build commands run in a sandbox; air-gap an entire session over SSH with one command.
- **It's open source (MIT)** and runs inside Zed over ACP.

Coming from another tool? See the honest comparisons: [vs Claude Code](https://agentty.org/compare/agentty-vs-claude-code) · [vs Aider](https://agentty.org/compare/agentty-vs-aider) · [vs Cursor](https://agentty.org/compare/agentty-vs-cursor) · [all alternatives](https://agentty.org/alternatives).

## installation

```bash
curl -fsSL https://raw.githubusercontent.com/1ay1/agentty/master/install.sh | sh
cd your-project
agentty
```

First launch opens auth — **paste an API key** (Anthropic `sk-ant-…`, or any provider's key) or use a local Ollama model that needs no key at all. You can also sign in with your Claude Pro/Max OAuth if you prefer. Once you're in, a first-run welcome card suggests a few things to try; just type and hit Enter.
