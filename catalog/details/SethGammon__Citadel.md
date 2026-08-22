# SethGammon/Citadel

The operating layer for Claude Code + OpenAI Codex: persistent project memory, intent routing, safety hooks, cost telemetry, and parallel agent fleets.

## installation

**Requires:** Claude Code or OpenAI Codex, Node.js 22+, and a git repository.

Citadel is installed through the plugin marketplace already built into your
coding agent. The commands below pin the complete `v1.3.5` release; if that tag
is not present on [GitHub Releases](https://github.com/SethGammon/Citadel/releases),
do not substitute floating `main`.

**Verified release · Project-local activation · Removable · No npm package**

### OpenAI Codex

Run these commands from the repository you want Citadel to manage:

```bash
codex plugin marketplace add SethGammon/Citadel --ref v1.3.5
codex plugin add citadel@citadel-local
```

Start a new Codex task, review Citadel through `/hooks`, then give it a real
request such as `/do review README.md`.

### Claude Code

Run these commands from the repository you want Citadel to manage:

```bash
claude plugin marketplace add SethGammon/Citadel@v1.3.5 --scope local
claude plugin install citadel@citadel-local --scope local
```

Run `/reload-plugins` if Claude Code is already open, then give Citadel a real
request such as `/do review README.md`.

### Prefer to have your agent install it?

Paste this into Claude Code or Codex. It explains both what Citadel is and the
boundary the installer must preserve:

```text
Citadel is an open-source operating layer for Claude Code and OpenAI Codex. It
adds one /do entry point, repository-local state that survives sessions,
guarded multi-step workflows, and reviewable evidence with explicit Needs You
and Resume boundaries.

Install Citadel v1.3.5 from https://github.com/SethGammon/Citadel using this
runtime's native plugin marketplace, then enable it for this repository. Use
project-local defaults and preserve removal evidence for every change. Do not clone main or change shared
configuration, sandbox settings, permissions, or user-wide settings without
asking me.

Only interrupt me for a platform-required trust or reload action, or for a real
configuration conflict. Verify the result, then tell me the single next action.
```

The platform owns plugin acquisition and executable-code trust. Citadel owns
bounded project state and recovery. Plans, digests, receipts, and doctor checks
remain available as evidence, but are not user chores on the normal path.

<details>
<summary><strong>Manual, offline, and high-assurance installation</strong></summary>

<br>

1. Open the [GitHub Releases](https://github.com/SethGammon/Citadel/releases)
   page and choose an explicit `vX.Y.Z` release.
2. Download `citadel-vX.Y.Z.tar.gz`, its `.manifest.json`, and its `.sha256`
   sidecar into one directory.
3. Compare the archive's SHA-256 with both published values before extraction.
   A missing asset or mismatch is a blocked install.
4. Extract the archive, then use its single `citadel-X.Y.Z/` directory as the
   immutable source for the governed adoption plan.

From the target repository, with `CITADEL_ROOT` pointing at that extracted
directory, the compact Linux/macOS form is below. Windows users should use the
quoted `$env:CITADEL_ROOT` PowerShell path in [Installation](INSTALL.md).

```bash
node "$CITADEL_ROOT/scripts/adopt.js" plan "$CITADEL_ROOT" \
  --target . --project-runtime codex \
  --out ../citadel-adoption.plan.json --json

node "$CITADEL_ROOT/scripts/adopt.js" apply ../citadel-adoption.plan.json \
  --confirm <plan-token> --json

node "$CITADEL_ROOT/scripts/adopt.js" doctor --target . --json
```

Use `--project-runtime claude` for Claude Code or `both` only when both runtime
projections are intentional. Runtime-specific enable steps are in
[Installation](INSTALL.md).

Keep every saved plan outside the target repository. Writing the plan inside
the target changes the preflight snapshot and causes apply to reject
`TARGET_DRIFT`.

</details>

For contributor testing only, a source checkout may use
`git clone --branch main https://github.com/SethGammon/Citadel.git`. That path
is development-only: it has no release trio or immutable version boundary and
must not be 
