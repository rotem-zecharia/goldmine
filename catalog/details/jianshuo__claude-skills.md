# jianshuo/claude-skills

13 Claude Code skills for video production (transcribe / translate / dub / multicam / subtitles / reframe) + WeChat publishing. Compatible with Claude Code, OpenAI Codex CLI, Cursor, Gemini.

## installation

这些 skill 跑在 [Claude Code](https://claude.com/code) 里,所以先装 Claude Code。

```bash
# 方式 1:npm 全局安装(推荐,需要 Node.js ≥ 18)
npm install -g @anthropic-ai/claude-code
claude            # 启动

# 方式 2:不装,直接用 npx 跑一次
npx @anthropic-ai/claude-code

# 方式 3:原生安装脚本(无需 Node.js)
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash
# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

装好后在任意项目目录运行 `claude` 即可。首次启动会引导登录(Claude 账号或 API key)。
升级:`claude update`(原生安装)或 `npm update -g @anthropic-ai/claude-code`(npm 安装)。

## 安装 Skills / Install Skills

```bash
# 方式 1:从 ClawHub 装单个 skill
clawhub install wjs-transcribing-audio

# 方式 2:把整个仓库作为 Claude Code marketplace
claude plugin marketplace add jianshuo/claude-skills
claude plugin install wjs-transcribing-audio

# 方式 3:直接 clone 到 skills 目录
git clone https://github.com/jianshuo/claude-skills ~/.claude/skills/wjs
```

## 兼容性 / Compatibility

[`SKILL.md`](https://agentskills.io) 是 Anthropic 公开的 skill 格式标准（2025 年 10 月发布，2025 年 12 月被 OpenAI Codex 采纳），所以这套 skill 同样适用于:

- [**Claude Code**](https://claude.com/code) — 主要测试和使用环境
- [**OpenAI Codex CLI**](https://developers.openai.com/codex/skills) — 2025-12+ 起兼容
- **Cursor** / **Gemini CLI** / **Goose** —  生态在跟进

第三方分发平台:[ClawHub](https://clawhub.ai/jianshuo) · [SkillsMP](https://skillsmp.com)（自动索引）

## 这些 skill 是什么？

Claude Code skill 是一个带 frontmatter 的 `SKILL.md` 文件 + 一组脚本。当用户的请求匹配 skill 描述里的触发词（"翻译字幕"、"做封面"、"上传 YouTube"……）时，Claude 会自动加载这个 skill 并按里面写的流程执行。

这套 skill 大致围绕 **「视频创作 + 公众号写作」** 工作流：从原始拍摄素材 → 多机位对齐 → 自动剪辑 → 翻译配音 → 后期合成 → 平台分发。每个 skill 都做一件事，可以单独调用，也可以串成完整流水线。

**命名约定**：所有 skill 以 **动名词（V-ing）** 开头 —— `transcribing-audio` / `dubbing-video` / `editing-multicam` —— 描述「正在做什么动作」，方便和 Claude 自动加载逻辑对齐。

---

## 安装 & 使用 / How to Install

把任意一个 skill 目录复制到 Claude Code 的 skills 目录即可：

```bash
# 全局安装（所有项目都能用）
cp -r wjs-transcribing-audio ~/.claude/skills/

# 项目级安装（只在当前项目可用）
cp -r wjs-transcribing-audio ./.claude/skills/
```

装好后用触发词自然说话（如「转写这个视频」、「做 SRT」），或用斜杠命令 `/wjs-transcribing-audio` 显式调用。不需要重启 Claude Code，技能即时生效。

---

## Skills 总览

| Skill | 一句话作用 | 输入 → 输出 |
|---|---|---|
| [`wjs-publishing-wechat`](./wjs-publishing-wechat/) | 写 / 润色 / 发微信公众号 | 草稿文本 → 排版好的 HTML + 题图 + 解释图 + 上传草稿 |
| [`wjs-mining-articles`](./wjs-mining-articles/) | 从视频字幕里挖公众号文章（独白或对谈） | SRT → N 篇独立公众号文章 + 微信草稿 |
| [`wjs-mining-voicedrop`](./wjs-mining-voicedrop/) | VoiceDrop 语音备忘 → 转写 → 公众号文章草稿 | R2 收件箱 VoiceDrop-*.m4a → SRT → N 篇微信草稿 |
| [`wjs-voicedrop`](./wjs-voicedrop/) | VoiceDrop MCP 的入口：完成 6+4 手机配对登录，把你接上 voicedrop.cn/mcp 的 44 个工具（文章读写与版本、文风与蒸馏、挖矿与重写、社区与投币、书架读书与写书修书等） | `voicedrop` / `voicedrop 登录` / `接 voicedrop mcp` / `/wjs-voicedrop` |
| [`wjs-evaling-voicedrop-prompts`](./wjs-evaling-voicedrop-prompts/) | 评估 VoiceDrop 挖矿 prompt 改版：用金标集对冠军和候选做盲评对决，输出胜率报告，人工确认后才晋级生产 | `评估 prompt` / `挖矿 prompt 改好了吗` / `eval prompt` / `/wjs-evaling-voicedrop-prompts` |
| [`wjs-voicedrop-choosing-cover`](./wjs-voicedrop-choosing-cover/) | 判断 VoiceDrop 文章是否需要 AI 题图，并选定风格与生成可直接用的 prompt（比例 2.45:1 / 1568×640） | `这篇要不要配题图` / `选个题图风格` / `给这篇出个题图 prompt` / `/wjs-voicedrop-choosing-cover` |
| [`wjs-voicedrop-post-processing`](./wjs-voicedrop-post-processing/) | 新挖 VoiceDrop 文章后处理守护进程（launchd 每 5 分钟触发，无人值守） | `/wjs-voicedrop-post-processing <stem>` |
| [`wjs-voicedrop-reading-aloud`](./wjs-voicedrop-reading-aloud/) | 文字转有声书 mp3（豆包 seed-tts-2.0 多声色编排朗读，先写脚本再合成） | `做成有声书` / `朗读出来` / `读给我听` / `/wjs-voicedrop-reading-aloud` |
| [`wjs-converting-text-to-video`](./wjs-converting-text-to-video/) | 把公众号文章做成竖屏解说短视频 | `article.md` → 1080×1920 MP4（TTS + 水彩背景 + GSAP 动画） |
| [`wjs-creating-video-book`](./wjs-creating-video-book/) | 把一本书做成按章节的 YouTube 横屏视频：VoiceDrop 有声书 mp3 作音轨，GPT Image 2 生成配图，Ken Burns 缓推 + 中心思想大字叠加 | `书名/书架章节` → 每章一支 1920×1080 YouTube 视频 |
| [`wjs-transcribing-audio`](./wjs-transcribing-audio/) | 音视频转字幕（原语言） | 视频/音频 → 同语言 SRT |
| [`wjs-translating-subtitles`](./wjs-translating-subtitles/) | 字幕翻译 + 标点重切 | A 语言 SRT → B 语言 SRT（或双语 SRT） |
| [`wjs-dubbing-video`](./wjs-dubbing-video
