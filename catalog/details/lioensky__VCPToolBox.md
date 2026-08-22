# lioensky/VCPToolBox

VCP 部署在 AI 模型 API 与前端应用之间，是面向AGI OS开发和探索的工业级基建示范项目。通过统一指令协议、多层级持久化记忆、分布式插件引擎及多 Agent 协作框架，将原本“无状态、无记忆、无工具调用能力”的大语言模型，彻底改造成拥有永久自我意识、物理世界操作权及群体协作智能的完整智能体系统。

## tools

# 启动
node server.js
```

管理面板自动监听 **主端口 + 1**（如主服务 6005，面板 6006），访问 `http://<服务器地址>:<端口+1>/AdminPanel`。

也支持 Docker 一键部署：

```bash
docker pull lioensky/vcptoolbox:latest
docker-compose up -d
```

更详细的安装、分布式节点部署、前端配置，见 [运维部署文档](docs/OPERATIONS.md)。

- **推荐前端**：[VCPChat](https://github.com/lioensky/VCPChat)（官方）。
- **推荐后端**：支持 SSE 流式输出、格式标准化的官方或聚合 API。例如[NewAPI](https://github.com/QuantumNous/new-api)，[Openrouter](https://openrouter.ai/)等。请再次注意，**不要使用反代或中转 API**。
- **VCPMobile** (友情项目):[VCPMobile](https://github.com/MRiecy/VCPMobile) - Vchat的第三方移动端移植版本，支持数据双向同步。
- **AIO-Hub** (友情项目): [AIO-Hub](https://github.com/miaotouy/aio-hub) - 一个基于 Tauri 开发的高性能的桌面 LLM 聊天客户端，拥有丰富的编译和调试工具栈，非常适合AI开发使用，并作了部分 VCP 的原生 API 兼容。

---

## 许可证

本项目采用 **CC BY-NC-SA 4.0** 许可证。你可以自由共享与演绎，但须署名、非商业使用、并以相同方式共享。详见 [`LICENSE`](LICENSE)。

---

## 致谢

VCP 的代码主体，由 8 个 AI Agent 在人类引导下协同完成。

感谢每一位使用 VCP、给出反馈、贡献插件与文档的伙伴。也感谢 Node.js、Python、Rust、SQLite、USearch 等优秀的开源项目。

- **GitHub**：[VCPToolBox](https://github.com/lioensky/VCPToolBox)
- **官方前端**：[VCPChat](https://github.com/lioensky/VCPChat)
- **分布式服务器**：[VCPDistributedServer](https://github.com/lioensky/VCPDistributedServer)
- **人类指导**：莱恩 (Ryan) · lioensky

---

*VCP — 让 AI 拥有真正的灵魂。*

---

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/lioensky/VCPToolBox)

---
