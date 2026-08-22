# CVHub520/X-AnyLabeling

X-AnyLabeling: A lightweight, efficient, and unified cross-platform desktop application for annotating text, image, video, and multimodal data, combining versatile built-in tools with state-of-the-art

## features

<img src="https://github.com/user-attachments/assets/2925bc88-e22b-4e81-873c-45fd85164f6b" width="100%" />

* Unified support for annotating and processing text, image, video, and multimodal data.
* Covers tasks such as image classification, object detection, instance segmentation, pose estimation, oriented object detection, multi-object tracking, optical character recognition, lane annotation, image captioning, visual question answering, and document parsing.
* Provides polygons, rectangles, cuboids, rotated boxes, quadrilaterals, circles, lines, polylines, points, masks, and task-specific tools for text detection, text recognition, and KIE.
* Integrates a wide range of state-of-the-art deep learning models for AI-assisted annotation, automated labeling, and batch dataset prediction.
* Supports both local and remote inference through engines and serving frameworks such as `ONNX Runtime`, `TensorRT`, `OpenCV DNN`, `vLLM`, and `SGLang`.
* Supports importing and exporting formats such as `COCO`, `VOC`, `YOLO`, `DOTA`, `MOT`, `MASK`, `PPOCR`, `MMGD`, `VLM-R1`, and `ShareGPT`.
* Runs on Windows, Linux, and macOS, with interfaces available in English, Simplified Chinese, Japanese, and Korean.
* Supports custom model integration, flexible extension, and secondary development.

## tools

- [Classification](./examples/classification/)
  - [Image-Level](./examples/classification/image-level/README.md)
  - [Shape-Level](./examples/classification/shape-level/README.md)
- [Detection](./examples/detection/)
  - [HBB Object Detection](./examples/detection/hbb/README.md)
  - [OBB Object Detection](./examples/detection/obb/README.md)
- [Segmentation](./examples/segmentation/README.md)
  - [Instance Segmentation](./examples/segmentation/instance_segmentation/)
  - [Binary Semantic Segmentation](./examples/segmentation/binary_semantic_segmentation/)
  - [Multiclass Semantic Segmentation](./examples/segmentation/multiclass_semantic_segmentation/)
- [Description](./examples/description/)
  - [Tagging](./examples/description/tagging/README.md)
  - [Captioning](./examples/description/captioning/README.md)
- [Estimation](./examples/estimation/)
  - [Face Estimation](./examples/estimation/face_estimation/README.md)
  - [Pose Estimation](./examples/estimation/pose_estimation/README.md)
  - [Depth Estimation](./examples/estimation/depth_estimation/README.md)
- [OCR](./examples/optical_character_recognition/)
  - [Text Recognition](./examples/optical_character_recognition/text_recognition/)
  - [Key Information Extraction](./examples/optical_character_recognition/key_information_extraction/README.md)
- [MOT](./examples/multiple_object_tracking/README.md)
  - [Tracking by HBB Object Detection](./examples/multiple_object_tracking/README.md)
  - [Tracking by OBB Object Detection](./examples/multiple_object_tracking/README.md)
  - [Tracking by Instance Segmentation](./examples/multiple_object_tracking/README.md)
  - [Tracking by Pose Estimation](./examples/multiple_object_tracking/README.md)
- [iVOS](./examples/interactive_video_object_segmentation)
  - [SAM2-Video](./examples/interactive_video_object_segmentation/sam2/README.md)
  - [SAM3-Video](./examples/interactive_video_object_segmentation/sam3/README.md)
- [Matting](./examples/matting/)
  - [Image Matting](./examples/matting/image_matting/README.md)
- [Vision-Language](./examples/vision_language/)
  - [Rex-Omni](./examples/vision_language/rexomni/README.md)
  - [Florence 2](./examples/vision_language/florence2/README.md)
- [Counting](./examples/counting/)
  - [GeCo](./examples/counting/geco/README.md)
  - [GeCo2](./examples/counting/geco2/README.md)
- [Grounding](./examples/grounding/)
  - [YOLOE](./examples/grounding/yoloe/README.md)
  - [SAM 3](./examples/grounding/sam3/README.md)
  - [LocateAnything](./examples/grounding/locateanything/README.md)
- [Training](./examples/training/)
  - [Ultralytics](./examples/training/ultralytics/README.md)
