# neomjs/neo

Neo.mjs is a self-evolving software organism: a professional end-to-end AI engineering team whose cross-model swarm inhabits live apps via Neural Link, Active Hybrid GraphRAG, DreamService, and self-h

## installation

```bash
npx neo-app@latest
```

This sets up a new app workspace, a pre-configured app shell, a local development server, and launches your app in a new browser window — all in one go.

* :book: **[Getting Started](https://neomjs.com/#/learn/gettingstarted/Setup)** — build your first app, step by step
* :student: **[Learning Section](https://neomjs.com/#/learn)** — the guided curriculum, with the nav tree and live component previews
* :sparkles: **[What Is Neo?](https://neomjs.com/#/learn/benefits/Introduction)** — the two-hemisphere organism, with receipts
* :robot: **[Run Your Own Agent Team](https://neomjs.com/#/learn/agentos/OwnAgentTeam)** — point the Agent OS at your own fork

</br></br>
## Who This Is For

Neo.mjs is a category-shaped substrate. The two hemispheres filter audience:

- **Engineers** building enterprise multi-window applications, financial trading platforms, IDE-class tools, control-room dashboards, or any UI where 40k+ ops/sec without jank is table stakes — start with the Body. The rendering engine is production-ready.
- **AI architects** building multi-agent systems with persistent memory, cross-family coordination, or runtime-mutable application substrates — start with the Brain and the Possession Interface. The Agent OS substrate is what you're looking for.
- **Researchers** studying autopoietic systems, gated-RSI patterns, or empirical multi-agent organism governance — start with [Discussion #10137 (MX coinage)](https://github.com/orgs/neomjs/discussions/10137) and [Discussion #10119 (harness coordination — graduated to ADR 0020 / Epic #13012)](https://github.com/orgs/neomjs/discussions/10119).

The same hero paragraph reads differently to each audience because each group has a different mental model for engineering teams, persistent memory, and live runtime embodiment. The vocabulary self-filters.

**Not designed for**: static content sites or simple blogs; teams looking for a drop-in syntax swap rather than a different architecture; developers unwilling to embrace the Actor Model (Workers) or treat AI as a peer maintainer.

</br></br>
## Architecture

Neo.mjs is split into two complementary layers (engine ↔ toolchain):

### The Runtime
*Runs in the browser. Production-ready. Zero-bloat.*
- **App Worker** — application logic, state, VDOM diffing
- **VDom Worker** — Asymmetric VDOM (JSON blueprints diffed off the main thread)
- **Data Worker** — data processing isolation
- **Canvas Worker** — 60fps offscreen rendering for high-frequency surfaces (grids, charts)
- **SharedWorker** — multi-window orchestration; one engine instance, many windows
- **Main Thread** — restricted to DOM patching only; the neurosurgeon thread

### The Toolchain (Agent OS)
*Runs in Node.js. AI-native.*
- **Knowledge Base MCP server** — semantic codebase understanding in the unified Chroma store, embedded through local-or-remote providers.
- **Memory Core MCP server** — agent persistent memory (SQLite Native Edge Graph + ChromaDB episodic)
- **GitHub Workflow MCP server** — autonomous PR review, issue management, bi-directional sync
- **Neural Link MCP server** — runtime introspection + mutation of the live App Worker heap
- **File System MCP server** — sandboxed file IO for internal `Neo.ai.Agent` local loops; frontier harnesses use their native file tools
- **DreamService** — REM-cycle daemon that distills sessions into Golden Path topology

**Read**: [`learn/benefits/ArchitectureOverview.md`](./learn/benefits/ArchitectureOverview.md)

</br></br>
## A Platform at Scale

Neo.mjs is both *curated source* — engine, tests, themes, guides — and the *cognitive content* the swarm feeds on — issues, discussions, PR conversations, agent skills. Both are version-controlled; both compound.

As of May 2026 (`sloc` methodology per the [Codebase Overview](./learn/guides/fundamentals/CodebaseOverview.md)): roughly **191,000 lines** of engine source, **306,000 lines** of agent-readable cognitive content, and **36,000 lines** of guides — a c
