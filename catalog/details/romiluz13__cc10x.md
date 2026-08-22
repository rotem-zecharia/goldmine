# romiluz13/cc10x

The Loop Engine for Claude Code — engineer the loop, not the prompt. 1 router · 9 agents · 16 skills · 4 workflows. Fail-closed gates, test honesty, anti-anchored review.

## installation

**Step 1 — Add the marketplace:**

```bash
/plugin marketplace add romiluz13/cc10x
```

**Step 2 — Install the plugin:**

```bash
/plugin install cc10x@cc10x
```

Then say **"set up cc10x for me"** in Claude Code and restart. Done.

---

## Quick Start Examples

### Build Something

```
"build a user authentication system"

→ Router detects BUILD intent
→ Stops to resolve missing requirements first
→ component-builder drives RED → GREEN → REFACTOR
→ code-reviewer + failure-hunter run in parallel
→ integration-verifier checks wiring, artifacts, and behavior
→ Workflow state and memory are updated
```

### Fix a Bug

```
"debug the payment processing error"

→ Router detects DEBUG intent
→ Loads prior failures and project memory
→ bug-investigator starts from logs and observed behavior
→ code-reviewer checks the fix path
→ integration-verifier confirms the bug is actually closed
→ Useful findings go back into memory
```

### Review Code

```
"review this PR for security issues"

→ Router detects REVIEW intent
→ code-reviewer uses repo and git context
→ Reports findings only when confidence clears the bar
→ Every finding includes file:line evidence
```

---

## features

Ask Claude for something complex. It works for a while. Then it declares **"Done!"** — tests still red, refactor half-finished, and by message 40 it's contradicting itself because the context is gone.

**cc10x fixes the loop, not the prompt.** A better model running free loses to the same model, constrained and looped correctly. That's the whole bet.

| The pain you know | How cc10x handles it |
| --- | --- |
| "Done!" on red tests | `integration-verifier` is independent of the builder. Phase-exit gates block advancement on partial evidence. |
| Silent failures nobody asked about | `failure-hunter` runs in parallel with review — greps for swallowed errors and empty catches. |
| Context falls apart after compaction | Workflow state on disk with stable UUIDs. Memory files the router auto-heals. |
| Planning is just a chat | Three planning modes chosen by intent, with a fresh anti-anchored review by a reviewer who never saw the planner's rationale. |
| 12 slash commands to remember | One router. Every request hits `cc10x-router` first. |
| `.claude/` prompt spam on every fanout | State lives at `.cc10x/` — outside `.claude/`, so the harness's sensitive-file gate never fires. |
| Green tests that prove nothing | Test Honesty Gates grep for `getByTestId('…-mock')`, `as any`, `.find()` bypass, `setTimeout()` waits. A hit can't count as PASS on that test's strength alone. |
| Reviewer findings that sound right but aren't | Every finding at confidence ≥80 needs a verbatim `file:line` quote or it's auto-demoted. The verifier independently re-reads the line and drops hallucinated findings before they can gate. |
| Orchestrator context rotting with pasted history | Dispatch by reference, not by blob — the diff is written to disk, the prompt passes a path, never a body. (One real dispatch hit 42k chars, 99% pasted history. The scar became law.) |

---

## How It Works

**You describe the work. cc10x routes it, brings in the right specialists, and keeps the bar for "done" higher than a convincing paragraph.**

```
                        YOU
                         │
                         ▼
            ┌────────────────────────┐
            │      cc10x-router      │  ◄── only entry point
            │   detects intent       │
            └────────────┬───────────┘
                         │
          ┌──────────────┼──────────────┬─────────────┐
          │              │              │             │
          ▼              ▼              ▼             ▼
        BUILD          DEBUG         REVIEW         PLAN
          │              │              │             │
          ▼              ▼              ▼             ▼
    component-      bug-          code-          planner
      builder    investigator   reviewer            │
          │              │              │             ▼
          ▼              ▼           (done)     plan-gap-
  [code-reviewer    code-reviewer             reviewer
   ∥ silent-            │
   failure-            ▼
    hunter]      integration-
          │         verifier
          ▼
   integration-
     verifier

                 ┌──────────────────────────┐
                 │  STATE (every workflow)  │
                 │  activeContext.md        │
                 │  patterns.md            │
                 │  progress.md            │
                 │  {wf}.json + .events    │
                 └──────────────────────────┘
```

---
