# alibaba/page-agent

JavaScript in-page GUI agent. Control web interfaces with natural language.

## features

- **🎯 Easy integration**
    - No need for `browser extension` / `python` / `headless browser`.
    - Just in-page javascript. Everything happens in your web page.
- **📖 Text-based DOM manipulation**
    - No screenshots. No multi-modal LLMs or special permissions needed.
- **🧠 Bring your own LLMs**
    - Works with most mainstream models, including locally deployed ones. See [supported models](https://alibaba.github.io/page-agent/docs/features/models).
- **🐙 Optional [chrome extension](https://alibaba.github.io/page-agent/docs/features/chrome-extension) for multi-page tasks.**
    - And an [MCP Server (Beta)](https://alibaba.github.io/page-agent/docs/features/mcp-server) to control it from outside

## installation

```bash
npm install page-agent
```

```javascript
import { PageAgent } from 'page-agent'

const agent = new PageAgent({
    model: 'qwen3.5-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'en-US',
})

await agent.execute('Click the login button')
```

For more programmatic usage, see [📖 Documentations](https://alibaba.github.io/page-agent/docs/introduction/overview).
