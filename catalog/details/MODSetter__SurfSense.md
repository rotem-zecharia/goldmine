# MODSetter/SurfSense

Open-source NotebookLM alternative. Research the open web with live data(Reddit, YT, IG, TikTok, Indeed, Google Search, Maps etc) through one platform, API or MCP server. Join our Discord: https://dis

## features

Ask any capable agent "what is Reddit saying about this product since launch?" or "what do the reviews of these ten places actually complain about?" and it has nowhere trustworthy to look. Official platform APIs are rate-limited, priced for enterprises, or missing entirely; scraping plumbing is brittle; and driving a browser with an LLM burns minutes and tokens per page. SurfSense gives agents the primitives instead:

- **One typed surface for wherever the data lives.** Every connector is a REST endpoint returning structured JSON — posts, comments, transcripts, reviews, SERPs, pages. No rate-limit roulette, no HTML parsing, no browser loop.
- **An MCP server** that exposes every connector as a native tool (`surfsense_reddit_scrape`, `surfsense_google_search`, and more) to Claude, Cursor, or any agent framework.
- **An agent harness**, not just raw data: retries, structured output, and credit metering are built in, so agents go from a question to a cited brief without you building the plumbing.
- **Open source and self-hostable**, so your research stays on your own infrastructure.

## Live data connectors

| Connector | What your agents get | Learn more |
|---|---|---|
| **Reddit** | Posts, comments, and subreddit streams without the official API's rate limits | [Reddit Scraper API](https://www.surfsense.com/reddit) |
| **YouTube** | Videos, transcripts, and comment threads at scale | [YouTube Scraper API](https://www.surfsense.com/youtube) |
| **Instagram** | Public profiles, posts, and reels without the Graph API | [Instagram Scraper API](https://www.surfsense.com/instagram) |
| **TikTok** | Videos, comments, hashtags, and profiles without Research API approval | [TikTok Scraper API](https://www.surfsense.com/tiktok) |
| **Google Maps** | Places, ratings, and reviews for local business research | [Google Maps Scraper API](https://www.surfsense.com/google-maps) |
| **Google Search** | Live SERPs for search research and monitoring | [Google Search API](https://www.surfsense.com/google-search) |
| **Indeed** | Public job postings with salaries and full descriptions, by search or company | [Indeed Scraper API](https://www.surfsense.com/indeed) |
| **Amazon** | Public product data: prices, ratings, offers, sellers, and best-seller ranks | [Amazon Product API](https://www.surfsense.com/amazon) |
| **Walmart** | Public product data plus the full review history: prices, ratings, sellers, and variants | [Walmart Product & Review API](https://www.surfsense.com/walmart) |
| **Web Crawl** | Any page on the open web as clean, structured content | [Web Crawling API](https://www.surfsense.com/web-crawl) |
| **External MCP Connectors** | Bring any MCP server to your agents, with one-click OAuth for Notion, Slack, Jira, and more | [External MCP Connectors](https://www.surfsense.com/external-mcp-connectors) |

The connector catalog is growing beyond social platforms and search; every new source lands as a typed endpoint on the same API and MCP server.

Billing is pay as you go: connectors bill per item actually returned, crawls per page successfully fetched, and failed calls are never billed. Self-hosted installs run with billing off. See [pricing](https://www.surfsense.com/pricing).

## installation

### Call a connector from code

Every connector is a REST endpoint you can call from any language with your SurfSense API key:

```bash
curl -X POST "$SURFSENSE_API_URL/workspaces/$WORKSPACE_ID/scrapers/reddit/scrape" \
  -H "Authorization: Bearer $SURFSENSE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_queries": ["your brand"],
    "community": "SaaS",
    "sort": "top",
    "time_filter": "week"
  }'
```

Each [connector page](https://www.surfsense.com/connectors) has copy-paste examples in Python, JavaScript, Go, PHP, Ruby, Java, and C#.

## tools

Add the SurfSense MCP server to Claude, Cursor, or your own agent framework:

```json
{
  "mcpServers": {
    "surfsense": {
      "url": "https://mcp.surfsense.com/mcp",
      "headers": { "Authorization": "Bearer ${SURFSENSE_API_KEY}" }
    }
  }
}
```

Your agent can now call every connector as a native tool. See the [SurfSense MCP server](https://www.surfsense.com/mcp-server) page for the full tool list, or run the server locally from [`surfsense_mcp`](./surfsense_mcp).

### Use the cloud

Go to [surfsense.com](https://www.surfsense.com), log in, and ask the agent for live web data in plain English. New accounts start with $5 of free credit and no subscription.

### Self-host for free

Run the entire platform, connectors, agents, automations, and the MCP server on your own infrastructure. Self-hosted installs ship with billing off, so scraping, crawling, and agent runs are limited only by your hardware and the model keys you bring.

**Prerequisites:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed and running.

For Linux/macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh | bash
```

For Windows:

```bash
irm https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.ps1 | iex
```

The install script sets up [Watchtower](https://github.com/nicholas-fedor/watchtower) automatically for daily auto-updates. To skip it, add the `--no-watchtower` flag. For Docker Compose, manual installation, and other deployment options, see the [docs](https://www.surfsense.com/docs/).

## Everything else in the box

The research workspace that made SurfSense the leading open-source NotebookLM alternative is still here, and everything your agents gather lands in it.

**Knowledge base**

- Upload PDFs, Office docs, images, and audio, or sync **Google Drive, OneDrive, and Dropbox**. 50+ file formats supported.
- Hybrid semantic and full-text search with cited, Perplexity-style answers.
- AI file sorting auto-organizes documents by source, date, and topic.

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/BQnaGif_compressed.gif" alt="Chat With Your PDFs and Docs" /></p>

**Deliverable studio**

- Downloadable AI artifacts for reports, resumes, documents, spreadsheets, and presentations.
- Two-host AI podcasts from any document or folder in under 20 seconds.
- Editable slide decks, narrated video overviews, and AI image generation.

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/ReportGenGif_compressed.gif" alt="AI Report Generator" /></p>

**Automations**

- Run full agent turns on a schedule or in response to events, described in plain English, with results written back to Notion, Slack, Linear, and Jira.

**Team collaboration**

- Real-time collaborative AI chats with comments and mentions.
- RBAC with Owner, Admin, Editor, and Viewer roles.

<p align="center"><img src="surfsense_web/public/homepage/hero_realtime/RealTimeChatGif.gif" alt="Collaborative AI Chat" /></p>

**Desktop app**

Native AI assistance in every application on your computer. Download from the [latest release](https://github.com/MODSetter/SurfSense/releases/latest).

- **General Assist**: launch SurfSense from any app with a global shortcut.
- **Quick Assist**: select text anywhere, then ask AI to explain, rewrite, or act on it.
- **Screenshot Assist**: capture any region of your screen and ask AI about it.
- **Watch Local Folder**: auto-sync a local folder to your knowledge base. Point it at your Obsidian vault to keep your notes searchable.

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/quick_assist.gif" alt="Quick Assist" /></p>

**No vendor lock-in**

- 100+ LLMs via the OpenAI spec and LiteLLM, including GPT-5.5, Claude Sonnet 5, and Gemini 3.1 Pro.
- 6,000+ embedding models and all major rerankers.
- Full local and private LLM support (vLLM, Ollama), so your data stays yours.

## 

## limitations

Stay up to date with our development progress and upcoming features. Check out our public roadmap and contribute your ideas or feedback:

**Roadmap Discussion:** [SurfSense 2026 Roadmap](https://github.com/MODSetter/SurfSense/discussions/565)

**Kanban Board:** [SurfSense Project Board](https://github.com/users/MODSetter/projects/3)

## Contribute

All contributions welcome, from stars and bug reports to backend improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

Thanks to all our Surfers:

<a href="https://github.com/MODSetter/SurfSense/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MODSetter/SurfSense" />
</a>

## Star History

<a href="https://www.star-history.com/#MODSetter/SurfSense&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date" />
 </picture>
</a>

---
---
<p align="center">
    <img 
      src="https://github.com/user-attachments/assets/329c9bc2-6005-4aed-a629-700b5ae296b4" 
      alt="Catalyst Project" 
      width="200"
    />
</p>

---
---
