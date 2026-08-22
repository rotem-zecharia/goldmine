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
