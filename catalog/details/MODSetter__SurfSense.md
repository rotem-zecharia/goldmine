# MODSetter/SurfSense

Open-source NotebookLM alternative. Research the open web with live data(Reddit, YT, IG, TikTok, Indeed, Google Search, Maps etc) through one platform, API or MCP server. Join our Discord: https://dis

## features

Ask any capable agent "what is Reddit saying about this product since launch?" or "what do the reviews of these ten places actually complain about?" and it has nowhere trustworthy to look. Official platform APIs are rate-limited, priced for enterprises, or missing entirely; scraping plumbing is brittle; and driving a browser with an LLM burns minutes and tokens per page. SurfSense gives agents the primitives instead:

- **One typed surface for wherever the data lives.** Every connector is a REST endpoint returning structured JSON — posts, comments, transcripts, reviews, SERPs, pages. No rate-limit roulette, no HTML parsing, no browser loop.
- **An MCP server** that exposes every connector as a native tool (`surfsense_reddit_scrape`, `surfsense_google_search`, and more) to Claude, Cursor, or any agent framework.
- **An agent harness**, not just raw data: retries, structured output, and credit metering are built in, so agents go from a question to a cited brief without you building the plumbing.
- **Open source and self-hostable**, so your research stays on your own infrastructure.

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

## limitations

Stay up to date with our development progress and upcoming features. Check out our public roadmap and contribute your ideas or feedback:

**Roadmap Discussion:** [SurfSense 2026 Roadmap](https://github.com/MODSetter/SurfSense/discussions/565)

**Kanban Board:** [SurfSense Project Board](https://github.com/users/MODSetter/projects/3)
