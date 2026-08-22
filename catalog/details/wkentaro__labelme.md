# wkentaro/labelme

Image annotation with Python. Supports polygon, rectangle, circle, line, point, and AI-assisted annotation.

## features

- [x] Image annotation for polygon, rectangle, circle, line and point ([tutorial](examples/tutorial))
- [x] Image flag annotation for classification and cleaning ([#166](https://github.com/wkentaro/labelme/pull/166))
- [x] Video annotation ([video annotation](examples/video_annotation))
- [x] GUI customization (predefined labels / flags, auto-saving, label validation, etc) ([#144](https://github.com/wkentaro/labelme/pull/144))
- [x] Exporting VOC-format dataset for [semantic segmentation](examples/semantic_segmentation), [instance segmentation](examples/instance_segmentation)
- [x] Exporting COCO-format dataset for [instance segmentation](examples/instance_segmentation)
- [x] AI-assisted point-to-polygon/mask annotation by SAM, EfficientSAM models
- [x] AI text-to-annotation by YOLO-world, SAM3 models

**🌏 Available in 20 languages** - English · 日本語 · 한국어 · 简体中文 · 繁體中文 · Deutsch · Ελληνικά · Français · Español · Italiano · Português · Nederlands · Magyar · Русский · ไทย · Tiếng Việt · Türkçe · Українська · Polski · فارسی (`LANG=ja_JP.UTF-8 labelme`)

## installation

There are 3 options to install labelme:

## tools

Run `labelme --help` for detail.\
The annotations are saved as a [JSON](http://www.json.org/) file.

```bash
labelme  # just open gui
