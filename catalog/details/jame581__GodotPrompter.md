# jame581/GodotPrompter

Agentic skills framework for Godot 4.x. Domain-specific skills for AI coding agents (Claude Code, Copilot, Antigravity, Cursor)

## installation

### Claude Code (recommended)

```bash
# Add the marketplace
claude plugins marketplace add jame581/skillsmith

# Install the plugin
claude plugins install godot-prompter@skillsmith
```

Or install from a local clone:

```bash
git clone https://github.com/jame581/GodotPrompter.git
claude plugins marketplace add ./GodotPrompter
claude plugins install godot-prompter@godot-prompter
```

Then start a new session and ask:

```
"I'm starting a new Godot 4.3 project. How should I organize it?"
```

The agent loads the `godot-project-setup` skill and provides a complete directory structure, autoload setup, and .gitignore — not generic advice.

### Grok Build

```bash
grok plugin install jame581/GodotPrompter --trust
grok plugin enable godot-prompter
```

Pin to a release:

```bash
grok plugin install jame581/GodotPrompter@v1.11.0 --trust
grok plugin enable godot-prompter
```

### Antigravity CLI (`agy`)

```bash
agy plugin install https://github.com/jame581/GodotPrompter
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add jame581/skillsmith
copilot plugin install godot-prompter@skillsmith
```

### Cursor

```
/add-plugin godot-prompter
```

Or clone and place in your project — Cursor reads `.cursor-plugin/plugin.json`.

### Codex

```bash
git clone https://github.com/jame581/GodotPrompter.git ~/.codex/godot-prompter
mkdir -p ~/.agents/skills
ln -s ~/.codex/godot-prompter/skills ~/.agents/skills/godot-prompter
```

See `.codex/INSTALL.md` for Windows instructions.

### OpenCode

Add to `opencode.json`:

```json
{
  "plugin": ["godot-prompter@git+https://github.com/jame581/GodotPrompter.git"]
}
```

See `.opencode/INSTALL.md` for details.

## How It Works

### Automatic activation

GodotPrompter registers a SessionStart hook that injects its skill-routing card when it detects
a Godot project. It looks for `project.godot` up to four directories above your working
directory **and up to three below it**, so the common monorepo layout — docs and tooling at the
repo root, the engine project in `source/`, `game/`, or `godot/` — is detected when you open a
session at the root. Vendored `addons/` and dot-directories are skipped, so a plugin's bundled
demo project is never mistaken for yours. In any other repository the hook does nothing at all.

The hook reads only your project's `project.godot` and its own state file under your home
directory, makes no network requests, and writes nothing. If bash is unavailable on Windows it
exits silently and the plugin behaves exactly as it did before v1.13.0.

Verified end-to-end on Claude Code and GitHub Copilot CLI. Cursor's registration ships but is
not yet confirmed. Codex and Antigravity have no hook mechanism and continue to load the
bootstrap through `AGENTS.md` / `GEMINI.md`.

> The hook covers your session. **Subagents do not receive it** — `SessionStart` does not fire on
> subagent dispatch. When none of a Godot project's agent instructions files has a
> `## GodotPrompter` section, the agent offers once to add one, since that is what subagents read.
> `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md` and the `.claude/rules/`
> and `.cursor/rules/` directories all count — whichever agent they belong to — and the offer names
> the file your repo already keeps, so an agent-agnostic project is never asked to start a
> `CLAUDE.md` it does not want. It never adds the section silently, and a refusal is remembered in
> `~/.godot-prompter/state/` so you are asked once, not at every session start. Changed your mind?
> Just ask the agent to add the section; nothing has to be un-set by hand.

### Mentor mode

Say "teach me as we go" in a Godot project and GodotPrompter switches to teaching delivery: the
Godot concept and why that node, the editor setup, annotated GDScript and C#, what to verify when
you run it, and one suggested next step. It wraps the domain skills rather than replacing them,
so the guidance stays version-checked.

Your preference is remembered per pro
