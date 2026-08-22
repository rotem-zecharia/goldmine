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

# Load a YOLOv3 model (choices: 'yolov3', 'yolov3_spp', 'yolov3_tiny')
model = torch.hub.load("ultralytics/yolov3", "yolov3", pretrained=True)

# Run inference on an image (local file, URL, PIL image, OpenCV frame, or numpy array)
results = model("https://ultralytics.com/images/zidane.jpg")

# Inspect the results
results.print()  # print detections to the console
results.show()  # display the annotated image
results.save()  # save the annotated image to runs/detect/exp
```

</details>

<details>
<summary>Inference with detect.py</summary>

`detect.py` runs inference on a wide range of sources, downloading models automatically and saving results to `runs/detect`.

```bash
python detect.py --weights yolov3.pt --source 0                              # webcam
python detect.py --weights yolov3.pt --source img.jpg                        # image
python detect.py --weights yolov3.pt --source vid.mp4                        # video
python detect.py --weights yolov3.pt --source screen                         # screenshot
python detect.py --weights yolov3.pt --source path/                          # directory
python detect.py --weights yolov3.pt --source 'path/*.jpg'                   # glob
python detect.py --weights yolov3.pt --source 'rtsp://example.com/media.mp4' # RTSP, RTMP, HTTP stream
```

</details>

<details>
<summary>Training</summary>

Train YOLOv3 on the [COCO](https://docs.ultralytics.com/datasets/detect/coco) dataset. Models and datasets download automatically. Use the largest `--batch-size` your hardware allows.

```bash
# Train YOLOv3-tiny
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov3-tiny.yaml --batch-size 64

# Train YOLOv3
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov3.yaml --batch-size 32

# Train YOLOv3-SPP
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov3-spp.yaml --batch-size 16
```

Validate accuracy with `python val.py --weights yolov3.pt --data coco.yaml`, and export to other formats (TorchScript, ONNX, OpenVINO, TensorRT, CoreML, and PaddlePaddle) with `python export.py --weights yolov3.pt --include onnx`.

</details>

<details>
<summary>Tutorials</summary>

These guides cover the shared Ultralytics training framework and apply to YOLOv3:

- [Train Custom Data](https://docs.ultralytics.com/modes/train) — train on your own dataset.
- [Tips for Best Training Results](https://docs.ultralytics.com/guides/model-training-tips) — get the most out of training.
- [Multi-GPU Training](https://docs.ultralytics.com/yolov5/tutorials/multi-gpu-training) — scale training across GPUs.
- [PyTorch Hub Loading](https://docs.ultralytics.com/yolov5/tutorials/pytorch-hub-model-loading) — load models programmatically.
- [Model Export](https://docs.ultralytics.com/modes/export) — deploy to ONNX, TensorRT, CoreML, and more.
- [Test-Time Augmentation (TTA)](https://docs.ultralytics.com/yolov5/tutorials/test-time-augmentation) — improve accuracy at inference.
- [Model Ensembling](https://docs.ultralytics.com/yolov5/tutorials/model-ensembling) — combine models for better results.
- [Hyperparameter Tuning](https://docs.ultralytics.com/guides/hyperparameter-tuning) — tune hyperparameters automatically.
- [Transfer Learning with Frozen Layers](https://docs.ultralytics.com/yolov5/tutorials/transfer-learning-with-frozen-layers) — adapt pretrained models efficiently.

</details>

## 🧠 Architecture

YOLOv3 builds detection on a few core ideas that make it both accurate and fast:

- **Darknet-53 backbone** — a 53-layer convolutional feature extractor with residual (skip) connections, deeper and more accurate than the Darknet-19 backbone of YOLOv2 while staying efficient.
- **Multi-s

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

## 🤝 Contribute

Contributions are welcome! Please see the [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started, and share your feedback through the [Ultralytics Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). Thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/yolov3/graphs/contributors)

## 📜 License

Ultralytics offers two licensing options:

- **AGPL-3.0 License**: An [OSI-approved](https://opensource.org/license/agpl-3.0) open-source license ideal for research and collaboration. See the [LICENSE](https://github.com/ultralytics/yolov3/blob/master/LICENSE) file for details.
- **Enterprise License**: For commercial use, this license allows integration of Ultralytics software and models into commercial products without AGPL-3.0 obligations. Contact us via [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📧 Contact

For bug reports and feature requests, please use [GitHub Issues](https://github.com/ultralytics/yolov3/issues). For questions and discussion, join our [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Forums](https://community.ultralytics.com).

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultraly
