# revfactory/harness

A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the skills they use.

## features

Harness leverages Claude Code's agent team system to decompose complex tasks into coordinated teams of specialized agents. Say "build a harness for this project" and it automatically generates agent definitions (`.claude/agents/`) and skills (`.claude/skills/`) tailored to your domain.

## installation

```shell

## tools

Trigger in Claude Code with prompts like:

```
Build a harness for this project
Design an agent team for this domain
Set up a harness
```

## requirements

- [Agent Teams enabled](https://code.claude.com/docs/en/agent-teams): `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
