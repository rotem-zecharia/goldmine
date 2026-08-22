# ultralytics/yolov5

Ultralytics YOLOv5 in PyTorch for object detection, instance segmentation, classification, training, and export.

## installation

pip install ultralytics
```

<div align="center">
  <a href="https://docs.ultralytics.com/models" target="_blank">
  <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/refs/heads/main/yolo/performance-comparison.png" alt="Ultralytics YOLO performance comparison"></a>
</div>

## 📚 Documentation

See the [YOLOv5 Docs](https://docs.ultralytics.com/yolov5) for full documentation on training, testing, and deployment. See below for quickstart examples.

<details open>
<summary>Install</summary>

Clone the repository and install dependencies in a [**Python>=3.8.0**](https://www.python.org/) environment. Ensure you have [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/) installed.

```bash
# Clone the YOLOv5 repository
git clone https://github.com/ultralytics/yolov5

# Navigate to the cloned directory
cd yolov5

# Install required packages
pip install -r requirements.txt
```

</details>

<details open>
<summary>Inference with PyTorch Hub</summary>

Use YOLOv5 via [PyTorch Hub](https://docs.ultralytics.com/yolov5/tutorials/pytorch-hub-model-loading) for inference. [Models](https://github.com/ultralytics/yolov5/tree/master/models) are automatically downloaded from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases).

```python
import torch

## configuration

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

# Define the input image source (URL, local file, PIL image, OpenCV frame, numpy array, or list)
img = "https://ultralytics.com/images/zidane.jpg"  # Example image

# Perform inference (handles batching, resizing, normalization automatically)
results = model(img)

# Process the results (options: .print(), .show(), .save(), .crop(), .pandas())
results.print()  # Print results to console
results.show()  # Display results in a window
results.save()  # Save results to runs/detect/exp
```

</details>

<details>
<summary>Inference with detect.py</summary>

The `detect.py` script runs inference on various sources. It automatically downloads [models](https://github.com/ultralytics/yolov5/tree/master/models) from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases) and saves the results to the `runs/detect` directory.

```bash
# Run inference using a webcam
python detect.py --weights yolov5s.pt --source 0

# Run inference on a local image file
python detect.py --weights yolov5s.pt --source img.jpg

# Run inference on a local video file
python detect.py --weights yolov5s.pt --source vid.mp4

# Run inference on a screen capture
python detect.py --weights yolov5s.pt --source screen

# Run inference on a directory of images
python detect.py --weights yolov5s.pt --source path/to/images/

# Run inference on a text file listing image paths
python detect.py --weights yolov5s.pt --source list.txt

# Run inference on a text file listing stream URLs
python detect.py --weights yolov5s.pt --source list.streams

# Run inference using a glob pattern for images
python detect.py --weights yolov5s.pt --source 'path/to/*.jpg'

# Run inference on a YouTube video URL
python detect.py --weights yolov5s.pt --source 'https://youtu.be/LNwODJXcvt4'

# Run inference on an RTSP, RTMP, or HTTP stream
python detect.py --weights yolov5s.pt --source 'rtsp://example.com/media.mp4'
```

</details>

<details>
<summary>Training</summary>

The commands below demonstrate how to reproduce YOLOv5 [COCO dataset](https://docs.ultralytics.com/datasets/detect/coco) results. Both [models](https://github.com/ultralytics/yolov5/tree/master/models) and [datasets](https://github.com/ultralytics/yolov5/tree/master/data) are downloaded automatically from the latest YOLOv5 [release](https://github.com/ultralytics/yolov5/releases). Training times for YOLOv5n/s/m/l/x are approximately 1/2/4/6/8 days on a single [NVIDIA V100 GPU](https://www.nvidia.com/en-us/data-center/v100/). Using [Multi-GPU training](https://docs.ultralytics.com/yolov5/tutorials/multi-gpu-training) can significantly reduce training time. Use the largest `--batch-size` your hardware allows, or use `--batch-size -1` for YOLOv5 [AutoBatch](https://github.com/ultralytics/yolov5/pull/5092). The batch sizes shown below are for V100-16GB GPUs.

```bash
# Train YOLOv5n on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml --batch-size 128

# Train YOLOv5s on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5s.yaml --batch-size 64

# Train YOLOv5m on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5m.yaml --batch-size 40

# Train YOLOv5l on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5l.yaml --batch-size 24

# Train YOLOv5x on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5x.yaml --batch-size 16
```

<img width="800" src="https://user-images.githubusercontent.com/26833433/90222759-949d8800-ddc1-11ea-9fa1-1c97eed2b963.png" alt="YOLOv5 Training Results">

</details>

<details open>
<summary>Tutorials</summary>

- **[Train Custom Data](https://docs.ultralytics.com/yolov5/tutorials/train-custom-data)** 🚀 **RECOMMENDED**: Learn how to train YOLOv5 on your own datasets.
- **[Tips for Best Training Results](https://docs.

## features

YOLOv5 is designed for simplicity and ease of use. We prioritize real-world performance and accessibility.

<p align="left"><img width="800" src="https://user-images.githubusercontent.com/26833433/155040763-93c22a27-347c-4e3c-847a-8094621d3f4e.png" alt="YOLOv5 Performance Chart"></p>
<details>
  <summary>YOLOv5-P5 640 Figure</summary>

<p align="left"><img width="800" src="https://user-images.githubusercontent.com/26833433/155040757-ce0934a3-06a6-43dc-a979-2edbbd69ea0e.png" alt="YOLOv5 P5 640 Performance Chart"></p>
</details>
<details>
  <summary>Figure Notes</summary>

- **COCO AP val** denotes the [mean Average Precision (mAP)](https://www.ultralytics.com/glossary/mean-average-precision-map) at [Intersection over Union (IoU)](https://www.ultralytics.com/glossary/intersection-over-union-iou) thresholds from 0.5 to 0.95, measured on the 5,000-image [COCO val2017 dataset](https://docs.ultralytics.com/datasets/detect/coco) across various inference sizes (256 to 1536 pixels).
- **GPU Speed** measures the average inference time per image on the [COCO val2017 dataset](https://docs.ultralytics.com/datasets/detect/coco) using an [AWS p3.2xlarge V100 instance](https://aws.amazon.com/ec2/instance-types/p4/) with a batch size of 32.
- **EfficientDet** data is sourced from the [google/automl repository](https://github.com/google/automl) at batch size 8.
- **Reproduce** these results using the command: `python val.py --task study --data coco.yaml --iou 0.7 --weights yolov5n6.pt yolov5s6.pt yolov5m6.pt yolov5l6.pt yolov5x6.pt`

</details>

### Pretrained Checkpoints

This table shows the performance metrics for various YOLOv5 models trained on the COCO dataset.

| Model                                                                                                                                                                   | Size<br><sup>(pixels) | mAP<sup>val<br>50-95 | mAP<sup>val<br>50 | Speed<br><sup>CPU b1<br>(ms) | Speed<br><sup>V100 b1<br>(ms) | Speed<br><sup>V100 b32<br>(ms) | Params<br><sup>(M) | FLOPs<br><sup>@640 (B) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------- | ----------------- | ---------------------------- | ----------------------------- | ------------------------------ | ------------------ | ---------------------- |
| [YOLOv5n](https://platform.ultralytics.com/ultralytics/yolov5/yolov5nu)                                                                                                 | 640                   | 28.0                 | 45.7              | **45**                       | **6.3**                       | **0.6**                        | **1.9**            | **4.5**                |
| [YOLOv5s](https://platform.ultralytics.com/ultralytics/yolov5/yolov5su)                                                                                                 | 640                   | 37.4                 | 56.8              | 98                           | 6.4                           | 0.9                            | 7.2                | 16.5                   |
| [YOLOv5m](https://platform.ultralytics.com/ultralytics/yolov5/yolov5mu)                                                                                                 | 640                   | 45.4                 | 64.1              | 224                          | 8.2                           | 1.7                            | 21.2               | 49.0                   |
| [YOLOv5l](https://platform.ultralytics.com/ultralytics/yolov5/yolov5lu)                                                                                                 | 640                   | 49.0                 | 67.3              | 430                          | 10.1                          | 2.7                            | 46.5               | 109.1                  |
| [YOLOv5x](https://platform.ultral
