# Anionex/banana-slides

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向＂Vibe PPT＂; 支持上传任意模板图片，上传任意素材&智能解析，一句话/大纲/页面描述自动生成PPT，口头修改指定区域、一键导出可编辑ppt - An AI-native slides generator based on nano banana pro🍌

## tools

# OpenAI 格式配置（当 AI_PROVIDER_FORMAT=openai 时使用）
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1
# 代理示例: https://api.inferera.com/v1

# 火山方舟 Agent Plans 配置（当 AI_PROVIDER_FORMAT=volcengine 时使用）
# 注意: Agent Plan 需使用专属 API Key 与模型名 (doubao-seed-2.1-turbo / doubao-seedream-5.0-lite)
VOLCENGINE_API_KEY=your-volcengine-api-key-here
VOLCENGINE_API_BASE=https://ark.cn-beijing.volces.com/api/plan/v3

# Vertex AI 配置（AI_PROVIDER_FORMAT=vertex）
# 需要 GCP 项目和服务账户密钥
# VERTEX_PROJECT_ID=your-gcp-project-id
# VERTEX_LOCATION=global
# GOOGLE_APPLICATION_CREDENTIALS=./gcp-service-account.json

# Lazyllm 格式配置（当 AI_PROVIDER_FORMAT=lazyllm 时使用）
# 选择文本生成和图片生成使用的厂商
TEXT_MODEL_SOURCE=deepseek        # 文本生成模型厂商
IMAGE_MODEL_SOURCE=doubao         # 图片编辑模型厂商
IMAGE_CAPTION_MODEL_SOURCE=qwen   # 图片描述模型厂商

# 各厂商 API Key（只需配置你要使用的厂商）
DOUBAO_API_KEY=your-doubao-api-key            # 火山引擎/豆包
DEEPSEEK_API_KEY=your-deepseek-api-key        # DeepSeek
QWEN_API_KEY=your-qwen-api-key                # 阿里云/通义千问
GLM_API_KEY=your-glm-api-key                  # 智谱 GLM
SILICONFLOW_API_KEY=your-siliconflow-api-key  # 硅基流动
SENSENOVA_API_KEY=your-sensenova-api-key      # 商汤日日新
MINIMAX_API_KEY=your-minimax-api-key          # MiniMax
KIMI_API_KEY=your-kimi-api-key                # 月之暗面 Kimi
PPIO_API_KEY=your-ppio-api-key                # PPIO 派欧云
AIPING_API_KEY=your-aiping-api-key            # AIPing 爱拼
...
```

> Banana Slides explicitly packages the LazyLLM online provider SDKs used by domestic vendors:
> `volcengine-python-sdk[ark]` for Doubao, `dashscope` for Qwen/Wanxiang, and `zhipuai` for GLM/Zhipu.
> LazyLLM also exposes `lazyllm install online-advanced`, but the PyPI wheel may not publish that group as a standard install extra, so Docker/prebuilt images rely on these explicit dependencies instead.
>
> Desktop (PyInstaller) builds register every LazyLLM online vendor explicitly
> (qwen, doubao, deepseek, glm, kimi, minimax, sensenova, siliconflow, ppio,
> aiping, openai) so packaged backends never hit `Unsupported source: ...`.
  
</details>


**使用新版可编辑导出配置方法，获得更好的可编辑导出效果**: 需在[百度智能云平台](https://console.bce.baidu.com/iam/#/iam/apikey/list)（点击此处进入）中获取API KEY，填写在.env文件中的BAIDU_API_KEY字段（有充足的免费使用额度）。详见https://github.com/Anionex/banana-slides/issues/121 中的说明


<details>
  <summary>📒 Vertex AI 配置指南（适用于 GCP 用户）</summary>

Google Cloud Vertex AI 允许通过 GCP 服务账户调用 Gemini 模型，新用户可使用赠金额度。配置步骤：

1. 前往 [GCP Console](https://console.cloud.google.com/)，创建一个服务账户并下载 JSON 格式的密钥文件
2. 将密钥文件保存为项目根目录下的 `gcp-service-account.json`
3. 在 `.env` 中设置：
   ```env
   AI_PROVIDER_FORMAT=vertex
   VERTEX_PROJECT_ID=your-gcp-project-id
   VERTEX_LOCATION=global
   ```
4. 如果使用 Docker 部署，还需要在 `docker-compose.yml` 中取消相关注释，将密钥文件挂载到容器内并设置 `GOOGLE_APPLICATION_CREDENTIALS` 环境变量。

> `gemini-3-*` 系列模型要求 `VERTEX_LOCATION=global`

</details>

2. **启动服务**

**⚡ 使用预构建镜像（推荐）**

项目在 Docker Hub 提供了构建好的前端和后端镜像（同步主分支最新版本），可以跳过本地构建步骤，实现快速部署：

```bash
# 使用预构建镜像启动（无需从头构建）
docker compose -f docker-compose.prod.yml up -d
```

镜像名称：
- `anoinex/banana-slides-frontend:latest`
- `anoinex/banana-slides-backend:latest`

启动后可在应用内进入 **设置 → 关于 → 检查更新**，应用会根据当前版本 SHA 判断是否已有可用更新；源码运行时也会用当前 Git SHA 参与判断。

**从头构建镜像**

```bash
docker compose up -d
```


> [!TIP]
> 如遇网络问题，可在 `.env` 文件中取消镜像源配置的注释, 再重新运行启动命令：
> ```env
> # 在 .env 文件中取消以下注释即可使用国内镜像源
> DOCKER_REGISTRY=docker.1ms.run/
> GHCR_REGISTRY=ghcr.nju.edu.cn/
> APT_MIRROR=mirrors.aliyun.com
> PYPI_INDEX_URL=https://mirrors.cloud.tencent.com/pypi/simple
> NPM_REGISTRY=https://registry.npmmirror.com/
> ```


3. **访问应用**

- 前端：http://localhost:3011
- 后端 API：http://localhost:5011

4. **查看日志**

```bash
# 查看后端日志（最后 200 行）
docker logs --tail 200 banana-slides-backend

# 实时查看后端日志（最后 100 行）
docker logs -f --tail 100 banana-slides-backend

# 查看前端日志（最后 100 行）
docker logs --tail 100 banana-slides-frontend
```

5. **停止服务**

```bash
docker compose down
```

6. **更新项目**

**使用预构建镜像（docker-compose.prod.yml）**

也可以先在应用内进入 **设置 → 关于 → 检查更新** 查看是否已有新版本。

```bash
docker compose -f docker-co
