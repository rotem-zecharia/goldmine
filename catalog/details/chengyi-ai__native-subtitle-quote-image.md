# chengyi-ai/native-subtitle-quote-image

保留视频内嵌字幕，精确取帧并生成 3:4 社交长图的 Agent Skill

## installation

在 Codex 中调用 `$skill-installer`，并让它安装下面的 Skill 目录：

```text
https://github.com/chengyi-ai/native-subtitle-quote-image/tree/main/skills/native-subtitle-quote-image
```

### 手动安装到 Codex

```bash
git clone https://github.com/chengyi-ai/native-subtitle-quote-image.git
cp -R native-subtitle-quote-image/skills/native-subtitle-quote-image ~/.agents/skills/
```

重新打开 Codex 任务后即可使用 `$native-subtitle-quote-image`。

### 其他 Agent

该 Skill 使用开放的 Agent Skills 目录格式。把 `skills/native-subtitle-quote-image/` 复制到目标 Agent 支持的 Skills 目录；具体目录和启用方式以目标 Agent 的说明为准。

## 依赖

- Python 3.10+
- Pillow
- FFmpeg，或可提供 FFmpeg 的 `imageio-ffmpeg`

```bash
python3 -m pip install -r skills/native-subtitle-quote-image/requirements.txt
```

## 使用

在 Agent 中输入：

```text
使用 $native-subtitle-quote-image，把这个带内嵌中文字幕的视频做成原生字幕拼图。
```

Agent 会先检查视频字幕与裁切区域，再选择字幕稳定出现的时间点，最后生成：

- 逐张 3:4 JPG；
- `原生字幕时间点.json`；
- `final_contact_sheet.jpg` 总览图。

## 适用边界

- 只适用于字幕已经烧录在视频画面中的素材。
- 外挂字幕、自动翻译或重新绘制字幕不属于这个 Skill 的工作范围。
- 使用者应确保自己有权处理和发布输入视频及生成画面。

## 开源许可

代码与 Skill 指令采用 [MIT License](LICENSE)。输入视频、生成图片及其中出现的第三方内容不因本许可证获得额外授权。
