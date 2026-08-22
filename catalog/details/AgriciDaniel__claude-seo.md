# AgriciDaniel/claude-seo

Universal SEO skill for Claude Code. 25 sub-skills + 18 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, semantic clustering, e-commerce SEO, inter

## features

- **AI-search first.** Aligned with [Google's AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). Question-based citability scoring, primary-source evidence on llms.txt, IPTC `TrainedAlgorithmicMedia` for AI-generated product images, agent-friendly page checks per [web.dev](https://web.dev/).
- **Parallel execution.** Full site audits spawn up to 15 specialist agents simultaneously. Site-level audits complete in minutes rather than hours.
- **Falsifiable, not promotional.** Every recommendation carries the first-principle observation it rests on, its dependency relationships, an explicit "how would we know this failed?" check, and a leading indicator. See [Methodology](#methodology).

## installation

> ℹ️ **Which version are you installing?**
>
> - **Public open-source (default).** The commands below install from [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) — MIT, public releases, no membership required.
> - **AI Marketing Hub Pro member?** Install the community version with early access instead: swap `AgriciDaniel/claude-seo` for `AI-Marketing-Hub/claude-seo` and the plugin slug `claude-seo@agricidaniel-claude-seo` for `claude-seo@ai-marketing-hub-claude-seo`. Requires `gh auth login` (or PAT) with access to the `AI-Marketing-Hub` org. If `/plugin marketplace add` 404s, DM in the [Skool community](https://www.skool.com/ai-marketing-hub-pro) to get added.

## tools

![Claude SEO sub-skill ecosystem: 25 modules grouped into 8 categories (audit, content, schema, technical, AI search, local + maps, commerce + intl, extensions) around the central orchestrator](assets/sub-skills.svg)

32 user-invocable `/seo` commands across the orchestrator, its sub-skills, and 8 MCP extensions. Full reference in [docs/COMMANDS.md](docs/COMMANDS.md).

| Command | Description |
|---------|-------------|
| `/seo setup` | Create or refresh the isolated Python runtime and Chromium |
| `/seo doctor` | Check runtime readiness without changing the system |
| `/seo audit <url>` | Full website audit with parallel sub-agent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo technical <url>` | Technical SEO audit across 9 categories |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo content-brief <topic>` | Detailed content brief: target keywords, outline, internal links |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo sitemap <url \| generate>` | Analyze or generate XML sitemaps |
| `/seo images <url>` | Image optimization analysis |
| `/seo plan <type>` | Strategic SEO planning (saas, local, ecommerce, publisher, agency) |
| `/seo programmatic <url>` | Programmatic SEO analysis and planning |
| `/seo competitor-pages <url>` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang <url>` | Hreflang / i18n SEO audit and generation |
| `/seo google [command]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4, PDF reports) |
| `/seo backlinks <url>` | Backlink profile analysis (Moz, Bing, Common Crawl) |
| `/seo cluster <keyword>` | SERP-based semantic clustering |
| `/seo sxo <url>` | Search Experience Optimization (page-type, user stories, personas) |
| `/seo drift baseline \| compare \| history <url>` | SEO drift monitoring with SQLite snapshots |
| `/seo ecommerce <url>` | E-commerce SEO and marketplace intelligence |
| `/seo flow [stage]` | FLOW framework prompts (CC BY 4.0, evidence-led) |
| `/seo firecrawl [command] <url>` | Full-site crawling (extension) |
| `/seo dataforseo [command]` | Live SEO data (extension) |
| `/seo image-gen [use-case]` | AI image generation for SEO assets (extension) |
| `/seo ahrefs [command] <url>` | Backlinks, organic keywords, and content data via the official Ahrefs MCP (extension) |
| `/seo seranking [command]` | AI Share-of-Voice across ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode (extension) |
| `/seo profound [command]` | LLM citation tracking with time-series data (extension) |
| `/seo bing [command] <url>` | Bing Webmaster Tools + IndexNow URL submission (extension) |
| `/seo unlighthouse <url>` | Multi-page Lighthouse runner, runs locally (extension) |

## limitations

Two real boundaries worth being upfront about.

**Heavy client-side hydration timing.** Phase A's headless renderer handles most SPAs out of the box (`--render auto` detects empty `<div id="root">` shells and switches to Playwright). Edge cases that still produce noisy findings: pages with hydration tied to scroll position past the fold, pages that fetch critical content after user interaction (modal opens, tab clicks), pages with race-condition-prone third-party widget mounts. For these, manually triggering the `seo-visual` subagent and comparing its Playwright snapshot to the raw-HTML subagents' findings is the recommended workflow.

**Local-only without enrichment.** The free tier makes no third-party API calls by default (audits still fetch the target URLs you point them at). Adding Google API credentials (Tier 0 through 3) unlocks real field data and live indexation status; without them, Core Web Vitals are lab estimates only and indexation is inferred from page-level signals. Adding MCP extensions (Ahrefs, DataForSEO, SE Ranking, Profound) similarly unlocks competitive and AI-citation data but requires their respective accounts.

## requirements

- Python 3.10+
- Claude Code CLI
- Optional: Playwright Chromium — install.sh offers to install it (you can skip the prompt); needed only for SPA rendering and screenshots
- Optional: Google API credentials for enriched CWV / GSC / GA4 data (see `/seo google setup`)
