# roboflow/rf-detr

RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026]

## installation

To install RF-DETR, install the `rfdetr` package in a [**Python>=3.10**](https://www.python.org/) environment with `pip`.

```bash
pip install rfdetr
```

<details>
<summary>Install from source</summary>

<br>

By installing RF-DETR from source, you can explore the most recent features and enhancements that have not yet been officially released. **Please note that these updates are still in development and may not be as stable as the latest published release.**

```bash
pip install https://github.com/roboflow/rf-detr/archive/refs/heads/develop.zip
```

</details>

## Benchmarks

RF-DETR achieves state-of-the-art results in both object detection and instance segmentation, with benchmarks reported on Microsoft COCO and RF100-VL (RF100-VL for detection only). The charts and tables below compare RF-DETR against other top real-time models across accuracy and latency for detection and segmentation. All COCO accuracy numbers are measured in-house for every model shown, computed with pycocotools in SAB over the full 5,000-image `val2017` split, so every row is directly comparable and may differ from vendor-reported figures. The sole exception is rows marked †, which are quoted from the original authors' paper and were not measured in SAB. All latency numbers were measured on an NVIDIA T4 using TensorRT, FP16, and batch size 1. Parameter counts are deployment (fused) `nn.Module` parameter counts (`model.parameters()`, not the raw tensor count of the saved checkpoint), except rows marked †, which are the authors' reported counts. For full benchmarking methodology and reproducibility details, see [roboflow/sab](https://github.com/roboflow/single_artifact_benchmarking).

### Detection

<img alt="rf_detr_1-4_latency_accuracy_object_detection" src="https://storage.googleapis.com/com-roboflow-marketing/rf-detr/rf_detr_1-4_latency_accuracy_object_detection.png" />

<details>
<summary>See object detection benchmark numbers</summary>

<br>

| Architecture  | COCO AP<sub>50</sub> | COCO AP<sub>50:95</sub> | RF100VL AP<sub>50</sub> | RF100VL AP<sub>50:95</sub> | Latency (ms) | Params (M) | Resolution |  License   |
| :-----------: | :------------------: | :---------------------: | :---------------------: | :------------------------: | :----------: | :--------: | :--------: | :--------: |
|   RF-DETR-N   |         67.6         |          48.4           |          85.0           |            57.7            |     2.3      |    30.5    |  384x384   | Apache 2.0 |
|   RF-DETR-S   |         72.1         |          53.0           |          86.7           |            60.2            |     3.5      |    32.1    |  512x512   | Apache 2.0 |
|   RF-DETR-M   |         73.6         |          54.7           |          87.4           |            61.2            |     4.4      |    33.7    |  576x576   | Apache 2.0 |
|   RF-DETR-L   |         75.1         |          56.5           |          88.2           |            62.2            |     6.8      |    33.9    |  704x704   | Apache 2.0 |
| RF-DETR-XL △  |         77.4         |          58.6           |          88.5           |            62.9            |     11.5     |   126.4    |  700x700   |  PML 1.0   |
| RF-DETR-2XL △ |         78.5         |          60.1           |          89.0           |            63.2            |     17.2     |   126.9    |  880x880   |  PML 1.0   |
|   YOLO11-N    |         52.0         |          37.4           |          81.4           |            55.3            |     2.5      |    2.6     |  640x640   |  AGPL-3.0  |
|   YOLO11-S    |         59.7         |          44.4           |          82.3           |            56.2            |     3.2      |    9.4     |  640x640   |  AGPL-3.0  |
|   YOLO11-M    |         64.1         |          48.6           |          82.5           |            56.5            |     5.1      |    20.1    |  640x640   |  AGPL-3.0  |
|   YOLO11-L    |         64.9         |          49.9           |          82.2           |            56.
