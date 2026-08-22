# oxylabs/oxylabs-ai-studio-js

Structured data gathering from any website using AI-powered scraper, crawler, and browser automation. Scraping and crawling with natural language prompts. Equip your LLM agents with fresh data. AI Stu

## installation

```bash
npm install oxylabs-ai-studio
```

## Quick Start

### 1. Environment Setup

Either add `OXYLABS_AI_STUDIO_API_URL` and `OXYLABS_AI_STUDIO_API_KEY` values to the `.env` file, or as your environment variables:

```bash
export OXYLABS_AI_STUDIO_API_KEY=your_api_key_here
```

## AI-Scraper

### Generate Schema 

```javascript
import { 
  OxylabsAIStudioSDK
} from 'oxylabs-ai-studio';

const sdk = new OxylabsAIStudioSDK({
  apiKey: 'your_api_key_here',
  timeout: 120000,
  retryAttempts: 3,
});

async function testGenerateSchema() {
  try {
    console.log('Testing schema generation...');
    const schema = await sdk.aiScraper.generateSchema({
      user_prompt: 'Extract the title of the page'
    });
    console.log('Schema:', schema);
  } catch (error) {
    console.error('Schema generation error:', error.message);
  }
}

testGenerateSchema();
```

## tools

```javascript
import { 
  OxylabsAIStudioSDK, 
  OutputFormat
} from 'oxylabs-ai-studio';

const sdk = new OxylabsAIStudioSDK({
  apiKey: 'your_api_key_here',
  timeout: 120000,
  retryAttempts: 3,
});

async function testScrapeOutputJson() {
  try {
    console.log('Testing synchronous scraping with JSON output...');
    
    const options = {
      url: 'https://www.freelancer.com',
      output_format: OutputFormat.JSON,
      geo_location: "US",
      schema: {
        type: 'object',
        properties: {
          links: { type: 'array', items: { type: 'string' } }
        }
      }
    };
    
    const results = await sdk.aiScraper.scrape(options);
    console.log('Sync scraping results:', results);
  } catch (error) {
    console.error('Sync scraping error:', error.message);
  }
}

testScrapeOutputJson();
```

### Available Parameters
- `url` (*string*): The target URL to process.
- `output_format` (*string*): The desired format for the output. Can be either `markdown`, `json`, `screenshot`, `csv` or `toon`. Defaults to `markdown`.
- `render_javascript` (*boolean | "auto"*): Whether to render JavaScript before extraction. Can be `"auto"` to auto-detect if rendering is needed. Defaults to `false`.
- `schema` (*Record<string, any>*): A JSON Schema object that defines the structure of the output data. This is required when `output_format` is `json`, `csv` or `toon`.
- `geo_location` (*string*): Specifies the geographic location (ISO2 format) or country canonical name from which the request should be simulated.
- `user_agent` (*string*): User-Agent request header. See [available values](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/http-context-and-job-management/user-agent-type).
- `optimize_content` (*boolean*): Return cleaner markdown by focusing on the main page content. Output will be smaller in size when set to `true`. Defaults to `true`.
- `browser_instructions` (*BrowserInstruction[]*): Browser actions to run before capture (click, input, wait, etc.). Requires `render_javascript: true`. Format follows [Web Scraper API browser instructions](https://developers.oxylabs.io/products/web-scraper-api/features/js-rendering-and-browser-control#browser-instructions).

## AI-Crawler

### Basic usage

```javascript
import { 
  OxylabsAIStudioSDK, 
  OutputFormat
} from 'oxylabs-ai-studio';

const sdk = new OxylabsAIStudioSDK({
  apiKey: 'your_api_key_here',
  timeout: 120000,
  retryAttempts: 3,
});

async function testCrawlOutputJson() {
  try {
    console.log('Testing crawling with JSON output...');
    
    const options = {
      url: 'https://www.freelancer.com',
      output_format: OutputFormat.JSON,
      user_prompt: 'Get job ad pages',
      return_sources_limit: 3,
      geo_location: "Germany",
      schema: {
        type: "object",
        properties: {
          jobAd: {
            type: "object",
            properties: {
              position_title: {
                type: "string"
              },
              salary: {
                type: "string"
              }
            }
          }
        }
      }
    };
    
    const results = await sdk.aiCrawler.crawl(options);
    console.log('Crawling results:', JSON.stringify(results, null, 2));      
  } catch (error) {
    console.error('Crawling error:', error.message);
  }
}

testCrawlOutputJson();
```

### Available Parameters
- `url` (*string*): The starting URL for the crawl.
- `user_prompt` (*string*): Crawling instructions.
  - For auto-schema flow, use `parse_prompt` in `crawlWithAutoSchema()` to generate the `schema`.
- `output_format` (*string*): The desired format for the output. Can be either `markdown`, `json`, `csv` or `toon`. Defaults to `markdown`.
- `return_sources_limit` (*integer*): The maximum number of pages/sources to return. Defaults to `25`.
- `render_javascript` (*boolean*): Whether to render JavaScript on pages before extraction. Defaults to `false`.
- `schema` (*Record<string, any>*): A JSON Schem
