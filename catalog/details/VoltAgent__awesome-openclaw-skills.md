# VoltAgent/awesome-openclaw-skills

The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞

## installation

#### OpenClaw CLI

```bash
openclaw skills install <skill-slug>
```

#### ClawHub CLI

Or with the ClawHub CLI, for registry-managed skill folders outside a full OpenClaw workspace:

```bash
npx clawhub install <skill-slug>
```

#### Manual Installation

Copy the skill folder to one of these locations:

| Location | Path |
|----------|------|
| Global | `~/.openclaw/skills/` |
| Workspace | `<project>/skills/` |

Priority: Workspace > Local > Bundled

#### Alternative

You can also paste the skill's GitHub repository link directly into your assistant's chat and ask it to use it. The assistant will handle the setup automatically in the background.

## features

OpenClaw's public registry (ClawHub) hosts thousands of community-built skills. This awesome list curates the best of them. Here's what we filtered out:

| Filter | Excluded |
|--------|----------|
| Possibly spam — bulk accounts, bot accounts, test/junk | 4,065 |
| Duplicate / Similar name | 1,040 |
| Low-quality or non-English descriptions | 851 |
| Crypto / Blockchain / Finance / Trade | 886 |
| Malicious — identified by security audits published by researchers (excluding VirusTotal) | 373 |
| **Total not taken from OpenClaw's official skill registry** | **7,215** |


#### Want to add a skill?

This list only includes skills that are **already published** on [ClawHub](https://clawhub.ai), OpenClaw's public skills registry. We do not accept links to personal repos, gists, or any other external source. If your skill isn't on ClawHub yet, publish it there first.

Include the ClawHub link for your skill (e.g. `https://clawhub.ai/steipete/slack`) in your PR description — the `clawskills.sh` listings are managed by us separately. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## configuration

As you add more skills, custom code, and connected services, your OpenClaw setup accumulates secrets, file access, and tool permissions that are easy to lose track of. You can review these by hand, or run a continuous audit that surfaces misconfigurations and over-broad permissions before they become a problem.

<a href="https://trent.ai/openclaw/?utm_source=github&utm_medium=referral&utm_campaign=volt-agent">
<img src="https://cdn.voltagent.dev/awesome-repo/trentclaw-banner.png" alt="trentclaw"  /><br/>
trentclaw: audits your OpenClaw config, installed skills and custom code, then returns fixes as diffs. Install with: openclaw skills install trentclaw
</a>
