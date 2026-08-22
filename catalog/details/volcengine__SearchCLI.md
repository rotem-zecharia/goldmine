# volcengine/SearchCLI

Open CLI for integrating AI search, recommendation, and conversational retrieval into agent systems and business systems

## features

- `vs item profile | plan | apply` for structured item onboarding.
- `vs app`, `vs dataset`, and `vs data` for application and dataset management.
- `vs search run`, `vs recommend run`, and `vs chat run` for runtime verification.
- `vs search tune query-generate | plan | run | report` for first-version automated text-similarity evaluation and tuning.
- Installable `Viking skills` so external agents can use the same workflows.

## requirements

- Node.js 20 or newer
- `git`
- Volcengine AK/SK with access to AI Search

## installation

### 1. Install

```bash
git clone git@github.com:volcengine/SearchCLI.git vs
cd vs
bash ./scripts/install.sh
```

### 2. Authenticate

If the current shell already has `VIKING_AK` and `VIKING_SK`:

```bash
vs auth import-env
vs auth status --json
vs doctor --json
```

Otherwise, run interactive login in a real terminal:

```bash
vs auth login
```

If you will use search tuning query generation or LLM relevance judging, configure an OpenAI-compatible LLM API without placing the API key in plain config:

```bash
vs llm login
vs llm status --json
vs search tune llm-check --live --json
```

If the current shell already has `VIKING_LLM_BASE_URL`, `VIKING_LLM_API_KEY`, and `VIKING_LLM_MODEL`, use `vs llm import-env` instead. The API key is stored in the local secure credential store; base URL and model are stored as non-secret config.

### 3. Run the First Onboarding Flow

If the user wants a new app plus bind-time config review and runtime verification, use the `dataset+app` path:

```bash
vs item profile --file ./items.json --pretty
vs item plan --file ./items.json --goal "Build item search"
vs item apply --plan-dir ./.viking/item-plans/<plan> --dry-run
vs item apply --plan-dir ./.viking/item-plans/<plan> --confirm-review --wait-ready --run-trials
```

If you only need dataset provisioning, use the `dataset-only` path, generate a dataset-only plan with `--skip-app`, and stop after dataset create + ingest:

```bash
vs item profile --file ./items.json --pretty
vs item plan --file ./items.json --goal "Build item search" --skip-app
vs dataset create --data @dataset-create.json
vs dataset ingest --dataset-id <dataset-id> --fields @<normalized-items-artifact>
```

Prefer `dataset-create.json` when the plan emitted it so dataset creation keeps `Schema` and `DataFieldConfig` together. The `--name <dataset-name> --type item --schema @schema.json` form remains the manual schema-only fallback when a full create payload is unavailable or unsuitable.

`--skip-app` is also accepted by `vs item provision` and `vs item apply` as an execution-time guard rail when you need to enforce the dataset-only boundary from an existing plan.

If you need a video dataset, do not rely on the default type. Always pass `--type video` explicitly:

For `dataset+app`:

```bash
vs item profile --file ./videos.jsonl --type video --pretty
vs item plan --file ./videos.jsonl --type video --goal "Build video search"
vs item apply --plan-dir ./.viking/item-plans/<plan> --dry-run
vs item apply --plan-dir ./.viking/item-plans/<plan> --confirm-review --wait-ready --run-trials
```

For `dataset-only`:

```bash
vs item profile --file ./videos.jsonl --type video --pretty
vs item plan --file ./videos.jsonl --type video --goal "Build video search" --skip-app
vs dataset create --data @dataset-create.json
vs dataset ingest --dataset-id <dataset-id> --fields @<normalized-items-artifact>
```

For video dataset-only provisioning, prefer `dataset-create.json` so the create request includes `DataFieldConfig`; `--schema @schema.json` alone can fail with `MissingParameter.DefaultFieldStrategy`.

## Quick Start (AI Agents)

If an external agent needs to operate AI Search through this repository:

### 1. Install SearchCLI

```bash
git clone git@github.com:volcengine/SearchCLI.git vs
cd vs
bash ./scripts/install.sh
```

### 2. Install Viking skills

```bash
npx skills add "git@github.com:volcengine/SearchCLI.git" -y -g
```

The default public skill bundle is:

- `vs-shared`
- `vs-item-onboarding`
- `vs-search`
- `vs-search-tuning`
- `vs-chat`
- `vs-recommend`

### 3. Authenticate

If the current shell already has `VIKING_AK` and `VIKING_SK`, prefer:

```bash
vs auth import-env
```

Otherwise:

```bash
vs auth login
```

### 4. Verify

```bash
vs --help
vs auth status --json
vs llm status --json
vs doctor --json
vs skill list
```

## Public Command Groups

- `vs auth`
- `vs llm`
- `vs doctor`
- `vs skill`
- `vs item`
- `vs app`
- `vs dataset`
- `vs data`
- `vs search`
- `vs chat`
- `vs recomm
