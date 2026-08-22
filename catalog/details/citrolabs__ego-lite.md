# citrolabs/ego-lite

The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero conf

## installation

ego lite runs on macOS today. Windows and Linux are on the [roadmap](https://lite.ego.app/roadmap).

### 1. Install

Pick whichever fits your flow.

**1.1 Download the macOS app**

<a href="https://cdn.ego.app/setup/macos/arm64/egolite-Y7MbxKIuhzFB.dmg"><img src="https://img.shields.io/badge/⬇%20Apple%20Silicon-.dmg-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download ego lite for Apple Silicon" /></a>
<a href="https://cdn.ego.app/setup/macos/x64/egolite-Y7MbxKIuhzFB.dmg"><img src="https://img.shields.io/badge/⬇%20Intel-.dmg-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download ego lite for Intel" /></a>

Click to download, then open it to install. Either way, ego lite adds the `ego-browser` skill to every agent's skills directory on your machine.

**1.2 Add the skill with npx**

Install just the `ego-browser` skill:

```bash
npx skills add citrolabs/ego-lite
```

The first time your agent runs a browser task, it walks you through installing the ego lite app.

**1.3 Let your agent set it up**

Paste this into your agent:

```
Set up ego lite for me: https://github.com/citrolabs/ego-lite

Read `skills/ego-browser/references/install.md` and follow the steps to install ego lite.
```

On first launch, ego lite asks one question, whether to migrate your Chrome data. Say yes and your agent inherits your existing logins, cookies, extensions, and bookmarks.

### 2. Run your first task

In your agent CLI, type `/ego-browser` followed by a space, then describe what you want in plain language:

```
ego-browser follow @ego_agent on x.com for me
```

The agent picks up the `ego-browser` skill, opens the page in its own Space, reads a Snapshot, acts on the page, and reports back, all while your own tabs stay untouched.

Your browsing data stays on your device. ego lite only records whether you opted into Chrome migration during setup.

## Highlight of ego lite

| Feature | What it does |
|---|---|
| **Code base, not CLI base, for faster runs with fewer tokens on complex tasks** | The capabilities ego lite exposes to the agent are wrapped as JavaScript functions the agent calls directly. The agent gets to do what it does best: write code, composing a multi-step task into a single output instead of getting stuck in a "call two commands, look at the result, call two more commands" loop. Compared to the conventional CLI approach, complex workflows finish up to 2.5× faster with higher task success rates and far fewer tool calls per task. |
| **A dedicated Space for every agent** | ego lite gives each agent its own fully isolated Space. You browse up front, your agent works in the background, and they don't get in each other's way. You can see which Space has an agent running at any moment, and take it over or stop it whenever you want. |
| **Your agents multitask in Spaces, parallel workspaces inside the same browser** | Each Space gets its own AI agent or its own task, all running at the same time. Claude Code enriching 10 leads in 10 parallel Spaces. Codex scraping 5 competitor sites in 5 more. They don't collide or steal your tabs. Your mouse stays where you left it. |
| **The strongest page Snapshot on the market** | Thanks to kernel-level customization, ego lite produces the highest-quality page snapshots, the view text models rely on to "see" and act on a webpage. It reliably handles tough cases like deeply nested iframes, exactly where other approaches consistently break down. |
| **Any agent can drive it through `ego-browser`** | `ego-browser` is the connection layer between any agent CLI (Claude Code, Codex, Cursor, or a custom one) and ego lite. It exposes the browser as a set of in-page JavaScript tools: snapshot, fill, click, wait, navigate, capture. The agent writes a JavaScript snippet calling those tools, and `ego-browser` runs it on the page in one pass. |
| **Experience accumulation that makes your agent faster the more you use it** *(coming soon)* | Most of an agent's time on browser tasks goes to
