# Windy3f3f3f3f/claude-code-from-scratch

Build your own Claude Code from scratch. 🔍 Claude Code 开源了 50 万行代码，读不动？用 ~5000 行 TypeScript / Python 从零复现核心架构，11 章分步教程带你理解 coding agent 精髓

## tools

读代码最怕读不懂又跑不起来，改一行也不知道对不对。所以每个代码章都配了一份能单独跑的最小实现：一条命令、不用 API key，就能看它真的转起来。

```bash
node steps/run.mjs --list     # 列出所有能跑的章节
node steps/run.mjs 7          # 跑第 7 章：对话变长了，它把旧消息压成摘要
node steps/run.mjs 7 --diff   # 只看这一章比上一章多写的那几行
node steps/run.mjs 7 --py     # 换成 Python 版
```

看到的输出是真跑出来的（本地 mock 模型驱动，不联网），`--diff` 标出的正是这一章新增的代码。想拿自己的 prompt 连真模型试，加 `--live` 就行。每章的这段代码、文档里贴的代码块、跑出来的那段输出，全从同一份源码生成——不会出现"文档说的和代码对不上"。

## 🚀 快速开始

**TypeScript 版**

```bash
git clone https://github.com/Windy3f3f3f3f/claude-code-from-scratch.git
cd claude-code-from-scratch
npm install && npm run build
```

**Python 版**（需要 Python 3.11+，[详细说明](./python/README.md)）

```bash
cd python
pip install -e .
mini-claude-py          # 命令行入口（避免与 TS 版 mini-claude 冲突）
python -m mini_claude   # 或用 python -m 方式运行
```

### 配置 API

支持两种后端，通过环境变量自动识别：（支持自定义base url）

**方式一：Anthropic 格式（推荐）**

```bash
export ANTHROPIC_API_KEY="sk-ant-xxx"
# 可选：使用代理
export ANTHROPIC_BASE_URL="https://aihubmix.com"
```

**方式二：OpenAI 兼容格式**

```bash
export OPENAI_API_KEY="sk-xxx"
export OPENAI_BASE_URL="https://api.openai.com/v1"
```

默认模型为 `claude-opus-4-6`，可通过环境变量或命令行参数自定义：

```bash
export MINI_CLAUDE_MODEL="claude-sonnet-4-6"    # 环境变量方式
npm start -- --model gpt-4o                      # 命令行方式（优先级更高）
```

### 运行

**TypeScript 版**

```bash
npm start                    # 交互式 REPL 模式（推荐）
npm start -- --resume        # 恢复上次会话继续对话
npm start -- --yolo          # 跳过安全确认（危险命令自动执行）
npm start -- --plan          # Plan 模式：只分析不修改
npm start -- --accept-edits  # 自动批准文件编辑
npm start -- --dont-ask      # CI 模式：需确认的操作自动拒绝
npm start -- --max-cost 0.50 # 费用限制（美元）
npm start -- --max-turns 20  # 轮次限制
```

**Python 版**

```bash
mini-claude-py               # 交互式 REPL 模式（推荐）
mini-claude-py --resume      # 恢复上次会话继续对话
mini-claude-py --yolo        # 跳过安全确认
mini-claude-py --plan        # Plan 模式：只分析不修改
mini-claude-py --accept-edits # 自动批准文件编辑
mini-claude-py --dont-ask    # CI 模式：需确认的操作自动拒绝
mini-claude-py --max-cost 0.50 # 费用限制（美元）
mini-claude-py --max-turns 20  # 轮次限制
```

全局安装后可在任意目录使用：

**TypeScript 版**

```bash
npm link                     # 全局安装
cd ~/your-project
mini-claude                  # 直接启动
```

**Python 版**

```bash
cd python
pip install -e .             # 全局安装（editable 模式）
cd ~/your-project
mini-claude-py               # 直接启动
```

### REPL 命令

| 命令 | 功能 |
|------|------|
| `/clear` | 清空对话历史 |
| `/cost` | 显示累计 token 用量和费用估算 |
| `/compact` | 手动触发对话压缩 |
| `/memory` | 列出所有已保存的记忆 |
| `/skills` | 列出可用的技能 |
| `/<skill>` | 调用已注册的技能（如 `/commit`） |

> 详见 [CLI 与会话](https://windy3f3f3f3f.github.io/claude-code-from-scratch/#/docs/04-cli-session) 和 [功能测试](https://windy3f3f3f3f.github.io/claude-code-from-scratch/#/docs/14-testing)

## ⚖️ 与 Claude Code 的对比

| 维度 | Claude Code | Mini Claude Code |
|------|------------|-----------------|
| 定位 | 生产级编程智能体 | 学习 / 最小可用实现 |
| 工具数量 | 66+ 内置工具 | 13 个工具（6 核心 + web_fetch + tool_search + skill + agent + plan mode） |
| 工具执行 | 并发 + streaming 早期启动 | 并行执行 + streaming 早期启动 |
| 上下文管理 | 4 级压缩流水线 | 4 层压缩 + 大结果持久化（>30KB） |
| 权限系统 | 7 层 + AST 分析 | 5 种模式 + 声明式规则 + 正则检测 |
| 编辑验证 | 14 步流水线 | 引号容错 + 唯一性 + mtime 防护 + diff 输出 |
| 记忆系统 | 4 类型 + 语义召回 | 4 类型 + 语义召回 + 异步预取 |
| 技能系统 | 6 源 + inline/fork | 2 源 + inline/fork |
| 多 Agent | Sub-Agent + Coordinator + Swarm | Sub-Agent（3 内置 + 自定义 Agent） |
| MCP 集成 | mcpClient.ts + 动态工具发现 | McpManager + JSON-RPC over stdio |
| 预算控制 | USD/轮次/abort 三维 | USD + 轮次限制 |
| 代码量 | 50 万+ 行 | ~5500 行（TS）/ ~5000 行（Python） |

## ⚡ 核心能力

- **Agent 循环**：自动调用工具、处理结果、持续迭代，直到任务完成
- **13 个工具**：读写编辑文件（mtime 防护）、搜索、Shell、WebFetch、ToolSearch（延迟加载）、技能、子 Agent、Plan Mode
- **流式输出**：逐字实时显示，Anthropic + OpenAI 双后端，streaming 工具早期执行
- **并行工具执行**：只读工具（read_file、grep_search 等）自动并发，2-3x 加速
- **4 层上下文压缩**：budget 截断 → stale snip → microcompact → auto-compact + 大结果持久化（>30KB 写磁盘）
- **权限系统**：5 种模式 + `.claude/settings.json` 声明式 allow/deny 规则 + 16 个危险命令正则
- **记忆系统**：4 类型记忆 + 语义召回（sideQuery 调模型选择相关记忆）+ 异步预取
- **技能系统**：`.claude/skills/` 目录加载，支持 inline 注入和 fork 子 Agent 两种执行模式
- **多 Agent**：Sub-Agent
