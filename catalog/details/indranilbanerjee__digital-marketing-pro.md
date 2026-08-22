# indranilbanerjee/digital-marketing-pro

An open-source AI marketing operating system for strategy, SEO, AEO/GEO, paid media, content, CRM, and analytics - grounded in brand context, human approval, and verifiable outputs.

## installation

/plugin marketplace add indranilbanerjee/neels-plugins
/plugin install digital-marketing-pro@neels-plugins
```

> If this saves you time, [give it a star ⭐](https://github.com/indranilbanerjee/digital-marketing-pro/stargazers) — it's the single thing that helps other marketers find it.

---

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
