# titanwings/colleague-skill

将冰冷的离别化为温暖的 Skill，欢迎加入数字生命1.0！Transforming cold farewells into warm skills? It's giving rebirth era. Welcome to Digital Life 1.0. 🫶

## installation

It's 2026 — you have an Agent, let it install itself. Open your Claude Code / Hermes / OpenClaw / Codex / DeepSeek Harness and hand it this line:

> Install the dot-skill skill for me: `https://github.com/titanwings/colleague-skill`

The Agent will detect the current host's skills directory, clone the repo, and register the entrypoint. Once done, type `/dot-skill` in any host to launch.

<details>
<summary><b>🛠️ Want to install it yourself? Click for paths</b></summary>

<br>

```bash
git clone https://github.com/titanwings/colleague-skill <TARGET>
```

| Host | `<TARGET>` path |
|------|-----------------|
| Claude Code | `~/.claude/skills/dot-skill` |
| OpenClaw | `~/.openclaw/workspace/skills/dot-skill` |
| Codex | `~/.codex/skills/dot-skill` |
| DeepSeek Harness | `~/.dsh/skills/dot-skill` (global) or `.dsh/skills/dot-skill` (project) |
| Hermes | After clone, run `python3 tools/install_hermes_skill.py --force` |

</details>

Generated character Skills can be published with `tools/install_claude_generated_skill.py`,
`tools/install_openclaw_generated_skill.py`, and `tools/install_codex_generated_skill.py`.
On DeepSeek Harness, place a generated Skill directory under `~/.dsh/skills/<skill-name>` or the current project's `.dsh/skills/<skill-name>`; no host-specific wrapper is required.

> For Feishu/DingTalk auto-collection credentials, publishing a generated character Skill to any host, Windows-specific handling, etc., see **[Detailed Install Guide (INSTALL.md)](INSTALL.md)**

---

## tools

In the host where dot-skill is installed, launch it — type `/dot-skill`, or just tell your Agent "start dot-skill".

It first asks which family you want to distill: `colleague` · `relationship` · `celebrity`.

Then enter alias, basic profile, personality tags, and pick a data source. All fields can be skipped — even a description alone can generate a Skill.

Once created, invoke the generated Skill with `/{character}-{slug}`.
