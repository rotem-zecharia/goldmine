# mindsdb/mindshub

The unified workspace where open-source models get things done for you.

## features

This repo is a superproject that pins each module (`frontend`, `backend/core_api`, `backend/core_agent`, `backend/data-vault`) to a commit. To work on module branches without polluting `git status` or fighting over pins:

**1. Pick your branches** in a gitignored `dev.env` (copy the template):

```bash
cp dev.env.example dev.env      # then set REF=feat/my-thing (or per-module API_REF=…)
```

**2. `make` follows it** — one knob, both run paths:

| Command | What it does |
|---|---|
| `make use` | check out your `dev.env` refs across all submodules |
| `make dev` / `make watch` | run the Electron app with live reload against local source |
| `make dev-web` | run the web SPA with live reload against local source |
| `make server` + `make app` | (re)install the desktop server from the configured branch, then launch |
| `make server-local` + `make app-local` | install the desktop server from **local uncommitted source**, then launch |
| `make pack-local` | build the macOS `.app` from local uncommitted source (no push needed) |
| `make refs` | show which refs the next run will use |
| `make baseline` | reset submodules to the pinned commits |
| `make pin` | record the current submodule commits as the superproject's pins (one deliberate commit) |

Submodules are configured with `ignore = all`, so your branch work never shows up as superproject changes — the parent `git status` stays clean. Pins move **only** via `make pin`. See [`CLAUDE.md`](CLAUDE.md) for the full workflow.
