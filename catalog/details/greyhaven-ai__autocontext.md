# greyhaven-ai/autocontext

a recursive self-improving harness designed to help your agents (and future iterations of those agents) succeed on any task

## installation

| Surface             | Command                               |
| ------------------- | ------------------------------------- |
| Python CLI          | `uv tool install autocontext==0.16.1` |
| Python library/dev  | `uv pip install autocontext==0.16.1`  |
| TypeScript/Node CLI | `bun add -g autoctx@0.16.1`           |
| Pi extension        | `pi install npm:pi-autocontext@0.10.0` |

The PyPI package is `autocontext`; the CLI is `autoctx`. The npm package is `autoctx` (not the unrelated `autocontext` npm package). Provider variables live in [`.env.example`](.env.example).
The npm CLI and TUI require Node.js 22.19.0 or newer; contributors should use
the version pinned in [`ts/.nvmrc`](ts/.nvmrc).

## 30-Second Run

Pi is the lowest-friction provider because it uses your local agent auth:

```bash
AUTOCONTEXT_AGENT_PROVIDER=pi \
AUTOCONTEXT_PI_COMMAND=pi \
autoctx solve "improve customer-support replies for billing disputes" --iterations 3
```

Use `AUTOCONTEXT_AGENT_PROVIDER=anthropic`, `openai-compatible`, `openrouter`, `claude-cli`, `codex`, `pi-rpc`, or another provider when you need that runtime. See [agent integration](autocontext/docs/agent-integration.md) for the full matrix.

Running it on your own GPU instead? [Self-hosted models](autocontext/docs/self-hosted-models.md) covers the whole loop on vLLM, Ollama, or any OpenAI-compatible endpoint — including what each role actually resolves to, and why constrained output matters more on open weights.
Self-hosted endpoints can additionally declare `AUTOCONTEXT_PROVIDER_HOSTING=local` and a `fast`, `mid_tier`, or `frontier` `AUTOCONTEXT_PROVIDER_CAPABILITY`; role-specific endpoints use matching `<ROLE>_PROVIDER_*` declarations.

## Agent Entry Points

- **Pi:** install `pi-autocontext`, then ask Pi to solve, judge, improve, list, or inspect runs through the packaged skill.
- **MCP clients:** run `autoctx serve mcp` or `bunx autoctx serve mcp` and expose the tools to Claude Code, Cursor, or another MCP client.
- **Hermes:** export the CLI-first skill with `uv run autoctx hermes export-skill --with-references --json`.

Full setup: [autocontext/docs/agent-integration.md](autocontext/docs/agent-integration.md).

## What A Run Leaves Behind

```text
runs/<run_id>/
├── trace.jsonl
├── generations/<n>/{strategy.json,analysis.md,score.json}
├── report.md
└── artifacts/

knowledge/<scenario>/
├── playbook.md
├── hints.md
├── tools/
└── context_bundles/{bundles,candidates,promotions,active.json}
```

Everything is filesystem-first: inspect it, diff it, replay it, export it, or feed it into training.
Coach and architect context changes are stored as immutable candidates and are
not served until matched candidate/incumbent trials confirm them. The live
serving boundary can additionally require a cancellable independent audit and
a durable campaign-wide false-promotion budget; exact causal credit is accepted
only from verified single-component manifest additions. See
[context bundles and outcome-gated promotion](docs/context-bundles.md).
Controlled component trials feed
[ablation-backed attribution](docs/context-attribution.md), so prompt selection
can demote low-value context without presenting edit-size correlation as causal.

## Core Surfaces

| Surface       | Command                                                 | Use it for                                              |
| ------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `solve`       | `autoctx solve "..." --iterations 3`                    | Start from a plain-language goal                        |
| `run`         | `autoctx run <scenario> --iterations 3`                 | Improve a saved scenario                                |
| `status`      | `autoctx status <run-id> --json`                        | Read one run snapshot                                   |
| `watch`       | `autoctx watch <run-id> --ndjson`                       | Stream run 
