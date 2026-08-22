# cvat-ai/cvat

Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling service

## installation

> 💡 Want to explore CVAT before deploying anything?
> **[Try CVAT Online (Free plan)](https://app.cvat.ai)** directly in your browser.
> Feature availability and usage limits vary by plan; see
> [CVAT Online pricing](https://www.cvat.ai/pricing/cvat-online) for details.

### Installation

**Prerequisites:**

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

> 💡 CVAT is primarily tested with Chromium-based browsers (Google Chrome, Microsoft Edge).
> Firefox may work with some caveats; Safari/WebKit is not supported.

**1. Start the default stack**

Clone the repository and launch the services.

```bash
git clone https://github.com/cvat-ai/cvat
cd cvat

# Optional: set your IP or domain
# export CVAT_HOST=your-ip-or-domain

docker compose up -d
```

**2. Create an admin account**

```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

See the [Installation Guide](https://docs.cvat.ai/docs/administration/community/basics/installation/) for full
instructions and OS-specific setup.

**3. Sign in and start labeling**

- Open [http://localhost:8080](http://localhost:8080) (or your `CVAT_HOST`) in your browser.
- Log in with your superuser account.
- Create a project or task, upload your data (images, videos, or point clouds), and define labels to start annotating.

Learn more about annotation tools and workflows in the [CVAT Documentation](https://docs.cvat.ai/docs/) or
take our free course – [CVAT Academy](https://www.cvat.ai/resources/academy).

_For alternative deployments (AWS, Kubernetes, external PostgreSQL, backups, upgrades), see the [Deployment Guides](https://docs.cvat.ai/docs/administration/community/advanced/)._

## features

- **[Manual & Auto-labeling](https://docs.cvat.ai/docs/annotation/manual-annotation/):** Annotate images, videos, and
  3D point clouds with bounding boxes, polygons, masks, keypoints, cuboids, tags, and more. Speed up labeling
  by connecting your own models for automatic annotation.
- **[Task Management](https://docs.cvat.ai/docs/workspace/):** Organize datasets into projects, split them into tasks
  and jobs, assign work to annotators, and track progress in real time.
- **[Collaboration](https://docs.cvat.ai/docs/account_management/user-roles/):** Create organizations, invite teammates,
  assign roles, and collaborate on annotations with comments and issues.
- **[Quality Control](https://docs.cvat.ai/docs/qa-analytics/manual-qa/):** Review annotations, flag issues, compare
  results across annotators with consensus, and run Ground Truth and Honeypot checks through the server API.
- **[Analytics](https://docs.cvat.ai/docs/administration/community/advanced/analytics/):** Monitor user activity,
  working time by job, events, and server logs with Grafana dashboards.
- **[Data Ops & Integrations](https://docs.cvat.ai/docs/dataset_management/export-datasets/):** Export/import in 20+
  formats (COCO, YOLO, Pascal VOC, KITTI, etc.), connect to cloud storage (S3, Azure, Google Cloud), and automate
  via REST API and Python SDK.

Advanced capabilities such as advanced project analytics, quality control UI, built-in auto-labeling with SAM 2
 and SAM 3, AI agents, SSO, and more are available in [CVAT Online](https://www.cvat.ai/pricing/cvat-online)
 paid plans (Solo, Team) and [CVAT Enterprise](https://www.cvat.ai/enterprise).

## tools

CVAT is designed for automation. Beyond the Web UI, you can integrate it into your pipelines using:

- [Python SDK](https://docs.cvat.ai/docs/api_sdk/sdk/): install with `pip install cvat-sdk` and automate task creation,
uploads, and exports from Python.
- [Command line tool](https://docs.cvat.ai/docs/api_sdk/cli/): install with `pip install cvat-cli`
and script common CVAT workflows from the terminal.
- [REST API](https://docs.cvat.ai/docs/api_sdk/api/): full programmatic control over CVAT.

## Data and Formats

CVAT Community supports image, video, and 3D (point cloud) annotation workflows. You can move data in and out using 20+
industry-standard formats: CVAT (XML), COCO (JSON), YOLO (TXT), Ultralytics YOLO (TXT/YAML), Pascal VOC (XML),
KITTI (TXT), MOT (TXT), and more.

[Full list of supported formats.](https://docs.cvat.ai/docs/dataset_management/formats/)

## ML and AI Models

CVAT Community supports automatic annotation via pre-built serverless models powered by Nuclio,
covering detection, segmentation, pose estimation, and tracking:

| Model | Framework | Type |
| --- | --- | --- |
| [Segment Anything (SAM)](https://github.com/cvat-ai/cvat/tree/develop/serverless/pytorch/facebookresearch/sam/nuclio) | PyTorch | Interactor |
| [Inside-Outside Guidance (IOG)](https://github.com/cvat-ai/cvat/tree/develop/serverless/pytorch/shiyinzhang/iog/nuclio) | PyTorch | Interactor |
| [RetinaNet R101](https://github.com/cvat-ai/cvat/tree/develop/serverless/pytorch/facebookresearch/detectron2/retinanet_r101/nuclio) | PyTorch | Detector |
| [HRNet32 Whole Body Pose](https://github.com/cvat-ai/cvat/tree/develop/serverless/pytorch/mmpose/hrnet32/nuclio) | PyTorch | Pose Estimation |
| [TransT](https://github.com/cvat-ai/cvat/tree/develop/serverless/pytorch/dschoerk/transt/nuclio) | PyTorch | Tracker |
| [YOLO v7](https://github.com/cvat-ai/cvat/tree/develop/serverless/onnx/WongKinYiu/yolov7/nuclio) | ONNX | Detector |
| [Mask RCNN Inception ResNet v2](https://github.com/cvat-ai/cvat/tree/develop/serverless/openvino/omz/public/mask_rcnn_inception_resnet_v2_atrous_coco/nuclio) | OpenVINO | Detector |
| [Face Detection 0205](https://github.com/cvat-ai/cvat/tree/develop/serverless/openvino/omz/intel/face-detection-0205/nuclio) | OpenVINO | Detector |
| [Faster RCNN Inception v2](https://github.com/cvat-ai/cvat/tree/develop/serverless/tensorflow/faster_rcnn_inception_v2_coco/nuclio) | TensorFlow | Detector |

To enable automatic annotation, add the serverless component to your deployment:

```bash
docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
```

This starts the serverless infrastructure. To make models available in CVAT, install `nuctl` and deploy
the functions you need, for example SAM or YOLO, as described in the [Automatic Annotation Guide](https://docs.cvat.ai/docs/annotation/auto-annotation/automatic-annotation/).

## Which CVAT edition should I choose?

- **CVAT Online**: the fastest way to try CVAT and start labeling without deployment. Use it to evaluate CVAT in
the browser, explore managed features, and move to cost-efficient paid plans when you need more capacity or team
workflows.
- **CVAT Community**: the MIT-licensed self-hosted edition for teams that want to run CVAT themselves, customize the
stack, and control their infrastructure.
- **CVAT Enterprise**: for organizations that need CVAT in their own cloud or internal environment, enterprise support,
security controls such as SSO, paid platform features, and SLAs.
- **Labeling Services**: for teams that want to outsource annotation work to CVAT.ai’s experienced labeling team instead
of building an internal labeling operation. Customers get trial access to CVAT Online during the project.

For detailed plan limits and feature availability, see [CVAT Online pricing](https://www.cvat.ai/pricing/cvat-online),
 [CVAT Enterprise](https://www.cvat.ai/enterprise), and [Labeling Services](https://www.cvat.ai/annotation-services).

## S
