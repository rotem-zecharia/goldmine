# Dicklesworthstone/cass_memory_system

Procedural memory for AI coding agents: transforms scattered session history into persistent, cross-agent memory so every agent learns from every other

## installation

**Always use `--json` in agent contexts.** stdout = data, stderr = diagnostics, exit 0 = success.

```bash
# 1) Get task-specific memory before you start
cm context "implement auth rate limiting" --json

# 2) See the minimum viable workflow
cm quickstart --json

# 3) Build the playbook (memory onboarding)
cm onboard status --json
cm onboard sample --fill-gaps --json
cm onboard read /path/to/session.jsonl --template --json
cm onboard mark-done /path/to/session.jsonl
```

## Table of Contents

- [Why This Exists](#-why-this-exists)
- [How It Works](#-how-it-works)
- [Key Features](#-key-features)
- [For AI Agents](#-for-ai-agents-the-most-important-section)
- [Installation](#-installation)
- [CLI Reference](#-cli-reference)
- [The ACE Pipeline](#-the-ace-pipeline)
- [Data Models](#-data-models)
- [Scoring Algorithm](#-scoring-algorithm)
- [Configuration](#-configuration)
- [MCP Server](#-mcp-server)
- [Architecture & Engineering](#-architecture--engineering)
- [Deep Dive: Core Algorithms](#-deep-dive-core-algorithms)
- [Privacy & Security](#-privacy--security)
- [Trauma Guard: Safety System](#-trauma-guard-safety-system)
- [Performance Characteristics](#-performance-characteristics)
- [Starter Playbooks](#-starter-playbooks)
- [Extensibility](#-extensibility-adding-new-components)
- [Troubleshooting](#-troubleshooting)
- [Design Philosophy](#-design-philosophy)
- [Comparison with Alternatives](#-comparison-with-alternatives)
- [Roadmap](#-roadmap)

---

## features

### The Problem

AI coding agents accumulate valuable knowledge through sessions: debugging strategies, code patterns, user preferences, project-specific insights. But this knowledge is:

1. **Trapped in sessions** — Each session ends, context is lost forever
2. **Agent-specific** — Claude Code doesn't know what Cursor learned yesterday
3. **Unstructured** — Raw conversation logs aren't actionable as guidance
4. **Subject to collapse** — Naive summarization loses critical nuances and details

You've solved authentication bugs three times this month across different agents. Each time, you started from scratch because the knowledge from previous sessions was inaccessible.

### The Solution

`cass-memory` implements a **three-layer cognitive architecture** that transforms raw session logs into actionable, confidence-tracked rules:

| Layer | Role | Implementation |
|-------|------|----------------|
| **Episodic Memory** | Raw ground truth from all agents | `cass` search engine |
| **Working Memory** | Structured session summaries | Diary entries |
| **Procedural Memory** | Distilled rules with tracking | Playbook bullets |

This mirrors how human expertise develops: raw experiences (episodic) are consolidated into structured memories (working), which eventually become automatic knowledge (procedural).

### Who Benefits

- **AI Agents**: Get relevant rules and historical context before starting any task
- **Developers**: Build institutional memory that persists across tools and sessions
- **Teams**: Share patterns discovered by any team member's AI assistant
- **Power Users**: Create sophisticated workflows that leverage cross-agent learning

---

## 🔄 How It Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EPISODIC MEMORY (cass)                           │
│   Raw session logs from all agents — the "ground truth"             │
│   Claude Code │ Codex │ Cursor │ Aider │ PI │ Gemini │ ChatGPT │ ... │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ cass search
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    WORKING MEMORY (Diary)                           │
│   Structured session summaries bridging raw logs to rules           │
│   accomplishments │ decisions │ challenges │ outcomes               │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ reflect + curate (automated)
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROCEDURAL MEMORY (Playbook)                     │
│   Distilled rules with confidence tracking                          │
│   Rules │ Anti-patterns │ Feedback │ Decay                          │
└─────────────────────────────────────────────────────────────────────┘
```

Every agent's sessions feed the shared memory. A pattern discovered in Cursor **automatically** helps Claude Code on the next session.

---

## ✨ Key Features

### Cross-Agent Learning

Sessions from all your AI coding agents feed a unified knowledge base:

```
Claude Code session    →  ┐
Cursor session         →  │→  Unified Playbook  →  All agents benefit
Codex session          →  │
Aider session          →  │
PI session             →  ┘
```

A debugging technique discovered in Cursor is immediately available to Claude Code. No manual knowledge transfer required.

### Confidence Decay System

Rules aren't immortal. A rule helpful 8 times in January but never validated since loses confidence over time:

- **90-day half-life**: Confidence halves every 90 days without revalidation
- **4x harmful multiplier**: One mistake counts 4× as much as one success
- **Maturity progression**: `candidate` → `established` → `proven`

This prevents stale rules from polluting your playbook while rewarding consistently helpful guidance.

### Anti-Pattern Learn

## tools

`cass-memory` teaches agents how to use it—no external documentation required:

```bash
# Quick capability check and self-explanation
cm quickstart --json
# → Returns complete explanation of the system and how to use it

## configuration

Filter sessions by various criteria to focus on specific areas:

```bash
# Filter by workspace/project
cm onboard sample --workspace /Users/x/my-project

# Filter by agent
cm onboard sample --agent claude
cm onboard sample --agent cursor

# Filter by recency
cm onboard sample --days 30

# Combine filters
cm onboard sample --agent claude --days 14 --workspace /Users/x/api-project

# Include already-processed sessions (for re-analysis)
cm onboard sample --include-processed

# Adjust sample size
cm onboard sample --limit 20
```

### Onboarding Workflow for Agents

Recommended protocol for AI agents doing onboarding:

```markdown
## Onboarding Protocol

### Phase 1: Assessment
1. Run `cm onboard status --json` to check current progress
2. Run `cm onboard gaps --json` to see category distribution
3. Decide target: ~20 rules across diverse categories for a good initial playbook

### Phase 2: Session Analysis Loop
For each session until target reached:
1. `cm onboard sample --fill-gaps --json` → get prioritized sessions
2. `cm onboard read <path> --template --json` → get session with context
3. Analyze session content, identify 2-5 reusable patterns
4. Format as rules following extraction guidelines
5. `cm playbook add --file rules.json --session <path>` → add rules
6. Repeat with next session

### Phase 3: Verification
1. `cm onboard status` → verify progress
2. `cm onboard gaps` → check remaining gaps
3. `cm stats --json` → verify playbook health
```

## requirements

- **cass CLI**: The episodic memory layer. Install from [cass repo](https://github.com/Dicklesworthstone/coding_agent_session_search)
- **LLM API Key** (optional): For AI-powered reflection. Set `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_GENERATIVE_AI_API_KEY`

## limitations

### Near-Term
- [ ] Improved semantic search with better embedding models
- [ ] More starter playbooks (Ruby, Go, Rust, Java)
- [ ] Better conflict resolution in curation
- [ ] VS Code extension for inline feedback visualization

### Medium-Term
- [ ] Team playbook sharing (opt-in, encrypted)
- [ ] Web dashboard for playbook visualization
- [ ] Active learning - ask agents for feedback on uncertain rules
- [ ] Git-based playbook sync across machines

### Long-Term
- [ ] Federated learning across teams
- [ ] Automatic rule refinement based on outcomes
- [ ] Multi-modal rules (diagrams, code snippets)
- [ ] Integration with more agent platforms

### Non-Goals

These are explicitly out of scope:

- **Cloud sync** - This is local-first by design
- **Real-time collaboration** - That's a different tool category
- **Agent execution** - We search and advise, not execute
- **Universal knowledge base** - Focus remains on coding agents

---

## 🧪 Development

```bash
git clone https://github.com/Dicklesworthstone/cass_memory_system.git
cd cass_memory_system
bun install

# Dev with hot reload
bun --watch run src/cm.ts <command>

# Tests
bun test
bun run test:watch
bun run test:coverage

# Type check
bun run typecheck

# Lint
bun run lint

# Build all platforms
bun run build:all
```

### Testing Categories

| Category | Naming | Run |
|----------|--------|-----|
| Unit | `*.test.ts` | `bun run test:unit` |
| Integration | `*.integration.test.ts` | `bun run test:integration` |
| E2E | `*.e2e.test.ts` | `bun run test:e2e` |
| Property | `*.property.test.ts` | `bun run test:property` |

Coverage targets: ~80% lines, 80% functions, 70% branches.

### Build Outputs

| Platform | Output |
|----------|--------|
| Linux x64 | `dist/cass-memory-linux-x64` |
| macOS ARM64 | `dist/cass-memory-macos-arm64` |
| macOS x64 | `dist/cass-memory-macos-x64` |
| Windows x64 | `dist/cass-memory-windows-x64.exe` |

---

## 📜 License

MIT License (with OpenAI/Anthropic Rider). See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **[cass](https://github.com/Dicklesworthstone/coding_agent_session_search)** — The foundation that makes cross-agent search possible
- **ACE Paper** — The Agentic Context Engineering framework that inspired the pipeline design
- **Xenova/transformers** — Browser/Node.js transformers for embeddings
- **Bun** — Fast JavaScript runtime that makes CLI tools snappy

---

> *About Contributions:* Please don't take this the wrong way, but I do not accept outside contributions for any of my projects. I simply don't have the mental bandwidth to review anything, and it's my name on the thing, so I'm responsible for any problems it causes; thus, the risk-reward is highly asymmetric from my perspective. I'd also have to worry about other "stakeholders," which seems unwise for tools I mostly make for myself for free. Feel free to submit issues, and even PRs if you want to illustrate a proposed fix, but know I won't merge them directly. Instead, I'll have Claude or Codex review submissions via `gh` and independently decide whether and how to address them. Bug reports in particular are welcome. Sorry if this offends, but I want to avoid wasted time and hurt feelings. I understand this isn't in sync with the prevailing open-source ethos that seeks community contributions, but it's the only way I can move at this velocity and keep my sanity.
