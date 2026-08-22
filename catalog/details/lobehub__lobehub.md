# lobehub/lobehub

🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

## installation

We are a group of e/acc design-engineers, hoping to provide modern design components and tools for AIGC.
By adopting the Bootstrapping approach, we aim to provide developers and users with a more open, transparent, and user-friendly product ecosystem.

Whether for users or professional developers, LobeHub will be your AI Agent playground. Please be aware that LobeHub is currently under active development, and feedback is welcome for any [issues][issues-link] encountered.

| [![](https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1065874&theme=light&t=1769347414733)](https://www.producthunt.com/products/lobehub?launch=lobehub-2&embed=true&utm_source=badge-featured&utm_medium=badge&utm_campaign=badge-lobehub) | We are live on Product Hunt! We are thrilled to bring LobeHub to the world. If you believe in a future where humans and agents co-evolve, please support our journey. |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![][discord-shield-badge]][discord-link]                                                                                                                                                                                                                          | Join our Discord community! This is where you can connect with developers and other enthusiastic users of LobeHub.                                                    |

> \[!IMPORTANT]
>
> **Star Us**, You will receive all release notifications from GitHub without any delay \~ ⭐️

[![][image-star]][github-stars-link]

<details>
  <summary><kbd>Star History</kbd></summary>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=lobehub%2Flobehub&theme=dark&type=Date">
    <img width="100%" src="https://api.star-history.com/svg?repos=lobehub%2Flobehub&type=Date">
  </picture>
</details>

## features

Today’s agents are one-off, task-driven tools. They lack context, live in isolation, and require manual hand-offs between different windows and models. While some maintain memory, it is often global, shallow, and impersonal. In this mode, users are forced to toggle between fragmented conversations, making it difficult to form structured productivity.

**LobeHub changes everything.**

LobeHub is a work-and-lifestyle space to find, build, and collaborate with agent teammates that grow with you. In LobeHub, we treat **Agents as the unit of work**, providing an infrastructure where humans and agents co-evolve.

![](https://github.com/user-attachments/assets/89d1c402-a62b-4794-82ea-17e5ee1a6165)

## configuration

This project provides some additional configuration items set with environment variables:

| Environment Variable | Required | Description                                                                                                                                                               | Example                                                                                                              |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `OPENAI_API_KEY`     | Yes      | This is the API key you apply on the OpenAI account page                                                                                                                  | `sk-xxxxxx...xxxxxx`                                                                                                 |
| `OPENAI_PROXY_URL`   | No       | If you manually configure the OpenAI interface proxy, you can use this configuration item to override the default OpenAI API request base URL                             | `https://api.chatanywhere.cn` or `https://aihubmix.com/v1` <br/>The default value is<br/>`https://api.openai.com/v1` |
| `OPENAI_MODEL_LIST`  | No       | Used to control the model list. Use `+` to add a model, `-` to hide a model, and `model_name=display_name` to customize the display name of a model, separated by commas. | `qwen-7b-chat,+glm-6b,-gpt-3.5-turbo`                                                                                |

> \[!NOTE]
>
> The complete list of environment variables can be found in the [📘 Environment Variables][docs-env-var]

## tools

An API Key is required to chat with LLMs in LobeHub. This section uses the OpenAI model provider as an example to briefly introduce how to obtain an API Key.

#### `A` Via the Official OpenAI Channel

- Sign up for an [OpenAI account](https://platform.openai.com/signup); you will need an international phone number and a non-mainland-China email address;
- After signing up, go to the [API Keys](https://platform.openai.com/api-keys) page and click `Create new secret key` to create a new API Key:

| Step 1: Open the creation dialog                                                                                                                   | Step 2: Create the API Key                                                                                                                         | Step 3: Get the API Key                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/28616219/296253192-ff2193dd-f125-4e58-82e8-91bc376c0d68.png" height="200"/> | <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/28616219/296254170-803bacf0-4471-4171-ae79-0eab08d621d1.png" height="200"/> | <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/28616219/296255167-f2745f2b-f083-4ba8-bc78-9b558e0002de.png" height="200"/> |

- Fill this API Key into the LobeHub API Key configuration and you are ready to go.

> \[!TIP]
>
> Newly registered accounts usually come with a $5 free credit, but it is only valid for three months.
> If you want to keep using your API Key long-term, you need to bind a credit card to complete payment. Since OpenAI only supports foreign-currency credit cards, you will need to find a suitable payment channel yourself, which is not covered in detail here.

<br/>

#### `B` Via an OpenAI Third-Party Proxy

If you find signing up for an OpenAI account or binding a foreign-currency credit card troublesome, you can consider using a well-known OpenAI third-party proxy to obtain an API Key, which can effectively lower the barrier to getting one. At the same time, however, once you use a third-party service, you may also need to bear its potential risks — please decide based on your own actual situation. Below is a list of common third-party model proxies for your reference:

|                                                                     | Provider     | Features                                                                                                | Proxy URL                 | Link                              |
| ------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------- |
| <img src="https://resource.aihubmix.com/logo.png?v=1" width="48" /> | **AIHubMix** | Uses the OpenAI enterprise API; all models site-wide at **14% off** the official price (incl. GPT-5.6 and Claude Fable 5) | `https://aihubmix.com/v1` | [Get](https://console.aihubmix.com/token?aff=8DBz) |

> \[!WARNING]
>
> **Disclaimer**: The OpenAI API Keys recommended here are provided by third-party proxies, so we are not responsible for the **validity** or **security** of these API Keys. Please bear the risks of purchasing and using them yourself.

> \[!NOTE]
>
> If you are a model service provider and believe your service is stable enough and reasonably pric
