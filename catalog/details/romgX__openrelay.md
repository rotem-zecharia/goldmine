# romgX/openrelay

几百个免费 AI 模型配额，一键接入本地项目。/ Hundreds of free AI model quotas, one-click access to local projects.

## installation

No more editing `.zshrc` or juggling environment variables. Open the Web dashboard, pick a provider for each tool, flip a switch:

- **Claude Code** → route through Kiro (using your Kiro account quota)
- **Aider** → route through Groq (low-latency inference)
- **Goose** → route through Gemini API (large-context models)
- **OpenCode** → route through DeepSeek (cheapest coding model)

Reopen your terminal. Done. Every tool is configured.

### 4. Supercharge your IDE with external quotas

Cursor quota burned through? Windsurf credits gone? Don't stop coding — seamlessly plug in any other quota source:

| IDE | How it works | What you get |
|-----|-------------|--------------|
| **Cursor** | RPC proxy (ConnectRPC, HTTP/2) | Use Claude/Kiro/Groq/any provider inside Cursor |
| **Windsurf** | RPC proxy (ConnectRPC) | Replace Windsurf's built-in models |
| **VS Code Copilot** | Ollama BYOK bridge | Use any model as a Copilot backend |
| **Antigravity** | Gemini REST proxy | Route through any provider |

Start the proxy from the dashboard. Your IDE doesn't know the difference.

### 5. Combine quotas with failover

Take quotas from multiple providers and merge them into a single virtual model:

```
"fast-group" = Groq (Llama 90B) + Cerebras (Llama 70B) + SambaNova (Llama 405B)
```

When Groq quota is unavailable → automatic failover to Cerebras → then SambaNova. Round-robin and failover keep using the providers you configured while quota remains, reducing manual switching.

---

## Supported Providers (58 non-virtual)

### Local / CLI / IDE Providers (13)

These use local app sessions, CLI auth files, or local gateways when available.

| Provider | Credential source | Notes |
|----------|-------------------|-------|
| **Claude Desktop** | Local Claude Desktop session | Claude Pro/Max account quota |
| **Claude Code** | Claude Code credentials | Claude account quota |
| **Kiro** (AWS) | Kiro app session | Kiro account quota |
| **Windsurf** (Codeium) | Windsurf session | IDE quota and models |
| **Antigravity** | Antigravity app session | Gemini-compatible route |
| **OpenCode** | OpenCode local config | Built-in route |
| **VS Code Copilot** | VS Code / GitHub Copilot session | Copilot account quota |
| **OpenAI Codex** | Codex local auth | REST + WebSocket transport |
| **Gemini CLI** | `~/.gemini/oauth_creds.json` | Gemini CLI OAuth |
| **Rovo Dev** | Atlassian / Rovo Dev config or env | Rovo account quota |
| **QClaw** | QClaw local gateway | Agent gateway; best for QClaw workflows |
| **Trae** | Trae app session | Trae account models |
| **Cursor** | Cursor app session | Supply-side Auto quota (experimental) |

## tools

These use your provider API key, provider account, or local endpoint. Quotas and free tiers are controlled by each upstream provider and can change.

| Provider | Type |
|----------|------|
| **Groq** | OpenAI-compatible API |
| **Cerebras** | OpenAI-compatible API |
| **OpenRouter** | OpenAI-compatible API |
| **SambaNova** | OpenAI-compatible API |
| **Gemini API** | OpenAI-compatible API |
| **Mistral** | OpenAI-compatible API |
| **xAI** | OpenAI-compatible API |
| **SiliconFlow** | OpenAI-compatible API |
| **Zhipu / GLM** | OpenAI-compatible API |
| **Together AI** | OpenAI-compatible API |
| **DashScope** | OpenAI-compatible API |
| **DeepSeek** | OpenAI-compatible API |
| **NVIDIA NIM** | OpenAI-compatible API |
| **GitHub Models** | OpenAI-compatible API |
| **Fireworks** | OpenAI-compatible API |
| **Volcengine** | OpenAI-compatible API |
| **Qianfan** | OpenAI-compatible API |
| **Qiniu** | OpenAI-compatible API |
| **Moonshot** | OpenAI-compatible API |
| **Baichuan** | OpenAI-compatible API |
| **Stepfun** | OpenAI-compatible API |
| **MiniMax** | OpenAI-compatible API |
| **Hunyuan** | OpenAI-compatible API |
| **Cloudflare AI** | OpenAI-compatible API |
| **HuggingFace** | OpenAI-compatible API |
| **LongCat** | OpenAI-compatible API |
| **Kilo** | OpenAI-compatible API |
| **LLM7** | OpenAI-compatible API |
| **Vercel AI Gateway** | OpenAI-compatible API |
| **BlazeAPI** | OpenAI-compatible API |
| **Pollinations** | OpenAI-compatible API |
| **BazaarLink** | OpenAI-compatible API |
| **Qwen Cloud** | OpenAI-compatible API |
| **ModelScope** | OpenAI-compatible API |
| **Agnes AI** | OpenAI-compatible API (free multimodal) |
| **Puter** | OpenAI-compatible API |
| _…and more_ | see the in-app provider list |
| **Anthropic API** | Native Anthropic API |
| **Ollama** | Local endpoint |

---
