# alirezarezvani/claude-skills

410 Claude Code skills & agent skills & plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engi

## installation

**Claude Code**

```bash
/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-skills@claude-code-skills
```

**Codex, Cursor, Gemini CLI, Copilot and other agents** (the open-source [`skills`](https://github.com/vercel-labs/skills) installer)

```bash
npx skills add alirezarezvani/claude-skills
```

More options for each tool are under [Quick Install](#quick-install).

## Pick your role

| You are | Install | You get |
|---|---|---|
| Software engineer | `engineering-skills` | Architecture, code review, TDD, frontend, backend, DevOps, security, QA |
| Platform or AI engineer | `engineering-advanced-skills` | Agent design, RAG, MCP servers, CI/CD, observability, SLOs, evals |
| Product manager | `product-skills` | Discovery, RICE, PRDs, user stories, roadmaps, UX research |
| Delivery lead or scrum master | `pm-skills` | Sprint health, Jira and Confluence, flow metrics, forecasts |
| Marketer | `marketing-skills` | SEO, answer-engine optimization, copywriting, CRO, email, paid ads |
| Founder or executive | `c-level-skills` | CEO, CTO, CFO, CMO, CRO and other advisors, board prep, hard calls |
| Regulated industry | `ra-qm-skills` | ISO 13485, EU MDR, FDA, ISO 27001, SOC 2, GDPR, CAPA, risk files |
| Finance | `finance-skills` | DCF, budgets, SaaS metrics, month-end close |

Install with `/plugin install <name>@claude-code-skills`.

## Start with these

Each of these loaded on every plain-language test prompt. [See all verified skills](VERIFIED.md).

| Skill | What it does | Install |
|---|---|---|
| [agent-run-forensics](engineering/agent-run-forensics/) | Checks what your agent actually did against what it said it did, from the session transcript | `agent-run-forensics` |
| [human-gate](engineering/human-gate/) | Refuses to ship a plan, spec or migration until a named person has reviewed it and no blocker is open | `human-gate` |
| [skill-retro](engineering/skill-retro/) | Grades your skills from your own past sessions and proposes only the edits the evidence supports | `skill-retro` |
| [i18n-localization](engineering/i18n-localization/) | Finds missing keys, broken placeholders and wrong plural forms before a language ships | `i18n-localization` |
| [month-end-close](finance/month-end-close/) | Runs the close calendar, proves reconciliations and refuses boilerplate variance explanations | `month-end-close` |
| [cmmc-readiness](ra-qm-team/cmmc-readiness/) | Scores CMMC 2.0 Level 2 readiness, SPRS and POA&M close-out | `cmmc-readiness` |

[^hermes]: Hermes Agent is **BYO-sync tier**: the repo ships a pre-generated `.hermes/skills/claude-skills/` tree, but you run `python scripts/sync-hermes-skills.py` once locally to install into `~/.hermes/skills/`. Uses the same agentskills.io SKILL.md standard — no format conversion.
[^vibe]: Mistral Vibe is also **BYO-sync tier**: the repo ships a pre-generated `.vibe/skills/claude-skills/` tree, run `./scripts/vibe-install.sh` once locally to install into `~/.vibe/skills/`. Same agentskills.io SKILL.md standard — no format conversion. Docs: <https://docs.mistral.ai/mistral-vibe/agents-skills>.

---

## What Are Claude Code Skills & Agent Plugins?

Claude Code skills (also called agent skills or coding agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill includes:

- **SKILL.md** — structured instructions, workflows, and decision frameworks
- **Python tools** — 807 CLI scripts (all stdlib-only, zero pip installs)
- **Reference docs** — 917 templates, checklists, and domain-specific knowledge files

**One repo, thirteen platforms.** Works natively as Claude Code plugins, Codex agent skills, Gemini CLI skills, Hermes Agent skills, Mistral Vibe skills, and converts to more tools via `scripts/convert.sh`. All 807 Python tools run anywhere Python runs.

### Skills vs Agents vs Personas

| | Skills | Agents | Personas |
|---|---|---|---|
| **Purpose** | How to execute a task | What task

## tools

./scripts/convert.sh --tool all

## features

**411 production-ready skills across 20 domains:**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 54 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test gen, flaky fix, migrations), self-improving agent (auto-memory curation), security suite, a11y audit, **named-persona-adversarial-review** (review via named engineering philosophies), **embedded-iot-mentor** (MCU/board selection, firmware-reuse-first, breadboard-MVP discipline) | [engineering-team/](engineering-team/) |
| **⚡ Engineering — POWERFUL** | 104 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, **reliability portfolio** (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, security-guidance PreToolUse hook, **Matt Pocock skills** (write-a-skill, caveman, grill-me, handoff, grill-with-docs), **zero-hallucination-coder** (Discuss→Map→Decompose→Execute→Verify), **agent-harness** (goal→plan→execute→verify→close loops over any domain), **memory-engineering** (price the memory write path, pick which cost to pay, audit FACT/SKILL/LOG density, gate on a forgetting policy), **skillopt-sleep** (nightly gated self-evolution from real Claude Code sessions, vendored from microsoft/SkillOpt), **book-to-skill** (compile a book, docs folder, or spec collection into a knowledge-base skill, then package it as a plugin), **boost-asio-pro** (async C++ networking — version-gated coroutine/callback styles, strand discipline), **human-gate** (batched human review as a structured artifact + a gate that refuses to close on open blockers), **agent-memory** (four-tier L0-L3 memory ladder over Claude Code hooks; promotion earned by recurrence across sessions and days, redacted or contested claims refuse to promote, nothing reaches CLAUDE.md without a human adopt), **skill-retro** (grade the agent setup from real session history — rubric-judged, deterministically gated, evidence-traced skill edits), **deep-learning-book** (companion to the free Goodfellow/Bengio/Courville textbook — 20 chapter files with a 2016→2026 delta layer, reading-path planner, Ch-11 training diagnostic, capacity planner, FLOP/activation-memory calculator), **spinning-up-deep-rl** (knowledge base compiled from OpenAI's Spinning Up in Deep RL — RL fundamentals, the model-free taxonomy, policy-gradient derivations, and one chapter per reference algorithm), **agent-regression-evals** (repeated-trial eval gate: trajectory grading, flake detection with pass^k, paired regression statistics that block a merge), **coding-agent-rollout** (team settings, permissions, MCP and plugin governance, CLAUDE.md layering, privacy-safe adoption counts), **commit-craft** (split a tangled working tree into a reviewable commit series, block staged secrets, lint messages for the why), **i18n-localization** (check translation files against CLDR plural rules, find hardcoded UI strings, build pseudo-locales) | [engineering/](engineering/) |
| **🎯 Product** | 19 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert, UI finish QA (design-qa) | [product-team/](product-team/) |
| **📣 Marketing** | 50 | 8 pods: Content, SEO + AEO (`aeo` — E-E-A-T audit, citation tracking across 5 LLMs) + local (`local-seo-manager` — GBP/NAP/Map-Pack), CRO, Channels, Growth, Intelligence, Sales + `business-name-fit` (cross-cultural naming) + context foundation + orchestration router | [marketing-skill/](marketing-skill/) |
| **🚀 Productivity** | 12 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage), `reflect` (journal), `handoff` (Matt Pocock-inspired), `andreessen` (market-first decision mode), `roast` (5-angle idea pane
