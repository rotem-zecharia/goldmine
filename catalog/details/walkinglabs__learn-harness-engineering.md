# walkinglabs/learn-harness-engineering

Harness engineering beginner tutorial, from 0 to 1

## features

The question isn't "can models write code?" They can. The question is: **can they reliably complete real engineering tasks inside real repositories, over multiple sessions, without constant human supervision?**

Right now, the answer is: not without a harness.

```text
    WITHOUT HARNESS                            WITH HARNESS
    ==============                             ============

    Session 1: agent writes code               Session 1: agent reads instructions
               agent breaks tests                         agent runs init.sh
               agent says "done"                          agent works on one feature
               you fix it manually                        agent verifies before claiming done
                                                          agent updates progress log
    Session 2: agent starts fresh                         agent commits clean state
               agent has no memory
               of what happened before         Session 2: agent reads progress log
               agent re-does work                         agent picks up exactly where it left off
               or does something else entirely            agent continues the unfinished feature
               you fix it again                           you review, not rescue

    Result: you spend more time                Result: agent does the work,
            cleaning up than if you                    you verify the result
            did it yourself
```

The questions this course actually cares about:

- Which harness designs improve task completion rates?
- Which designs reduce rework and incorrect completions?
- Which mechanisms keep long-running tasks progressing steadily?
- Which structures keep the system maintainable after multiple agent runs?

---

## Course Curriculum & Documentation

For the full course materials, please visit the **[Documentation Website](https://walkinglabs.github.io/learn-harness-engineering/)**.

The curriculum is divided into three parts:

1. **Lectures**: 13 conceptual units explaining the theory behind harness engineering.
2. **Projects**: 7 hands-on projects where you build an agentic workspace from scratch.
3. **Resource Library**: Copy-ready templates (`AGENTS.md`, `feature_list.json`, `init.sh`, etc.) to use in your own repositories today.

---

## installation

You don't need to read all 14 lectures before you start getting value. If you're already using a coding agent on a real project, here's how to improve it right now.

The idea is simple: instead of just writing prompts, give your agent a set of structured files that define what to do, what's been done, and how to verify the work. These files live inside your repo, so every session starts from the same state.

```text
    YOUR PROJECT ROOT
    ├── AGENTS.md              <-- the agent's operating manual
    ├── CLAUDE.md              <-- (alternative, if using Claude Code)
    ├── init.sh                <-- runs install + verify + start
    ├── feature_list.json      <-- what features exist, which are done
    ├── claude-progress.md     <-- session progress (historical filename; agent-agnostic)
    └── src/                   <-- your actual code
```

Grab the starter templates from the [Resource Library](https://walkinglabs.github.io/learn-harness-engineering/en/resources/) and drop them into your project. That's it. Four files, and your agent sessions will already be significantly more stable than running on prompts alone.

`claude-progress.md` is a generic, repository-local session progress log; the
name is retained for compatibility with the course examples. It is not tied to
Claude Code and is not updated automatically by any agent. Codex, OpenHands,
Antigravity, and other coding agents can use the same file when their root
instructions tell them to read it at startup and update it before handoff.

---

## Capstone Project: A Real App

All six course projects revolve around the same product: **an Electron-based personal knowledge base desktop app**.

```text
    ┌──────────────────────────────────────────────────────┐
    │             Knowledge Base Desktop App               │
    │                                                      │
    │  ┌──────────────┐  ┌──────────────────────────────┐  │
    │  │ Document List│  │       Q&A Panel              │  │
    │  │              │  │                              │  │
    │  │ doc-001.md   │  │  Q: What is harness eng?     │  │
    │  │ doc-002.md   │  │  A: The environment built    │  │
    │  │ doc-003.md   │  │     around an agent model... │  │
    │  │ ...          │  │     [citation: doc-002.md]   │  │
    │  └──────────────┘  └──────────────────────────────┘  │
    │                                                      │
    │  ┌─────────────────────────────────────────────────┐ │
    │  │ Status Bar: 42 docs | 38 indexed | last sync 3m │ │
    │  └─────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────┘

    Core features:
    ├── Import local documents
    ├── Manage a document library
    ├── Process and index documents
    ├── Run AI-powered Q&A over imported content
    └── Return grounded answers with citations
```

This project was chosen because it combines strong practical value, enough real-world product complexity, and a good setting for observing before/after harness improvements.

Each course project's starter/solution is a complete copy of this Electron app at that evolutionary stage. P(N+1)'s starter is derived from P(N)'s solution — the app evolves as your harness skills grow.

---

## Learning Path

The course is designed to be done in order. Each phase builds on the last.

```text
    Phase 1: SEE THE PROBLEM              Phase 2: STRUCTURE THE REPO
    ========================              ==========================

    L01  Strong models ≠ reliable         L03  Repository as single
         execution                              source of truth
    L02  What harness actually means
                                          L04  Split instructions across
         |                                     files, not one giant file
         v
    P01  Prompt-only vs.                       |
         rules-first comparison                v
                                               P02  Agent-readab

## requirements

This is a course where you actually run coding agents.

You need at least one of these tools:

- Claude Code
- Codex
- Another IDE or CLI coding agent that supports file editing, command execution, and multi-step tasks

The course assumes you can:

- Open a local repository
- Allow the agent to edit files
- Allow the agent to run commands
- Inspect output and re-run tasks

If you don't have such a tool, you can still read the course content, but you won't be able to complete the projects as intended.

---

## Local Preview

This repository uses VitePress as a documentation viewer.

```sh
npm install
npm run docs:dev        # Dev server with hot reload
npm run docs:build      # Production build
npm run docs:preview    # Preview built site
```

Then open the local URL that VitePress outputs in your browser.

---

## Prerequisites

Required:

- Familiarity with the terminal, git, and local development environments
- Ability to read and write code in at least one common application stack
- Basic software debugging experience (reading logs, tests, and runtime behavior)
- Enough time to commit to implementation-focused coursework

Helpful but not required:

- Experience with Electron, desktop apps, or local-first tools
- Background in testing, logging, or software architecture
- Prior exposure to Codex, Claude Code, or similar coding agents

---

## Core References

Primary:

- [OpenAI: Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [OpenAI: Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [LangChain: Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)
- [Thoughtworks / Martin Fowler: Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)
- [Cursor: Continually improving our agent harness](https://cursor.com/blog/continually-improving-agent-harness)

See the full layered reference list in [`docs/en/resources/reference/`](./docs/en/resources/reference/index.md).

---

## Repository Structure

```text
learn-harness-engineering/
├── docs/                          # VitePress documentation site
│   ├── lectures/                  # 14 lectures (index.md + code/ examples)
│   │   ├── lecture-01-*/
│   │   └── ... (14 total)
│   ├── projects/                  # 8 project descriptions
│   │   ├── project-01-*/
│   │   └── ... (8 total)
│   └── resources/                 # Multilingual templates & references (14 languages)
│       ├── en/
│       └── ... (14 total)
├── projects/
│   ├── shared/                    # Shared Electron + TypeScript + React foundation
│   └── project-NN/                # Per-project starter/ and solution/ directories
├── skills/                        # Reusable AI agent skills
│   └── harness-creator/           # Harness engineering skill
├── tools/                         # Zero-dependency shell utilities
│   └── audit-harness.sh           # Shell-based harness audit (L03–L12, no Node.js needed)
├── package.json                   # VitePress + dev tooling
└── CLAUDE.md                      # Claude Code instructions for this repo
```

---

## How the Course Is Organized

- Each lecture focuses on one question
- The course includes 8 projects
- Every project requires the agent to do real work
- Every project compares weak vs. strong harness results
- What matters is the measured difference, not how many docs were written

---

## Skills

This repository also includes reusable AI agent ski

## tools

Zero-dependency utilities you can run without installing Node.js.

- [**audit-harness.sh**](./tools/audit-harness.sh): A shell-based audit script that checks an existing repo against all five harness subsystems (L03–L12). Exits 0 when all CRITICAL items pass. No Node.js required — complements `harness-creator`'s `validate-harness.mjs`.

```bash
# Run directly on any repo
curl -fsSL https://raw.githubusercontent.com/walkinglabs/learn-harness-engineering/main/tools/audit-harness.sh | bash -s -- /path/to/your/repo

# Or after cloning
bash tools/audit-harness.sh /path/to/your/repo
```

---

## Other Courses

Our team has also created other courses! Check them out:

[![Hands-on Modern RL](https://img.shields.io/badge/HANDS--ON_MODERN_RL-0052cc?style=for-the-badge)](https://github.com/walkinglabs/hands-on-modern-rl)

**Hands-on Modern RL**: An open-source, hands-on curriculum bridging the gap from basic RL concepts to LLM alignment, RLVR, and advanced Agentic systems.

[![Modern LLM Notebook](https://img.shields.io/badge/MODERN_LLM_NOTEBOOK-0052cc?style=for-the-badge)](https://github.com/walkinglabs/modern-llm-notebook)

**Modern LLM Notebook**: A hands-on course for building modern LLMs from scratch in PyTorch, with 23 runnable Jupyter Notebooks covering tokenizers, attention, MoE, RLHF, inference, evaluation, and distillation.

---

## Acknowledgments

This course was inspired by and draws ideas from [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) — a progressive guide to building an agent from scratch, from a single loop to isolated autonomous execution.
