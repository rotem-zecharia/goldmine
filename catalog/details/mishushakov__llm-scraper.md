# mishushakov/llm-scraper

Turn any webpage into structured data using LLMs

## features

- Supports GPT, Sonnet, Gemini, Llama, Qwen model series
- Schemas defined with Zod or JSON Schema
- Full type-safety with TypeScript
- Based on Playwright framework
- Streaming objects
- [Code-generation](#code-generation)
- Supports 6 formatting modes:
  - `html` for loading pre-processed HTML
  - `raw_html` for loading raw HTML (no processing)
  - `markdown` for loading markdown
  - `text` for loading extracted text (using [Readability.js](https://github.com/mozilla/readability))
  - `image` for loading a screenshot (multi-modal only)
  - `custom` for loading custom content (using a custom function)

**Make sure to give it a star!**

<img width="165" alt="Screenshot 2024-04-20 at 22 13 32" src="https://github.com/mishushakov/llm-scraper/assets/10400064/11e2a79f-a835-48c4-9f85-5c104ca7bb49">

## installation

1. Install the required dependencies from npm:

   ```
   npm i zod playwright llm-scraper
   ```

2. Initialize your LLM:

   **OpenAI**

   ```
   npm i @ai-sdk/openai
   ```

   ```js
   import { openai } from '@ai-sdk/openai'

   const llm = openai('gpt-4o')
   ```

   **Anthropic**

   ```
   npm i @ai-sdk/anthropic
   ```

   ```js
   import { anthropic } from '@ai-sdk/anthropic'

   const llm = anthropic('claude-3-5-sonnet-20240620')
   ```

   **Google**

   ```
   npm i @ai-sdk/google
   ```

   ```js
   import { google } from '@ai-sdk/google'

   const llm = google('gemini-1.5-flash')
   ```

   **Groq**

   ```
   npm i @ai-sdk/openai
   ```

   ```js
   import { createOpenAI } from '@ai-sdk/openai'
   const groq = createOpenAI({
     baseURL: 'https://api.groq.com/openai/v1',
     apiKey: process.env.GROQ_API_KEY,
   })

   const llm = groq('llama3-8b-8192')
   ```

   **Ollama**

   ```
   npm i ollama-ai-provider-v2
   ```

   ```js
   import { ollama } from 'ollama-ai-provider-v2'

   const llm = ollama('llama3')
   ```

3. Create a new scraper instance provided with the llm:

   ```js
   import LLMScraper from 'llm-scraper'

   const scraper = new LLMScraper(llm)
   ```
