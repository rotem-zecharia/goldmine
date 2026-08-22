# yizhiyanhua-ai/fireworks-tech-graph

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

## features

`fireworks-tech-graph` is one Agent Skill that works unchanged in **Codex and Claude Code**. It turns natural language descriptions into polished, geometry-checked SVG diagrams, high-resolution PNGs, validated SVG-to-GIF semantic motion, and offline interactive HTML. The focused animation path accepts a generated semantic SVG and emits one compact, probed GIF. It ships with **11 generator-backed styles** and **1 AI-authored style (Dark Luxury)**. Four engineering-first styles add executable contracts for C4 reviews, cloud deployments, event streams, and reliability investigations, alongside deep AI/Agent domain patterns and all 14 UML diagram types.

```
User: "Generate a Mem0 memory architecture diagram, dark style"
  → Skill classifies: Memory Architecture Diagram, Style 2
  → Generates SVG with swim lanes, cylinders, semantic arrows
  → Exports 1920px PNG
  → Reports: mem0-architecture.svg / mem0-architecture.png
```

---

## Sponsors

<table>
  <tr>
    <td width="200" align="center"><a href="https://aigocode.app/invite/yizhiyanhua"><img src="assets/sponsors/aigocode.png" alt="AIGoCode" width="160" /></a></td>
    <td>Thanks to <strong>AIGoCode</strong> for sponsoring this project! AIGoCode is an all-in-one platform that integrates Claude Code, Codex, and the latest Gemini models, providing you with stable, efficient, and highly cost-effective AI coding services. The platform offers flexible subscription plans, zero risk of account suspension, direct access with no VPN required, and lightning-fast responses. AIGoCode has prepared a special benefit for <strong>fireworks-tech-graph</strong> users: if you register via <a href="https://aigocode.app/invite/yizhiyanhua">this link</a>, you'll receive an extra <strong>10% bonus credit</strong> on your first top-up!</td>
  </tr>
</table>

Interested in becoming a sponsor? Contact: <a href="mailto:ccc7574@gmail.com">ccc7574@gmail.com</a>

---

## Work With the Builder

This project is also a proof surface for a broader capability: turning vague AI/devtool workflows into constrained, reusable systems with validation, documentation, export paths, and product-facing polish.

If you are building agent infrastructure, AI IDEs, internal copilots, developer tools, technical documentation systems, or applied AI workflow products, I am open to scoped paid sprints, design-partner work, and founding engineer conversations.

- Founder-facing profile: https://bradzhang.dev/en
- Commercial case study: https://bradzhang.dev/en/case-studies/fireworks-tech-graph
- Work with me: https://bradzhang.dev/en/work-with-me

---

## Showcase

> The animated previews use the user-approved 5.75-second settled-flow timeline: routes draw in first, then the final topology keeps live data moving for two additional seconds. Each full-size GIF is 960px wide at 20fps / 115 frames; the 3×4 overview is an optimized 1200px preview. Lossless 1920px PNGs remain in `assets/samples/` as static regression baselines.

![Animated 12-style showcase — one distinct engineering scenario per style](assets/samples/showcase-12-styles.gif)

The v1.2.0 overview above and every full-size animated sample below come from the approved regression set. Each style keeps a distinct scenario while sharing the same geometry, text-fit, wire-routing, and semantic-motion quality gates.

### Style 1 — Flat Icon (default)
*Mem0 Memory Architecture — personal-memory extraction, conflict resolution, storage, and retrieval*
![Style 1 — Flat Icon](assets/samples/sample-style1-flat.gif)

### Style 2 — Dark Terminal
*Tool Call Flow — dark terminal execution, source grounding, retrieval, and answer synthesis*
![Style 2 — Dark Terminal](assets/samples/sample-style2-dark.gif)

### Style 3 — Blueprint
*Microservices Architecture — engineering grid, domain services, data stores, events, and telemetry*
![Style 3 — Blueprint](assets/samples/sample-style3-blueprint.gif)

### Style 4 — Notion Clean
*Agent Memory Types — minimal hierarchy from sensory and working co

## installation

### Recommended: install the complete skill for both runtimes

Use the real nested skill path. The final `/skills/fireworks-tech-graph` segment is required because a bare repository install can select only the root `SKILL.md` in current versions of `skills` CLI.

```bash
npx -y skills@1.5.17 add \
  yizhiyanhua-ai/fireworks-tech-graph/skills/fireworks-tech-graph \
  --agent codex claude-code -g -y --copy
```

This creates complete copies at `~/.agents/skills/fireworks-tech-graph` for Codex and `~/.claude/skills/fireworks-tech-graph` for Claude Code, including scripts, schemas, fixtures, templates, tests, references, and metadata.

### Editable Git checkout for Codex

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.agents/skills/fireworks-tech-graph
```

Codex discovers personal skills from `~/.agents/skills` and reads the optional `agents/openai.yaml` metadata included in this repository.

### Editable Git checkout for Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.claude/skills/fireworks-tech-graph
```

Claude Code discovers personal skills from `~/.claude/skills` and ignores the Codex-only UI metadata.

### One editable checkout shared by Codex and Claude Code

For a fresh install with Claude Code 2.1.203 or newer, keep one checkout and link both discovery paths to it. Move any existing destinations aside before creating the links.

```bash
mkdir -p ~/.local/share/agent-skills ~/.agents/skills ~/.claude/skills
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.local/share/agent-skills/fireworks-tech-graph
ln -s ~/.local/share/agent-skills/fireworks-tech-graph ~/.agents/skills/fireworks-tech-graph
ln -s ~/.local/share/agent-skills/fireworks-tech-graph ~/.claude/skills/fireworks-tech-graph
```

This keeps `SKILL.md`, references, scripts, templates, and future updates identical in both agents. The npm registry is a separate distribution channel and may lag GitHub Releases. For the current Skill version, use the nested GitHub path above; the npm page remains available for package metadata:

```text
https://www.npmjs.com/package/@yizhiyanhua-ai/fireworks-tech-graph
```

## Update

For a `skills` CLI copy, rerun the recommended nested-path command. For Git installations, update whichever checkout you installed:

```bash
git -C ~/.agents/skills/fireworks-tech-graph pull
# or
git -C ~/.claude/skills/fireworks-tech-graph pull
# or, for the shared checkout
git -C ~/.local/share/agent-skills/fireworks-tech-graph pull
```

After the first install, restart Codex and Claude Code so both discover the skill. Later `SKILL.md` edits are detected automatically; restart the runtime after changing bundled scripts or references if the update is not visible.

The shell commands above target macOS, Linux, WSL, and Git Bash. On native Windows, use the equivalent `%USERPROFILE%\.agents\skills` and `%USERPROFILE%\.claude\skills` paths. Python 3.9+ is required; the optional Puppeteer path requires Node.js 18+.

---

## Unified CLI

```bash
SKILL_ROOT="${CLAUDE_SKILL_DIR:-$HOME/.agents/skills/fireworks-tech-graph}"

python3 "$SKILL_ROOT/scripts/fireworks.py" doctor
python3 "$SKILL_ROOT/scripts/fireworks.py" validate architecture "$SKILL_ROOT/fixtures/api-flow-style7.json"
python3 "$SKILL_ROOT/scripts/fireworks.py" render architecture "$SKILL_ROOT/fixtures/api-flow-style7.json" diagram.svg --report layout.json
python3 "$SKILL_ROOT/scripts/fireworks.py" check diagram.svg
python3 "$SKILL_ROOT/scripts/fireworks.py" export-html diagram.svg diagram.html --title "Agent Runtime Architecture"
python3 "$SKILL_ROOT/scripts/fireworks.py" animate diagram.svg diagram.gif
```

The HTML export is one offline file. It sanitizes the SVG, adds pan/zoom/reset, light and dark themes, SVG source copy, and SVG/PNG/JPEG/WebP downloads at 1×–4×.

For motion, say **“Generate a GIF”**, **“Animate this diagram”**, `生成 GIF`, `制作 GIF`

## requirements

The bundled SVG/PNG scripts require **cairosvg** (recommended) or `rsvg-convert`. Optional SVG-to-GIF export requires FFmpeg/FFprobe, Chrome/Chromium, and `puppeteer` or `puppeteer-core`.

```bash
# Recommended: cairosvg (best CSS support)
python3 -m pip install cairosvg

# Fallback: rsvg-convert (system package; may drop CSS / <foreignObject>)
brew install librsvg                   # macOS
sudo apt install librsvg2-bin          # Ubuntu/Debian

## tools

### Trigger phrases

The skill auto-triggers on:

```
generate diagram / draw diagram / create chart / visualize
architecture diagram / flowchart / sequence diagram / data flow
Generate a GIF / animate this diagram / animate this SVG as a GIF / 生成 GIF / 制作 GIF / 让这张图动起来 / 把刚才的 SVG 转成 GIF
```

### Basic usage

```
Draw a RAG pipeline flowchart
```

```
Generate an Agentic Search architecture diagram
```

### Specify style

```
Draw a microservices architecture diagram, style 2 (dark terminal)
```

```
Draw a multi-agent collaboration diagram --style glassmorphism
```

### Specify output path

```
Generate a Mem0 architecture diagram, output to ~/Desktop/
```

```
Create a tool call flow diagram --output /tmp/diagrams/
```

---

## Example Prompts by Scenario

### AI/Agent Systems

```
Compare Agentic RAG vs standard RAG in a feature matrix, Notion clean style
```
→ Comparison matrix: RAG vs Agentic RAG, covering retrieval strategy, agent loop, tool use

```
Generate a Mem0 memory architecture diagram with vector store, graph DB, KV store, and memory manager
```
→ Memory Architecture with swim lanes: Input → Memory Manager → Storage tiers → Retrieval

```
Draw a Multi-Agent diagram: Orchestrator dispatches 3 SubAgents (search / compute / code execution), results aggregated
```
→ Agent Architecture with hexagons, tool layers, and result aggregation

```
Visualize the Tool Call execution flow: LLM → Tool Selector → Execution → Parser → back to LLM
```
→ Flowchart with decision loop showing tool invocation cycle

```
Draw the 5 agent memory types: Sensory, Working, Episodic, Semantic, Procedural
```
→ Mind map or layered architecture showing memory tiers from sensory to procedural

### Infrastructure & Cloud

```
Draw a microservices architecture: Client → API Gateway → [User Service / Order Service / Payment Service] → PostgreSQL + Redis
```
→ Architecture diagram with horizontal layers, swim lanes per service cluster

```
Generate a data pipeline diagram: Kafka → Spark processing → write to S3 → Athena query
```
→ Data flow diagram with labeled arrows (stream / batch / query)

```
Draw a Kubernetes deployment: Ingress → Service → [Pod × 3] → ConfigMap + PersistentVolume
```
→ Architecture with dashed containers per namespace, solid arrows for traffic flow

### API & Sequence Flows

```
Draw an OAuth2 authorization code flow sequence diagram: User → Client → Auth Server → Resource Server
```
→ Sequence diagram with vertical lifelines and activation boxes

```
Draw the ChatGPT Plugin call sequence diagram
```
→ Sequence: User → ChatGPT → Plugin Manifest → API → Response chain

### Decision & Process Flows

```
Draw a pre-launch QA flowchart for an AI app: Code Review → Security Scan → Performance Test → Manual Approval → Deploy
```
→ Flowchart with diamond decision nodes and parallel branches

```
Generate a feature comparison matrix: RAG vs Fine-tuning vs Prompt Engineering
```
→ Comparison matrix with checked/unchecked cells across cost, latency, accuracy, flexibility

### Concept Maps

```
Visualize the LLM application tech stack: from foundation model to SDK to app framework to deployment
```
→ Layered architecture or mind map from model layer to product layer

```
Draw an AI Agent capability map: Perception / Memory / Reasoning / Action / Learning
```
→ Mind map with central "AI Agent" node and 5 radial branches

---

## 12 Styles

| # | Name | Background | Font | Best For |
|---|------|-----------|------|----------|
| 1 | **Flat Icon** *(default)* | `#ffffff` | Helvetica | Blogs, slides, docs |
| 2 | **Dark Terminal** | `#0f0f1a` | SF Mono / Fira Code | GitHub README, dev articles |
| 3 | **Blueprint** | `#0a1628` | Courier New | Architecture docs, engineering |
| 4 | **Notion Clean** | `#ffffff` | system-ui | Notion, Confluence, wikis |
| 5 | **Glassmorphism** | `#0d1117` gradient | Inter | Product sites, keynotes |
| 6 | **Claude Official** | `#f8f6f3` | system-ui | Anthropic-style diagrams, warm aesthetic |
| 7 | **OpenAI 
