# tmchow/illo-skill

illo skill — an AI agent skill that turns ideas and articles into original print-style editorial illustrations, starring a recurring mascot. 30+ characters packs, with ability to create your own.

## installation

**Recommended: use your platform's native plugin or skill manager.** These
lanes install the same `illo` skill, but they preserve the runtime's managed
update path. Use the generic `npx skills` installer only when your runtime
doesn't have a native lane yet.

| Platform | Install | Update |
| --- | --- | --- |
| **Claude Code** | `/plugin marketplace add tmchow/illo-skill` then `/plugin install illo@illo-skill` | `claude plugin update illo`, or enable marketplace auto-update |
| **Codex** | `codex plugin marketplace add tmchow/illo-skill` then `codex plugin add illo@illo-skill` | `codex plugin marketplace upgrade` |
| **Grok CLI** | `grok plugin marketplace add tmchow/illo-skill` then `grok plugin install tmchow/illo-skill --trust` | `grok plugin update illo` |
| **Grok Bot** | paste the prompt below into Grok Bot. | paste the prompt again after updates |
| **Gemini CLI** | `gemini extensions install https://github.com/tmchow/illo-skill` | `gemini extensions update illo` |
| **Copilot / GitHub CLI** | `gh skill install tmchow/illo-skill illo` (cross-agent via `--agent`) | `gh skill update illo` |
| **Hermes** | `hermes skills install tmchow/illo-skill/illo` | `hermes skills update illo` |
| **OpenClaw** | `openclaw skills install illo` | reinstall with the same command |
| **Cursor** | `npx skills add tmchow/illo-skill --skill illo` (Cursor Marketplace listing pending review) | re-run the installer |
| **Other agents / last resort** | `npx skills add tmchow/illo-skill --skill illo` | `npx skills update` |
