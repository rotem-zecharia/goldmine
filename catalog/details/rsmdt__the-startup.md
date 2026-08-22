# rsmdt/the-startup

The Agentic Startup - A collection of Claude Code commands, skills, and agents.

## installation

**Requirements:** Claude Code v2.0+ with marketplace support

```bash
curl -fsSL https://raw.githubusercontent.com/rsmdt/the-startup/main/install.sh | sh
```

This installs the core plugins, configures the default output style, and sets up the [statusline](#-statusline) with a customizable config file.

<details>
<summary><strong>Manual Installation</strong></summary>

Start `claude` and run the following:

```bash
# Add The Agentic Startup marketplace
/plugin marketplace add rsmdt/the-startup

/plugin install start@the-startup  # Install the Start plugin (core workflows)
/plugin install team@the-startup   # (Optional) Install the Team plugin (specialized agents)
```

</details>

**After installation:**

```bash
# (Optional) Create project governance rules
/constitution                      # Auto-enforced during specify, implement, review

# Switch output styles anytime
/output-style "start:The Startup"   # High-energy, fast execution (default)
/output-style "start:The ScaleUp"   # Calm confidence, educational
```

---

## 🚀 Quick Start

Create a specification and implement it:

```bash
# Create a specification
/specify Add user authentication with OAuth support

# Execute the implementation
/implement 001
```

That's it! You're now using spec-driven development.

---

## 📖 The Complete Workflow

The Agentic Startup follows **spec-driven development**: comprehensive specifications before code, ensuring clarity and reducing rework.

### All Skills at a Glance

```
┌──────────────────────────────────────────────────────────┐
│                    SETUP (optional)                      │
│                                                          │
│  /constitution ► Create project governance rules         │
│                  (auto-enforced in BUILD workflow)       │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                    BUILD (primary flow)                  │
│                                                          │
│  /specify ────► Create specs (Requirements + Solution)   │
│      │           ↳ Classifies complexity: Direct / Incremental / Factory │
│      │           ↳ Constitution checked on SDD           │
│      ▼                                                   │
│  /validate ───► Check quality (3 Cs framework)           │
│      │           ↳ Constitution mode available           │
│      ▼                                                   │
│  /implement ──► Auto-dispatch by tier, then execute      │
│      │           ↳ Direct (no plan) / Incremental (phase loop) / Factory (parallel units) │
│      │           ↳ Constitution + drift enforced         │
│      ▼                                                   │
│  /test ───────► Run tests, enforce ownership             │
│      │           ↳ No "pre-existing" excuses             │
│      ▼                                                   │
│  /review ─────► Multi-agent code review                  │
│      │           ↳ Constitution compliance checked       │
│      ▼                                                   │
│  /document ───► Generate/sync documentation              │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                    MAINTAIN (as needed)                  │
│                                                          │
│  /analyze ────► Discover patterns & rules                │
│                                                          │
│  /refactor ───► Improve code (preserve behavior)         │
│                                                          │
│  /debug ──────► Fix bugs (root cause analysis)           │
└──────────────────────────────────────────────────────────┘
```

### Step-by-Step Walkthrough

#### Step 1: Create Your Specification

```bash
/s

## configuration

The statusline reads from `~/.config/the-agentic-startup/statusline.toml`:

```toml
# Format string (customize what's displayed)
format = "<path> <branch>  <model>  <context>  <session>  <help>"

## tools

plan = "auto"
fallback_plan = "pro"

[thresholds.context]
warn = 70    # percentage
danger = 90

[thresholds.cost]
# Uncomment to override plan defaults:
# warn = 2.00
# danger = 5.00
```

### Plan-Based Cost Defaults

| Plan | Monthly | Warn | Danger |
|------|---------|------|--------|
| `pro` | $20 | $1.50 | $5.00 |
| `max5x` | $100 | $5.00 | $15.00 |
| `max20x` | $200 | $10.00 | $30.00 |
| `api` | Pay-as-you-go | $2.00 | $10.00 |

### Format Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `<path>` | Abbreviated directory | `~/C/p/project` |
| `<branch>` | Git branch with dirty indicator | `⎇ main*` |
| `<model>` | Model and output style | `🤖 Opus 4.5 (The Startup)` |
| `<context>` | Context usage bar and percentage | `🧠 ⣿⣿⡇⠀⠀ 50%` |
| `<session>` | Duration and cost | `🕐 30m  💰 $1.50` |
| `<lines>` | Lines added/removed | `+156/-23` |
| `<spec>` | Active spec ID (when in .start/specs/) | `📋 005` |
| `<help>` | Help text | `? for shortcuts` |

**Example minimal format:**
```toml
format = "<context>  <session>"
```

---

## features

Real workflow features that solve real problems — not just another AI wrapper.

### Resume Across Sessions

Hit a context limit? Start a new conversation and pick up exactly where you left off. Specs persist on disk — Claude reads them and continues.

```bash
/specify 001    # ← resumes spec creation from where you left off
/implement 001  # ← resumes implementation, tracking progress in spec files
```

### Code Ownership Mandate

No more "pre-existing failure" excuses. When `/test` finds a failing test, it fixes it — period. You touched the codebase, you own it.

### Drift Detection

Implementation drifting from the spec? Caught automatically during `/implement`. Scope creep, missing items, contradictions — flagged with options to update the spec or the code.

### Adaptive Code Review

`/review` auto-detects what matters. Async code triggers concurrency review. Dependency changes trigger supply-chain checks. UI changes trigger accessibility audits. 5 base perspectives + conditional specialists.

### Implement Any Plan

Not just for specs created with `/specify`. `/implement` works with any markdown implementation plan — bring your own architecture docs, migration guides, or design documents.

```bash
/implement path/to/plan.md
```

### Non-Linear Specs

Skip what you don't need. Start with a solution design, jump straight to decomposition, or go full PRD → SDD → tier-appropriate decomposition. Skipped phases are logged as decisions, not gaps.

### Adversarial Debugging

Tough bugs get multiple investigators that actively try to disprove each other's hypotheses. The surviving theory is most likely the root cause — competing hypotheses, not confirmation bias.

### Agent Teams (Experimental) — New in v3

Enable multi-agent collaboration where specialized agents coordinate autonomously on complex tasks. The installer configures this automatically, or enable manually:

```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

---

## 🎯 Philosophy

Research shows **2-22% accuracy improvement** with specialized task agents vs. single broad agents ([Multi-Agent Collaboration, 2025](https://arxiv.org/html/2501.06322v1)). Leading frameworks organize agents by **capability**, not job titles. The Agentic Startup applies this research through activity-based specialization.

### The Problem We Solve

Development often moves too fast without proper planning:
- Features built without clear requirements
- Architecture decisions made ad-hoc during coding
- Technical debt accumulates from lack of upfront design
- Teams struggle to maintain consistency across implementations

### Our Approach

**1. Specify First** — Create comprehensive specifications before writing code
- **requirements.md** — What to build and why
- **solution.md** — How to build it technically
- **plan/** — Executable tasks and phases (README.md manifest + phase-N.md files)

**2. Review & Refine** — Validate specifications with stakeholders
- Catch issues during planning, not during implementation
- Iterate on requirements and design cheaply
- Get alignment before costly development begins

**3. Implement with Confidence** — Execute validated plans phase-by-phase
- Clear acceptance criteria at every step
- Parallel agent coordination for speed
- Built-in validation gates and quality checks

**4. Document & Learn** — Capture patterns for future reuse
- Automatically document discovered patterns
- Build organizational knowledge base
- Prevent reinventing solutions

### Core Principles

- **Measure twice, cut once** — Investing time in specifications saves exponentially more time during implementation.
- **Documentation as code** — Specs, patterns, and interfaces are first-class artifacts that evolve with your codebase.
- **Parallel execution** — Multiple specialists work simultaneously within clear boundaries, maximizing velocity without chaos.
- **Quality gates** — Definition of Ready (DOR) and Definition of Done (DOD) ensure st
