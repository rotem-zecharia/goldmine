# santifer/career-ops

Open-source AI job search: scan job portals, evaluate listings with a structured A-F rubric into a 1.0-5.0 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, 

## features

| Feature                  | Description                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Auto-Pipeline**        | Paste a URL, get a full evaluation + PDF + tracker entry                                                                                 |
| **A-H Evaluation**       | Role summary, CV match, level strategy, comp research, personalization, interview prep (STAR+R) -- plus a Block G posting-legitimacy check that flags scams and ghost jobs, and a Work-Auth signal that flags an explicit no-sponsorship JD as a hard blocker |
| **Interview Story Bank** | Accumulates STAR+Reflection stories across evaluations -- 5-10 master stories that answer any behavioral question                        |
| **Negotiation Scripts**  | Salary negotiation frameworks, geographic discount pushback, competing offer leverage                                                    |
| **ATS PDF Generation**   | Keyword-injected CVs with Space Grotesk + DM Sans design                                                                                 |
| **Cover Letter Generator** | Research-backed cover letters with keyword mirroring, four interactive angle prompts (why/problems/approach/tone), draft-in-chat approval gate, and A4 PDF via the same HTML + Playwright pipeline as CVs. Auto-drafts on every evaluation; complete and generate on demand via `/career-ops cover` |
| **Application Email Drafts** | Formal recruiter/referral/cold application emails from a report or pasted JD, with subject line, attachment checklist, source-backed fit points, and a profile-driven contact block. Draft-only -- career-ops never sends, submits, or clicks anything. |
| **Portal Scanner**       | 100+ companies pre-configured (Anthropic, OpenAI, ElevenLabs, Retool, n8n...) + custom queries across Ashby, Greenhouse, Lever, Wellfound |
| **Funded Company Discovery** | Review-first `company:funded` command surfaces recently funded companies and source diagnostics from structured public feeds without editing your data |
| **Batch Processing**     | Parallel evaluation with headless CLI workers (`claude -p` / `opencode run`)                                                             |
| **Dashboard TUI**        | Terminal UI to browse, filter, and sort your pipeline                                                                                    |
| **Human-in-the-Loop**    | AI evaluates and recommends, you decide and act. The system never submits an application -- you always have the final call               |
| **Pipeline Integrity**   | Automated merge, dedup, status normalization, health checks                                                                              |
| **Interview Suite**      | Time-blocked prep plans, practice sessions with feedback, post-interview debriefs ([`interview/`](modes/interview/README.md)), and a company red-flag detector ([`interview-redflag`](modes/interview-redflag.md)) |
| **Offer Stage**          | Contract reading companion -- clause walk plus a lawyer question list ([`offer-prep`](modes/offer-prep.md)) -- and a desired/advertised/actual salary-gap analyzer (`salary-gap.mjs`) |
| **Follow-ups & Replies** | Follow-up cadence calculator and seeded reminders (`followup-cadence.mjs`, `followup-seed.mjs`); employer reply classification into tracker updates ([`reply-watch`](modes/reply-watch.md)) |
| **Pattern Analysis**     | Rejection patterns and per-ATS-channel advance rates (`analyze-patterns.mjs`), lifetime funnel stats (`stats.mjs`), repost/ghost-job detection (`detect-reposts.mjs`) |
| **Plugin System**        | Opt-in integrations (Gmail, Notion, Apify + a community registry), disabled by default -- see [docs/PLUGINS.md](docs/PLUGINS.md)        |
| **Beyond the CV**        | Compa

## installation

**Fastest way — one command:**

```bash
npx @santifer/career-ops init
```

> 💡 `npx` ships with [Node.js](https://nodejs.org) — it runs the installer once,
> without installing anything globally. No Node yet? Install it first.
> (Already using a Claude Code / Gemini / Codex CLI? Then you already have it.)

This clones the latest release into `./career-ops` and installs dependencies. Then:

```bash
cd career-ops
claude   # or codex / qwen / opencode / agy / grok — open your AI CLI here
```

**On first launch, career-ops walks you through setup — your CV, profile and target roles — just by chatting. Nothing to edit by hand.**

<details>
<summary><b>Prefer to set it up manually? (git clone)</b></summary>

```bash
git clone https://github.com/santifer/career-ops.git
cd career-ops && npm install
npx playwright install chromium   # only needed for PDF generation

## configuration

cp config/profile.example.yml config/profile.yml  # Edit with your details
cp templates/portals.example.yml portals.yml       # Customize companies

## tools

/career-ops "Senior AI Engineer at Anthropic..."
/career-ops pipeline
/career-ops scan
/career-ops pdf
/career-ops tracker
```

The skill is defined using the open standard in `.agents/skills/career-ops/SKILL.md` and symlinked/referenced for each supported CLI (e.g. `.claude/`, `.cursor/`, `.qwen/`, `.antigravitycli/`, `.grok/`).
