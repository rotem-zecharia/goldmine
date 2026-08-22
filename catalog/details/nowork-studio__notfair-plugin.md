# nowork-studio/notfair-plugin

Open-source SEO, GEO, and marketing skills for AI agents.

## installation

### Claude Code

Install the NotFair plugin from its marketplace:

```text
/plugin marketplace add nowork-studio/notfair-plugin
/plugin install notfair@nowork-studio
```

Then ask for the workflow you need:

```text
/notfair:seo-analysis
/notfair:geo-optimizer
/notfair:google-ads-audit
/notfair:meta-ads-creative
/notfair:paid-ads-x
/notfair:google-analytics
/notfair:search-console
```

You can also use plain language:

> Audit my site and tell me why organic traffic fell.

> Find pages that could earn citations in AI answers.

> Review last month's ad spend and show me the safest opportunities to improve ROAS.

### Codex, Hermes, and other agents

Install the universal NotFair plugin directly through Codex:

```bash
codex plugin marketplace add nowork-studio/notfair-plugin --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

Codex installs the skills, registers one NotFair MCP connection, and opens its OAuth flow. If you prefer a workspace-local checkout, clone the repository and open it as a workspace; [`AGENTS.md`](AGENTS.md) maps marketing requests to the right skill.

```bash
git clone https://github.com/nowork-studio/notfair-plugin.git
cd notfair-plugin
```

If the `nowork-studio` marketplace is already configured, refresh it instead:

```bash
codex plugin marketplace upgrade nowork-studio --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

For host-specific setup, give your agent [`INSTALL_FOR_AGENTS.md`](INSTALL_FOR_AGENTS.md), or paste:

```text
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/nowork-studio/notfair-plugin/main/INSTALL_FOR_AGENTS.md
```

## features

Marketing work gets unreliable when every request goes through the same vague prompt. The NotFair Plugin splits the work into focused, testable procedures.

- **Specialized:** each skill has a defined job, required inputs, decision rules, and output format.
- **Evidence-led:** live-data workflows use Search Console, Google Analytics, Google Ads, Meta Ads, X Ads, or LinkedIn Ads instead of guessing from generic best practices.
- **Safe by design:** read-only review comes before mutation, paid-media changes stay explicit, and unsupported capabilities are never implied.
- **Host-agnostic:** the canonical skills are plain files, not logic trapped inside one agent runtime.
- **Forkable:** everything is MIT licensed, so teams can review and adapt the workflows to their own standards.

## Skill catalog

### SEO and GEO

| Skill | What it does |
|---|---|
| [`seo-analysis`](seo/seo-analysis/) | Audits a full site with Search Console and crawl data, then prioritizes the highest-impact fixes. |
| [`seo-page`](seo/seo-page/) | Performs a deep audit of one URL for intent, content, structure, and on-page SEO. |
| [`content-writer`](seo/content-writer/) | Writes or improves search-led articles, landing pages, and service pages. |
| [`content-planner`](seo/content-planner/) | Turns Search Console opportunities into a prioritized, dated editorial calendar. |
| [`keyword-research`](seo/keyword-research/) | Builds a keyword universe, classifies intent, and organizes topic clusters. |
| [`meta-tags-optimizer`](seo/meta-tags-optimizer/) | Improves titles, meta descriptions, Open Graph tags, and SERP click-through potential. |
| [`schema-markup-generator`](seo/schema-markup-generator/) | Creates and validates JSON-LD structured data. |
| [`broken-link-checker`](seo/broken-link-checker/) | Finds broken internal and external links and reports site-health issues. |
| [`geo-optimizer`](seo/geo-optimizer/) | Audits and rewrites content for citation in AI search and answer engines. |
| [`local-seo`](seo/local-seo/) | Reviews Google Business Profile, local pages, NAP consistency, reviews, and local schema. |
| [`hreflang-international`](seo/hreflang-international/) | Diagnoses hreflang, canonical, language, and regional targeting problems. |
| [`sitemap-audit`](seo/sitemap-audit/) | Checks XML sitemap structure, freshness, coverage, and URL validity. |
| [`image-seo`](seo/image-seo/) | Reviews alt text, formats, compression, responsive images, CLS, and image discovery. |
| [`ecommerce-seo`](seo/ecommerce-seo/) | Audits product pages, category pages, variants, faceted navigation, and product schema. |
| [`programmatic-seo`](seo/programmatic-seo/) | Plans useful templated pages at scale with demand, uniqueness, and indexation guardrails. |
| [`competitor-pages`](seo/competitor-pages/) | Compares ranking pages and produces a practical SERP brief. |
| [`sxo`](seo/sxo/) | Connects search visibility and SERP CTR to the post-click conversion experience. |
| [`seo-drift`](seo/seo-drift/) | Creates a baseline and detects ranking, metadata, canonical, and indexation regressions. |
| [`backlink-audit`](seo/backlink-audit/) | Reviews referring domains, anchor text, link risk, and internal-link opportunities. |
| [`setup-cms`](seo/setup-cms/) | Connects WordPress, Strapi, Contentful, or Ghost. |

### Paid media

| Skill | What it does |
|---|---|
| [`paid-ads`](paid-ads/paid-ads/) | Routes broad paid-media questions to the right channel and workflow. |
| [`paid-ads-setup`](paid-ads/paid-ads-setup/) | Connects accounts and captures business, economics, tracking, and budget context. |
| [`paid-ads-launch`](paid-ads/paid-ads-launch/) | Produces a reviewable campaign or multi-channel experiment plan before spend begins. |
| [`paid-ads-review`](paid-ads/paid-ads-review/) | Creates comparable weekly or monthly scorecards and checks tracking health. |
| [`paid-ads-optimize`](paid-ads/paid-ads-optimize/) | Finds waste and pacing problems, then proposes narrow, reversible cha
