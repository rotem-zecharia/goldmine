# Deuz-AI/Deuz-SDK

Zero-dependency TypeScript framework for production AI agents: durable execution, long-term memory, hybrid RAG, MCP tool calling, human-in-the-loop approval, planning and CodeAct sandboxes. One stream

## installation

```sh
npm install @deuz-sdk/core     # the runtime
npm install @deuz-sdk/react    # optional: useChat, useObject, headless UI
```

Node ≥ 22, or any edge runtime with `fetch`. Optional peers only when you use them: `zod` (or any Standard Schema library), `@modelcontextprotocol/sdk`, `react`, `pg` / `redis`, `unpdf` / `mammoth` / `xlsx`, `playwright`, `@opentelemetry/api`.

### Teach your coding agent

```sh
npx skills add Deuz-AI/Deuz-SDK
```

Two Agent Skills, for Claude Code and any other agent that reads the format.

**`deuz-sdk`** is a build guide over the whole surface — the mental model and its invariants, a task-to-file router, and thirteen reference files the agent loads only when the task needs them, covering every one of the 53 subpaths. **`migrate-from-ai-sdk`** is the verified name-by-name port from `ai` and `@ai-sdk/*`.

They are gated, not just written. Every `@deuz-sdk` symbol in them is resolved against the real export table on every commit, every code example is compiled against the built package, and a freshness check fails the moment the version or the locked API contract moves — so an agent reading them cannot confidently invent a function that does not exist. Written test-first: nine build tasks were given to agents without the skill first, which produced 19 imaginary imports across 8 of 9 answers.

## How it is built

One design rule explains most of the code: **normalize provider bytes to a canonical delta stream first.** Retry, failover, resume, budgets, sub-agents and typed UI events then share one language, and no code path streams a provider's raw SSE to a caller.

The rest follows from it:

- **Zero runtime dependencies.** Ours to test, version and secure.
- **No ambient state.** One `Dependencies` seam for clock, randomness, `fetch`, logging and keys — lint bans `Date.now()` and `Math.random()` in core, which is also why tests are deterministic.
- **Your infrastructure.** Checkpoints and journals live in your process and your database.
- **Privacy by default.** Content capture is opt-in and always redacted; API keys never reach a log, error or span.
- **The gate is the contract.** `npm run check` runs formatting, lint, types, 1,892 tests, a dual build, `publint` + Are-the-Types-Wrong, an edge bundle with no Node leaks, byte budgets, and a locked list of 242 public exports across 54 subpaths. A removed export fails the release, not your build.

Most tests replay recorded provider bytes, which proves the SDK builds the request it means to but never that a provider accepts it. So a separate [live suite](./packages/core/test/live) calls the real endpoints. It has already earned its keep: it confirmed that Gemini answers a tool request with `finishReason: STOP` — the exact shape that makes a naive loop hang up holding a tool call instead of an answer — and that a thinking model can spend 112 reasoning tokens against 1 answer token, which an SDK that misreads the usage envelope would under-report by an order of magnitude.

## What this is not

**Need the largest ecosystem today? Use the Vercel AI SDK.** Years of production hours, hundreds of contributors, integrations everywhere. That gap is real and it is not closing this year, and no feature list here changes it.

Our bet is smaller: a runtime you can hold in your head. Durability without a workflow vendor. Autonomy without an Agent god-class. Observability without an account. Nothing phones home.

So the limitations sit next to the features rather than in an issue tracker. Overflow recovery does not reach the Gemini native wire. `generateObject` cannot coerce a DeepSeek V4 model — it refuses both strategies, and [the page says why](./docs/content/docs/providers/compat.mdx#deepseek-v4-always-thinks). The Redis pack has no `MULTI`. Token counting is a calibrated heuristic unless you supply a tokenizer. `rerank` is still the identity reranker, MCP has no WebSocket transport, and the `Part` union has no `AudioPart`. Speech, transcription and video are cov
