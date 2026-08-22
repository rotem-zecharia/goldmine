# KhazP/vibe-coding-prompt-template

Templates and workflow for generating PRDs, Tech Designs, and MVP and more using LLMs for AI IDEs

## installation

### Phase 1: thinking through the product
Do the first three steps in ChatGPT, Claude.ai, Gemini, or any other chat tool. You do not need a repo yet.

### ![Step 1](https://img.shields.io/badge/Step_1-Deep_Research-764ba2?style=flat-square) Deep Research
<details open>
<summary><b>Check whether the idea is worth building</b> - 20-30 min</summary>

This step gives you a quick read on demand, competitors, and whether the scope looks realistic.

1. Open [`part1-deepresearch.md`](part1-deepresearch.md) and **copy all of its contents**.
2. **Paste it** into your preferred AI platform Chat (like Claude.ai, ChatGPT, or Gemini) and press **Enter**.
3. The AI will ask you a few questions about your idea. Answer them truthfully in the chat.
4. The AI will generate a comprehensive research document based on your answers.
5. **Save the output** into a local file named `research-[YourAppName].md` (or `.txt`) or simply **keep this chat open** for Step 2.

Tip: if your chat tool supports web search, source grounding, URL context, or deep research mode, turn it on and require cited claims with access dates.
</details>

## requirements

<details open>
<summary><b>Write down what the MVP actually needs to do</b> - 15-20 min</summary>

This turns the rough idea into a scope you can build against.

1. Copy the contents of [`part2-prd-mvp.md`](part2-prd-mvp.md).
2. **Option A (Same Chat):** If you kept your chat open, paste the prompt right below the Deep Research output.
3. **Option B (New Chat):** Start a fresh chat, paste your saved `research-[YourAppName].md` content, and then paste the Part 2 prompt below it.
4. Press Enter, answer any clarifying questions the AI asks, and let it generate your requirements.
5. **Save the final output** as `PRD-[YourAppName]-MVP.md`.
</details>

### ![Step 3](https://img.shields.io/badge/Step_3-Technical_Design-4facfe?style=flat-square) Technical Design
<details open>
<summary><b>Pick a stack you can actually ship with</b> - 15-20 min</summary>

This step helps you choose the stack, deployment target, AI provider strategy if the product needs AI, and the verification path.

1. Copy the contents of [`part3-tech-design-mvp.md`](part3-tech-design-mvp.md).
2. Paste it into your **ongoing conversation** (or into a new one, making sure to attach the `PRD-[YourAppName]-MVP.md` from Step 2 as context).
3. The AI will ask questions regarding your budget, timeline, and complexity tolerance.
4. Discuss the trade-offs it presents, including no-code/full-code, Vercel vs. Cloudflare, and whether AI evals are required.
5. Once a stack is decided, **save the output** as `TechDesign-[YourAppName]-MVP.md`.
</details>

### Phase 2: execution in your IDE
Move into Codex, Cursor, VS Code with Copilot, Claude Code, Antigravity/Gemini-compatible agents, or your preferred coding setup. This is where the project becomes code and verified artifacts.

### ![Step 4](https://img.shields.io/badge/Step_4-Instantiate_Templates-00f2fe?style=flat-square) Set up the agent files
<details open>
<summary><b>Create the docs and instructions your coding agent will rely on</b> - 1-2 min</summary>

> **CLI shortcut:** tell your AI agent to run `npx vibeworkflow` from your project folder — the CLI is agent-driven, not meant to be run by hand. If you already have `docs/PRD-*.md` + `docs/TechDesign-*.md` (with the JSON meta block), it scaffolds the files below (skipping anything you've already edited) and verifies with `npx vibeworkflow doctor`. If the docs are missing, it installs the planning skills, auto-detects your AI tools, and prints agent instructions that drive the research → PRD → Tech Design interviews for you — your agent asks the questions one at a time; you just answer. The paste flow below still works everywhere.

This step fills out `AGENTS.md` and the supporting docs from your PRD and tech design.

1. Click **"Use this template"** in GitHub (or clone this repository locally).
2. Open this cloned repository folder in your **AI IDE** (like Cursor or VS Code).
3. Create a `docs/` folder in your project root if it does not already exist.
4. Move your saved documents into `docs/` using these names:
   - `docs/PRD-[YourAppName]-MVP.md`
   - `docs/TechDesign-[YourAppName]-MVP.md`
   - optional: `docs/research-[YourAppName].md` (or `.txt` for backward compatibility)
5. Open the AI Chat inside your IDE, type: *"Read [`part4-notes-for-agent.md`](part4-notes-for-agent.md), follow its instructions, and set up my workspace."*
6. The agent should copy the boilerplates from `/templates/`, generate selected tool configs (`CLAUDE.md`, `.cursor/rules/`, `GEMINI.md`, `.codex/config.toml`, `.agents/skills/`, etc.), and fill placeholders using the files in `docs/`.

Default generated files:
- `AGENTS.md`
- `MEMORY.md`
- `REVIEW-CHECKLIST.md`
- `agent_docs/project_brief.md`
- `agent_docs/tech_stack.md`
- `agent_docs/testing.md`

Optional generated files:
- `agent_docs/code_patterns.md` when the codebase has real conventions to preserve.
- `agent_docs/product_requirements.md` when the PRD is long enough to need a build-facing summary.
- `.claude/`, `.cursor/`, `.github/`, `.c

## tools

You need a modern browser, a few hours, and enough comfort with files and copy-paste to move between tools. You do not need to be an experienced developer.

### Platform selection guide

| Focus Area | Recommended Tools |
|------------|-------------------|
| **Fast Prototype** | Lovable, v0, or Google AI Studio Build mode; verify export and deployment path before committing |
| **Production Web App** | Next.js/Vercel, Cloudflare Workers, or another boring stack the team can maintain |
| **AI Product Features** | Provider SDKs, AI SDKs, Workers AI, or local models with cost and data checks |
| **Learning / Sandbox Coding** | Cursor rules, Codex skills, Antigravity/Gemini legacy, VS Code with Copilot, Continue, Cline, or Aider |
| **Complex Logic / Delegation** | Claude Code subagents, Codex subagents, or Cursor background agents with scoped tasks |
| **Budget-Limited AI** | Antigravity/Gemini where currently supported, free-tier provider APIs, or Workers AI, with quota checks and current pricing verification |
| **Private / Local AI** | LM Studio, Ollama, Continue, Cline, Aider, OpenHands, llama.cpp, or MLX with explicit tool approvals |

Note: I would not use this workflow as-is for native hardware work, heavily regulated products, or safety-critical systems.

---

## Advanced agent practices

<details open>
<summary><b>1. Artifact-first memory and compaction</b></summary>

To avoid context overload, let the agent write durable project facts into files instead of trying to keep everything in one giant chat:
- **Compaction and handoffs:** Use native compaction/summarization where the tool supports it. When you switch sessions, have the agent write a `specs/001-feature.md` or `recap.md` and load only that file into the new chat.
- **Repo-owned memory:** Keep decisions and current state in `MEMORY.md`; tool-side memories are personal and should not replace versionable project docs.
- **Cursor/Codex/Gemini context:** Use project rules, skills, or `GEMINI.md` as concise pointers to `AGENTS.md` and `agent_docs/`, not as huge prompt dumps.
- If you must restart, attach `AGENTS.md`, `docs/PRD-[YourAppName]-MVP.md`, `docs/TechDesign-[YourAppName]-MVP.md`, and your latest handoff artifact.
</details>

<details open>
<summary><b>2. Multi-agent orchestration and plugins</b></summary>

- **Subagents first:** Use focused subagents for research, code review, debugging, and test verification. Use experimental team-style coordination only when agents truly need to communicate or split disjoint modules.
- **Plan before edit:** Use the tool's actual plan/approval mode where available, then require a short plan before multi-file changes.
- **Scoped rules and skills:** Keep `AGENTS.md` as the cross-tool source of truth, then add `.cursor/rules/`, `.claude/agents/`, `.codex/config.toml`, `.agents/skills/`, or `GEMINI.md` only as concise tool-specific adapters.
- **Task routing:** Use [Agent tooling compatibility](docs/tools/agent-tooling-compatibility.md) to decide when to use Codex, Claude Code, Cursor, Copilot, Antigravity, local agents, or builder tools.
</details>

<details>
<summary><b>3. Model strategy matrix</b></summary>

Use model families instead of pinned version names. It ages better as models get swapped underneath you.

| Strategy | Primary Families | Best For | Speed |
|----------|------------------|----------|:-----:|
| Speed-first | Gemini Flash, Claude Sonnet | Fast prototyping, broad iteration | High |
| Balanced | Claude Sonnet, Gemini Pro | Daily coding, debugging, planning | Med-High |
| Depth-first | Claude Opus, Gemini Pro | Deep reasoning, complex refactors | Medium |
</details>

Always verify current model names, quotas, and pricing against official docs before writing them into project artifacts. Reasoning effort and verbosity are product settings, not automatic quality upgrades.

<details>
<summary><b>4. Agent observability</b></summary>

When an agent ignores instructions or behaves inconsistently:
1. Check which instru
