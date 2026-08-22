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

## installation

1. Install from Chrome Web Store (may not be the latest version due to approval delays): [Chrome Web Store](https://chromewebstore.google.com/detail/prompt-optimizer/cakkkhboolfnadechdlgdcnjammejlna)
2. Click the icon to open the Prompt Optimizer

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
