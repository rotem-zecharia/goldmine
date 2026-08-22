# op7418/guizang-ppt-skill

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

## limitations

- 补充更多真实案例和可打开的 HTML deck 示例
- 扩展封面规格,覆盖更多内容平台
- 增加更多瑞士风版式校验规则
- 优化截图再设计和信息图生成工作流
- 整理 WorkBuddy 等平台上架版本
- 增加更多主题包,但继续限制自定义颜色

## FAQ

**可以导出 PPTX 吗?**
当前核心交付是 HTML。你可以用浏览器演示、截图或录屏。如果需要 PPTX,建议把 HTML 页面作为视觉稿再转换,但这不是当前主流程。

**为什么不允许自定义颜色?**
这个 Skill 的重点是稳定产出。自由选色很容易破坏整体风格,所以只允许从预设主题里选。

**我能加自己的版式吗?**
可以。Style A 可以在 `references/layouts.md` 里扩展；Style B 更严格,需要同步更新 `template-swiss.html`、`layouts-swiss.md`、`swiss-layout-lock.md` 和校验器。

**Codex 配图是必须的吗?**
不是。没有配图也能生成 PPT。配图流程只在需要照片、信息图、UI 情景图或封面时使用。

**演讲者模式需要联网或额外服务吗?**
不需要。双窗口同步、备注、计时、排练、自动翻页和标注都在本地浏览器完成。它不会提供实时字幕、手机遥控或 AI 排练评分。

**为什么关掉观众窗口后显示“未连接”?**
演讲者端会通过观众屏确认和心跳判断软件链路。窗口关闭或心跳超时会显示“未连接”,点击“重新打开观众屏”即可恢复。浏览器无法判断 HDMI 或投影仪线缆是否真的接通,现场仍需目视确认。

**怎么更新到最新版?**
重新运行安装命令,或在本地 skill 目录执行 `git pull`。

## 贡献

Bug、排版问题、新布局需求——欢迎开 Issue 或 PR。改动请优先:

- 在 `template.html` 里补类,不要让 layouts.md 使用未定义的类
- 在 `template-swiss.html` 里补类时,同步更新 `layouts-swiss.md` 和 `swiss-layout-lock.md`
- 瑞士风新增规则后,同步更新 `scripts/validate-swiss-deck.mjs`
- 演讲者运行时必须同时更新两套模板,并运行 `scripts/check-presenter-runtime-sync.mjs`；CI 会拦截两份模板的 CSS / JavaScript 漂移
- 演讲备注或现场行为变化时,同步更新 `references/presenter-mode.md`、`references/checklist.md` 和 `scripts/validate-presenter-mode.mjs`
- 把踩过的坑写到 `checklist.md` 对应的 P0 / P1 / P2 / P3 级别
- 新主题色进 `themes.md` 并给出适合的场景

## License

AGPL-3.0 © 2026 [op7418](https://github.com/op7418)
