# ultralytics/yolov5

Ultralytics YOLOv5 in PyTorch for object detection, instance segmentation, classification, training, and export.

## installation

pip install ultralytics
```

<div align="center">
  <a href="https://docs.ultralytics.com/models" target="_blank">
  <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/refs/heads/main/yolo/performance-comparison.png" alt="Ultralytics YOLO performance comparison"></a>
</div>

## configuration

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

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
