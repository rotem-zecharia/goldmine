# revfactory/harness

A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the skills they use.

## features

Harness leverages Claude Code's agent team system to decompose complex tasks into coordinated teams of specialized agents. Say "build a harness for this project" and it automatically generates agent definitions (`.claude/agents/`) and skills (`.claude/skills/`) tailored to your domain.

## Category — Where Harness Sits

Harness lives at the **L3 Meta-Factory** layer of the Claude Code ecosystem — the layer that generates other harnesses rather than being one. Inside L3, we pick a specific sub-layer: **Team-Architecture Factory**.

| Layer | What it does | Neighbors we coexist with |
|-------|--------------|---------------------------|
| **L3 — Meta-Factory / Team-Architecture Factory** (us) | Domain sentence → agent team + skills, via 6 pre-defined team patterns | — |
| L3 — Meta-Factory / Runtime-Configuration Factory | Deterministic, repeatable runtime configurations | [coleam00/Archon](https://github.com/coleam00/Archon) |
| L3 — Meta-Factory / Codex Runtime Port | Same concept, Codex runtime | [SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness) |
| L2 — Cross-Harness Workflow | Standardize skills/rules/hooks across multiple harnesses | [affaan-m/ECC](https://github.com/affaan-m/everything-claude-code) |

> Archon generates deterministic runtime configurations. Harness generates team architectures (pipeline, fan-out/fan-in, expert pool, producer-reviewer, supervisor, hierarchical delegation) plus the skills agents use. Different sub-layers of the same L3. Pick Archon for runtime determinism, Harness for team architecture, or combine them.

## Star History

<a href="https://www.star-history.com/?repos=revfactory%2Fharness&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=revfactory/harness&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=revfactory/harness&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=revfactory/harness&type=date&legend=top-left" />
 </picture>
</a>


## Key Features

- **Agent Team Design** — 6 architectural patterns: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, and Hierarchical Delegation
- **Skill Generation** — Auto-generates skills with Progressive Disclosure for efficient context management
- **Orchestration** — Inter-agent data passing, error handling, and team coordination protocols
- **Validation** — Trigger verification, dry-run testing, and with-skill vs without-skill comparison tests


## Workflow

```
Phase 1: Domain Analysis
    ↓
Phase 2: Team Architecture Design (Agent Teams vs Subagents)
    ↓
Phase 3: Agent Definition Generation (.claude/agents/)
    ↓
Phase 4: Skill Generation (.claude/skills/)
    ↓
Phase 5: Integration & Orchestration
    ↓
Phase 6: Validation & Testing
```

## installation

### Via Marketplace

#### Add the marketplace
```shell
/plugin marketplace add revfactory/harness
```

#### Install the plugin
```shell
/plugin install harness@harness-marketplace
```

### Direct Installation as Global Skill

```shell
# Copy the skills directory to ~/.claude/skills/harness/
cp -r skills/harness ~/.claude/skills/harness
```

## Plugin Structure

```
harness/
├── .claude-plugin/
│   └── plugin.json                 # Plugin manifest
├── skills/
│   └── harness/
│       ├── SKILL.md                # Main skill definition (6-Phase workflow)
│       └── references/
│           ├── agent-design-patterns.md   # 6 architectural patterns
│           ├── orchestrator-template.md   # Team/subagent orchestrator templates
│           ├── team-examples.md           # 5 real-world team configurations
│           ├── skill-writing-guide.md     # Skill authoring guide
│           ├── skill-testing-guide.md     # Testing & evaluation methodology
│           └── qa-agent-guide.md          # QA agent integration guide
└── README.md
```

## tools

Trigger in Claude Code with prompts like:

```
Build a harness for this project
Design an agent team for this domain
Set up a harness
```

### Execution Modes

| Mode | Description | Recommended For |
|------|-------------|-----------------|
| **Agent Teams** (default) | TeamCreate + SendMessage + TaskCreate | 2+ agents requiring collaboration |
| **Subagents** | Direct Agent tool invocation | One-off tasks, no inter-agent communication needed |

<p align="center">
  <img src="harness_team.png" alt="Harness Agent Team" width="500">
</p>

### Architecture Patterns

| Pattern | Description |
|---------|-------------|
| Pipeline | Sequential dependent tasks |
| Fan-out/Fan-in | Parallel independent tasks |
| Expert Pool | Context-dependent selective invocation |
| Producer-Reviewer | Generation followed by quality review |
| Supervisor | Central agent with dynamic task distribution |
| Hierarchical Delegation | Top-down recursive delegation |

## Output

Files generated by Harness:

```
your-project/
├── .claude/
│   ├── agents/          # Agent definition files
│   │   ├── analyst.md
│   │   ├── builder.md
│   │   └── qa.md
│   └── skills/          # Skill files
│       ├── analyze/
│       │   └── SKILL.md
│       └── build/
│           ├── SKILL.md
│           └── references/
```

## Use Cases — Try These Prompts

Copy any prompt below into Claude Code after installing Harness:

**Deep Research**
```
Build a harness for deep research. I need an agent team that can investigate
any topic from multiple angles — web search, academic sources, community
sentiment — then cross-validate findings and produce a comprehensive report.
```

**Website Development**
```
Build a harness for full-stack website development. The team should handle
design, frontend (React/Next.js), backend (API), and QA testing in a
coordinated pipeline from wireframe to deployment.
```

**Webtoon / Comic Production**
```
Build a harness for webtoon episode production. I need agents for story
writing, character design prompts, panel layout planning, and dialogue
editing. They should review each other's work for style consistency.
```

**YouTube Content Planning**
```
Build a harness for YouTube content creation. The team should research
trending topics, write scripts, optimize titles/tags for SEO, and plan
thumbnail concepts — all coordinated by a supervisor agent.
```

**Code Review & Refactoring**
```
Build a harness for comprehensive code review. I want parallel agents
checking architecture, security vulnerabilities, performance bottlenecks,
and code style — then merging all findings into a single report.
```

**Technical Documentation**
```
Build a harness that generates API documentation from this codebase.
Agents should analyze endpoints, write descriptions, generate usage
examples, and review for completeness.
```

**Data Pipeline Design**
```
Build a harness for designing data pipelines. I need agents for schema
design, ETL logic, data validation rules, and monitoring setup that
delegate sub-tasks hierarchically.
```

**Marketing Campaign**
```
Build a harness for marketing campaign creation. The team should research
the target market, write ad copy, design visual concepts, and set up
A/B test plans with iterative quality review.
```

## Coexistence — Harness and Neighbors

Harness is not alone in the Claude Code / agent-framework ecosystem. The following repos live in adjacent layers; each is described in a parallel "X is …, Harness is …" form so you can pick the one that fits your need or combine several.

| Repo | Their position | Relationship to Harness |
|------|----------------|-------------------------|
| [coleam00/Archon](https://github.com/coleam00/Archon) | "harness builder" — deterministic, repeatable runtime configurations | **Same L3, neighbor sub-layer.** Archon is a Runtime-Configuration Factory, Harness is a Team-Architecture Factory. Pick Archon for runtime determinism, Harness for team architecture, or combine them. |
| [SaehwanPark/meta

## requirements

- [Agent Teams enabled](https://code.claude.com/docs/en/agent-teams): `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

## FAQ

<details>
<summary><b>Q1. Isn't "+60%" oversold?</b></summary>

**A.** The +60% figure comes from an **author-measured A/B (n=15, 15 tasks, measured on the sister repo `claude-code-harness`)**. Every citation in this repo pairs the number with the disclosure "n=15, author-measured, third-party replications pending" in the same sentence. For adoption decisions, we recommend running a 2–4 week internal pilot and measuring your own numbers.

**Evidence:**
- Author A/B: [revfactory/claude-code-harness](https://github.com/revfactory/claude-code-harness)
- Paper: *Hwang, M. (2026). Harness: Structured Pre-Configuration for Enhancing LLM Code Agent Output Quality*
</details>

<details>
<summary><b>Q2. Why "harness factory" and not "harness builder"? Isn't this competing with Archon?</b></summary>

**A.** Archon generates deterministic runtime configurations — it's a **Runtime-Configuration Factory**. Harness generates agent team architectures (team structure, message protocols, review gates) — it's a **Team-Architecture Factory**. They are **neighbor sub-layers of the same L3 Meta-Factory** and serve different needs. Pick Archon for runtime determinism, Harness for team-architecture patterns, or combine them (design architecture with Harness → deploy runtime with Archon).

**Evidence:**
- Archon self-definition: [clawfit docs/reference-levels.md](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)
- Sub-layer declaration: see the **Category — Where Harness Sits** section above
- Archon repo: [github.com/coleam00/Archon](https://github.com/coleam00/Archon)
</details>

<details>
<summary><b>Q3. Isn't "Claude Code only" too narrow? What about Gemini/Codex?</b></summary>

**A.** Currently the official runtime is Claude Code only. A Codex port of the same concept — [SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness) — is already public, so Codex teams can start there. Harness chose "Claude-Code-native, deep" over "multi-runtime, shallow"; cross-runtime collaboration with sibling repos (meta-harness, harness-init, OpenRig) is on the roadmap.

**Evidence:**
- Codex port: [github.com/SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness)
- Cross-runtime scaffolder: [github.com/Gizele1/harness-init](https://github.com/Gizele1/harness-init)
</details>

## License

Apache 2.0
