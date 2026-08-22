# indranilbanerjee/digital-marketing-pro

An open-source AI marketing operating system for strategy, SEO, AEO/GEO, paid media, content, CRM, and analytics - grounded in brand context, human approval, and verifiable outputs.

## installation

/plugin marketplace add indranilbanerjee/neels-plugins
/plugin install digital-marketing-pro@neels-plugins
```

> If this saves you time, [give it a star ⭐](https://github.com/indranilbanerjee/digital-marketing-pro/stargazers) — it's the single thing that helps other marketers find it.

---

## Who this is for

| If you're a... | Run this | What you get |
|---|---|---|
| 🏢 **Marketing agency** managing 50–200 brands | `/digital-marketing-pro:engagement` per brand, then `/digital-marketing-pro:cowork-setup` for team Drive persistence | Same 12-Part Strategy Flow audited across every brand. New-hire onboarding goes from 6 weeks to 6 hours. Per-brand AI cost rollup via `:agency-dashboard`. |
| 👔 **In-house marketing team** (B2B SaaS · e-commerce · fintech · healthtech) | `/digital-marketing-pro:engagement` once to anchor strategy, then `:content-engine` + `:campaign-plan` for ongoing work | A single canonical strategy doc, monthly stakeholder reports via `:performance-report`, content + campaigns that tie back to the strategy instead of drifting. |
| 🚀 **Marketing automation builder** (n8n · Zapier · Make · Pipedream · custom) | `/digital-marketing-pro:doctor` to see what's wired, `:execute-action` to fire real API calls | 8 verified HTTP connectors executing end-to-end (Slack · HubSpot · Klaviyo · SendGrid · Brevo · Customer.io · Mailchimp · Ahrefs); 25 OAuth connectors via MCP manifest. Stdlib only, no third-party deps. |
| 💼 **Solo consultant** or freelance marketer | `/digital-marketing-pro:engagement` per client | 50–60 canonical files per client engagement in ~60 minutes for $15–40 of API spend. Same depth on every project. Installs on Codex / Cursor / Copilot CLI / Antigravity if you don't live in Claude. |
| 📈 **Growth team** / product marketer | `:funnel-architect` → `:analytics-insights` → `:attribution-model` → `:churn-risk` → `:cohort-analysis` | Journey design + measurement + retention + churn — all aligned to the strategy document, not isolated outputs. MMM + incrementality testing baked in. |
| 🛡 **Compliance-led marketer** (EU · UK · India · Brazil · California) | `/digital-marketing-pro:check` before publishing anything | C2PA content provenance, EU AI Act Article 50 disclosure, GDPR + CCPA + DPDPA + LGPD across 16 jurisdictions, deepfake disclosure clauses on every AI creative brief. |

---

## How does this compare?

| | **Digital Marketing Pro** | Anthropic Marketing (official) | Composio Marketing | claude-seo (community) |
|---|---|---|---|---|
| Skills count | **163** | ~7 | ~12 | 25 SEO-only sub-skills |
| Specialist agents | **24** | 0 | 0 | 18 SEO-only |
| Has a methodology | **Yes — 12-Part Strategy Flow (61 explicit steps)** | No | No | No |
| Multi-brand / agency support | **Yes — per-brand state, brand-switch, agency-dashboard** | No | No | No |
| EU AI Act Article 50 ready | **Yes — C2PA + deepfake disclosure + 16 jurisdictions** | No | No | Partial |
| Cowork team persistence | **Yes — Drive MCP routing (v3.12.0)** | Cowork-native | Composio cloud | n/a |
| Real API execution | **Yes — 8 connectors live, 25 manifest-ready** | OAuth via plugin | OAuth via Composio | Optional DataForSEO / Firecrawl |
| 6-platform AEO/GEO audit | **Yes — incl. Google AI Mode (May 2026)** | No | No | Yes (AEO + GEO) |
| Cross-platform install | **9 native — CC + Cowork + Codex + Cursor + Copilot CLI + Antigravity + Hermes + OpenClaw + Grok** | Cowork only | Cowork + Codex | CC + Codex |
| Tests | **209 stdlib unittest** | unknown | unknown | 271 incl. SSRF/DNS coverage |
| License | **MIT — no telemetry, no seats** | Proprietary | Proprietary | MIT |
| Maintainer responsiveness | Direct via [@askneelnow](https://linkedin.com/in/askneelnow) | Anthropic queue | Composio queue | Community |

---

## Get started in 5 minutes (non-developer path)

**Are you a marketer, agency owner, or content lead who doesn't live in a terminal?** Here's the fastest path:

1. **Open [Anthropic Cowork](https://claude.com/cowork)** in your b

## features

Most AI marketing tools generate isolated outputs — a campaign brief here, an email there. No canonical sequence, no shared state, no enforced structure. Result: inconsistent depth, missed dependencies, outputs that don't compound.

**DM Pro runs every brand through the same 12 parts, producing the same files in the same order, with explicit dependency rules between them.** That's the whole product. Everything else — the 163 skills, 24 agents, May–June 2026 compliance updates, Cowork persistence — exists to make that 12-Part Flow ship cleanly across real marketing operations.

| What this gives you that ad-hoc prompts don't | Why it matters |
|---|---|
| **Canonical 12-Part Strategy Flow** producing the Four Core Documents (61 explicit steps) | Every engagement looks the same, so handoffs work and quality is auditable |
| **Two-Views Model** (v1 unbiased + v2 client-validated) | You never lose the original market view when the client pushes back |
| **Decision Matrix** — maps validation responses to re-runs | Stops over-running (wasted hours) and under-running (broken strategy) |
| **Living Project Instruction File** — single source of truth per engagement | All skills read it first; corrections propagate automatically |
| **EU AI Act Article 50 readiness** built in | C2PA provenance signing, deepfake disclosure, final Article 50 Guidelines + Code of Practice (10 June 2026) in compliance |
| **6-platform AEO/GEO audit** (incl. Google AI Mode) | The first marketing plugin to treat AI Mode as a distinct surface from AI Overviews |

---

## What you get in 60 minutes

Run `/digital-marketing-pro:engagement` and the plugin produces a full brand-strategy engagement in roughly 60 minutes on Opus 4.8/Opus 5-class models — **~50–60 canonical files** organized by part:

- **Part 1** — Stone-vs-Opinion intake (what the client knows for certain vs what they believe)
- **Part 2** — External market research (unbiased, no client docs)
- **Part 3** — Four Core Documents — 61 explicit steps across Business & SBU Analysis, Segmentation Framework, Brand Positioning & Communications, DMFlow
- **Part 4** — Competitive + Customer + Market analysis (4 unbiased docs)
- **Part 5** — Client Validation Document — the one true stop
- **Part 6** — Selective v2 re-runs per Decision Matrix
- **Part 7** — Preparation documents (campaign architecture, KPI tree, content pillars, approval chains)
- **Part 8** — **Growth Plan + 12-month Yearly Planner** (the flagship deliverable)
- **Part 9** — Channel-strategy fan-out (up to 17 channel docs in 7 families)
- **Part 10** — Execution artefacts (ad copy, post copy, headlines, CTAs)
- **Part 11** — AI creative briefs (with Nano Banana Pro / Veo 3.1 / Gemini Omni model guidance and C2PA + deepfake-disclosure clauses)
- **Part 12** — Continuous improvement loop

Cost: roughly **$15–40 in Claude API spend** for a full 12-part engagement using Opus 4.8 or Opus 5 (same $5/$25 per-MTok pricing). The plugin itself is MIT-licensed and free.

---

## configuration

# 3. Try: "Run a competitor analysis on stripe.com"
# Your agent picks /digital-marketing-pro:competitor-analysis automatically.
```

**Why we don't ship per-platform manifests for these:** the Agent Skills standard says agents discover by walking a directory tree for `SKILL.md` files — no manifest required. Shipping 35 extra wrapper manifests would create maintenance overhead with zero added value.

If you run into a platform-specific install snag, file a [GitHub issue](https://github.com/indranilbanerjee/digital-marketing-pro/issues) — we'll add platform-specific docs as users report patterns.

---

## The 12-Part Engagement Methodology

| Part | Name | Output |
|------|------|--------|
| 1 | Client Inputs | Stone vs Opinion intake (what client knows for certain vs what they believe) |
| 2 | External Research | Unbiased market research (no client docs used) |
| 3 | **Four Core Documents** | 61 explicit steps — Business & SBU (18), Segmentation (15), Brand Positioning (19), DMFlow (9) |
| 4 | Competitive + Customer + Market | 4 unbiased analysis documents (4.1–4.4) |
| 5 | **Client Validation Document** | The one true stop — client accepts/rejects/edits each finding |
| 6 | Selective v2 Re-runs | Subset of Part 3 + Part 4 docs re-run per the Decision Matrix |
| 7 | Preparation Documents | Internal operating layer (campaign architecture, KPI tree, content pillars, asset inventory, approval chains) |
| 8 | **Growth Plan + Yearly Planner** | The flagship 11-section client-facing strategy + 12-month operational calendar |
| 9 | Channel Strategy Fan-out | Up to 17 channel docs grouped into 7 families |
| 10 | Execution Artefacts | Ad copy, post copy, headlines, CTAs |
| 11 | AI Creative Instructions | Visual asset briefs with C2PA + EU Article 50 clauses |
| 12 | **Continuous Improvement Loop** | Quarterly briefs feeding signals back into product/offering decisions |

**Key architectural concepts:**
- **Two-Views Model** — Every engagement carries v1 (unbiased market view) and v2 (client-validated view) after Part 5. Operating decisions reference v2; ideation references both. v1 is never deleted.
- **Stone vs Opinion** — Every fact captured at intake is tagged with confidence. Stone = client knows for certain. Opinion = client believes (becomes a research question, not ground truth).
- **Decision Matrix** — Maps client validation responses to which v1 documents need v2 re-runs. Prevents over- and under-re-running.
- **Update-Back Rule** — Live operations surface corrections → source documents get versioned (v2.1, v2.2 …) → Living Project Instruction File propagates the change to all downstream skills.
- **Living Project Instruction File** — Single source of truth per engagement. All skills read it first.

15+ strategic-framework reference documents in `skills/context-engine/` support the methodology (Five Digital Markets, Channel Families, In-Market vs Out-Market, Multi-Dimensional Decision Framework, Unit Economics, Actionable Persona Format, B2B Decision-Making Unit, Three-Scenario Forecasting, 30/60/90-Day Framework, Reporting Cadence, Fixed vs Variable Budget, Competitor 3-Question Output, India Market Context, and more).

---

## What's new

### v3.31.1 — all five open community issues verified and fixed (August 17, 2026)

Each open GitHub issue was reproduced against the current release; all five were real, and every fix shipped with its own guard. #10: the percent-claim regex only matched when a word character followed `%` — inverted behavior, now `%(?!\w)` with CLI-level tests. #11: the keyword tokenizer split non-ASCII letters and exact-token Jaccard scored German compounds at 0.00 — Unicode tokenizer + compound-aware similarity (English scoring provably unchanged). #13: `engagement-workflow` mandated Task dispatch its `allowed-tools` didn't declare — fixed plus a contract guard across all 163 skills. #12: `plugin.yaml` said "158 skills" — 163 now, with the Hermes description in the derived-count guard. #9: the `_readme` 

## tools

| Command | What it does |
|---|---|
| `/digital-marketing-pro:brand-setup` | Set up a new brand profile (voice, audience, competitors, compliance) |
| `/digital-marketing-pro:engagement` | Run the full 12-Part Strategy Flow |
| `/digital-marketing-pro:campaign-plan` | Generate a multi-channel campaign plan with budget, timeline, KPIs |
| `/digital-marketing-pro:seo-audit` | Comprehensive SEO audit — technical, on-page, content, E-E-A-T, AI visibility |
| `/digital-marketing-pro:content-engine` | Draft blog, ad copy, emails, social, landing pages, video scripts |
| `/digital-marketing-pro:performance-report` | Performance report with trends, anomaly detection, recommendations |
| `/digital-marketing-pro:competitor-analysis` | Multi-dimensional competitive analysis (content, SEO, ads, social, pricing) |
| `/digital-marketing-pro:email-sequence` | Complete email sequences (subject lines, copy, timing, segmentation) |
| `/digital-marketing-pro:check` | Pre-publish quality gate (hallucination + brand voice + structure + claims) |
| `/digital-marketing-pro:status` | Unified brand snapshot (profile, engagements, insights, compliance) |
| `/digital-marketing-pro:resume` | Resume an interrupted long workflow from the last checkpoint |
| `/digital-marketing-pro:output-folder` | Print + open the visible output folder for a brand |
| `/digital-marketing-pro:doctor` | Per-action readiness diagnostic (which campaign-audit / launch-campaign actions are live vs need connector setup) |
| `/digital-marketing-pro:execute-action` | Actually fire an action against its real API (stdlib `urllib`, no third-party deps). 8 verified connectors execute end-to-end; 25 OAuth-only connectors fall back to the MCP path with the manifest still returned. |
| `/digital-marketing-pro:cowork-setup` | (v3.12.0) One-shot Cowork team setup — wires DMP through a Drive MCP so brand state survives across Cowork sessions |
| `/digital-marketing-pro:keyword-cluster` | Pillar + spokes content cluster from seed keywords with SERP-overlap clustering and 4-gate quality scorecard |
| `/digital-marketing-pro:backlink-gap` | Competitor backlink gap audit with priority scoring (DR + overlap + traffic + topical) |
| `/digital-marketing-pro:seo-drift` | Snapshot-vs-snapshot drift with auto-classification (growth/decline/reshuffle/stable/new/lost) |

Plus **140 additional skills** addressable via `/digital-marketing-pro:<skill-name>` — `:competitor-monitor`, `:churn-risk`, `:autopilot-status`, `:agency-dashboard`, `:aeo-audit`, `:geo-monitor`, `:c2pa-metadata`, `:client-onboarding`, `:journey-design` … see `/digital-marketing-pro:help` after install for the full list, or browse `skills/` in the repo.

### 93 Python scripts (optional)
Plugin works fully without Python — all marketing knowledge, frameworks, agent capabilities, and skills work out of the box via the 169 reference knowledge files.

| Mode | Size | Adds |
|---|---|---|
| **Knowledge-only** (default) | 0 MB | All 163 skills + 24 agents + 169 reference files |
| **Lite** (`pip install nltk textstat`) | ~15 MB | Brand-voice scoring, content quality scoring, readability analysis |
| **Full** (`pip install -r scripts/requirements.txt`) | ~50 MB | Competitor scraping, QR generation, AI visibility API checking, GEO tracking, C2PA signing |

### 14 HTTP MCP connectors
Notion · Slack · Canva · Figma · HubSpot · Amplitude · Ahrefs · SimilarWeb · Klaviyo · Google Calendar · Gmail · Stripe · Asana · Webflow

These are an **opt-in catalog** — the shipped `.mcp.json` is empty (`{"mcpServers":{}}`), so nothing auto-connects; enable only the ones you need. All HTTP, all Cowork-compatible. For services without first-party HTTP MCPs (Google Sheets, Drive, Salesforce, etc.), see `.mcp.json.connectors-reference` for **Pipedream / Composio / Zapier / Make.com** aggregator paths.

For the extended stdio catalog (Google Ads, Meta Ads, GA4, GSC, Brevo, etc. via npx, Claude Code only — not Cowork-compatible; verify each npm package exists befor
