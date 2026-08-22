# Hmbown/CodeWhale

Open-source coding agent for your terminal, built in Rust and on a journey of continuous community improvement. Issues and PRs welcome.

## installation

```bash
npm install -g codewhale
codewhale
```

The first run helps you connect a provider or stay offline. Codewhale also
supports Cargo, Docker, Nix, Scoop, prebuilt archives, Android/Termux, and a CNB
mirror. See [the installation guide](docs/INSTALL.md).

## features

- **Use the model you want.** Connect hosted providers or local models through
  Ollama, vLLM, or SGLang. Switch provider and model with `/model`.
- **Stay in control.** Plan is read-only. Ask, Auto-Review, and Full Access make
  approval behavior visible. `/undo` reverts the last turn and `/restore`
  returns the workspace to an earlier snapshot.
- **Keep long work organized.** Save sessions, set a durable `/goal`, review
  workflows before they run, and coordinate agents without turning their
  internal instructions into your transcript.
- **Extend the agent you already have.** Connect MCP servers and skills,
  configure hooks, and keep agent roles as readable files in your project or
  personal settings.

Run `/help` in the TUI for commands and keyboard shortcuts.
