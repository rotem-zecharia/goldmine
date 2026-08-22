# tobihagemann/turbo

A composable dev process for agentic coding harnesses, packaged as modular skills. Turbo has sibling editions for Claude Code and Codex.

## requirements

Pick your edition: [`claude/SETUP.md`](claude/SETUP.md) for Claude Code, [`codex/SETUP.md`](codex/SETUP.md) for Codex. Both editions work best with their respective Max-tier plans (pipeline workflows are context-heavy). Additional tools are installed during setup.

**External services:** The Claude edition benefits from ChatGPT Plus or higher for Codex peer review. The Codex edition benefits from Claude Code access for Claude peer review. ChatGPT Pro or Business is useful for [`/consult-oracle`](claude/skills/consult-oracle/SKILL.md), where Pro models are the only ones that reliably solve very hard problems. [`/peer-review`](claude/skills/peer-review/SKILL.md) and [`/consult-oracle`](claude/skills/consult-oracle/SKILL.md) are designed as swappable puzzle pieces, so if you don't have access, replace them with alternatives that work for you.

## installation

In Claude Code or Codex, prompt:

```
Walk me through the Turbo setup. Read SETUP.md from the tobihagemann/turbo repo and follow the guide for your edition.
```

The agent reads the root [`SETUP.md`](SETUP.md), picks the file that matches its harness ([`claude/SETUP.md`](claude/SETUP.md) or [`codex/SETUP.md`](codex/SETUP.md)), clones the repo, installs skills, configures the environment, and walks you through each step interactively.

### Updating

Run [`/update-turbo`](claude/skills/update-turbo/SKILL.md) (Claude Code) or [`$update-turbo`](codex/skills/update-turbo/SKILL.md) (Codex) to update all skills. It fetches the latest update instructions from GitHub, builds a changelog, handles conflict detection for customized skills, and manages exclusions.

## Editions

```text
claude/   # Claude Code edition
codex/    # Codex edition
```

Each edition is a self-contained tree with its own `SETUP.md`, `UPDATE.md`, `MIGRATION.md`, `ADDITIONS.md`, `SKILL-CONVENTIONS.md`, and `skills/`. The root-level files are short routers that point at the per-edition versions.

## What Is This?

Turbo covers the full dev lifecycle. Five ideas shape its design:

1. **Standardized process.** Skills capture dev workflows so you can run them directly instead of prompting from scratch. [`/turboplan`](claude/skills/turboplan/SKILL.md) analyzes complexity and routes to the right mode. [`/finalize`](claude/skills/finalize/SKILL.md) runs your entire post-implementation QA in one command. [`/investigate`](claude/skills/investigate/SKILL.md) follows a structured root cause analysis cycle. The skill is the prompt.
2. **Layered design.** Skills compose other skills to any depth. [`/review-code security`](claude/skills/review-code/SKILL.md) runs a single-concern scan. [`/review-code`](claude/skills/review-code/SKILL.md) with no argument runs all six types in parallel. [`/polish-code`](claude/skills/polish-code/SKILL.md) loops stage → format → lint → test → review → evaluate → apply → smoke test until stable. [`/finalize`](claude/skills/finalize/SKILL.md) wraps the whole pipeline with self-improvement and commit. [`/audit`](claude/skills/audit/SKILL.md) fans out to all analysis skills in parallel, evaluates the combined findings, and produces a health report. Each pipeline composes with a natural, predictable interface. See [The Turboplan Pipeline](#the-turboplan-pipeline) and [The Finalize Pipeline](#the-finalize-pipeline) for worked examples.
3. **Swappable by design.** Every skill owns one concern and communicates through standard interfaces. Replace any piece with your own and the pipeline adapts. See [The Puzzle Piece Philosophy](#the-puzzle-piece-philosophy) for details.
4. **Works out of the box.** Install the skills and the full workflow is ready. Dependencies are standard dev tooling (GitHub CLI, Codex) that most teams already have.
5. **Just skills.** No framework, no custom runtime, no new memory system. Skills are plain markdown that use the harness's native primitives (git, filesystem, built-in tools). Remove an independent skill and the rest still work.

The one thing beyond skills is each edition's `ADDITIONS.md` (e.g. [`claude/ADDITIONS.md`](claude/ADDITIONS.md)), a small set of behavioral rules added to your harness's instruction file during setup. The most important one is **Skill Loading**: without it, the agent tends to skip reloading skills it has already seen in a session, which causes it to silently drop steps in nested pipelines like [`/finalize`](claude/skills/finalize/SKILL.md). The additions are kept in sync by [`/update-turbo`](claude/skills/update-turbo/SKILL.md). See [claude/docs/skill-loading-reasoning.md](claude/docs/skill-loading-reasoning.md) for the full rationale (Claude-specific failure modes and mitigations; the Codex edition adapts the same rules in [`codex/ADDITIONS.md`](codex/ADDITIONS.md)).

The other core piece is [`/self-improve`](claude/skills/self-improve/SKILL.md), which makes the whole system compound: it routes ea

## tools

These are prompts you can type directly into Claude Code or Codex (use `$skill-name` in Codex). Skill names work as natural words in your sentences.

```
# Planning a change (single entry — /turboplan routes based on complexity)
/turboplan add a caching layer to the image pipeline  ← plan mode → draft → refine → halt; run /implement-plan after
/turboplan build a notification system with backend, API, and UI  ← same route, larger plan
/survey-patterns  ← pattern-ground an approach without drafting a plan
/implement-plan  ← execute the latest plan in .turbo/plans/ in a fresh session

# Investigating bugs
tests are failing in the auth module, can you please /investigate?
/investigate the app crashes when i click "save" after editing a profile

# Reviewing code
/review-code
/review-pr for PR #42

# Auditing project health
/audit
read @.turbo/audit.md and /apply-findings  ← follow-up session

# Onboarding to a new project
/onboard
/map-codebase  ← architecture report only

# Resolving PR feedback
/resolve-pr-comments
