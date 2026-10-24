# alirezarezvani/claude-skills

380 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom commands, 380+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — e

## installation

> **Windows users:** clone with `git clone -c core.symlinks=true` (Developer Mode enabled) — otherwise the `.gemini/`/`.codex/`/`.vibe/`/`.hermes/` mirror trees check out as 1-line pointer text files instead of skills — and set `PYTHONUTF8=1` so tools that print Unicode don't crash on legacy-codepage consoles. Details: [INSTALLATION.md → Windows Notes](INSTALLATION.md#windows-notes).

### Gemini CLI (New)

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

### Claude Code (Recommended)

```bash
# Add the marketplace
/plugin marketplace add alirezarezvani/claude-skills

# Install by domain
/plugin install engineering-skills@claude-code-skills          # 24 core engineering
/plugin install engineering-advanced-skills@claude-code-skills  # 25 POWERFUL-tier
/plugin install product-skills@claude-code-skills               # 12 product skills
/plugin install marketing-skills@claude-code-skills             # 43 marketing skills
/plugin install ra-qm-skills@claude-code-skills                 # 12 regulatory/quality
/plugin install pm-skills@claude-code-skills                    # 6 project management
/plugin install c-level-skills@claude-code-skills               # 28 C-level advisory (full C-suite)
/plugin install business-growth-skills@claude-code-skills       # 4 business & growth
/plugin install finance-skills@claude-code-skills               # 2 finance (analyst + SaaS metrics)

# Or install individual skills
/plugin install skill-security-auditor@claude-code-skills       # Security scanner
/plugin install playwright-pro@claude-code-skills                  # Playwright testing toolkit
/plugin install self-improving-agent@claude-code-skills         # Auto-memory curation
/plugin install content-creator@claude-code-skills              # Single skill
```

### OpenAI Codex

```bash
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
# Or: git clone + ./scripts/codex-install.sh --category <name>  (no arguments lists categories)
```

### OpenClaw

```bash
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

### Manual Installation

```bash
git clone https://github.com/alirezarezvani/claude-skills.git
# Copy any skill folder to ~/.claude/skills/ (Claude Code) or ~/.codex/skills/ (Codex)
```

---

## Multi-Tool Support (New)

**Convert all 345 skills to 9 AI coding tools** with a single script:

| Tool | Format | Install |
|------|--------|---------|
| **Cursor** | `.mdc` rules | `./scripts/install.sh --tool cursor --target .` |
| **Aider** | `CONVENTIONS.md` | `./scripts/install.sh --tool aider --target .` |
| **Kilo Code** | `.kilocode/rules/` | `./scripts/install.sh --tool kilocode --target .` |
| **Windsurf** | `.windsurf/skills/` | `./scripts/install.sh --tool windsurf --target .` |
| **OpenCode** | `.opencode/skills/` | `./scripts/install.sh --tool opencode --target .` |
| **Augment** | `.augment/rules/` | `./scripts/install.sh --tool augment --target .` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/install.sh --tool antigravity` |
| **Hermes Agent** | `~/.hermes/skills/` | `python scripts/sync-hermes-skills.py --verbose` |
| **Mistral Vibe** | `~/.vibe/skills/` | `./scripts/vibe-install.sh` |

**How it works:**

```bash

## tools

./scripts/convert.sh --tool all

## features

**398 production-ready skills across 20 domains:**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 54 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test gen, flaky fix, migrations), self-improving agent (auto-memory curation), security suite, a11y audit, **named-persona-adversarial-review** (review via named engineering philosophies), **embedded-iot-mentor** (MCU/board selection, firmware-reuse-first, breadboard-MVP discipline) | [engineering-team/](engineering-team/) |
| **⚡ Engineering — POWERFUL** | 97 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, **reliability portfolio** (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, security-guidance PreToolUse hook, **Matt Pocock skills** (write-a-skill, caveman, grill-me, handoff, grill-with-docs), **zero-hallucination-coder** (Discuss→Map→Decompose→Execute→Verify), **agent-harness** (goal→plan→execute→verify→close loops over any domain), **memory-engineering** (price the memory write path, pick which cost to pay, audit FACT/SKILL/LOG density, gate on a forgetting policy), **skillopt-sleep** (nightly gated self-evolution from real Claude Code sessions, vendored from microsoft/SkillOpt), **book-to-skill** (compile a book, docs folder, or spec collection into a knowledge-base skill, then package it as a plugin), **boost-asio-pro** (async C++ networking — version-gated coroutine/callback styles, strand discipline), **human-gate** (batched human review as a structured artifact + a gate that refuses to close on open blockers), **agent-memory** (four-tier L0-L3 memory ladder over Claude Code hooks; promotion earned by recurrence across sessions and days, redacted or contested claims refuse to promote, nothing reaches CLAUDE.md without a human adopt), **skill-doctor** (grade the agent setup from real session history — rubric-judged, deterministically gated, evidence-traced skill edits), **deep-learning-book** (companion to the free Goodfellow/Bengio/Courville textbook — 20 chapter files with a 2016→2026 delta layer, reading-path planner, Ch-11 training diagnostic, capacity planner, FLOP/activation-memory calculator), **spinning-up-deep-rl** (knowledge base compiled from OpenAI's Spinning Up in Deep RL — RL fundamentals, the model-free taxonomy, policy-gradient derivations, and one chapter per reference algorithm), **agent-regression-evals** (repeated-trial eval gate: trajectory grading, flake detection with pass^k, paired regression statistics that block a merge), **coding-agent-rollout** (team settings, permissions, MCP and plugin governance, CLAUDE.md layering, privacy-safe adoption counts) | [engineering/](engineering/) |
| **🎯 Product** | 17 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert | [product-team/](product-team/) |
| **📣 Marketing** | 50 | 8 pods: Content, SEO + AEO (`aeo` — E-E-A-T audit, citation tracking across 5 LLMs) + local (`local-seo-manager` — GBP/NAP/Map-Pack), CRO, Channels, Growth, Intelligence, Sales + `business-name-fit` (cross-cultural naming) + context foundation + orchestration router | [marketing-skill/](marketing-skill/) |
| **🚀 Productivity** | 12 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage), `reflect` (journal), `handoff` (Matt Pocock-inspired), `andreessen` (market-first decision mode), `roast` (5-angle idea panel → GO/RESHAPE/KILL), `fable-goal` (ramble → autonomous /goal prompt), `weekly-review` (GTD loop with refusal gate), `deep-work` (time-blocking + shallow-work budget), `meetings` (cost gate + agenda + action items), `swedish-mentor` (CEFR-leveled Swedish learning paths) | [produc
