# affaan-m/ECC

The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

## installation

Run these commands inside Claude Code:

```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

That installs ECC's skills, agents, commands, and plugin-managed hooks. If you choose this path, stop there. Do not also run a full manual install into Claude Code.

> Guided package setup is coming in `ecc-universal` 2.2.0. Use the native
> Claude plugin commands above while npm remains on 2.1.0.

<div align="center">

<table aria-label="ECC primary links">
<tr>
<td width="33%" align="center">
  <a href="https://ecc.tools/pricing">
    <img src="assets/images/community/ecc-tools-mark.svg" height="42" alt="ECC Tools" /><br />
    <strong>ECC Pro + GitHub App</strong>
  </a><br />
  <sub><a href="https://github.com/apps/ecc-tools">Install free</a> · <a href="https://ecc.tools/pricing">Private repos from $19/seat/mo</a></sub>
</td>
<td width="33%" align="center">
  <a href="https://github.com/sponsors/affaan-m">
    <img src="assets/images/community/heart.svg" height="42" alt="" /><br />
    <strong>Sponsor ECC</strong>
  </a><br />
  <sub>Fund the open-source project</sub>
</td>
<td width="33%" align="center">
  <a href="https://discord.gg/36yGMHGFbR">
    <img src="assets/images/community/discord.svg" height="42" alt="Discord" /><br />
    <strong>Community</strong>
  </a><br />
  <sub>Discord · Q&amp;A · Show and Tell</sub>
</td>
</tr>
</table>

</div>

<sub>**OSS stays free.** This repo is MIT-licensed forever. ECC Pro is the hosted GitHub App for private repos. <a href="https://github.com/sponsors/affaan-m">Sponsors</a> and <a href="https://ecc.tools/pricing">Pro subscribers</a> fund the work. That's why a single maintainer ships weekly across 7 harnesses.</sub>

<div align="center">

<sub><strong>Partners &amp; sponsors</strong></sub>

<p align="center" aria-label="Partners and sponsors">
  <a href="https://www.coderabbit.ai" title="CodeRabbit"><img src="assets/images/sponsors/coderabbit.png" height="54" alt="CodeRabbit" /></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.greptile.com/go/ecc" title="Greptile"><img src="assets/images/sponsors/greptile.png" height="54" alt="Greptile" /></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.atlascloud.ai/?utm_source=github&amp;utm_medium=link&amp;utm_campaign=ECC" title="Atlas Cloud"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/images/sponsors/atlascloud-dark.svg" /><img src="assets/images/sponsors/atlascloud.svg" width="154" alt="Atlas Cloud" /></picture></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.moonshot.ai" title="Moonshot AI - Kimi"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/images/sponsors/moonshot-dark.png" /><img src="assets/images/sponsors/moonshot.png" width="132" alt="Moonshot AI - Kimi" /></picture></a>&nbsp;&nbsp;&nbsp;
  <a href="https://compute.itomarkets.com" title="Itô Markets"><picture><source media="(prefers-color-scheme: light)" srcset="assets/images/sponsors/ito-transparent-light.png" /><img src="assets/images/sponsors/ito-transparent.png" width="96" alt="Itô Markets" /></picture></a>
</p>

<sub><strong>Community sponsors:</strong> <a href="https://github.com/mikejmorgan-ai">Mike Morgan</a> · <a href="https://github.com/jasonwu513">@jasonwu513</a> · <a href="https://github.com/1anter">@1anter</a> · <a href="https://github.com/massimotodaro">@massimotodaro</a> · <a href="https://github.com/meadmccabe">@meadmccabe</a></sub>

<sub><a href="https://github.com/sponsors/affaan-m"><strong>Become a Sponsor</strong></a> · <a href="SPONSORS.md">Sponsor Tiers</a> · <a href="SPONSORING.md">Sponsorship Program</a></sub>

</div>

<p align="center"><a href="#install-ecc">Jump to install ↓</a></p>

## tools

- **Python/Django support**: Django patterns, security, TDD, and verification skills
- **Java Spring Boot skills**: Patterns, security, TDD, and verification for Spring Boot
- **Session management**: `/sessions` command for session history
- **Continuous learning v2**: Instinct-based learning with confidence scoring, import/export, evolution

See the full changelog in [Releases](https://github.com/affaan-m/ECC/releases).
</details>

## features

| Without a system                                        | With ECC                                                              |
| ------------------------------------------------------- | --------------------------------------------------------------------- |
| Plans disappear into chat history                       | Plans become editable artifacts before implementation starts          |
| "Please use TDD" is an instruction the model may forget | TDD becomes a gated RED -> GREEN -> REFACTOR workflow with evidence   |
| The same context writes and reviews the code            | A fresh-context reviewer looks for regressions and blind spots        |
| Memory means saving an enormous transcript              | Sessions are distilled into summaries, instincts, and reusable skills |
| Quality checks depend on reminders                      | Hooks can enforce deterministic checks outside the prompt             |
| Agent configuration is trusted by default               | AgentShield scans the harness itself as an attack surface             |

## configuration

npx ecc-agentshield init
```

**What it scans:** CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories: secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

**The `--opus` flag** runs three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

**Output formats:** Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

Use `/security-scan` in Claude Code to run it, or add to CI with the [GitHub Action](https://github.com/affaan-m/agentshield).

[GitHub](https://github.com/affaan-m/agentshield) | [npm](https://www.npmjs.com/package/ecc-agentshield)
</details>

<details>
<summary><strong>Continuous Learning v2: instincts</strong></summary>

The instinct-based learning system automatically learns your patterns:

```bash
/instinct-status        # Show learned instincts with confidence
/instinct-import <file> # Import instincts from others
/instinct-export        # Export your instincts for sharing
/evolve                 # Cluster related instincts into skills
```

See `skills/continuous-learning-v2/` for full documentation. Keep `continuous-learning/` only when you explicitly want the legacy v1 Stop-hook learned-skill flow.
</details>

## requirements

<details>
<summary><strong>Claude Code CLI version + hooks auto-loading behavior</strong></summary>
