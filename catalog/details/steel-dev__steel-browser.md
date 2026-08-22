# steel-dev/steel-browser

🔥 Open Source Browser API for AI Agents & Apps. Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure.

## installation

The easiest way to get started with Steel is by creating a [Steel Cloud](https://app.steel.dev) account. Otherwise, you can deploy this Steel browser instance to a cloud provider or run it locally.

## ⚡ Quick Deploy
If you're looking to deploy to a cloud provider, we've got you covered.

| Deployment methods | Link |
| -------------------- | ----- |
| Pre-built Docker Image (combined API + UI) | [![Deploy with Github Container Registry](https://img.shields.io/badge/GHCR-478CFF?style=for-the-badge&labelColor=478CFF&logo=github&logoColor=white)](https://github.com/steel-dev/steel-browser/pkgs/container/steel-browser) |
| 1-click deploy to Railway | [![Deploy on Railway](https://img.shields.io/badge/Railway-B039CB?style=for-the-badge&labelColor=B039CB&logo=railway&logoColor=white)](https://railway.app/deploy/steelbrowser) |
| 1-click deploy to Render | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy) |


## 💻 Running Locally

### Docker

The simplest way to deploy/run a Steel browser instance locally is to run the pre-built Docker image:

```bash
# Pull and run the Docker image
docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser
```

This will start the Steel browser server on port 3000 (http://localhost:3000) and the UI at http://localhost:3000/ui. The 9223 port is used for the console debugger.

You can now create sessions, scrape pages, take screenshots, and more. Jump to the [Usage](#usage) section for some quick examples on how you can do that.

Alternatively, you can run the API and UI separately with docker compose:

```bash
docker compose up
```

For Mac Silicon users, you will need to pass this env flag to the Docker compose command to run the images on the correct platform:
```bash
DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose up
```

## Quickstart for Contributors
When developing locally, you will need to run the [`docker-compose.dev.yml`](./docker-compose.dev.yml) file instead of the default [`docker-compose.yml`](./docker-compose.yml) file so that your local changes are reflected. Doing this will build the Docker images from the [`api`](./api) and [`ui`](./ui) directories and run the server and UI on port 3000 and 5173 respectively.

```bash
docker compose -f docker-compose.dev.yml up
```

You will also need to run it with `--build` to ensure the Docker images are re-built every time you make changes:

```bash
docker compose -f docker-compose.dev.yml up --build
```

If you run on a custom host, create a `.env` file (see `docs/DEVELOPMENT_SETUP.md` for variables) or modify the environment variables used by `docker-compose.dev.yml` to use your host.

### Node.js
Alternatively, if you have Node.js and Chrome installed, you can run both the server and the UI directly:

```bash
npm install
npm run dev
```

This will also start the Steel server on port 3000 and the UI on port 5173.

Make sure you have the Chrome executable installed and in one of these paths:

- **Linux**:
  `/usr/bin/google-chrome`

- **MacOS**:
  `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

- **Windows**:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe` OR
  - `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

#### Custom Chrome Executable

If you have a custom Chrome executable or a different path, you can set the `CHROME_EXECUTABLE_PATH` environment variable to the path of your Chrome executable:

```bash
export CHROME_EXECUTABLE_PATH=/path/to/your/chrome
npm run dev
```

For more details on where this is checked look at [`api/src/utils/browser.ts`](./api/src/utils/browser.ts).

## tools

> If you're looking for quick examples on how to use Steel, check out the [Cookbook](https://github.com/steel-dev/steel-cookbook).
>
> Alternatively you can play with the [REPL package](./repl/README.md) too `cd repl` and `npm run start`

There are two main ways to interact with the Steel browser API:
1. [Using Sessions](#sessions)
2. [Using the Quick Actions Endpoints](#quick-actions-api)

In these examples, we assume your custom Steel API endpoint is `http://localhost:3000`.

The full REST OpenAPI documentation can be found [on our site](https://docs.steel.dev/api-reference) and on your local Steel instance at `http://localhost:3000/documentation`.

#### Using the SDKs
If you prefer to use the our Python and Node SDKs, you can install the `steel-sdk` package for Node or Python.

These SDKs are built on top of the REST API and provide a more convenient way to interact with the Steel browser API. They are fully typed, and are compatible with both Steel Cloud and self-hosted Steel instances (changeable using the `baseURL` option on Node and `base_url` on Python).

For more details on installing and using the SDKs, please see the [Node SDK Reference](https://github.com/steel-dev/steel-node/blob/main/api.md) and the [Python SDK Reference](https://github.com/steel-dev/steel-python/blob/main/api.md).


### Sessions
The `/sessions` endpoint lets you relaunch the browser with custom options or extensions (e.g. with a custom proxy) and also reset the browser state. Perfect for complex, stateful workflows that need fine-grained control.

Once you have a session, you can use the session ID or the root URL to interact with the browser. To do this, you will need to use Puppeteer or Playwright. You can find some examples of how to use Puppeteer and Playwright with Steel in the docs below:
* [Puppeteer Integration](https://docs.steel.dev/overview/guides/puppeteer)
* [Playwright with Node](https://docs.steel.dev/overview/guides/playwright-node)
* [Playwright with Python](https://docs.steel.dev/overview/guides/playwright-python)

<details open>
<summary><b>Creating a Session using the Node SDK</b></summary>
<br>

```typescript
import Steel from 'steel-sdk';

const client = new Steel({
  baseURL: "http://localhost:3000", // Custom API Base URL override
});

(async () => {
  try {
    // Create a new browser session with current API fields
    const session = await client.sessions.create({
      blockAds: true,
      proxyUrl: "user:pass@host:port", // optional
      dimensions: { width: 1280, height: 800 }, // optional
    });
    console.log("Created session with ID:", session.id);
  } catch (error) {
    console.error("Error creating session:", error);
  }
})();
````
</details>

<details>
<summary><b>Creating a Session using the Python SDK</b></summary>
<br>

````python
import os
from steel import Steel

client = Steel(
    base_url="http://localhost:3000",  # Custom API Base URL override
)

try:
    # Create a new browser session with custom options
    session = client.sessions.create(
        block_ads=True,
        proxy_url="user:pass@host:port",  # optional
        dimensions={"width": 1280, "height": 800},  # optional
    )
    print("Created session with ID:", session.id)
except Exception as e:
    print("Error creating session:", e)
````
</details>

<details>
<summary><b>Creating a Session using Curl</b></summary>
<br>

```bash
# Launch a new browser session
curl -X POST http://localhost:3000/v1/sessions \
  -H "Content-Type: application/json" \
  -d '{
    "proxyUrl": "user:pass@host:port",
    "blockAds": true,
    "dimensions": { "width": 1280, "height": 800 }
  }'
```
</details>


#### Selenium Sessions
>**Note:** This integration does not support all the features of the CDP-based browser sessions API.

For teams with existing Selenium workflows, the Steel browser provides a drop-in replacement that adds enhanced features while maintaining compatibility. You can simply use the `isSelenium` option to create a Selenium session:

`
