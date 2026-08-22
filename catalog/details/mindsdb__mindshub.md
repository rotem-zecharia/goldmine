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

## Deploy anywhere

Cowork is built for flexible deployment — **cloud, VPC, on-prem, air-gapped, and hybrid** infrastructure — so you keep full control over your infrastructure, models, permissions, and data.

## Help & support

- **Ask a question** — join the [Discord community](https://mindshub.ai/discord).
- **Report a bug** — open a [GitHub issue](https://github.com/mindsdb/minds/issues) with reproduction steps.
- **Read the docs** — guides, setup, and the API at [docs.mindshub.ai](https://docs.mindshub.ai/?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme).
- **Enterprise SLAs or custom deployments** — [contact the team](https://mindshub.ai/contact?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme).

## 🤝 Contribute

Cowork is open source and contributions are welcome — code, integrations, docs, bug reports, and feature ideas. Read the [docs](https://docs.mindshub.ai/?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme) to get set up, browse [open issues](https://github.com/mindsdb/minds/issues), and say hi on [Discord](https://mindshub.ai/discord).

## 🔒 Security

Found a security vulnerability? Please **don't** open a public issue. Report it privately through our [security policy](https://github.com/mindsdb/minds/security).

## 📚 Resources

- [Documentation](https://docs.mindshub.ai/?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme)
- [Blog](https://mindshub.ai/blog?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme)
- [Brand guidelines & press kit](https://mindshub.ai/press-kit?utm_source=github&utm_medium=repo-readme&utm_campaign=minds-readme)
- [Discord community](https://mindshub.ai/discord)

## 📄 License

This repository is released under the [MIT License](LICENSE). Bundled components are governed by their own licenses — see each submodule's repository for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
