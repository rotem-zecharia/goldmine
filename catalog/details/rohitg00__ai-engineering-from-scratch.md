# rohitg00/ai-engineering-from-scratch

Learn it. Build it. Ship it for others.

## installation

Three ways in. Pick one.

**Option A — learn in your terminal *(recommended)*.** After the Node.js,
`npx`, host, and scope preflight above, install the learning skills into a
compatible agent and let the course drive itself:

```bash
npx skills add rohitg00/ai-engineering-from-scratch
```

Use the host-specific invocation table above. The installed skills provide
`start-learning`, `learn`, `course-guide`, and the focused
`learn-mcp` and `learn-agent-skills` routes. Lesson prose can
stream from this repository without a clone. A local clone is required for
copied repository code commands and executable MCP or Agent Skills labs.
Progress lives in `LEARNING.md`, `MCP-LEARNING.md`, or
`AGENT-SKILLS-LEARNING.md` in your project, so every session can resume.

**Option B — read.** Open any completed lesson on
[aiengineeringfromscratch.com](https://aiengineeringfromscratch.com) or expand a phase under
[Contents](#contents). No setup, no cloning.

**Option C — clone and run.**

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/vectors.py
```

Cloning also auto-loads the learning skills in Claude Code, and gives every
lesson's code to the `learn` tutor for real execution instead of read-along.

## requirements

- You can write code (any language; Python helps).
- You want to understand how AI **actually works**, not just call APIs.

### Prepare for Claude certifications

The [Claude Certification Academy](certifications/claude/README.md) is a free,
open-source preparation program for all four official Claude certification tracks:
Associate Foundations, Developer Foundations, Architect Foundations, and Architect
Professional. Each route combines blueprint-mapped lessons, runnable labs, a
diagnostic, capstone work, and a full-length original practice exam.

Use the [AI-native GitHub onboarding guide](certifications/claude/GETTING_STARTED.md)
with Claude Code, Codex, ChatGPT, Cursor, or another agent. Run
`claude-certification` in Codex, `/claude-certification` in Claude Code, or ask
another host to use `claude-certification`. It chooses a track, creates a
persistent route in `CLAUDE-CERTIFICATION.md`, teaches one step at a time, runs
the real labs, and gives artifact-based feedback. The same curriculum remains
available on the [certification website](https://aiengineeringfromscratch.com/certifications.html).

The academy is independent study material based on public exam objectives. It is not
affiliated with Anthropic, does not reproduce live exam questions, and cannot guarantee
a passing score.

### The learning skills

| Skill | What it does |
|---|---|
| [`start-learning`](skills/start-learning/SKILL.md) | One-time onboarding: why you're learning, placement quiz, personalized plan saved to `LEARNING.md`. |
| [`learn`](skills/learn/SKILL.md) | The tutor loop. Warm-up recall, then the next lesson taught interactively, then its quiz; records progress and a review queue. |
| [`course-guide`](skills/course-guide/SKILL.md) | Topic router. "Where do I learn attention?" or "my loss is NaN" → the exact lessons, with links. |
| [`learn-mcp`](skills/learn-mcp/SKILL.md) | Focused Model Context Protocol (MCP) tutor. Creates `MCP-LEARNING.md`, follows the 17-lesson manifest, and records wire, security, reliability, and conformance evidence. |
| [`learn-agent-skills`](skills/learn-agent-skills/SKILL.md) | Focused Agent Skills tutor. Creates `AGENT-SKILLS-LEARNING.md`, teaches lessons 22, 24, 25, 26, and 27, and records real-host evidence. |
| [`claude-certification`](skills/claude-certification/SKILL.md) | Certification tutor. Chooses CCAO-F, CCDV-F, CCAR-F, or CCAR-P; teaches each lesson; runs labs; reviews artifacts; administers diagnostics and mocks; saves progress. |
| [`find-your-level`](skills/find-your-level/SKILL.md) | Ten-question placement quiz. Maps your knowledge to a starting phase and produces a personalized path with hour estimates. |
| [`check-understanding <phase>`](skills/check-understanding/SKILL.md) | Per-phase quiz, eight questions, with feedback and specific lessons to review. Use the Codex, Claude Code, or natural-language form in the invocation table above. |

```text
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```

## Read the core curriculum as a book

The 20-phase core curriculum under `phases/` compiles into a six-volume book series. EPUB and PDF are built by CI from the same core lesson sources and attached to every [GitHub release](https://github.com/rohitg00/ai-engineering-from-scratch/releases); the links below always resolve to the newest release. Volume numbers index the series, not versions: each copy carries a dated edition stamp, and older editions stay downloadable from their release.

Certification curricula are intentionally not converted into the books. Their
AI tutor state, runnable labs, interactive figures, diagnostics, and timed mocks
remain first-class on GitHub and the website.

| Vol | Title | Phases | Download |
|-----|-------|--------|----------|
| 1 | Foundations · Math, Tooling, and Classical Machine Learning | 00-02 | [EPUB](https://github.com/rohitg00/ai-engineering-from-scratch/releases/latest/download/aiefs-vol1-foundations.epub) · [PDF](https://

## features

<table>
<tr>
<th align="left" width="50%"><sub>FIG_003 · A</sub><br/><b>THE INDUSTRY SIGNAL</b></th>
<th align="left" width="50%"><sub>FIG_003 · B</sub><br/><b>FOUNDATIONAL PAPERS COVERED</b></th>
</tr>
<tr>
<td valign="top">

> *"The hottest new programming language is English."*<br/>
> — **Andrej Karpathy** ([tweet](https://x.com/karpathy/status/1617979122625712128))
>
> *"Software engineering is being remade in front of our eyes."*<br/>
> — **Boris Cherny**, creator of Claude Code
>
> *"Models will keep getting better. The skill that compounds is **knowing what to build**."*<br/>
> — Industry consensus, 2026

</td>
<td valign="top">

- *Attention Is All You Need* — Vaswani et al., 2017 → [Phase 7](#phase-7)
- *Language Models are Few-Shot Learners* (GPT-3) → [Phase 10](#phase-10)
- *Denoising Diffusion Probabilistic Models* → [Phase 8](#phase-8)
- *InstructGPT / RLHF* → [Phase 10](#phase-10)
- *Direct Preference Optimization* → [Phase 10](#phase-10)
- *Chain-of-Thought Prompting* → [Phase 11](#phase-11)
- *ReAct: Reasoning + Acting in LLMs* → [Phase 14](#phase-14)
- *Model Context Protocol* — Anthropic → [Phase 13](#phase-13)

</td>
</tr>
</table>

```text
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```

## Contributing

| Goal | Read |
|---|---|
| Contribute a lesson or fix | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Fork for your team or school | [FORKING.md](FORKING.md) |
| Lesson template | [LESSON_TEMPLATE.md](LESSON_TEMPLATE.md) |
| Track progress | [ROADMAP.md](ROADMAP.md) |
| Glossary | [glossary/terms.md](glossary/terms.md) |
| Code of conduct | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) |

Before submitting a lesson, run the invariant check:

```bash
python3 scripts/audit_lessons.py           # full curriculum
python3 scripts/audit_lessons.py --phase 14  # single phase
python3 scripts/audit_lessons.py --json    # CI-friendly output
```

Exit code is non-zero when any rule fails. Rules (L001–L010) validate directory
shape, `docs/en.md` presence + H1, `code/` non-emptiness, `quiz.json` schema
(rejects the legacy `q/choices/answer` keys that caused issue #102), and
relative links inside lesson docs.

```text
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```

## Sponsor the work

Free, MIT-licensed, 511 lessons. The curriculum is maintained on sponsorship alone. Cash only.

**Reach (verified 2026-05-14):** 55,593 monthly visitors · 90,709 page views · 7.5K stars ·
Twitter/X is the #1 acquisition channel.

<br />
<br />
<a href="https://vercel.com/open-source-program">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge-2026.svg" />
</a>

**Current sponsors:** [CodeRabbit](https://coderabbit.link/rohit-ghumare) · [iii](https://iii.dev?utm_source=ai-engineering-from-scratch&utm_medium=readme&utm_campaign=sponsor)

| Tier | $/mo | What you get |
|------|------|---|
| Backer | $25 | Name in BACKERS.md |
| Bronze | $250 | Text-only row in README sponsor block + launch-day tweet |
| Silver | $750 | Small logo in README + listed as one supported provider in API lessons |
| Gold | $2,000 | Medium logo in README + sponsor page + quarterly X / LinkedIn co-feature |
| Platinum | $5,000 | Hero logo above the fold + one dedicated integration lesson, max 1 partner |

Full rate card, hard rules, pricing anchors, and reach data: [SPONSORS.md](SPONSORS.md).
Sign up via [GitHub Sponsors](https://github.com/sponsors/rohitg00).

```text
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```

If this manual helped you, star the repo. It keeps the project alive.

## License

MIT. Use it however you want — fork it, teach it, sell it, ship it. Attribution appreciated,
not required.

Maintained by [Rohit Ghumare](https://github.com/rohitg00) and the community.

<sub>
  <a href="https://x.com/ghumare64">@ghumare64</a> &nbsp;·&nbsp;
  <a href="https://aiengineeringfromscratch.com">aiengineeringfrom
