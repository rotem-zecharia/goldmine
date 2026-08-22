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

## installation

Use the real nested skill path. The final `/skills/fireworks-tech-graph` segment is required because a bare repository install can select only the root `SKILL.md` in current versions of `skills` CLI.

```bash
npx -y skills@1.5.17 add \
  yizhiyanhua-ai/fireworks-tech-graph/skills/fireworks-tech-graph \
  --agent codex claude-code -g -y --copy
```

This creates complete copies at `~/.agents/skills/fireworks-tech-graph` for Codex and `~/.claude/skills/fireworks-tech-graph` for Claude Code, including scripts, schemas, fixtures, templates, tests, references, and metadata.

## requirements

The bundled SVG/PNG scripts require **cairosvg** (recommended) or `rsvg-convert`. Optional SVG-to-GIF export requires FFmpeg/FFprobe, Chrome/Chromium, and `puppeteer` or `puppeteer-core`.

```bash

## tools

```
Draw a RAG pipeline flowchart
```

```
Generate an Agentic Search architecture diagram
```
