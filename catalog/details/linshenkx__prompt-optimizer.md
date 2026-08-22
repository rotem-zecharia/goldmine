# linshenkx/prompt-optimizer

An AI prompt optimizer for writing better prompts and getting better AI results.

## features

<div align="center">
  <p><b>1. Hard-Nosed Reviewer: Turn Agreement into Useful Critique</b></p>
  <p>Starting from a minimal English role prompt, optimization pushes a small model away from generic pushback and toward a clearer, more structured review that surfaces weak assumptions, evidence gaps, and concrete revision advice.</p>
  <img src="images/demo/hard-nosed-reviewer-fullpage-en.png" alt="Hard-nosed reviewer full-page demo" width="85%">
  <br>
  <p><b>2. Marketplace Bargaining Reply: Let Variables Change the Strategy</b></p>
  <p>With a single reusable prompt template, you can swap in item details, price anchors, buyer offers, tone, and negotiation goals for different marketplace conversations. After optimization, the same small model does a better job turning those variables into a clearer, more transaction-ready reply instead of a generic helper-style response.</p>
  <img src="images/demo/pro-variable-bargaining-reply-en.png" alt="Marketplace bargaining reply variable-mode demo" width="85%">
  <br>
  <p><b>3. Text-to-Image: Optimize a One-Line Idea into a More Directable Key Visual Prompt</b></p>
  <p>This is not just prompt expansion. Starting from a vague one-line idea, Prompt Optimizer adds clearer subject cues, spatial relationships, and mood anchors. The left side is simply “a floating library in the night sky,” while the optimized version gives the model a more directed fantasy composition that feels closer to a reusable key visual than a lucky generic image.</p>
  <img src="images/demo/text2image-floating-library-creative-en.png" alt="Floating library text-to-image demo" width="85%">
</div>

## ✨ Core Features

- 🎯 **Intelligent Optimization**: One-click prompt optimization with multi-round iterative improvements to enhance AI response accuracy
- 📝 **Dual Mode Optimization**: Support for both system prompt optimization and user prompt optimization to meet different usage scenarios
- 🔄 **Analysis and Compare Evaluation**: Supports analysis, single-result evaluation, and multi-result compare evaluation to help determine whether a prompt has truly improved
- 🤖 **Multi-model Integration**: Support for mainstream AI models including OpenAI, Gemini, DeepSeek, Grok, Zhipu AI, SiliconFlow, MiniMax, etc.
- 🖼️ **Image Generation**: Support for Text-to-Image (T2I), Image-to-Image (I2I), and Multi-Image generation with models like Gemini, Seedream, Grok
- 🌱 **Prompt Sources**: Start from manual writing, templates, local imports, or Prompt Garden import codes
- ⭐ **Smart Favorites**: Resource-aware prompt assets with version history, reproducible examples, media support, source binding, and workspace application
- 📊 **Advanced Testing Mode**: Context variable management, multi-turn conversation testing, Function Calling support
- 🔒 **Secure Architecture**: Pure client-side processing with direct data interaction with AI service providers, bypassing intermediate servers
- 📱 **Multi-platform Support**: Available as web application, desktop application, Chrome extension, and Docker deployment
- 🔐 **Access Control**: Password protection feature for secure deployment
- 🧩 **MCP Protocol Support**: Supports Model Context Protocol (MCP), enabling integration with MCP-compatible AI applications like Claude Desktop

## 🚀 Advanced Features

### Image Generation Mode
- 🖼️ **Text-to-Image (T2I)**: Generate images from text prompts
- 🎨 **Image-to-Image (I2I)**: Transform and optimize images based on local files
- 🖼️ **Multi-Image Generation**: Use multiple input images to constrain subject relationships, sequential semantics, and final generation goals
- 🔌 **Multi-model Support**: Integrated with mainstream image generation models like Gemini, Seedream, Grok
- ⚙️ **Model Parameters**: Support model-specific parameter configuration (size, style, etc.)
- 📥 **Preview & Download**: Real-time preview of generated results with download support
- 🔄 **Style Transfer**: Learn style, composition, and color from reference images

### Prompt Source

## installation

### 1. Use Online Version (Recommended)

Direct access: [https://prompt.always200.com](https://prompt.always200.com)

This is a pure frontend project with all data stored locally in your browser and never uploaded to any server, making the online version both safe and reliable to use.

### 2. Web Deployment

#### Vercel Deployment
Method 1: One-click deployment to your own Vercel:
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Flinshenkx%2Fprompt-optimizer)

Method 2: Fork the project and import to Vercel (Recommended):
   - First fork the project to your GitHub account
   - Then import the project to Vercel
   - This allows tracking of source project updates for easy syncing of new features and fixes
- Configure environment variables:
  - `ACCESS_PASSWORD`: Set access password to enable access restriction
  - `VITE_OPENAI_API_KEY` etc.: Optional private-deployment model settings. Do not preconfigure API keys on public frontend deployments because `VITE_*` values are exposed in browser assets.

For more detailed deployment steps and important notes, please check:
- [Vercel Deployment Guide](docs/user/deployment/vercel_en.md)
- [Cloudflare Deployment Guide](docs/user/deployment/cloudflare-pages_en.md)

#### Cloudflare Deployment

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/linshenkx/prompt-optimizer)

Use the Deploy to Cloudflare button for the quickest public-repository setup. It creates a repository under your GitHub/GitLab account and deploys with Workers Builds. For private repositories or stricter repository-access control, import your own repository manually; keep the default deploy commands and clear the build command if Cloudflare auto-fills `pnpm run build`, because `wrangler.jsonc` builds the Web frontend and publishes `packages/web/dist` as static assets.

For access control and analytics on Cloudflare, configure Cloudflare Access and Cloudflare Web Analytics in the Cloudflare dashboard. No frontend dependency or application-code change is required.

### 3. Download Desktop Application
Download the latest version from [GitHub Releases](https://github.com/linshenkx/prompt-optimizer/releases). We provide both **installer** and **archive** formats for each platform.

- **Installer (Recommended)**: Such as `*.exe`, `*.dmg`, `*.AppImage`, etc. **Strongly recommended as it supports automatic updates**.
- **Archive**: Such as `*.zip`. Extract and use, but cannot auto-update.

**Core Advantages of Desktop Application**:
- ✅ **No CORS Limitations**: As a native desktop application, it completely eliminates browser Cross-Origin Resource Sharing (CORS) issues. This means you can directly connect to any AI service provider's API, including locally deployed Ollama or commercial APIs with strict security policies, for the most complete and stable functional experience.
- ✅ **Automatic Updates**: Versions installed through installers (like `.exe`, `.dmg`) can automatically check and update to the latest version.
- ✅ **Independent Operation**: No browser dependency, providing faster response and better performance.

### 4. Install Chrome Extension
1. Install from Chrome Web Store (may not be the latest version due to approval delays): [Chrome Web Store](https://chromewebstore.google.com/detail/prompt-optimizer/cakkkhboolfnadechdlgdcnjammejlna)
2. Click the icon to open the Prompt Optimizer

### 5. Docker Deployment
<details>
<summary>Click to view Docker deployment commands</summary>
```bash

## configuration

docker run -d -p 8081:80 --restart unless-stopped --name prompt-optimizer linshen/prompt-optimizer

## tools

docker run -d -p 8081:80 \
  -e VITE_OPENAI_API_KEY=your_key \
  -e ACCESS_USERNAME=your_username \  # Optional, defaults to "admin"
  -e ACCESS_PASSWORD=your_password \  # Set access password
  --restart unless-stopped \
  --name prompt-optimizer \
  linshen/prompt-optimizer
```
</details>

### 6. Docker Compose Deployment
<details>
<summary>Click to view Docker Compose deployment steps</summary>
```bash
# 1. Clone the repository
git clone https://github.com/linshenkx/prompt-optimizer.git
cd prompt-optimizer

# 2. Create .env file for API keys and authentication
cat > .env << EOF
# API Key Configuration
VITE_OPENAI_API_KEY=your_openai_api_key
VITE_GEMINI_API_KEY=your_gemini_api_key
VITE_DEEPSEEK_API_KEY=your_deepseek_api_key
VITE_GROK_API_KEY=your_xai_api_key
VITE_ZHIPU_API_KEY=your_zhipu_api_key
VITE_SILICONFLOW_API_KEY=your_siliconflow_api_key

# Basic Authentication (Password Protection)
ACCESS_USERNAME=your_username  # Optional, defaults to "admin"
ACCESS_PASSWORD=your_password  # Set access password
EOF

# Because the compose file is under docker/, pass the root .env explicitly.

# 3. Start the service
docker compose --env-file .env -f docker/docker-compose.yml up -d

# 4. View logs
docker compose --env-file .env -f docker/docker-compose.yml logs -f

# 5. Access the service
Web Interface: http://localhost:8081
MCP Server: http://localhost:8081/mcp
```
</details>

You can also directly edit the docker/docker-compose.yml file to customize your configuration:
<details>
<summary>Click to view docker/docker-compose.yml example</summary>

```yaml
services:
  prompt-optimizer:
    # Use Docker Hub image
    image: linshen/prompt-optimizer:latest
    container_name: prompt-optimizer
    restart: unless-stopped
    ports:
      - "8081:80"  # Web application port (MCP server accessible via /mcp path)
    environment:
      - VITE_OPENAI_API_KEY=your_openai_key
      - VITE_GEMINI_API_KEY=your_gemini_key
      - VITE_GROK_API_KEY=your_xai_key
      # Access Control (Optional)
      - ACCESS_USERNAME=admin
      - ACCESS_PASSWORD=your_password
```
</details>

### 7. MCP Server Usage Instructions
<details>
<summary>Click to view MCP Server usage instructions</summary>

Prompt Optimizer now supports the Model Context Protocol (MCP), enabling integration with AI applications that support MCP such as Claude Desktop.

When running via Docker, the MCP Server automatically starts and can be accessed via `http://ip:port/mcp`.

#### Environment Variable Configuration

MCP Server requires API key configuration to function properly. Main MCP-specific configurations:

```bash

## limitations

- [x] Basic feature development
- [x] Web application release
- [x] Chrome extension release
- [x] Internationalization support
- [x] Support for system prompt optimization and user prompt optimization
- [x] Desktop application release
- [x] MCP service release
- [x] Advanced mode: Variable management, context testing, function calling
- [x] Image generation: Text-to-Image (T2I) and Image-to-Image (I2I) support
- [x] Prompt favorites and template management
- [ ] Support for workspace/project management

For detailed project status, see [Project Status Document](docs/project/project-status.md)

## 📖 Related Documentation

- [Documentation Index](docs/README.md) - Index of all documentation
- [Technical Development Guide](docs/developer/technical-development-guide.md) - Technology stack and development specifications
- [LLM Parameters Configuration Guide](docs/developer/llm-params-guide.md) - Detailed guide for advanced LLM parameter configuration
- [Project Structure](docs/developer/project-structure.md) - Detailed project structure description
- [Project Status](docs/project/project-status.md) - Current progress and plans
- [Product Requirements](docs/project/prd.md) - Product requirements document
- [Vercel Deployment Guide](docs/user/deployment/vercel_en.md) - Detailed instructions for Vercel deployment
- [Cloudflare Deployment Guide](docs/user/deployment/cloudflare-pages_en.md) - Web frontend deployment on Cloudflare Workers / Pages

## Star History

<a href="https://star-history.com/#linshenkx/prompt-optimizer&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=linshenkx/prompt-optimizer&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=linshenkx/prompt-optimizer&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=linshenkx/prompt-optimizer&type=Date" />
 </picture>
</a>

## FAQ

<details>
<summary>Click to view frequently asked questions</summary>
