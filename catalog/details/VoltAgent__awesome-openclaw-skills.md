# VoltAgent/awesome-openclaw-skills

The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞

## installation

#### OpenClaw CLI

```bash
openclaw skills install <skill-slug>
```

#### ClawHub CLI

Or with the ClawHub CLI, for registry-managed skill folders outside a full OpenClaw workspace:

```bash
npx clawhub install <skill-slug>
```

#### Manual Installation

Copy the skill folder to one of these locations:

| Location | Path |
|----------|------|
| Global | `~/.openclaw/skills/` |
| Workspace | `<project>/skills/` |

Priority: Workspace > Local > Bundled

#### Alternative

You can also paste the skill's GitHub repository link directly into your assistant's chat and ask it to use it. The assistant will handle the setup automatically in the background.

## features

OpenClaw's public registry (ClawHub) hosts thousands of community-built skills. This awesome list curates the best of them. Here's what we filtered out:

| Filter | Excluded |
|--------|----------|
| Possibly spam — bulk accounts, bot accounts, test/junk | 4,065 |
| Duplicate / Similar name | 1,040 |
| Low-quality or non-English descriptions | 851 |
| Crypto / Blockchain / Finance / Trade | 886 |
| Malicious — identified by security audits published by researchers (excluding VirusTotal) | 373 |
| **Total not taken from OpenClaw's official skill registry** | **7,215** |


#### Want to add a skill?

This list only includes skills that are **already published** on [ClawHub](https://clawhub.ai), OpenClaw's public skills registry. We do not accept links to personal repos, gists, or any other external source. If your skill isn't on ClawHub yet, publish it there first.

Include the ClawHub link for your skill (e.g. `https://clawhub.ai/steipete/slack`) in your PR description — the `clawskills.sh` listings are managed by us separately. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## tools

### 🕸️ Web Crawling & Data Infrastructure

AI agents are only as good as the web data they can reach. Crawling at scale means dealing with JavaScript-heavy pages, rotating proxies, and anti-bot systems — you can build all that yourself, or use an API that handles it and hands your agent clean, ready-to-use data.

<a href="https://s.getdesign.md/crawl-og">
<img src="https://cdn.voltagent.dev/awesome-repo/crawlbase/crawlbase-sponsor-banner-560x120.png" alt="Crawlbase" width="560" /><br/>
Crawlbase is web data infrastructure trusted by 70,000+ developers: one API to crawl any URL at scale, with JS rendering, proxy rotation and anti-bot handling. Its MCP server gives agents live web access: crawl, crawl_markdown, crawl_screenshot.
</a>


### 🔍 Search & Web Data

OpenClaw agents often need fresh, real-world data — search results, product listings, videos, and more. You can scrape and parse it yourself, or use a search API that returns clean, structured data in real time without managing proxies, CAPTCHAs, or HTML parsing.

<a href="https://serpapi.com/search-engine-apis?utm_source=awesomeopenclawskills_github">
<img src="https://cdn.voltagent.dev/awesome-repo/serpapi.png" alt="SerpApi"  /><br/>
Give OpenClaw agents access to real-time Google Search, YouTube, Amazon Product, and web search data through a single API.
</a>

## configuration

As you add more skills, custom code, and connected services, your OpenClaw setup accumulates secrets, file access, and tool permissions that are easy to lose track of. You can review these by hand, or run a continuous audit that surfaces misconfigurations and over-broad permissions before they become a problem.

<a href="https://trent.ai/openclaw/?utm_source=github&utm_medium=referral&utm_campaign=volt-agent">
<img src="https://cdn.voltagent.dev/awesome-repo/trentclaw-banner.png" alt="trentclaw"  /><br/>
trentclaw: audits your OpenClaw config, installed skills and custom code, then returns fixes as diffs. Install with: openclaw skills install trentclaw
</a>

</br>
</br>

<div align="center">

<table>
<tr>
<td align="center" width="100%">

<h3>🦞 You can feature your OpenClaw ecosystem tool in the section above.</h3>

<p></p>

<sub>The #1 most visited community resource after the official OpenClaw resource</sub>


<a href="https://sponsors.voltagent.dev/#awesome-openclaw-skills"><img src="https://img.shields.io/badge/📩_Become_a_Sponsor-Contact_Us-blue?style=for-the-badge&logoColor=white" alt="Become a Sponsor" /></a>

</td>
</tr>
</table>

</div>



## Security Notice

Skills in this list are **curated, not audited**. They may be updated, modified, or replaced by their original maintainers at any time after being added here.

Before installing or using any Agent Skill, review potential security risks and validate the source yourself. OpenClaw has a **VirusTotal partnership** that provides security scanning for skills, visit a skill's page on ClawHub and check the VirusTotal report to see if it's flagged as risky.

**Recommended tools:**

- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)
  
> Agent skills can include prompt injections, tool poisoning, hidden malware payloads, or unsafe data handling patterns. Always review the source code before installing and use skills at your own discretion.

 For a broader overview of the ClawHub ecosystem, see Trent AI's **[ClawHub by the Numbers](https://trent.ai/blog/clawhub-by-the-numbers/)**.


If you believe a skill in this list should be flagged or has a security concern, please [open an issue](https://github.com/VoltAgent/awesome-clawdbot-skills/issues) so we can review it.


## Table of Contents

| | | |
|---|---|---|
| [Git & GitHub](#git--github) (167) | [Marketing & Sales](#marketing--sales) (107) | [Communication](#communication) (146) |
| [Coding Agents & IDEs](#coding-agents--ides) (1184) | [Productivity & Tasks](#productivity--tasks) (207) | [Speech & Transcription](#speech--transcription) (46) |
| [Browser & Automation](#browser--automation) (323) | [AI & LLMs](#ai--llms) (176) | [Smart Home & IoT](#smart-home--iot) (41) |
| [Web & Frontend Development](#web--frontend-development) (920) | [Data & Analytics](#data--analytics) (28) | [Shopping & E-commerce](#shopping--e-commerce) (51) |
| [DevOps & Cloud](#devops--cloud) (393) | [Calendar & Scheduling](#calendar--scheduling) (66) | |
| [Image & Video Generation](#image--video-generation) (170) | [Media & Streaming](#media--streaming) (86) | [PDF & Documents](#pdf--documents) (105) |
| [Apple Apps & Services](#apple-apps--services) (44) | [Notes & PKM](#notes--pkm) (69) | [Self-Hosted & Automation](#self-hosted--automation) (33) |
| [Search & Research](#search--research) (342) | [iOS & macOS Development](#ios--macos-development) (29) | [Security & Passwords](#security--passwords) (54) |
| [Clawdbot Tools](#clawdbot-tools) (37) | [Transportation](#transportation) (111) | [Moltbook](#moltbook) (29) |
| [CLI Utilities](#cli-utilities) (180) | [Personal Development](#personal-development) (53) | [Gaming](#gaming) (35) |
| [Health & Fitness](#health--fitness) (87) | | |



<br/>

You ship products with AI, but every launch still dies quietly because nobody posts about it. [EveryFeed](https://everyfeed.ai/) plugs your AI assistant into a social workspace 
