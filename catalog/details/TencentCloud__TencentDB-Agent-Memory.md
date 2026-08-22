# TencentCloud/TencentDB-Agent-Memory

TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, s

## installation

Start all three services in one go (`memory-core` + `memory-hub` + `proxy`):

```bash
git clone https://github.com/Tencent/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images
cp .env.example .env
$EDITOR .env       # Fill in two sets of LLM parameters (memory group + proxy group)
./start-all.sh     # Launch everything with one command; when finished, it prints a one-liner you can paste directly into Claude
```

Open the panel: [http://localhost:8125](http://localhost:8125).

Complete installation documentation (standalone Memory Hub deployment, Proxy + Claude Code / CodeBuddy usage, stop and cleanup, port reference, etc.) is available in [**INSTALL.md**](./INSTALL.md) (中文: [INSTALL_CN.md](./INSTALL_CN.md)).

## limitations

Current release is **v2.0.0**. Next up (**v2.0.1**): zero-config cold start, faster Wiki generation, user/team custom prompts, Skill export, and Codex (IDE Plan mode) support.

👉 See the full plan in [**ROADMAP.md**](./ROADMAP.md) (中文: [ROADMAP_CN.md](./ROADMAP_CN.md)).

---
