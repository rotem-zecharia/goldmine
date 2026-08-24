# santifer/career-ops

Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Cod

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
| **Human-in-the-Loop**    | AI evaluates and recommends, you decide and act. The system never submits an application -- you always have the final call <!-- hitl: absolute guarantee. Do not add "automatically", "by itself", "without your permission" or any other hedge when translating this row. -->               |
| **Pipeline Integrity**   | Automated merge, dedup, status normalization, health checks                                                                              |
| **Interview Suite**      | Time-blocked prep plans, practice sessions with feedback, post-interview debriefs ([`interview/`](modes/interview/README.md)), and a company red-flag detector ([`interview-redflag`](modes/interview-redflag.md)) |
| **Offer Stage**          | Contract reading companion -- clause walk plus a lawyer question list ([`offer-prep`](modes/offer-prep.md)) -- and a desired/advertised/actual salary-gap analyzer (`salary-gap.mjs`) |
| **Follow-ups & Replies** | Follow-up cadence calculator and seeded reminders (`followup-cadence.mjs`, `followup-seed.mjs`); employer reply classification into tracker updates ([`reply-watch`](modes/reply-watch.md)) |
| **Pattern Analysis**     | Rejection patterns and per-ATS-channel advance rates (`analyze-patterns.mjs`), lifetime funnel stats (`stats.mjs`), repost/ghost-job detection (`detect-reposts.mjs`) |
| **Plugin System**        | Opt-in integrations (Gma

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

# 2. Check setup
npm run doctor                     # Validates all prerequisites

## configuration

cp config/profile.example.yml config/profile.yml  # Edit with your details
cp templates/portals.example.yml portals.yml       # Customize companies

# 4. Add your CV
# Create cv.md in the project root with your CV in markdown

# 5. Open your AI CLI in this directory
claude   # or codex / opencode / qwen / agy / grok

# Then ask your CLI to adapt the system to you:
# "Change the archetypes to backend engineering roles"
# "Translate the modes to English"
# "Add these 5 companies to portals.yml"
# "Update my profile with this CV I'm pasting"

# 6. Start using
# Paste a job URL or JD text to trigger auto-pipeline

## tools

# In Codex, ask for the same mode in plain language, e.g.:
# "Run the career-ops scan mode"
# "Run the career-ops pipeline mode for data/pipeline.md"
# "Run the career-ops pdf mode for the latest evaluated role"
# "Run the career-ops tracker mode and summarize the current statuses"
```

</details>
