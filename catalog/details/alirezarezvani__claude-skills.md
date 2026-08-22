# alirezarezvani/claude-skills

345 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom commands, 330+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — e

## installation

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
# Or: git clone + ./scripts/codex-install.sh
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

**364 skills across 18 domains:**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 52 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test gen, flaky fix, migrations), self-improving agent (auto-memory curation), security suite, a11y audit, **named-persona-adversarial-review** (review via named engineering philosophies) | [engineering-team/](engineering-team/) |
| **⚡ Engineering — POWERFUL** | 86 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, **reliability portfolio** (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, security-guidance PreToolUse hook, **Matt Pocock skills** (write-a-skill, caveman, grill-me, handoff, grill-with-docs), **zero-hallucination-coder** (Discuss→Map→Decompose→Execute→Verify), **agent-harness** (goal→plan→execute→verify→close loops over any domain), **memory-engineering** (price the memory write path, pick which cost to pay, audit FACT/SKILL/LOG density, gate on a forgetting policy), **skillopt-sleep** (nightly gated self-evolution from real Claude Code sessions, vendored from microsoft/SkillOpt), **book-to-skill** (compile a book, docs folder, or spec collection into a knowledge-base skill, then package it as a plugin) | [engineering/](engineering/) |
| **🎯 Product** | 17 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert | [product-team/](product-team/) |
| **📣 Marketing** | 48 | 8 pods: Content, SEO + AEO (`aeo` — E-E-A-T audit, citation tracking across 5 LLMs) + local (`local-seo-manager` — GBP/NAP/Map-Pack), CRO, Channels, Growth, Intelligence, Sales + context foundation + orchestration router | [marketing-skill/](marketing-skill/) |
| **🚀 Productivity** | 11 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage), `reflect` (journal), `handoff` (Matt Pocock-inspired), `andreessen` (market-first decision mode), `roast` (5-angle idea panel → GO/RESHAPE/KILL), `fable-goal` (ramble → autonomous /goal prompt), `weekly-review` (GTD loop with refusal gate), `deep-work` (time-blocking + shallow-work budget), `meetings` (cost gate + agenda + action items) | [productivity/](productivity/) |
| **🎨 Marketing (top-level)** | 1 | `landing` — single-file HTML landing-page generator (4 design styles, GSAP patterns, brand palette validator) | [marketing/](marketing/) |
| **🔬 Research (academic)** | 9 | `research` orchestrator (hybrid router + fallback) + 8 specialists: `pulse`, `litreview`, `grants` (NIH), `dossier`, `patent`, `syllabus`, `notebooklm`, `deep-research` (rigor-first meta-research) | [research/](research/) |
| **🧪 Research Operations** ✨v2.9.0 | 5 | Enterprise/cross-functional research: orchestrator + `clinical-research` (study design), `research-finance` (R&D program finance), `market-research` (sizing/survey/segmentation), `product-research` (user research) — each with onboarding + customization + opt-in autoresearch bridge | [research-ops/](research-ops/) |
| **📋 Project Management** | 9 | Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates + bundled Atlassian Remote MCP | [project-management/](project-management/) |
| **🏥 Regulatory & QM** | 19 | ISO 13505, MDR 2017/745, FDA, ISO 27001, GDPR, SOC 2, CAPA, risk management, agent-decision-receipts (PQ-signed action receipts) | [ra-qm-team/](ra-qm-team/) |
| **🛡️ Compliance OS** | 9 | Compliance operating system — controls, evidence, audit-readiness workflows | [compliance-os/](compliance-os/) |
| **💼 C-Level Advisory** | 68 | Full C-suite (CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE) + founder-mode agents + orchestration + board meetings + culture & collaboration
