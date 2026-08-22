# coze-dev/coze-studio

An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze your way to AI Agent creation.

## features

| **Module** | **Feature** |
| --- | --- |
| Model service | Manage the model list, integrate services such as OpenAI and Volcengine |
| Build agent | * Build, publish, and manage agent <br> * Support configuring workflows, knowledge bases, and other resources |
| Build apps | * Create and publish apps <br> * Build business logic through workflows |
| Build a workflow | Create, modify, publish, and delete workflows |
| Develop resources | Support creating and managing the following resources: <br> * Plugins <br> * Knowledge bases <br> * Databases <br> * Prompts |
| API and SDK | * Create conversations, initiate chats, and other OpenAPI <br> * Integrate agents or apps into your own app through Chat SDK |

## installation

Learn how to obtain and deploy the open-source version of Coze Studio, quickly build projects, and experience Coze Studio's open-source version.

Environment requirements:

* Before installing Coze Studio, please ensure that your machine meets the following minimum system requirements: 2 Core、4 GB
* Pre-install Docker and Docker Compose, and start the Docker service.

Deployment steps:

1. Retrieve the source code.
   ```Bash
   # Clone code
   git clone https://github.com/coze-dev/coze-studio.git
   ```
2. Deploy and start the service. When deploying and starting Coze Studio for the first time, it may take a while to retrieve images and build local images. Please be patient. If you see the message "Container coze-server Started," it means the Coze Studio service has started successfully.

   ```Bash
   cd coze-studio
   # start service
   # for macOS or Linux
   make web  
   # for windows
   cp ./docker/.env.example ./docker/.env
   docker compose -f ./docker/docker-compose.yml up
   ```

   For common startup failure issues, **please refer to the [FAQ](https://github.com/coze-dev/coze-studio/wiki/9.-FAQ)**.
3.	Register an account by visiting `http://localhost:8888/sign`, entering your username and password, and clicking the Register button.
4.	Configure the model at `http://localhost:8888/admin/#model-management` by adding a new model. (The image version must be greater than or equal to 0.5.0.)
5.	Visit Coze Studio at `http://localhost:8888/`.

> [!WARNING]
> If you want to deploy Coze Studio in a public network environment, it is recommended to assess security risks before you begin, and take corresponding protection measures. Possible security risks include account registration functions, Python execution environments in workflow code nodes, Coze Server listening address configurations, SSRF (Server - Side Request Forgery), and some horizontal privilege escalations in APIs.  For more details, refer to [Quickstart](https://github.com/coze-dev/coze-studio/wiki/2.-Quickstart#security-risks-in-public-networks).

## Developer Guide

* **Project Configuration**:
   * [Model Configuration](https://github.com/coze-dev/coze-studio/wiki/3.-Model-configuration): Before deploying the open-source version of Coze Studio, you must configure the model service. Otherwise, you cannot select models when building agents, workflows, and apps.
   * [Plugin Configuration](https://github.com/coze-dev/coze-studio/wiki/4.-Plugin-Configuration): To use official plugins from the plugin store, you must first configure the plugins and add the authentication keys for third-party services.
   * [Basic Component Configuration](https://github.com/coze-dev/coze-studio/wiki/5.-Basic-component-configuration): Learn how to configure components such as image uploaders to use functions like image uploading in Coze Studio .
* [API Reference](https://github.com/coze-dev/coze-studio/wiki/6.-API-Reference): The Coze Studio Community Edition API and Chat SDK are authenticated using Personal Access Token, providing APIs for conversations and workflows.
* [Development Guidelines](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards):
   * [Project Architecture](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#project-architecture): Learn about the technical architecture and core components of the open-source version of Coze Studio.
   * [Code Development and Testing](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#code-development-and-testing): Learn how to perform secondary development and testing based on the open-source version of Coze Studio.
   * [Troubleshooting](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#troubleshooting): Learn how to view container states and system logs.

## Using the open-source version of Coze Studio
> Regarding how to use Coze Studio, refer to the [Coze Development Platform Official Documentation Center](https://www.coze.cn/open/docs) for more informatio
