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

### Choose a Windows build

- **Windows 10 / 11 x64 (recommended):** use `FlyingMouse-Format-Setup-0.6.4-x64.exe` with Electron 43, Sharp 0.35, and PDF.js 6.
- **Windows 7 SP1 x64 (compatibility build):** use `FlyingMouse.Format-Setup-0.6.4-win7-x64.exe`, derived from the same source and mouse UI with Electron 22.3.27, Sharp 0.32.6, and PDF.js 2.16.105 pinned in isolation.

The Windows 7 package is a Legacy build and does not downgrade the standard build. Electron 22 no longer receives upstream security maintenance, and other known legacy dependency risks cannot be upgraded without dropping Windows 7. PDF.js dynamic evaluation is disabled as a mitigation, but this build should remain offline and process trusted files only. v0.6.4 passed Windows, native macOS arm64, and native macOS x64 automation gates plus real-sample regressions; acceptance on a physical Windows 7 SP1 x64 system is still pending. Both Windows installers are unsigned and may trigger SmartScreen.

### Choose a macOS build

- **Apple Silicon (M1 or newer):** use `FlyingMouse.Format-Setup-0.6.4-mac-arm64.dmg`.
- **Intel Mac:** use `FlyingMouse.Format-Setup-0.6.4-mac-x64.dmg`.

The first macOS packages support macOS 11 or newer and are unsigned and unnotarized, so Gatekeeper may warn. Both architectures passed pinned-engine, full-conversion, bundle, and 12-second launch gates on native GitHub runners; physical Mac acceptance remains pending.

The complete build requires only:

```powershell
npm run dist:win7
```

The Win7 staging tree is rebuilt with its dedicated `win7-package-lock.json` via `npm ci`. Node.js 22 LTS is recommended (host majors 18–22 are accepted; other majors fail before staging changes). The script binds child processes to the active Node, copies sources safely on Unicode paths, binds the staged manifest/lockfile, and rejects local builder or packaged resources that escape their allowed roots or traverse junctions/symlinks.

Use `node scripts/build-win7.js --prepare-only` only to inspect staging without packaging. A complete build prepares staging again.

## Supported formats / 支持格式

| Category / 类别 | Input / 输入 | Output / 输出 |
|---|---|---|
| Images / 图片 | jpg, png, webp, avif, tiff, gif, bmp, heic, heif, cr2, cr3, crw, nef, arw, dng, raf, rw2, orf, pef, srw, 3fr, erf, fff, iiq, kdc, mef, mrw, x3f | png, jpg, webp, avif, tiff, gif (动图), pdf, txt (OCR), mp4, webm |
| Text / 文本 | txt, md, html, json, csv, log, xml, yaml | txt, md, html, json, csv, pdf, docx, epub |
| E-book / 电子书 | epub, mobi | txt, md, epub (mobi→epub 实验性) |
| Word/WPS/OFD | doc, docx, odt, rtf, wps, wpt, wpd, ofd | pdf, docx, odt, rtf, txt, html, md |
| Excel/WPS | xls, xlsx, xlsm, ods, csv, tsv, et, ett | pdf, xlsx, xls, o
