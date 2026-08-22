# bojieli/ai-agent-book

《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

## tools

建议申请下面几个平台的 API Key 方便学习。模型选型可参考 [这篇指南](https://01.me/2025/07/llm-api-setup/)。

| 平台 | 链接 | 特色 | 访问节点 |
| --- | --- | --- | --- |
| **Kimi**（月之暗面） | <https://platform.moonshot.cn/> | Kimi 系列，Coding、Agent 能力强 | 中国大陆 |
| **智谱 GLM** | <https://open.bigmodel.cn/> | GLM-5.2 等，Coding、Agent 能力强 | 中国大陆 |
| **Siliconflow** | <https://siliconflow.cn/> | 各种开源模型（DeepSeek、Qwen 等），中国大陆访问速度快 | 中国大陆 |
| **DeepSeek** | <https://platform.deepseek.com/> | DeepSeek 官方 API | 全球 + 中国大陆 |
| **Krill AI** | [www.krill-ai.net](https://www.krill-ai.net/register?invite=Q8D3L35725) | 一站式访问全球及国内主流模型（OpenAI、Claude、Gemini、Grok、Kimi、GLM、DeepSeek、Qwen、Minimax） | 全球 + 中国大陆 |
| **OpenRouter** | <https://openrouter.ai/> | 一站式访问全球及国内主流模型（GPT、Claude、Gemini、Kimi、GLM、DeepSeek、Qwen 等） | 全球 |

## 💎 赞助商

感谢 **Krill AI** 赞助本项目！Krill 提供 GPT / Claude / Gemini / 多款国产模型的官方稳定极速 API 中转服务，支持企业级定制、报销开票、7×16h 专属技术支持，更有独家适配的 WebSocket 连接方式，畅享极速首字速度。

Krill 为本书读者提供特别优惠：使用[此链接](https://www.krill-ai.net/register?invite=Q8D3L35725)注册并在充值时填写优惠码「ai-agent-book」，首次购买 Codex 套餐可享 77 折优惠！

> 🧪 配套实验的执行状态、证据与未完成门禁单独记录在 [`docs/EXPERIMENT_STATUS.md`](docs/EXPERIMENT_STATUS.md)；克隆或安装源码不代表实验完成。

## 📦 附录 · 外部仓库获取

本附录列出第 6、7、8、10 章与实验直接映射的 22 个外部仓库，另含 1 个辅助训练 cookbook；它们**不作为本书源码内置依赖**（出于体积与版权），需要自行克隆到对应目录。部分训练项目还会按各自 README 拉取模型、数据集和模拟器依赖，不计入这 22 个直接映射。以下版本来自 2026-07-30 工作区 checkout 或同日只读上游审计；固定源码只建立复现起点，不代表训练、硬件、浏览器或多 Agent 实验已经执行。

### 一键克隆脚本

<details>
<summary><b>🔧 展开克隆命令</b>（共 23 个 checkout：22 个实验映射 + 1 个辅助 cookbook）</summary>

```bash
# 第 6 章 · GUI 与机器人外部复现轨道
git clone https://github.com/anthropics/claude-quickstarts.git chapter6/claude-quickstarts && git -C chapter6/claude-quickstarts checkout --detach 9bcc95e316e5ef6542b4c9d0469f4078829eead5  # 实验 6-7 使用 computer-use-demo/
git clone https://github.com/browser-use/browser-use.git chapter6/browser-use && git -C chapter6/browser-use checkout --detach ec9277c5001f2cb78ee419c927775a3cfc227ff8  # 实验 6-8
git clone https://github.com/Vector-Wangel/XLeRobot.git chapter6/XLeRobot && git -C chapter6/XLeRobot fetch origin 3d14695e40c9c68229c0aacffca6053c75cd3eb6 && git -C chapter6/XLeRobot checkout --detach 3d14695e40c9c68229c0aacffca6053c75cd3eb6 && test "$(git -C chapter6/XLeRobot rev-parse HEAD)" = "3d14695e40c9c68229c0aacffca6053c75cd3eb6"  # 实验 6-9、6-11 共用
git clone https://github.com/Grigorij-Dudnik/RoboCrew.git chapter6/RoboCrew && git -C chapter6/RoboCrew fetch origin c749148f29bd14e61347f9fc3530c343fff0d994 && git -C chapter6/RoboCrew checkout --detach c749148f29bd14e61347f9fc3530c343fff0d994 && test "$(git -C chapter6/RoboCrew rev-parse HEAD)" = "c749148f29bd14e61347f9fc3530c343fff0d994"  # 实验 6-10、6-11；RoboCrew v0.3.1
git clone https://github.com/StoneT2000/lerobot-sim2real.git chapter6/lerobot-sim2real && git -C chapter6/lerobot-sim2real fetch origin 87d6c1d969f6e0ca4dc5697940804e231118a63a && git -C chapter6/lerobot-sim2real checkout --detach 87d6c1d969f6e0ca4dc5697940804e231118a63a && test "$(git -C chapter6/lerobot-sim2real rev-parse HEAD)" = "87d6c1d969f6e0ca4dc5697940804e231118a63a"  # 实验 6-13

# 第 7 章 · 评测基准
git clone https://github.com/google-research/android_world.git chapter7/android_world && git -C chapter7/android_world checkout --detach 0e95d641e244504c22087cc29b013f3b2428a261
git clone https://huggingface.co/datasets/gaia-benchmark/GAIA chapter7/GAIA && git -C chapter7/GAIA checkout --detach 682dd723ee1e1697e00360edccf2366dc8418dd9
git clone https://github.com/xlang-ai/OSWorld.git chapter7/OSWorld && git -C chapter7/OSWorld checkout --detach 8365edc975efd0477a0d62444a5beed562ab5a7b
git clone https://github.com/SWE-bench/SWE-bench.git chapter7/SWE-bench && git -C chapter7/SWE-bench checkout --detach 5cd4be9fb23971679cbbafe5a0ecade27cef99be
git clone https://github.com/sierra-research/tau2-bench.git chapter7/tau2-bench && git -C chapter7/tau2-bench checkout --detach 8d005b0e5b9e4af0bc055886fa7f95fc86d1710e
git clone https://github.com/laude-institute/terminal-bench.git chapter7/terminal-bench && git -C chapter7/terminal-bench ch
