# rtk-ai/rtk

CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

## installation

**macOS, and Linux with Homebrew**

```bash
brew install rtk
```

**Windows, with winget**

```bash
winget install rtk-ai.rtk
```

**Linux, macOS or WSL, with the install script**

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

**Then plug it into your agent**

```bash
rtk init -g                      # Claude Code; every other agent: see "Works in your agent"
```

Restart your agent. That's it: when it runs `git status`, RTK runs `rtk git status` and the agent reads a 3-line summary instead of 40 lines. Nothing to learn, nothing to call, and upgrading RTK never changes this.

> Another project named "rtk" exists on crates.io. Check you have this one: `rtk gain` must show the savings dashboard, not "command not found".
>
> Cargo, pre-built binaries, native Windows, WSL and uninstall: **[Installation guide](https://www.rtk-ai.app/docs/getting-started/installation/)** · per-agent setup and `--dry-run`: **[Quick Start](https://www.rtk-ai.app/docs/getting-started/quick-start/)**

<br>

## Measure it: `rtk gain`

Every command RTK touches is counted on your machine. One command shows what it saved, today and since you installed it.

```bash
rtk gain                        # Summary stats
rtk gain --graph                # ASCII graph (last 30 days)
rtk gain --history              # Recent command history
rtk gain --daily                # Day-by-day breakdown
rtk gain --all --format json    # JSON export for dashboards

rtk discover                    # Find missed savings opportunities
rtk discover --all --since 7    # All projects, last 7 days

rtk session                     # Show RTK adoption across recent sessions
```

**What the numbers mean.** The compressor reduces the **command output** your agent reads, which is one part of the input tokens, which are one part of the bill: a 90% cut in command output is not a 90% cut in cost. Token counts are estimated as `bytes / 4`, so the percentages are reliable and the absolute numbers are approximate.

After a week of data, `rtk gain` ends with one line about RTK Pro, at most once a day and only on a terminal. `pro_hint = false` under `[display]` in `config.toml` turns it off.

> Full explanation: [How RTK Savings Work](docs/guide/resources/savings-explained.md) · attribution, the live dashboard and export formats: **[Token Savings Analytics](https://www.rtk-ai.app/docs/analytics/gain/)**

<br>

## Out of the box: the bash compressor

The part 85k developers starred. Built by 200+ contributors, written against real command output, and every filter has to cut at least 20% to ship.

<p align="center">
  <img src=".github/assets/before-after.png" alt="cargo test on a 48-test crate: 71 lines of raw output on the left; on the right, the 11 lines the agent reads with rtk: the failing test's panic, assertion and location, the pass/fail summary, and an rtk recall line to get the full output back">
</p>

| Operation | What the agent reads |
|-----------|----------------------|
| `cargo test` / `npm test` / `pytest` / `go test` | Failures only, with their assertion; passing tests collapsed to a count |
| `git status` / `git diff` / `git log` | Compact status, reduced diff context, one line per commit |
| `git add/commit/push` | A confirmation line instead of progress output |
| `ls` / `tree` / `grep` / `rg` | Trees with counts, matches grouped by file, long lines cut |
| `ruff check` / `eslint` / `cargo clippy` | Grouped by rule and file |
| `docker ps` / `kubectl` | Essential fields only |

100+ commands across Git, GitHub CLI, Cargo/Rust, JavaScript (npm, pnpm, vitest, jest, tsc, Next.js, Angular, Playwright, Prisma), Python (ruff, pytest, mypy, pip), Go (go test, golangci-lint), Ruby, .NET, JVM (Gradle, Maven), PHP, Docker, Kubernetes, AWS, Terraform, and the file/search builtins. Every command and its filter: **[What RTK Optimizes](https://www.rtk-ai.app/docs/resources/what-rtk-covers/)**

**Three promises**

- **Never blocks.** If a 
