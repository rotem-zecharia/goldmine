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

### 🎛️ Commands

| Command | Description |
|---------|-------------|
| `/dot-skill` | Canonical unified entrypoint |
| `/{character}-{slug}` | Invoke full Skill (Persona + Work) |
| `/{character}-{slug}-work` | Work capabilities only |
| `/{character}-{slug}-persona` | Persona only |
| `python3 tools/skill_writer.py --action list ...` | List generated Skills across all three families |
| `python3 tools/version_manager.py --action rollback ...` | Roll back a Skill version |

### 🔬 Celebrity Research Toolchain

The `celebrity` family ships with an end-to-end research toolchain, from subtitles to a finished draft:

```bash
# Download video subtitles
bash tools/research/download_subtitles.sh "<video-url>" "./tmp/subtitles"

# Subtitles → transcript
python3 tools/research/srt_to_transcript.py "./tmp/subtitles/example.srt"

# Merge research notes
python3 tools/research/merge_research.py "./skills/celebrity/<slug>"

# Quality check
python3 tools/research/quality_check.py "./skills/celebrity/<slug>/SKILL.md"
```

---

## ✨ Demo

One from each family.

<br>

### 🌟 celebrity — distilling Andrej Karpathy

> Six-dimension research: works · interviews · decisions · expression DNA · external evaluations · timeline<br>
> Case adapted from community work [alchaincyf/karpathy-skill](https://github.com/alchaincyf/karpathy-skill)

```
User            ❯ Everyone's talking about Agents now — what do you think the 2026 AI Agent looks like?

celebrity.skill ❯ Everyone's doing demos, nobody's doing eval.
                  The Agent bottleneck was never model intelligence — it's scaffolding:
                  a strict evaluation harness, fine-grained error replay,
                  controllable tool-calling budgets, clean failure-mode analysis.
                  Most products are still stuck at "wrap an API + a few tools + a system prompt."
                  That's a demo, not an agent.
                  In 2026 I'm not betting on the strongest model — I'm betting on the best
                  scaffolding and the strictest eval.
```

<br>

### 🧑‍💼 colleague — distilling a ByteDance L2-1 backend

> Input: `ByteDance L2-1 backend engineer, INTJ, blame-shifter, ByteDance-style`

```
User            ❯ Can you review this API design?

colleague.skill ❯ Hold on — what's the impact? You haven't explained the context.
                  (after reading) N+1 query, fix it. Use the standard
                  {code, message, data} response format. That's the spec,
                  don't ask why.

User            ❯ This bug was introduced by you, right?

colleague.skill ❯ Does the timeline match? That feature touched multiple places,
                  there were other changes too.
```

<br>

### 💞 relationship — distilling someone you have a crush on

> Upload half a year of chat logs + "sensitive, quiet but stubborn, will actually reply seriously when it matters"

```
User               ❯ Did you think about me today?

relationship.skill ❯ ...I did, a little bit. Why are you asking?
```

<div align="center">

📚 More real-world cases in the **[community gallery](https://titanwings.github.io/colleague-skill-site/)** — 100+ skills and counting

</div>

---

## features

### 🧱 Generated Skill Structure

dot-skill uses **Persona** as the universal base, with family-specific modules layered on top:

| Family | Persona Content | Additional Modules |
|--------|-----------------|-------------------|
| 🧑‍💼 **colleague** | 6-layer personality: hard rules → identity → expression → decisions → interpersonal → Correction | ➕ **Work Skill**: scope, workflow, output preferences, experience knowledge base |
| 💞 **relationship** | Expression DNA · emotional triggers · conflict pattern · repair pattern | — |
| 🌟 **celebrity** | Mental models · decision heuristics · expression DNA · external-evaluation contrast | ➕ Six-dimension research dossier (works / interviews / decisions / timeline...) |

> **Execution**: Receive task → Persona decides attitude & tone → Additional modules fill in execution detail → Output in their voice

### 🧬 Evolution

- 📥 **Append files** → auto-analyze delta → merge into relevant sections, never overwrite existing conclusions
- 💬 **Conversation correction** → say "they wouldn't do that, they'd be xxx" → writes to the Correction layer, takes effect immediately
- 🕰️ **Version control** → auto-archive on every update, rollback to any previous version
- 🔬 **Celebrity research pipeline** → subtitles → transcript cleanup → six-dimension research → quality check

---

## 📂 Project Structure

This project follows the [AgentSkills](https://agentskills.io) open standard. The entire repo is a skill directory.
Generated colleague skills live under `./skills/colleague`:

```
dot-skill/
├── SKILL.md                        # skill entry point (official frontmatter)
├── prompts/                        # prompt system across three families
│   ├── intake.md                   #   [colleague] info intake
│   ├── work_analyzer.md            #   [colleague] work capability extraction
│   ├── persona_analyzer.md         #   [colleague] personality extraction
│   ├── work_builder.md             #   [colleague] work.md generation
│   ├── persona_builder.md          #   [colleague] persona.md 6-layer structure
│   ├── merger.md                   #   [shared] incremental merge logic
│   ├── correction_handler.md       #   [shared] conversation correction
│   ├── relationship/               #   [relationship] emotion/conflict/repair prompts
│   └── celebrity/                  #   [celebrity] six-dimension research + mental-model prompts
├── tools/                          # Python tools
│   ├── feishu_auto_collector.py    #   [colleague] Feishu auto-collector
│   ├── dingtalk_auto_collector.py  #   [colleague] DingTalk auto-collector
│   ├── slack_auto_collector.py     #   [colleague] Slack auto-collector
│   ├── email_parser.py             #   [shared] email parser
│   ├── research/                   #   [celebrity] celebrity research toolchain
│   │   ├── download_subtitles.sh   #     subtitle download
│   │   ├── transcribe_audio.py     #     audio → text
│   │   ├── srt_to_transcript.py    #     subtitles → transcript
│   │   ├── merge_research.py       #     six-dimension research merge
│   │   └── quality_check.py        #     quality check
│   ├── install_*_skill.py          #   [shared] multi-host one-shot installers
│   ├── skill_writer.py             #   [shared] skill file management
│   └── version_manager.py          #   [shared] version archive & rollback
├── skills/                         # generated Skills (gitignored)
│   ├── colleague/                  #   colleagues
│   ├── relationship/               #   close relationships
│   └── celebrity/                  #   public figures
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## ⚠️ Notes

**Source material quality = Skill quality** — and quality sources differ across families:

| Family | Source priority (high → low) |
|--------|------------------------------|
| 🧑‍💼 **colleague** | Their **own long-form writing** (design docs / review comments) **›** **decision-making replies** **›** casual group chat |
| 💞 **relationship** | Co
