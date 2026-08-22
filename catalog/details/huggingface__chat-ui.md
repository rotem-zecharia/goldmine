# huggingface/chat-ui

The open source codebase powering HuggingChat

## installation

Chat UI speaks to OpenAI-compatible APIs only. The fastest way to get running is with the Hugging Face Inference Providers router plus your personal Hugging Face access token.

**Step 1 – Create `.env.local`:**

```env
OPENAI_BASE_URL=https://router.huggingface.co/v1
OPENAI_API_KEY=hf_************************
```

`OPENAI_API_KEY` can come from any OpenAI-compatible endpoint you plan to call. Pick the combo that matches your setup and drop the values into `.env.local`:

| Provider                                      | Example `OPENAI_BASE_URL`          | Example key env                                                         |
| --------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------- |
| Hugging Face Inference Providers router       | `https://router.huggingface.co/v1` | `OPENAI_API_KEY=hf_xxx` (or `HF_TOKEN` legacy alias)                    |
| llama.cpp server (`llama.cpp --server --api`) | `http://127.0.0.1:8080/v1`         | `OPENAI_API_KEY=sk-local-demo` (any string works; llama.cpp ignores it) |
| Ollama (with OpenAI-compatible bridge)        | `http://127.0.0.1:11434/v1`        | `OPENAI_API_KEY=ollama`                                                 |
| OpenRouter                                    | `https://openrouter.ai/api/v1`     | `OPENAI_API_KEY=sk-or-v1-...`                                           |
| Poe                                           | `https://api.poe.com/v1`           | `OPENAI_API_KEY=pk_...`                                                 |

Check the root [`.env` template](./.env) for the full list of optional variables you can override.

**Step 2 – Install and launch the dev server:**

```bash
git clone https://github.com/huggingface/chat-ui
cd chat-ui
npm install
npm run dev -- --open
```

You now have Chat UI running locally. Open the browser and start chatting.

## configuration

Chat history, users, settings, files, and stats all live in MongoDB. You can point Chat UI at any MongoDB 6/7 deployment.

> [!TIP]
> For quick local development, you can skip this section. When `MONGODB_URL` is not set, Chat UI falls back to an embedded MongoDB that persists to `./db`.

## tools

Chat UI can call tools exposed by Model Context Protocol (MCP) servers and feed results back to the model using OpenAI function calling. You can preconfigure trusted servers via env, let users add their own, and optionally have the Omni router auto‑select a tools‑capable model.

Configure servers (base list for all users):

```env
