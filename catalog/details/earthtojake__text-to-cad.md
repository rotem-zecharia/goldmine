# earthtojake/text-to-cad

A library of agent skills for CAD, CAE and CAM

## installation

For production use, install or clone from `main`; that branch contains the
generated skill outputs needed by provider installers.

### Skills

Install text-to-cad with the Skills CLI:

```bash
npx skills add earthtojake/text-to-cad
```

This is the preferred installation path. It installs the individual skills
directly for supported agents.

**Use the same command to update.** `add` re-fetches the package and overwrites
what is already installed, so it both refreshes existing skills and installs any
skill added in a newer release. `npx skills update` only refreshes skills already
in your lockfile, so it silently misses new ones — which matters here, because
releases do add skills.

Neither command removes a skill that was retired upstream; drop one with
`npx skills remove <skill>` if you need to.

(`npx skills install …` still works — it is an undocumented alias for `add`.)

### Plugins

Provider-native plugin installs are also available for Codex, Claude Code, and
Grok Build:

```bash
# Codex (requires Codex 0.142.0 or newer)
codex plugin marketplace add earthtojake/text-to-cad
codex plugin add cad@text-to-cad
```

Codex resolves this repository-root plugin only from 0.142.0 onward. On older
versions the plugin is skipped silently and never appears in `codex plugin list`;
upgrade with `npm install -g @openai/codex@latest`.

```bash
# Claude Code
claude plugin marketplace add earthtojake/text-to-cad
claude plugin install cad@text-to-cad
```

Grok Build uses the existing `.claude-plugin/marketplace.json`; there is no
separate Grok plugin manifest.

```bash
# Grok Build
grok plugin install earthtojake/text-to-cad --trust
grok plugin enable cad
```

Restart your agent if newly installed skills do not appear. For local
development, branch from `develop`, open PRs against `develop`, and use the symlink
workflow in [CONTRIBUTING.md](CONTRIBUTING.md).

## 🛠️ Contributing

Development happens from the `develop` branch; open PRs against `develop`, not `main`.
For local contribution workflow, skill linking, and validation guidance, see
[CONTRIBUTING.md](CONTRIBUTING.md).
