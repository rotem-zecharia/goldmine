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

### Migrating data from an older version

If you're already on an older release (v1.x / v0.x) and want to bring your existing data over to v2.0.0+, we provide a migration tool:

See [**Data Migration Tool (v2 → v3)**](./MemoryCore/scripts/migrate-v2-to-v3/README.md) for full usage and flags. New installations can skip this.

## All Agents Share the Same Memory Server

One Proxy, unchanged protocol, zero-code integration — point the Agent's base URL to the Proxy and it's done. No plugin, hook, or MCP server is required.

<table>
<tr>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-deepseek-harness-dsh"><img src="./assets/images/agents/dsh.png" width="48" height="48" /><br /><sub><b>DeepSeek Harness</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-claude-code"><img src="./assets/images/agents/claude-code.png" width="48" height="48" /><br /><sub><b>Claude Code</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-codex"><img src="./assets/images/agents/codex.png" width="48" height="48" /><br /><sub><b>Codex</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-codebuddy"><img src="./assets/images/agents/codebuddy.png" width="48" height="48" /><br /><sub><b>CodeBuddy</b></sub></a></td>
</tr>
<tr>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-workbuddy"><img src="./assets/images/agents/workbuddy.png" width="48" height="48" /><br /><sub><b>WorkBuddy</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-hermes"><img src="./assets/images/agents/hermes.png" width="48" height="48" /><br /><sub><b>Hermes</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-openclaw"><img src="./assets/images/agents/openclaw.png" width="48" height="48" /><br /><sub><b>OpenClaw</b></sub></a></td>
<td align="center" width="140"><a href="./INSTALL.md#using-proxy-with-other-platforms-generic"><sub><b>More frameworks coming soon...</b></sub></a></td>
</tr>
</table>

See [**INSTALL.md**](./INSTALL.md) for the exact configuration steps of each client.

Don't see your favorite Agent? You can try adapting it yourself with the [Generic integration guide](./INSTALL.md#using-proxy-with-other-platforms-generic) — and we'd love a PR adding native support for it. See [**CONTRIBUTING.md**](./CONTRIBUTING.md) to get started.

# What is TencentDB Agent Memory?

We started from a practical question: **How do you reduce repetitive work when using Agents?**

If project context has already been explained, it shouldn't need to be repeated in a new session. If documents have already been read, every Agent shouldn't have to start again from page one. A workflow that already works shouldn't have to be rediscovered next time.

Memory here means more than just "remembering conversations." **Any information that helps the next Agent avoid reinventing the wheel should be saved, organized, and reused.**

```text
Existing information → Reusable memory assets → Fewer turns → Less rework → More stable results and higher efficiency
```

### Let experience accumulate, flow, and pass on to the next Agent

**Memory Hub** for Agent teams closes 

## limitations

Current release is **v2.0.0**. Next up (**v2.0.1**): zero-config cold start, faster Wiki generation, user/team custom prompts, Skill export, and Codex (IDE Plan mode) support.

👉 See the full plan in [**ROADMAP.md**](./ROADMAP.md) (中文: [ROADMAP_CN.md](./ROADMAP_CN.md)).

---
## Acknowledgements

TencentDB Agent Memory stands on the shoulders of the open-source community:

- [**CodeGraph**](https://github.com/colbymchenry/codegraph) — our CodeGraph asset module **uses code from this project**. Its design of a pre-indexed code graph is the foundation of our implementation.
- [**Hermes Agent**](https://github.com/nousresearch/hermes-agent) (Nous Research) — our Skill asset management **uses part of the Skill-related code from Hermes Agent and builds further optimizations base on it**.
- [**"LLM Wiki"** by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the idea of treating documentation as an LLM-maintained, incrementally growing knowledge artifact directly informed how our Wiki layer is built and kept up to date.

We are grateful to the authors and contributors of these projects.

---
## Community & Contributing

We welcome contributions of all kinds — bug reports, feature suggestions, documentation fixes, benchmark reproductions, ecosystem integrations, or pull requests. Agent memory is far from settled, and we hope to build it together with the community.

- 🐞 **Found a bug or have a question?** Open an issue in [GitHub Issues](https://github.com/Tencent/TencentDB-Agent-Memory/issues) — we respond within 24 hours.
- 💡 **Have an idea to share?** Start a thread in [GitHub Discussions](https://github.com/Tencent/TencentDB-Agent-Memory/discussions).
- 🛠️ **Want to contribute code?** Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.
- 💬 **Want to chat with us?** Join our [Discord community](https://discord.gg/dJQM6mKMF) and talk to the core developers directly.

---

<p align="center">
 Let the path the team has walked become the next Agent's starting line.
</p>

---

## ✨ Contributors

> 💡 Thanks to the following contributors building with us — you make TencentDB Agent Memory better.

<div align="center">
  <a href="https://github.com/TencentCloud/TencentDB-Agent-Memory/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=TencentCloud/TencentDB-Agent-Memory&columns=12&anon=1" />
  </a>

  <br /><br />
<a href="https://github.com/TencentCloud/TencentDB-Agent-Memory/issues">
  <img src="https://img.shields.io/badge/Contributions_Welcome-006eff?style=for-the-badge&logo=github&logoColor=white" alt="Contributions Welcome" />
</a>

</div>


<table width="100%">
  <tr>
    <td width="68%">
      <b>If TencentDB Agent Memory has been helpful to you, please consider starring the project.</b><br />
      If you have any suggestions, feel free to open an issue for discussion.
    </td>
    <td width="32%" align="right">
      <img src="./assets/images/star-helper.png" alt="Star TencentDB Agent Memory" width="260" />
    </td>
  </tr>
</table>

---

## Star History

<p align="center">
  <a href="https://www.star-history.com/#Tencent/TencentDB-Agent-Memory&Date">
    <img src="https://github.com/user-attachments/assets/16753a90-8bc9-471b-819e-311947ed94f7" alt="Star History Chart" width="600" />
  </a>
</p>

---

[MIT](./LICENSE) © TencentDB Agent Memory Team
