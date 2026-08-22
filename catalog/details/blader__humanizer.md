# blader/humanizer

Agent skill that removes signs of AI-generated writing from text

## tools

Call the skill directly:

```
/humanizer

[paste your text here]
```

Or ask in plain language:

```
Please humanize this text: [your text]
```

To rewrite a file, give Humanizer its path:

```
Humanize the prose in docs/launch-post.md
```

## installation

Install Humanizer with the Skills CLI:

```bash
npx skills add blader/humanizer --global
```

Leave off `--global` to install Humanizer only in the current project. Add `--agent <name>` or `--agent '*'` to choose which agents receive it, then reload their skills.

Claude Code 2.1.142 or newer can install the plugin instead:

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

The plugin command is `/humanizer:humanizer`.

In Claude Desktop, download this repository as a ZIP and upload it as a skill.

For a manual install, copy `SKILL.md` into the agent's skill folder.
