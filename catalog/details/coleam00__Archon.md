# coleam00/Archon

The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

## features

When you ask an AI agent to "fix this bug", what happens depends on the model's mood. It might skip planning. It might forget to run tests. It might write a PR description that ignores your template. Every run is different.

Archon fixes this. Encode your development process as a workflow. The workflow defines the phases, validation gates, and artifacts. The AI fills in the intelligence at each step, but the structure is deterministic and owned by you.

- **Repeatable** - Same workflow, same sequence, every time. Plan, implement, validate, review, PR.
- **Isolated** - Every workflow run gets its own git worktree. Run 5 fixes in parallel with no conflicts.
- **Fire and forget** - Kick off a workflow, go do other work. Come back to a finished PR with review comments.
- **Composable** - Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation, review). The AI only runs where it adds value.
- **Portable** - Define workflows once in `.archon/workflows/`, commit them to your repo. They work the same from CLI, Web UI, Slack, Telegram, or GitHub.

## What It Looks Like

Here's an example of an Archon workflow that plans, implements in a loop until tests pass, gets your approval, then creates the PR:

```yaml
# .archon/workflows/build-feature.yaml
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"

  - id: implement
    depends_on: [plan]
    loop:                                      # AI loop - iterate until done
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
      fresh_context: true                      # Fresh session each iteration

  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"                   # Deterministic - no AI

  - id: review
    depends_on: [run-tests]
    prompt: "Review all changes against the plan. Fix any issues."

  - id: approve
    depends_on: [review]
    loop:                                      # Human approval gate
      prompt: "Present the changes for review. Address any feedback."
      until: APPROVED
      interactive: true                        # Pauses and waits for human input

  - id: create-pr
    depends_on: [approve]
    prompt: "Push changes and create a pull request"
```

Tell your coding agent what you want, and Archon handles the rest:

```
You: Use archon to add dark mode to the settings page

Agent: I'll run the archon-idea-to-pr workflow for this.
       → Creating isolated worktree on branch archon/task-dark-mode...
       → Planning...
       → Implementing (task 1/4)...
       → Implementing (task 2/4)...
       → Tests failing - iterating...
       → Tests passing after 2 iterations
       → Code review complete - 0 issues
       → PR ready: https://github.com/you/project/pull/47
```

## Previous Version

Looking for the original Python-based Archon (task management + RAG)? It's fully preserved on the [`archive/v1-task-management-rag`](https://github.com/coleam00/Archon/tree/archive/v1-task-management-rag) branch.

## installation

> **Most users should start with the [Full Setup](#full-setup-5-minutes)** - it walks you through credentials, installs the Archon skill into your projects, and gives you the web dashboard.
>
> **Already have Claude Code and just want the CLI?** Jump to the [Quick Install](#quick-install-30-seconds).

### Full Setup (5 minutes)

Clone the repo and use the guided setup wizard. This configures credentials, platform integrations, and copies the Archon skill into your target projects.

<details>
<summary><b>Prerequisites</b> - Bun, Claude Code, and the GitHub CLI</summary>

**Bun** - [bun.sh](https://bun.sh)

```bash
# macOS/Linux
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
irm bun.sh/install.ps1 | iex
```

**GitHub CLI** - [cli.github.com](https://cli.github.com/)

```bash
# macOS
brew install gh

# Windows (via winget)
winget install GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

**Claude Code** - [claude.ai/code](https://claude.ai/code)

```bash
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

</details>

```bash
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```

Then say: **"Set up Archon"**

The setup wizard walks you through everything: CLI installation, authentication, platform selection, and copies the Archon skill to your target repo.

### Quick Install (30 seconds)

Already have Claude Code set up? Install the standalone CLI binary and skip the wizard.

**macOS / Linux**
```bash
curl -fsSL https://archon.diy/install | bash
```

> **x64 compatibility:** The macOS/Linux quick install requires AVX2 on x64
> CPUs. Older Intel/AMD hardware and virtual machines that mask AVX2 should use
> the [source installation guide](https://archon.diy/getting-started/installation/#from-source).
> ARM64 quick installs are unaffected.

**Windows (PowerShell)**
```powershell
irm https://archon.diy/install.ps1 | iex
```

**Homebrew**
```bash
brew install coleam00/archon/archon
```

> **Compiled binaries need a `CLAUDE_BIN_PATH`.** The quick-install binaries
> don't bundle Claude Code. Install it separately, then point Archon at it:
>
> ```bash
> # macOS / Linux / WSL
> curl -fsSL https://claude.ai/install.sh | bash
> export CLAUDE_BIN_PATH="$HOME/.local/bin/claude"
>
> # Windows (PowerShell)
> irm https://claude.ai/install.ps1 | iex
> $env:CLAUDE_BIN_PATH = "$env:USERPROFILE\.local\bin\claude.exe"
> ```
>
> Or set `assistants.claude.claudeBinaryPath` in `~/.archon/config.yaml`.
> The Docker image ships Claude Code pre-installed. See [AI Assistants → Binary path configuration](https://archon.diy/getting-started/ai-assistants/#binary-path-configuration-compiled-binaries-only) for details.

### Start Using Archon

Once you've completed either setup path, go to your project and start working:

```bash
cd /path/to/your/project
claude
```

```
Use archon to fix issue #42
```

```
What archon workflows do I have? When would I use each one?
```

The coding agent handles workflow selection, branch naming, and worktree isolation for you. Projects are registered automatically the first time they're used.

> **Important:** Always run Claude Code from your target repo, not from the Archon repo. The setup wizard copies the Archon skill into your project so it works from there.

## Web UI

Archon includes a web dashboard for chatting with your coding agent, running workflows, and monitoring activity. Binary installs: run `archon serve` to download and start the web UI in one step. From source: ask your coding agent to run the frontend from the Archon repo, or run `bun run dev` from the repo root yourself.

Register a project by clicking **+** next to "Project" in the chat sidebar - enter a GitHub URL or local path. Then start a conversation, invoke workflows, and watch progress in real time.

**Key pages:**
- **Chat** - Conversation interface with real-time streaming and tool call visualization
- **Dashboard** - 
