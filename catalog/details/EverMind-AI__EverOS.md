# EverMind-AI/EverOS

One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows.

## features

EverOS is a Python library and local-first memory runtime for agents and
makers. It gives one portable memory layer across coding assistants, apps,
devices, and workflows from day one. It stores conversations, files, and agent
trajectories as readable Markdown, then syncs local SQLite and LanceDB indexes
for fast retrieval and self-evolving reuse.

<table>
<tr>
<th width="28%">Title</th>
<th width="36%">EverOS</th>
<th width="36%">Other Agent Memory Libraries</th>
</tr>
<tr>
<td><strong>Markdown source of truth</strong></td>
<td>✅ Canonical <code>.md</code> files that are readable, editable, diffable, and Git-versioned</td>
<td>❌ Usually API, vector, graph, dashboard, or database state</td>
</tr>
<tr>
<td><strong>Direct file editing</strong></td>
<td>✅ Edit <code>.md</code> files; cascade watcher syncs</td>
<td>❌ Usually SDK, API, dashboard, or backend update paths</td>
</tr>
<tr>
<td><strong>Local three-part stack</strong></td>
<td>✅ Markdown + SQLite + LanceDB; no MongoDB, Elasticsearch, or Redis required</td>
<td>❌ Often depends on managed services, vector DBs, graph DBs, or server stacks</td>
</tr>
<tr>
<td><strong>User + agent tracks</strong></td>
<td>✅ User <code>episodes/profile</code> and agent <code>cases/skills</code> are separate first-class surfaces</td>
<td>❌ Usually centered on chat history, profiles, entities, facts, or retrieval records</td>
</tr>
<tr>
<td><strong>Orthogonal retrieval</strong></td>
<td>✅ Search by <code>user_id</code>, <code>agent_id</code>, <code>app_id</code>, <code>project_id</code>, and <code>session_id</code></td>
<td>❌ Usually app, namespace, tenant, thread, or graph scoped</td>
</tr>
<tr>
<td><strong>Knowledge Wiki</strong></td>
<td>✅ Editable, source-backed Markdown knowledge pages with taxonomy, CRUD APIs, and topic search</td>
<td>❌ Usually separate from memory, trapped in a dashboard, or not tied back to source files</td>
</tr>
<tr>
<td><strong>Reflection</strong></td>
<td>✅ Offline memory evolution that merges episode clusters and refines profiles and skills between sessions</td>
<td>❌ Usually retrieval-only memory with little background consolidation or long-horizon improvement</td>
</tr>
</table>

<br>

## installation

> One OpenRouter API key is enough to start EverOS, write durable memories,
> and retrieve them with keyword search.

## requirements

- Python 3.12+
- One [OpenRouter API key](https://openrouter.ai/keys)
