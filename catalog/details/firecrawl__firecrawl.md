# firecrawl/firecrawl

Knowledge infrastructure to make your agents smarter. Search, scrape and 550+ data providers through one API.

## tools

`serve` answers the Firecrawl v2 API on port 3002, so code written for Firecrawl runs against it unchanged and local routes need no API key.

```bash
firecrawl-local serve
```

Point any Firecrawl SDK at it by setting the API URL.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_url="http://localhost:3002")
print(app.scrape("https://firecrawl.dev").markdown)
```

The [Firecrawl Local README](apps/local) covers every command and option, the security defaults for `serve` and running it in Docker. Move to [Firecrawl Cloud](#firecrawl-cloud) when you need structured JSON, Interact, the Agent or scale beyond one machine.

---

## What runs where

| Feature | Firecrawl Local | Firecrawl Cloud |
|---------|-----------------|-----------------|
| [Scrape](#scrape) | Markdown, HTML, raw HTML and links | Adds structured JSON, summaries, screenshots and browser actions |
| [Crawl](#crawl), [Map](#map) and [Batch Scrape](#batch-scrape) | ✅ | ✅ |
| PDFs and Office documents | ✅ | ✅, plus [Parse](https://docs.firecrawl.dev/features/parse) for uploaded files |
| [Search](#search) | Through Firecrawl Cloud, no account needed | ✅ |
| [Alexandria](#alexandria) | Through Firecrawl Cloud after `firecrawl-local login` | ✅ |
| [Interact](#interact), [Agent](#agent) and [Monitor](https://docs.firecrawl.dev/features/monitoring) | | ✅ |

Scraping, crawling and mapping run on your machine. By default a single-page scrape that won't load there is fetched by Firecrawl Cloud instead and marked `"source": "firecrawl-cloud"` in the result. Those Cloud calls work without an account at a limited rate, and `firecrawl-local login` puts them on your Firecrawl account. Set `FIRECRAWL_CLOUD=off` to keep everything on your machine.

---

## Firecrawl Cloud

Firecrawl Cloud runs everything Firecrawl Local does at scale, with no browser or machine of your own to look after. It also gives your AI agents access to far more knowledge than scraping alone, with search, Alexandria, Interact and Agent all through a single API.

- **Works on the real web.** Covers 96% of the web, including JS-heavy pages and dynamic apps ([see benchmarks](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25)).
- **Fast.** P95 latency of 3.4s across millions of pages, built for real-time AI agents and dynamic apps.
- **LLM-ready output.** Clean markdown, structured JSON, screenshots and more, so your AI agents spend fewer tokens.

[Firecrawl Keyless](https://www.firecrawl.dev/blog/firecrawl-keyless-launch) gives you 1,000 free credits a month with no API key or signup across MCP, the CLI and the API. For an API key, sign up at [firecrawl.dev](https://firecrawl.dev) and try it in the [playground](https://firecrawl.dev/playground).

### Search

Search the web and get full content from results.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

search_result = app.search("firecrawl", limit=5)
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import { Firecrawl } from 'firecrawl';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

app.search("firecrawl", { limit: 5 })
```

**cURL**
```bash
curl -X POST 'https://api.firecrawl.dev/v2/search' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
  "query": "firecrawl",
  "limit": 5
}'
```

**CLI**
```bash
firecrawl search "firecrawl" --limit 5
```
</details>

```json
[
  {
    "url": "https://firecrawl.dev",
    "title": "Firecrawl",
    "markdown": "Turn websites into..."
  },
  {
    "url": "https://docs.firecrawl.dev",
    "title": "Firecrawl Docs",
    "markdown": "# Getting Started..."
  }
]
```

### Scrape

Get LLM-ready context from any website as markdown, JSON, screenshots and more.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape('firecrawl.dev')
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
impor

## features

- Search: Find information across the web
- Scrape: Clean data from any page
- Interact: Click, navigate, and operate pages
- Agent: Autonomous data gathering
```

### Interact

Scrape a page, then interact with it using AI prompts or code.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape("https://amazon.com")
scrape_id = result.metadata.scrape_id

app.interact(scrape_id, prompt="Search for 'mechanical keyboard'")
app.interact(scrape_id, prompt="Click the first result")
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import { Firecrawl } from 'firecrawl';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

const result = await app.scrape("https://amazon.com");

await app.interact(result.metadata.scrapeId, {
  prompt: "Search for 'mechanical keyboard'"
});
await app.interact(result.metadata.scrapeId, {
  prompt: "Click the first result"
});
```

**cURL**
```bash
# 1. Scrape the page
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"url": "https://amazon.com"}'

# 2. Interact with the page (use scrapeId from step 1)
curl -X POST 'https://api.firecrawl.dev/v2/scrape/SCRAPE_ID/interact' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Search for mechanical keyboard"}'
```

**CLI**
```bash
firecrawl scrape https://amazon.com
firecrawl interact exec --prompt "Search for 'mechanical keyboard'"
firecrawl interact exec --prompt "Click the first result"
```
</details>

```json
{
  "success": true,
  "output": "Keyboard available at $100",
  "liveViewUrl": "https://liveview.firecrawl.dev/..."
}
```

### Agent

Describe what you need, and our AI agent searches, navigates and retrieves it with no URLs required.

```bash
curl -X POST 'https://api.firecrawl.dev/v2/agent' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "prompt": "Find the pricing plans for Notion"
  }'
```

```json
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. Free - $0/month...\n2. Plus - $10/seat/month...\n3. Business - $18/seat/month...",
    "sources": ["https://www.notion.so/pricing"]
  }
}
```

Pass a schema to get structured data back.

```python
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from typing import List, Optional

app = Firecrawl(api_key="fc-YOUR_API_KEY")

class Founder(BaseModel):
    name: str = Field(description="Full name of the founder")
    role: Optional[str] = Field(None, description="Role or position")

class FoundersSchema(BaseModel):
    founders: List[Founder] = Field(description="List of founders")

result = app.agent(
    prompt="Find the founders of Firecrawl",
    schema=FoundersSchema
)

print(result.data)
```

The [Agent documentation](https://docs.firecrawl.dev/features/agent) covers starting URLs, effort levels and the `spark-2` model.

### Crawl

Crawl an entire website and get content from all pages.

```bash
curl -X POST 'https://api.firecrawl.dev/v2/crawl' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "limit": 100,
    "scrapeOptions": {
      "formats": ["markdown"]
    }
  }'
```

It returns a job ID, and the [SDKs](#sdks) poll it for you until the crawl finishes.

```json
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

### Map

Discover all URLs on a website instantly.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.map("https://firecrawl.dev", search="pricing")
# Returns URLs ordered by relevance to "pricing"
```

### Batch Scrape

Scrape many URLs at once.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

job = ap
