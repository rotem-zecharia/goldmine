# shareAI-lab/learn-claude-code

Bash is all you need - A nano claude code–like 「agent harness」, built from 0 to 1

## features

Because Claude Code is the most elegant, most complete agent harness implementation we have seen. Not because of any clever trick, but because of what it *does not* do: it does not try to be the agent. It does not impose rigid workflows. It does not substitute hand-crafted decision trees for the model's own judgment. It gives the model tools, knowledge, context management, and permission boundaries -- then gets out of the way.

Strip Claude Code down to its essence:

```
Claude Code = one agent loop
            + tools (bash, read, write, edit, glob, grep, browser...)
            + on-demand skill loading
            + context compaction
            + subagent spawning
            + task system with dependency graphs
            + async mailbox team coordination
            + task-bound worktrees for parallel edits
            + permission governance
            + hooks extension system
            + memory persistence
            + MCP external capability routing
```

That is it. The agent itself? Claude. A model. Trained by Anthropic on the full breadth of human reasoning and code. The harness did not make Claude smart. Claude was already smart. The harness gave Claude hands, eyes, and a workspace.

The takeaway is not "copy Claude Code." The takeaway is: **the best agent products come from engineers who understand that their job is the harness, not the intelligence.**

---

```
                    THE AGENT PATTERN
                    =================

    User --> messages[] --> LLM --> response
                                      |
                              contains tool_use block?
                           /                          \
                         yes                           no
                          |                             |
                    execute tools                    return text
                    append results
                    loop back -----------------> messages[]


    The model decides when to call tools and when to stop.
    The code just executes what the model asks for.
    This repo teaches you to build everything around this loop --
    the harness that makes the agent effective in a specific domain.
```

## Core Pattern

```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS,
        )
        messages.append({"role": "assistant",
                         "content": response.content})

        tool_calls = [
            block for block in response.content if block.type == "tool_use"
        ]
        if not tool_calls:
            return

        results = []
        for block in tool_calls:
            output = TOOL_HANDLERS[block.name](**block.input)
            results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": output,
            })
        messages.append({"role": "user", "content": results})
```

Each lesson isolates one harness mechanism around this loop. s15 reconnects the cumulative runtime; s16 and s17 then study workflow orchestration and goal closure as focused examples. The loop belongs to the agent. The mechanisms belong to the harness.

The loop is constant. Tools, knowledge, and permissions change. Agent = Model (LLM) + a generalized operational environment (Harness).

---

## Version Status

This repository currently contains two tutorial tracks:

- **Current track: root-level `s01-s17`**
  The root-level `s01_*` ... `s17_*` folders are the canonical version. Each chapter contains an English default README, Chinese/Japanese translations, runnable `code.py`, and diagrams where needed.
- **Legacy transition track: `docs/` and `agents/`**
  These preserve the older 12-lesson version for existing readers and old links during migration.

If you are starting now, read the root-level `s01_agent_loop/` through `s17_goal_loop/` chapters. The legacy and current cha

## installation

### Current 17-Lesson Track

```sh
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # configure ANTHROPIC_API_KEY

python s01_agent_loop/code.py        # Start here -- one loop + bash
python s08_context_compact/code.py   # Context compaction (complex)
python s17_goal_loop/code.py         # Endpoint: continue until a checkable goal is met
```

### Legacy 12-Lesson Track

```sh
python agents/s01_agent_loop.py
python agents/s12_worktree_task_isolation.py
python agents/s_full.py
```

### Web Platform

The web app extracts the root-level course. Lessons s16 and s17 include reading, source, simulator, and architecture views; only their dedicated hero visualizations remain intentionally minimal.

```sh
cd web && npm install && npm run dev   # http://localhost:3000
```

---

## Project Structure

```
learn-claude-code/
  s01_agent_loop/          # one folder per chapter
    README.md              #   English default (complete narrative)
    README.zh.md           #   Chinese translation
    README.ja.md           #   Japanese translation
    code.py                #   standalone runnable code
    images/                #   SVG diagrams
  s02_tool_use/
  ...
  s14_mcp_plugin/
  s15_integrated_harness/
  s16_workflow_runtime/
  s17_goal_loop/           # endpoint chapter
  agents/                  # legacy 12 runnable copies + s_full.py
  skills/                  # skill files used by s07
  docs/                    # legacy 12-lesson docs, kept during transition
  web/                     # generated from the root-level course
  tests/
```

---

## What's Next

After 17 lessons, you understand harness engineering from the inside out. Two paths to turn that knowledge into product:

### Kode Agent CLI -- Open-Source Coding Agent CLI

> `npm i -g @shareai-lab/kode`

Skill and LSP support, Windows compatible, works with GLM / MiniMax / DeepSeek and other open models. Install and go.

GitHub: **[shareAI-lab/Kode-CLI](https://github.com/shareAI-lab/Kode-CLI)**
