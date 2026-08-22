# LaoFeng-mouse/flyingmouse-format

飞鼠格式 FlyingMouse Format - Windows 免费文件格式转换工具（离线可用，内置 FFmpeg/LibreOffice/Poppler/Tesseract）。图片/文档/表格/PPT/PDF/音视频/WPS 格式互转 + OCR + 批量转换；音频仅支持普通格式。作者：牢蜂（LaoFeng）｜仅供个人免费使用，禁止商业售卖/转卖/套壳

## installation

1. Download the v0.6.4 build for your system from [Releases](https://github.com/LaoFeng-mouse/flyingmouse-format/releases/latest).
2. Install and launch FlyingMouse Format.
3. Drop in files, choose a target, and convert.
4. Choose a save location. The app remembers both the target preference and save folder.

> The source repository excludes the large FFmpeg, LibreOffice, Poppler, and Tesseract bundles. Regular users should install the Release build. Developers need to provide the corresponding resources under `bin/` for the complete conversion feature set.

CLI examples:

```powershell
node cli.js capabilities --json
node cli.js targets example.pdf --json
node cli.js convert input.docx --to pdf --output output.pdf --json
node cli.js convert a.png b.png --to webp --output-dir converted --json
node cli.js images-to-pdf 1.jpg 2.jpg --output album.pdf --json
node cli.js merge-pdfs a.pdf b.pdf --output merged.pdf --json
```

Packaged builds accept the same commands after `--cli`: use `FlyingMouse Format.app/Contents/MacOS/FlyingMouse Format --cli ...` on macOS or `FlyingMouse Format.exe --cli ...` on Windows. “Connect to Agent” discovers existing Codex, Claude, and generic Agent skill directories and installs the bundled lightweight wrapper after confirmation.
