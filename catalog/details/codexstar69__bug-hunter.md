# codexstar69/bug-hunter

Adversarial AI bug hunter with auto-fix skill for Claude Code, Cursor, Codex CLI, GitHub Copilot CLI, Kiro CLI, Opencode, Pi Coding Agent, and more. Multi-agent pipeline finds security vulnerabilities

## features

Many AI code-review tools produce a long list of possible issues but leave the
developer to discover which claims are real. A plausible explanation is not
proof that a runtime bug is reachable. Framework behavior, middleware,
validation in another file, and language guarantees can turn an alarming
finding into a false positive.

Bug Hunter treats a finding as a claim that must survive opposition:

1. The Hunter explains the exact runtime failure, source evidence, trigger,
   severity, and cross-file dependencies.
2. The Skeptic tries to disprove the claim by tracing the same code and checking
   protections the Hunter may have missed.
3. The Referee compares both sides, independently checks the strongest or most
   serious claims, and issues the final verdict.

For teams comparing an AI code-review tool, security code scanner,
vulnerability scanner, or static-analysis assistant, this separation matters:
automated code review stays useful only when the evidence and uncertainty are
visible.

This adversarial code review is designed to reduce false-positive overload
without hiding uncertainty. Results that cannot be settled become
`MANUAL_REVIEW` or `unreviewed`; they are not silently presented as clean.

The system focuses on behavioral correctness and security. It is not a style
linter. Naming preferences, formatting, unused code, missing comments, and
general refactoring suggestions are outside the Hunter's reporting scope unless
they create a reachable runtime problem.

## How the code-audit pipeline works

<p align="center">
  <img src="https://raw.githubusercontent.com/codexstar69/bug-hunter/183e0a957bd22ea5df83741cd31e396f68b14ae5/docs/images/pipeline-overview.png" alt="Bug Hunter adversarial code-audit pipeline from deterministic triage through Hunter, Skeptic, Referee, reporting, optional fix planning, and verification" width="100%">
</p>

Every phase has a separate job. Role, report, coverage, fix, adaptive, retrieval, verification, and benchmark artifacts use schema-validated JSON; triage JSON is deterministic pipeline input.

| Stage | What it does | Main evidence |
|---|---|---|
| Risk triage | Classifies source files and selects risk-ordered scan scope without an AI model | `triage.json` |
| Adaptive policy | Chooses bounded `fast`, `balanced`, or `assurance` context/review/verification policy when requested or supplied | `adaptive-plan.json` |
| Recon | Adds stack, architecture, and trust-boundary context for multi-file scans | `recon.json` |
| Retrieval planning | Selects hypothesis-relevant mandatory and optional evidence under hard budgets | `retrieval-plan.json` |
| Hunter | Finds reachable logic, security, concurrency, data, and error-path bugs | `hunter-findings.json` |
| Documentation lookup | Checks version-sensitive library or framework assumptions | Evidence added to the finding or challenge |
| Skeptic | Tries to disprove every Hunter claim with code and counter-evidence | `skeptic.json` |
| Referee | Delivers `REAL_BUG`, `NOT_A_BUG`, or `MANUAL_REVIEW` verdicts | `referee.json` |
| Hybrid verification | Runs bounded tests, type/static/build/reproduction/fuzz/security-static checks when configured | `verification-report.json` |
| Report join | Separates confirmed, dismissed, manual-review, and unreviewed results | `scan-report.json` and `report.md` |
| Fix strategy | Classifies confirmed bugs by remediation risk | `fix-strategy.json` |
| Fix plan | Records bug details, files, claimed ranges, remediation class, and rollout order | `fix-plan.json` |
| Fix and verify | Applies only authorized work and records checks or rollback results | `fix-report.json` |

A malformed or missing required canonical artifact is a failed phase, not
evidence of a clean scan. For schema-backed phases, JSON is the source of truth;
Markdown reports are readable views of those contracts.

Bug Hunter adjusts execution to the repository and the agent runtime. A
single-file scan stays small. Larger scans may use bounded parallel,
ch
