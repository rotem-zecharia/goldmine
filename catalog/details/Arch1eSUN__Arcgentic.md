# Arch1eSUN/Arcgentic

Mechanical plan/dev/self-audit/external-audit gates for AI coding agents, with a configurable role-routing topology engine, an MCP-UI live status panel, and native-tooling Claude Code V2 dispatch. Cla

## installation

```bash
git clone https://github.com/Arch1eSUN/Arcgentic.git arcgentic
cd arcgentic
bash scripts/install-codex-local.sh --plugin-root .
```

Then start in a saved project workspace and ask:

```text
Use Arcgentic to build this idea: <your idea>
```

## tools

Current evidence:

- Codex V2 has been exercised in a real project workflow.
- V2 completion evidence is recorded in the repository.
- Simulated user workflow evidence is recorded in the repository.

Planned adoption assets:

- short Codex demo;
- example project with before/after comparison;
- Claude Code experimental run notes for `multi-session-subthread` mode and
  the hook-backed fallback path, after those are verified in a real session
  (`single-session-subagent` mode's run notes already exist at
  `tests/dogfood/gate-3-claude-code-native-broker/RESULT.md`).

## limitations

Near-term:

- verify Claude Code V2's `multi-session-subthread` mode, the
  `SendMessage`-based reuse-dispatch path, and the hook-backed fallback path
  in a real Claude Code session (`single-session-subagent` mode's
  first-dispatch/`create` path is verified; repeat dispatch via `SendMessage`
  is implemented but not yet dogfooded);
- publish a small example project;
- add a short demo walkthrough;
- collect issue-template feedback from first users.

Longer-term:

- harden V2 across more project types;
- improve example libraries for common workflows;
- keep the README focused on adoption and first-run clarity.
