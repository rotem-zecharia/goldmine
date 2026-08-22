# Wei-Shaw/claude-relay-service

CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。

## tools

给每个使用者分配一个Key：

1. 点击「API Keys」标签
2. 点击「创建新Key」
3. 给Key起个名字，比如「张三的Key」
4. 设置使用限制（可选）：
   - **速率限制**: 限制每个时间窗口的请求次数和Token使用量
   - **并发限制**: 限制同时处理的请求数
   - **模型限制**: 限制可访问的模型列表
   - **客户端限制**: 限制只允许特定客户端使用（如ClaudeCode、Gemini-CLI等）
5. 保存，记下生成的Key

### 4. 开始使用 Claude Code 和 Gemini CLI

现在你可以用自己的服务替换官方API了：

**Claude Code 设置环境变量：**


**使用标准 Claude 账号池**

默认使用标准 Claude 账号池：

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:3000/api/" # 根据实际填写你服务器的ip地址或者域名
export ANTHROPIC_AUTH_TOKEN="后台创建的API密钥"
```

**使用 Antigravity 账户池**

适用于通过 Antigravity 渠道使用 Claude 模型（如 `claude-opus-4-5` 等）。

```bash
# 1. 设置 Base URL 为 Antigravity 专用路径
export ANTHROPIC_BASE_URL="http://127.0.0.1:3000/antigravity/api/"

# 2. 设置 API Key（在后台创建，权限需包含 'all' 或 'gemini'）
export ANTHROPIC_AUTH_TOKEN="后台创建的API密钥"

# 3. 指定模型名称（直接使用短名，无需前缀！）
export ANTHROPIC_MODEL="claude-opus-4-5"

# 4. 启动
claude
```

**VSCode Claude 插件配置：**

如果使用 VSCode 的 Claude 插件，需要在 `~/.claude/config.json` 文件中配置：

```json
{
    "primaryApiKey": "crs"
}
```

如果该文件不存在，请手动创建。Windows 用户路径为 `C:\Users\你的用户名\.claude\config.json`。

> 💡 **IntelliJ IDEA 用户推荐**：[Claude Code Plus](https://github.com/touwaeriol/claude-code-plus) - 将 Claude Code 直接集成到 IDE，支持代码理解、文件读写、命令执行。插件市场搜索 `Claude Code Plus` 即可安装。

**Gemini CLI 设置环境变量：**

**方式一（推荐）：通过 Gemini Assist API 方式访问**

```bash
CODE_ASSIST_ENDPOINT="http://127.0.0.1:3000/gemini"  # 根据实际填写你服务器的ip地址或者域名
GOOGLE_CLOUD_ACCESS_TOKEN="后台创建的API密钥"
GOOGLE_GENAI_USE_GCA="true"
GEMINI_MODEL="gemini-2.5-pro" # 如果你有gemini3权限可以填： gemini-3-pro-preview
```

> **认证**：只能选 ```Login with Google``` 进行认证，如果跳 Google请删除 ```~/.gemini/settings.json``` 后再尝试启动```gemini```。  
> **注意**：gemini-cli 控制台会提示 `Failed to fetch user info: 401 Unauthorized`，但使用不受任何影响。  

**方式二：通过 Gemini API 方式访问**


```bash
GOOGLE_GEMINI_BASE_URL="http://127.0.0.1:3000/gemini"  # 根据实际填写你服务器的ip地址或者域名
GEMINI_API_KEY="后台创建的API密钥"
GEMINI_MODEL="gemini-2.5-pro" # 如果你有gemini3权限可以填： gemini-3-pro-preview
```

> **认证**：只能选 ```Use Gemini API Key``` 进行认证，如果提示 ```Enter Gemini API Key``` 请直接留空按回车。如果一打开就跳 Google请删除 ```~/.gemini/settings.json``` 后再尝试启动```gemini```。

> 💡 **进阶用法**：想在 Claude Code 中直接使用 Gemini 3 模型？请参考 [Claude Code 调用 Gemini 3 模型指南](docs/claude-code-gemini3-guide/README.md)

**使用 Claude Code：**

```bash
claude
```

**使用 Gemini CLI：**

```bash
gemini  # 或其他 Gemini CLI 命令
```

**Codex 配置：**

在 `~/.codex/config.toml` 文件**开头**添加以下配置：

```toml
model_provider = "crs"
model = "gpt-5.5"
model_reasoning_effort = "high"
disable_response_storage = true
preferred_auth_method = "apikey"

[model_providers.crs]
name = "crs"
base_url = "http://127.0.0.1:3000/openai"  # 根据实际填写你服务器的ip地址或者域名
wire_api = "responses"
requires_openai_auth = true
```

在 `~/.codex/auth.json` 文件中配置API密钥为 null：

```json
{
    "OPENAI_API_KEY": "后台创建的API密钥"  
}
```

> ⚠️ 在通过 Nginx 反向代理 CRS 服务并使用 Codex CLI 时，需要在 http 块中添加 underscores_in_headers on;。因为 Nginx 默认会移除带下划线的请求头（如 session_id），一旦该头被丢弃，多账号环境下的粘性会话功能将失效。

**Droid CLI 配置：**

Droid CLI 读取 `~/.factory/config.json`。可以在该文件中添加自定义模型以指向本服务的新端点：

```json
{
  "custom_models": [
    {
      "model_display_name": "Opus 4.5 [crs]",
      "model": "claude-opus-4-5-20251101",
      "base_url": "http://127.0.0.1:3000/droid/claude",
      "api_key": "后台创建的API密钥",
      "provider": "anthropic",
      "max_tokens": 64000
    },
    {
      "model_display_name": "GPT5.5 [crs]",
      "model": "gpt-5.5",
      "base_url": "http://127.0.0.1:3000/droid/openai",
      "api_key": "后台创建的API密钥",
      "provider": "openai",
      "max_tokens": 16384
    },
    {
      "model_display_name": "Gemini-3-Pro [crs]",
      "model": "gemini-3-pro-preview",
      "base_url": "http://127.0.0.1:3000/droid/comm/v1/",
      "api_key": "后台创建的API密钥",
      "provider": "generic-chat-completion-api",
      "max_tokens": 65535
    },
    {
      "model_display_name": "GLM-4.6 [crs]",
      "model": "glm-4.6",
      "base_url": "http://127.0.0.1:3000/droid/comm/v1/",
      "api_key": "后台创建的API密钥",
      "provider": "generic-chat-completion-api",
      "ma
