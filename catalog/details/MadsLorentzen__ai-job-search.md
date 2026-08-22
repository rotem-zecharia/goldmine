# MadsLorentzen/ai-job-search

The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.

## requirements

- [Claude Code](https://claude.com/claude-code) (CLI). Using a different agent tool (Codex, Antigravity, Gemini CLI)? Start at [`AGENTS.md`](AGENTS.md) - the portal search skills work there out of the box, and [community forks](https://github.com/MadsLorentzen/ai-job-search/discussions/78) adapt the full workflow.
- Python 3.10+
- [Bun](https://bun.sh) (for job search CLI tools)
- LaTeX distribution with `lualatex` and `xelatex`: [TeX Live](https://tug.org/texlive/), [MacTeX](https://tug.org/mactex/), [TinyTeX](https://yihui.org/tinytex/), or [MiKTeX](https://miktex.org/). The CV compiles with `lualatex` (pdflatex often fails on modern MiKTeX installs with `fontawesome5` font-expansion errors); the cover letter compiles with `xelatex` because `cover.cls` requires `fontspec`. If using a minimal TeX install such as TinyTeX or BasicTeX, install the extra packages listed in [SETUP.md](SETUP.md#minimal-tex-install-tinytexbasictex).
- Optional: `pdftotext` from [poppler](https://poppler.freedesktop.org/) (macOS: `brew install poppler`, Debian/Ubuntu: `apt install poppler-utils`, Windows: `choco install poppler`) — used by `/apply`'s ATS parseability check on the compiled CV. If missing, the check degrades gracefully to a visual keyword review.

## installation

> 🎥 **Prefer to see it in action first?** [The Next New Thing did a hands-on walkthrough](https://www.youtube.com/watch?v=HoVxjMNFYv4) of how the workflow is actually used, from setup to a finished application (recorded August 2026 - commands may have evolved since).

### 1. Fork and clone

```bash
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
```

> [!IMPORTANT]
> **A fork of this repo is always public** — GitHub does not allow private forks of
> public repositories — and `/setup` (step 3 below) writes your personal data (name,
> contact details, employment history, salary expectations) into **tracked** files.
> If this copy is for your own job search rather than for contributing changes back,
> use a **private repository** with this repo as `upstream` instead — the two-minute
> recipe is in [SETUP.md section 8](SETUP.md#8-pulling-upstream-updates-into-your-fork),
> and every update workflow works identically. Fork only to contribute.

### 2. Install job search tools

PowerShell:

```powershell
$tools = @("jobbank-search", "jobdanmark-search", "jobindex-search", "jobnet-search", "linkedin-search", "freehire-search")
foreach ($tool in $tools) {
  Push-Location ".agents/skills/$tool/cli"
  bun install
  Pop-Location
}
```

Bash / zsh / Git Bash:

```bash
for tool in jobbank-search jobdanmark-search jobindex-search jobnet-search linkedin-search freehire-search; do
  (cd .agents/skills/$tool/cli && bun install)
done
```

For `linkedin-search` and `freehire-search` the install is optional: both have zero runtime dependencies and run with plain `bun`; `bun install` only pulls TypeScript dev types.

### 3. Set up your profile

```bash
claude
# Then inside Claude Code:
/setup
```

`/setup` offers three paths: read your `documents/` folder if you have one populated (CV PDF, LinkedIn export, diplomas, reference letters, past applications), import a single CV pasted in chat, or walk through an interview. It auto-detects what you have and asks. Documents-folder mode is idempotent and safe to re-run as you add more material; see `documents/README.md` for the layout.

### 4. Search for jobs

```bash
/scrape
```

This searches multiple job portals for positions matching your profile, deduplicates results, and presents them sorted by fit. Pick a match to run `/apply` on it directly — or, when a scrape returns more jobs than you want to eyeball, run `/rank` to batch-score them all against the fit framework and get a ranked shortlist first.

### 5. Apply to a job

```bash
/apply https://jobindex.dk/job/1234567
```

If the URL can't be fetched (some job portals block automated access), you can paste the job description directly instead:

```bash
/apply <paste the full job description here>
```

This runs the full workflow: evaluate fit, draft CV + cover letter, review with a second agent, revise, and present the final output.

Postings are treated as untrusted input (the workflow follows no instructions embedded in them and fetches no links from their body), but agentic defenses are instruction-level, not a sandbox - on an unfamiliar job board, skim what was fetched and written before you hit send. Details in [SECURITY.md](SECURITY.md).

## tools

`/setup`, `/scrape`, and `/apply` form the core workflow. Ten more commands extend it once your profile is in place:

- **`/interview`** preps you for a scheduled interview on a tracked application. It builds a stage-specific prep pack from the application's archive (the exact posting, the CV and cover letter the interviewer actually read, feedback recorded from earlier rounds), researches the company and interviewers with a verify-before-use rule, maps likely questions to your STAR examples, and offers a mock interview following the roleplay protocol in `07-interview-prep.md`. Gaps get honest bridge answers, never invented experience.
- **`/outcome`** records what happened to an application - interview stages, offers, rejections, silence. It archives the submitted CV, cover letter, and posting text into `documents/applications/<company>_<role>/`, keeps `outcome.md` in the format `/setup` Path A parses, and updates the tracker. It also owns the stretch before there is an outcome to record: `/outcome followup` surfaces open applications that have gone quiet (default 10 days), drafts a short channel-appropriate follow-up in your writing style using only claims from the materials you already submitted (drafts only, never sends; at most twice per application), and offers a thank-you note in the same turn an interview stage is recorded. Once a few applications resolve, it points you back to `/setup` to calibrate the fit framework from what actually got interviews.
- **`/notion-sync`** publishes a one-way, read-only view of the pipeline into a Notion database via the official Notion MCP server (OAuth, no API keys) - one row per ranked job plus every tracked application, with a write-once briefing page per row. The repo files stay the system of record: nothing syncs back, and documents sync as filenames only. Complements `/html-report`: that is the deep offline dashboard you regenerate at your desk; this is the glanceable live view from anywhere Notion runs (desktop, web, phone).
- **`/gmail-sync`** reads your Gmail (via the Gmail connector) for status signals on your open applications - interview invites, assessment links, offers, rejections - and proposes them as a batch for you to approve before anything is written to the tracker or `outcome.md`, citing the source email on every proposed change. Offers stop short of proposing `hired`/`offer_declined` since that's your call; conflicting or unmatched signals get flagged for a manual `/outcome` pass instead of guessed.
- **`/rank`** bridges `/scrape` and `/apply`: it batch-scores all newly scraped postings against the fit framework (parallel agents fetch each posting and score the five evaluation dimensions) and returns a ranked shortlist with honest per-job strengths and gaps. Deal-breakers veto, deadlines get urgency flags, dead postings get marked expired. Pick a number and it hands off to the full `/apply` workflow.
- **`/expand`** enriches your profile by scanning public sources you've already linked in it (GitHub repos, portfolio site, Kaggle, Google Scholar) and looking up syllabi for named courses and certifications. Discovered competencies are added to your profile with a source tag. Useful right after `/setup` to surface skills that documents alone don't make explicit.
- **`/upskill`** analyzes the gap between your profile, your tracked job postings, and your ranked-but-untracked postings (`/rank`'s recorded gaps in `seen_jobs.json`) — or a single posting via `/upskill <URL>`. Produces a prioritized heatmap of skill gaps and a learning plan with web-searched study resources and time estimates. Useful for career planning between applications.
- **`/html-report`** generates a self-contained HTML dashboard from `job_search_tracker.csv` and the application archives — stat cards, status/sector/channel/funnel charts (inline SVG, no external dependencies), and a filterable applications table. Opens directly in a browser, fully offline. Re-run it any time after `/apply` or `/outcom
