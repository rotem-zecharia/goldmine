# ultralytics/yolov3

PyTorch implementation of YOLOv3, YOLOv3-SPP, and YOLOv3-tiny for real-time object detection with training, validation, inference, and multi-format export.

## installation

pip install -r requirements.txt
```

</details>

<details open>
<summary>Inference with PyTorch Hub</summary>

Load YOLOv3 directly through [PyTorch Hub](https://docs.ultralytics.com/yolov5/tutorials/pytorch-hub-model-loading). Weights download automatically on first use.

```python
import torch

## features

YOLOv3 was a landmark in real-time object detection and remains a dependable, well-understood baseline:

- **Real-time single-stage detection** — one forward pass produces all detections, with no separate region-proposal stage.
- **Strong across object sizes** — multi-scale predictions handle small, medium, and large objects.
- **Multi-label friendly** — independent logistic classifiers allow overlapping class labels.
- **Simple and portable** — a fully-convolutional design that trains and exports cleanly to many deployment formats.

For the broader family of Ultralytics YOLO models, see the [Ultralytics repository](https://github.com/ultralytics/ultralytics).

## configuration

Get started quickly with pre-configured environments. Click an icon below for setup details.

<div align="center">
  <a href="https://docs.ultralytics.com/integrations/paperspace">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-gradient.png" width="10%" alt="Run on Gradient"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://docs.ultralytics.com/integrations/google-colab">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-colab-small.png" width="10%" alt="Open In Colab"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://docs.ultralytics.com/integrations/kaggle">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-kaggle-small.png" width="10%" alt="Open In Kaggle"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://docs.ultralytics.com/guides/docker-quickstart">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-docker-small.png" width="10%" alt="Docker Image"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://docs.ultralytics.com/integrations/amazon-sagemaker">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-aws-small.png" width="10%" alt="AWS Marketplace"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://docs.ultralytics.com/yolov5/environments/google-cloud-quickstart-tutorial">
    <img src="https://github.com/ultralytics/assets/releases/download/v0.0.0/logo-gcp-small.png" width="10%" alt="GCP Quickstart"/></a>
</div>
