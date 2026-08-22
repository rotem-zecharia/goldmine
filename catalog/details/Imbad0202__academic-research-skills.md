# Imbad0202/academic-research-skills

Academic Research Skills for Claude Code: research → write → review → revise → finalize

## features

Lu et al. (2026, *Nature* 651:914-919) built **The AI Scientist** — the first fully autonomous AI research system to publish a paper through blind peer review at a top-tier ML venue (ICLR 2025 workshop, score 6.33/10 vs workshop average 4.87). Their Limitations section enumerates the failure modes that any fully-autonomous AI research pipeline inherits: implementation bugs, hallucinated results, shortcut reliance, bug-as-insight reframing, methodology fabrication, frame-lock, citation hallucinations.

ARS is built on the premise that **a human researcher augmented by AI avoids these failure modes better than either alone**. Stage 2.5 and Stage 4.5 integrity gates run a 7-mode blocking checklist (see [`academic-pipeline/references/ai_research_failure_modes.md`](academic-pipeline/references/ai_research_failure_modes.md)); the reviewer offers an opt-in calibration mode that measures its own FNR/FPR against a user-supplied gold set.

[**Zhao et al.**](https://arxiv.org/abs/2605.07723) (2026-05) audited 111M references across 2.5M papers on arXiv, bioRxiv, SSRN, and PMC. Their conservative estimate is 146,932 hallucinated citations for 2025 alone, with an observed mid-2024 inflection; for the bioRxiv-to-PMC pairing they report 85.3% preprint-to-published persistence. The paper describes "real citations deployed to support claims the cited references do not actually make" as an open challenge. ARS v3.7.1 added trust-chain frontmatter for source provenance; v3.7.3 added locator infrastructure (three-layer citation anchors) for future claim-level audits and surfaces advisory risk signals at cite time (ARS labels the claim-faithfulness gap internally as "L3"; this is ARS terminology, not the paper's). v3.7.x is motivated by Zhao et al.'s corpus-scale findings; corpus-scale evaluation of ARS itself remains future work.

v3.8 closes the second half of the L3 gap. v3.7.3 made every citation carry a locator anchor; v3.8 adds an opt-in audit pass (`ARS_CLAIM_AUDIT=1`) that fetches the cited source against each anchor and judges whether the claim is actually supported. Five new HIGH-WARN classes (claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited) gate-refuse output through the formatter terminal hard gate. Calibration is shipped as a 20-tuple gold set with FNR<0.15 + FPR<0.10 acceptance thresholds; ramp-on plan is deferred to post-calibration evidence per v3.8 spec §5.

[**Ren et al.**](https://arxiv.org/abs/2607.13104) (2026, *Self-Improvements in Modern Agentic Systems: A Survey*) supplies a third, survey-level anchor. Its scientific-discovery synthesis (§7.4) concludes that discovery agents cannot easily verify novelty, correctness, or reproducibility on their own and may exploit weak proxies instead, must manage evidence across heterogeneous tools and literature, and raise governance issues — "scientific writing can also amplify misinformation when the evidence is weak." Its generation-loop chapters (§5.1–§5.2) list human auditing and retained human anchors among the practical safeguards for self-generated evaluation loops, and its historical chapter (§2.2) records the oldest form of the same lesson: the practical success of Lenat's EURISKO depended heavily on the user serving as the external evaluation signal, pruning unproductive heuristic drift — a limitation the survey notes persists in modern agentic systems. ARS cites the survey as design rationale for its human-in-the-loop stance, not as empirical proof that human-in-the-loop pipelines outperform autonomous ones; the survey's actionable deltas for ARS are tracked in #539–#541 and #547–#550.

v3.3 was inspired by [**PaperOrchestra**](https://arxiv.org/abs/2604.05018) (Song, Song, Pfister & Yoon, 2026, Google): Semantic Scholar API verification, anti-leakage protocol, VLM figure verification, and revision-trajectory tracking. ARS now implements that last idea through categorical, evidence-anchored criterion trajectorie

## installation

**Prerequisites**

- [Claude Code](https://docs.claude.com/en/docs/claude-code/setup) (latest; plugin packaging requires recent versions)
- `ANTHROPIC_API_KEY` exported, or set on first `claude` run
- *Optional:* Pandoc for DOCX, tectonic + Source Han Serif TC for APA 7.0 PDF (Markdown output works without either)
- *Optional (real Python):* The core skills (research / write / review) need no Python — they are prompt-driven. A **real Python interpreter** is needed only for: the `PreToolUse` write-scope guard (optional subagent hardening — if no real Python is found it cleanly no-ops and the guard is simply inactive; core skills are unaffected), plus a few opt-in features that shell out to Python (revision-patch mode, the submission-package verifier, and the `/ars-cache-invalidate` / `/ars-mark-read` / `/ars-unmark-read` commands). On Windows, note that `python3` is often a non-functional Microsoft Store placeholder rather than real Python; install Python from python.org (or via `winget`) so the launcher can find a real interpreter. The guard launcher is a POSIX shell script and `hooks.json` invokes it through `bash`, so on Windows it needs **Git Bash** (bundled with Git for Windows). With Git Bash present, a missing real Python degrades cleanly (the guard no-ops, silently). Without Git Bash, Claude Code falls back to PowerShell, which cannot run the `.sh` launcher at all: the guard is inactive and the `PreToolUse` hook will log an error per call rather than no-op quietly (accepted degradation — the guard is optional and never blocks your writes, but the hook noise is the trade-off until Git Bash is installed).

> **Which controls are active in *your* install channel?** Availability varies by install channel. See the per-channel map: [docs/CONTROL_AVAILABILITY.md](docs/CONTROL_AVAILABILITY.md).

**Plugin install (v3.7.0+, recommended):**

```text
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

**Verify it works:** run `/ars-plan` and describe a paper you're working on — ARS will start a Socratic dialogue to map out chapter structure. For a single-shot test instead, try `/ars-lit-review "your topic"`.

**👉 [docs/SETUP.md](docs/SETUP.md)** — full guide: install Claude Code, set up API keys, optional Pandoc/tectonic for DOCX/PDF, cross-model verification (`ARS_CROSS_MODEL`), and six installation methods (Plugin, project skills, global skills, claude.ai Project, repo-cloned, Claude Science import).

**👉 [docs/DATA_FLOWS.md](docs/DATA_FLOWS.md)** — what leaves your machine (bibliographic resolvers, optional consent-gated cross-model calls, the plugin update check), what is cached locally, for how long, and how to turn each path off.

**👉 [docs/RISK_REGISTER.md](docs/RISK_REGISTER.md)** — the standing risks the suite knows about, which existing controls address each one, the evidence status behind those controls, and what remains open.

**Using Claude Science?** The four skills import directly: **Skills → Import from GitHub**, paste `https://github.com/Imbad0202/academic-research-skills`, **Preview**, then **Import 4 skills** (requires v3.14.0+ of this repo — the importer reads the explicit skill paths in the marketplace manifest). Imports are point-in-time snapshots: re-import after ARS updates. Imported skills carry the ARS methodology (research / writing / review protocols); Claude Code-specific machinery — slash commands, hooks, subagent orchestration — does not transfer. See [docs/SETUP.md](docs/SETUP.md) Method 5 for details.

**Using Pi?** Install the in-tree, community-maintained wrapper with `pi install git:github.com/Imbad0202/academic-research-skills`. It keeps the original ARS content authoritative and documents Pi-specific orchestration and hook limitations. See [`pi/README.md`](pi/README.md).

**Using Codex CLI?** Install the sibling distribution instead: [`Imbad0202/academic-research-skills-codex`](https://github.com/Imbad0202/academic-research-skills-codex) — sa

## configuration

> Minor release bundling: the opt-in contamination-triangulation **terminal policy layer** (#127 — default citation behavior byte-equivalent to v3.9.0); **Kong et al. 2026 survey adoptions** — the Rebuttal Commitment Ledger (#256/#266/#268/#269) and discipline-relative domain evidence profiles (#259); the **v3.10 measurement infrastructure** — a generalized eval gold set + ranking-lift CI gate (#184); the **scoped-write guard MVP** (#134) — a deterministic `PreToolUse` hook that fences the 23 single-phase agents to their own phase directory and denies them Bash (they use the Grep/Glob and structured editing tools instead); the `/ars-mark-read` plugin commands (#190) plus a broken-on-arrival fix (#195); a Simplified-Chinese README (#185); and CI hardening (#156/#155). `academic-paper` → v3.2.0 and `academic-paper-reviewer` → v1.10.0 for the Commitment-Ledger and domain-profile additions; `academic-pipeline` tracks the suite at v3.10.0. Default skill behavior is unchanged unless a strict policy mode is opted into; the one default-on change is the #134 guard, which constrains the fenced subagents, not user-facing outputs.
