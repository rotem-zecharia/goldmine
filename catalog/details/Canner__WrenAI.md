# Canner/WrenAI

GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data s

## features

- **Generative BI, end to end.** Wren does **governed text-to-SQL** — and goes beyond it: generate the answer, deploy the dashboard, share the URL, all driven by the agents you already use.
- **Knowledge management built in.** Business meaning, approved definitions, and proven examples are captured as a reviewable, version-controlled **semantic layer (MDL)**, not buried in prompts.
- **Open by default.** Open-sourced core, SDK, and skills under the Apache-2.0 license.
- **Correctness as primitives.** Rich schema retrieval, dry-plan validation, structured errors with hints, value profiling, eval runner. The agent orchestrates; the trace lives in its reasoning.
- **Governed execution, reviewable context.** Dry-plan validation, row limits, and structured errors keep agent-generated SQL inside guardrails, and every definition and example lives in Git — reviewable, versioned, diff-able. (Row/column-level security and access control are Cloud / self-hosted — see [Open core: OSS vs. Cloud / self-hosted](#open-core-oss-vs-cloud--self-hosted).)
- **Sits on top of your existing stack.** Warehouse, transformation pipelines, your existing semantic layer. Not another tool to maintain.

## How Wren compares

|  | A raw LLM agent | A traditional BI tool | A bare semantic layer | **WrenAI** |
|---|:---:|:---:|:---:|:---:|
| Writes SQL for you | ✅ (often wrong) | ❌ | ❌ | ✅ governed |
| Knows your business definitions | ❌ | partial, in-tool | ✅ (schema only) | ✅ + non-schema knowledge |
| Generates & deploys dashboards | ❌ | ✅ (manual, in-tool) | ❌ | ✅ agent-driven |
| Works through *your* agents (Claude Code, Cursor, MCP…) | ✅ | ❌ | ❌ | ✅ |
| Open, reviewable, Git-friendly context | ❌ | ❌ | partial | ✅ |
| Governed execution across 22+ sources | ❌ | per-connector | ✅ (definitions only) | ✅ |

## Wren is for you if…

- You want **AI agents to produce trustworthy BI**, answers *and* dashboards, not just plausible SQL.
- Your business logic (definitions, enums, units, approved joins) lives **outside the database** and your agents keep getting it wrong.
- You want an **AI context layer** and **semantic layer** that are **open, reviewable, and version-controlled**, usable by every agent and person, not gated behind one vendor's UI.

**Skip Wren if** you only need a one-off chart from a single CSV, or you're happy letting an agent guess at SQL with no governance.

## installation

WrenAI is **agent-driven by design**: install the CLI, install a one-file
discovery stub for your AI client, then let your AI agent drive the rest.
Workflow guides live inside the CLI itself and are served on demand, so
content always matches the installed version.

### 1. Install the CLI

```bash
pip install wrenai                      # core (DuckDB included)
pip install "wrenai[postgres,memory]"   # add per-datasource and memory extras as needed
```

> **Tip for users in mainland China:** If `pip install` is slow or fails, use the Tsinghua mirror:
> ```bash
> pip install wrenai -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```
> If HuggingFace model downloads time out, add `export HF_ENDPOINT=https://hf-mirror.com` before running the CLI.

### 2. Install the discovery stub for your AI client

```bash
npx skills add Canner/WrenAI            # auto-detects Claude Code, Cursor, Cline, Codex, …
```

The stub is ~50 lines. It teaches your agent to fetch workflow guides via
`wren skills get <name>` and shaped prompts via
`wren ask "<question>" --guided|--direct`, and everything else lives in the CLI.

### 3. Ask your agent to set things up

Open your agent in a project directory and say something like:

> "Use Wren to set up my Postgres database."

The agent runs `wren skills get onboarding`, follows the guide step-by-step,
checks your environment, creates a connection profile, scaffolds the project,
and runs a first query.

### 4. (Optional) Enrich the project: the *Know* beat

Once onboarding finishes, ask:

> "Enrich my Wren project with the business context in `raw/`."

The agent runs `wren skills get enrich-context` and follows the guide in
**grill** mode (one question at a time) or **auto-pilot** mode (agent reads
`<project>/raw/` and proposes). Both modes write to MDL, instructions,
queries, and memory, all reviewable, all Git-friendly.

### 5. Ask questions: the *Generate* beat

> "Who are our top 10 customers by sales this quarter?"

Your agent fetches MDL context, recalls similar past queries, writes
governed SQL, and executes via `wren query`.

### 6. Build & deploy a dashboard: the *Deploy* beat

> "Turn that into an interactive dashboard I can filter and share, and deploy it to Vercel."

The agent runs `wren skills get genbi`, builds a browser-side GenBI app from
your project's context, previews it locally, and ships it to your own Vercel
or Cloudflare Pages account, returning a live, shareable URL. See the
[Build & deploy a GenBI app guide](https://docs.getwren.ai/oss/guides/genbi).

**Want to try it without your own database?** Ask your agent to use the
bundled `jaffle_shop` sample dataset. Same flow, querying a real warehouse
end-to-end in a couple of minutes.

## Two beats first, then the third

```bash
# Day 1 (agent-driven)
wren skills get onboarding         # workflow guide: set up project + first query  (Generate)
wren skills get enrich-context     # workflow guide: add business context           (Know)
wren skills get genbi              # workflow guide: build & deploy a dashboard      (Deploy)

# Day-to-day
wren query --sql '...'             # query through the MDL semantic layer
wren ask "<question>" --guided     # wrap a question for a weaker agent
wren ask "<question>" --direct     # wrap a question for a stronger agent
```

Fast at first. Deep when you need it. Always reviewable and Git-friendly.

## Semantic layer (MDL)

Wren **is** a governed semantic layer, expressed in the **Modeling Definition Language (MDL)** — a Git-friendly, reviewable definition of what your data *means*, not just where it lives. Every text-to-SQL answer and dashboard is planned against it, so agents inherit your business truth instead of guessing.

MDL covers:

- **Models, columns, relationships, and views** — the shape of your data, decoupled from any one warehouse.
- **Cubes and metrics** — approved, reusable definitions so "revenue" means the same thing everywhere.
- **Business context beyond the schema** — enums, units, ap
