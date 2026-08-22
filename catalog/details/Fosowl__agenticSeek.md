# Fosowl/agenticSeek

Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity.

## features

* 🔒 Fully Local & Private - Everything runs on your machine — no cloud, no data sharing. Your files, conversations, and searches stay private.

* 🌐 Smart Web Browsing - AgenticSeek can browse the internet by itself — search, read, extract info, fill web form — all hands-free.

* 💻 Autonomous Coding Assistant - Need code? It can write, debug, and run programs in Python, C, Go, Java, and more — all without supervision.

* 🧠 Smart Agent Selection - You ask, it figures out the best agent for the job automatically. Like having a team of experts ready to help.

* 📋 Plans & Executes Complex Tasks - From trip planning to complex projects — it can split big tasks into steps and get things done using multiple AI agents.

* 🎙️ Voice-Enabled - Clean, fast, futuristic voice and speech to text allowing you to talk to it like it's your personal AI from a sci-fi movie. (In progress)

### **Demo**

> *Can you search for the agenticSeek project, learn what skills are required, then open the CV_candidates.zip and then tell me which match best the project*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

Disclaimer: This demo, including all the files that appear (e.g: CV_candidates.zip), are entirely fictional. We are not a corporation, we seek open-source contributors not candidates.


> 🙏 This project started as a side-project and has zero roadmap and zero funding. It's grown way beyond what I expected by ending in GitHub Trending. Contributions, feedback, and patience are deeply appreciated.

## requirements

Before you begin, ensure you have the following software installed:

*   **Git:** For cloning the repository. [Download Git](https://git-scm.com/downloads)
*   **Python 3.10.x:** We strongly recommend using Python version 3.10.x. Using other versions might lead to dependency errors. [Download Python 3.10](https://www.python.org/downloads/release/python-3100/) (pick a 3.10.x version).
*   **Docker Engine & Docker Compose:** For running bundled services like SearxNG.
    *   Install Docker Desktop (which includes Docker Compose V2): [Windows](https://docs.docker.com/desktop/install/windows-install/) | [Mac](https://docs.docker.com/desktop/install/mac-install/) | [Linux](https://docs.docker.com/desktop/install/linux-install/)
    *   Alternatively, install Docker Engine and Docker Compose separately on Linux: [Docker Engine](https://docs.docker.com/engine/install/) | [Docker Compose](https://docs.docker.com/compose/install/) (ensure you install Compose V2, e.g., `sudo apt-get install docker-compose-plugin`).

## installation

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. Change the .env file content

```sh
SEARXNG_BASE_URL="http://searxng:8080" # value depends on where the backend runs — see the SEARXNG note below
SEARXNG_PORT=8080
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/Users/mlg/Documents/workspace_for_ai"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
CUSTOM_ADDITIONAL_LLM_PORT="11435"
OPENAI_API_KEY='optional'
DEEPSEEK_API_KEY='optional'
OPENROUTER_API_KEY='optional'
TOGETHER_API_KEY='optional'
GOOGLE_API_KEY='optional'
ANTHROPIC_API_KEY='optional'
```


Update the `.env` file with your own values as needed:

- **SEARXNG_PORT**: The **host** port Docker publishes SearXNG on. If port `8080` is already taken on your machine, set another one (e.g. `8001`). Inside Docker the container always listens on `8080` — this variable never changes that.
- **SEARXNG_BASE_URL**: The address the **backend** uses to reach SearXNG. It is set here in `.env` (not in `config.ini`) and depends only on where the backend runs:

| How you run AgenticSeek | `SEARXNG_BASE_URL` |
|---|---|
| Web interface — backend in Docker (`./start_services.sh full`) | `http://searxng:8080` — always port `8080`, even if you changed `SEARXNG_PORT` |
| CLI mode — backend on host (`uv run cli.py`) | `http://localhost:8080` — if you changed `SEARXNG_PORT`, use that port instead (e.g. `http://localhost:8001`). `http://searxng:...` does **not** work here: that hostname only exists inside Docker |

> To check SearXNG in a browser, always use the host port: `http://localhost:<SEARXNG_PORT>`. After changing `.env`, restart the backend — the file is only read at process start.
- **REDIS_BASE_URL**: Leave unchanged
- **WORK_DIR**: Path to your working directory on your local machine. AgenticSeek will be able to read and interact with these files.
- **OLLAMA_PORT**: Port number for the Ollama service.
- **LM_STUDIO_PORT**: Port number for the LM Studio service.
- **CUSTOM_ADDITIONAL_LLM_PORT**: Port for any additional custom LLM service.

**API Key are totally optional for user who choose to run LLM locally. Which is the primary purpose of this project. Leave empty if you have sufficient hardware**

### 3. **Start Docker**

Make sure Docker is installed and running on your system. You can start Docker using the following commands:

- **On Linux/macOS:**
    Open a terminal and run:
    ```sh
    sudo systemctl start docker
    ```
    Or launch Docker Desktop from your applications menu if installed.

- **On Windows:**
    Start Docker Desktop from the Start menu.

You can verify Docker is running by executing:
```sh
docker info
```
If you see information about your Docker installation, it is running correctly.

See the table of [Local Providers](#list-of-local-providers) below for a summary.

Next step: [Run AgenticSeek locally](#start-services-and-run)

*See the [Troubleshooting](#troubleshooting) section if you are having issues.*
*If your hardware can't run LLMs locally, see [Setup to run with an API](#setup-to-run-with-an-api).*
*For detailed `config.ini` explanations, see [Config Section](#config).*

---

## Setup for running LLM locally on your machine

**Hardware Requirements:**

To run LLMs locally, you'll need sufficient hardware. At a minimum, a GPU capable of running Magistral, Qwen or Deepseek 14B is required. See the FAQ for detailed model/performance recommendations.

**Setup your local provider**

Start your local provider (for example with ollama):

Unless you wish to to run AgenticSeek on host (CLI mode), export or set the provider listen address:

```sh
export OLLAMA_HOST=0.0.0.0:11434
```

Then, start you provider:

```sh
ollama serve
```

See below for a list of local supported provider.

**Update the config.ini**

Change the config.ini file to set the provider_name to a supported provider and provider_model to a LLM supported by your provider. We recommend reasoning model such as *Magistral* or *Deepseek*.

See t

## tools

Make sure the services are up and running with `./start_services.sh full` and go to `localhost:3000` for web interface.

You can also use speech to text by setting `listen = True` in the config. Only for CLI mode.

To exit, simply say/type `goodbye`.

Here are some example usage:

> *Make a snake game in python!*

> *Search the web for top cafes in Rennes, France, and save a list of three with their addresses in rennes_cafes.txt.*

> *Write a Go program to calculate the factorial of a number, save it as factorial.go in your workspace*

> *Search my summer_pictures folder for all JPG files, rename them with today’s date, and save a list of renamed files in photos_list.txt*

> *Search online for popular sci-fi movies from 2024 and pick three to watch tonight. Save the list in movie_night.txt.*

> *Search the web for the latest AI news articles from 2025, select three, and write a Python script to scrape their titles and summaries. Save the script as news_scraper.py and the summaries in ai_news.txt in /home/projects*

> *Friday, search the web for a free stock price API, register with supersuper7434567@gmail.com then write a Python script to fetch using the API daily prices for Tesla, and save the results in stock_prices.csv*

*Note that form filling capabilities are still experimental and might fail.*



After you type your query, AgenticSeek will allocate the best agent for the task.

Because this is an early prototype, the agent routing system might not always allocate the right agent based on your query.

Therefore, you should be very explicit in what you want and how the AI might proceed for example if you want it to conduct a web search, do not say:

`Do you know some good countries for solo-travel?`

Instead, ask:

`Do a web search and find out which are the best country for solo-travel`

---

## configuration

Example config:
```
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = http://127.0.0.1:11434 # Example for Ollama; use http://127.0.0.1:1234 for LM-Studio
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False

jarvis_personality = False
languages = en zh # List of languages for TTS and potentially routing.
[BROWSER]
headless_browser = False
stealth_mode = False
```

**Explanation of `config.ini` Settings**:

*   **`[MAIN]` Section:**
    *   `is_local`: `True` if using a local LLM provider (Ollama, LM-Studio, local OpenAI-compatible server) or the self-hosted server option. `False` if using a cloud-based API (OpenAI, Google, etc.).
    *   `provider_name`: Specifies the LLM provider.
        *   Local options: `ollama`, `lm-studio`, `openai` (for local OpenAI-compatible servers). `server` is deprecated — see [Setup to run the LLM on your own server](#setup-to-run-the-llm-on-your-own-server).
        *   API options: `openai`, `google`, `deepseek`, `huggingface`, `togetherAI`.
    *   `provider_model`: The specific model name or ID for the chosen provider (e.g., `deepseekcoder:6.7b` for Ollama, `gpt-3.5-turbo` for OpenAI API, `mistralai/Mixtral-8x7B-Instruct-v0.1` for TogetherAI).
    *   `provider_server_address`: The address of your LLM provider.
        *   For local providers: e.g., `http://127.0.0.1:11434` for Ollama, `http://127.0.0.1:1234` for LM-Studio.
        *   For an LLM server on another machine: e.g., `x.x.x.x:11434` for remote Ollama, `http://x.x.x.x:8080` for a remote OpenAI-compatible server (see [Setup to run the LLM on your own server](#setup-to-run-the-llm-on-your-own-server)).
        *   For cloud APIs (`is_local = False`): This is often ignored or can be left blank, as the API endpoint is usually handled by the client library.
    *   `agent_name`: Name of the AI assistant (e.g., Friday). Used as a trigger word for speech-to-text if enabled.
    *   `recover_last_session`: `True` to attempt to restore the previous session's state, `False` to start fresh.
    *   `save_session`: `True` to save the current session's state for potential recovery, `False` otherwise.
    *   `speak`: `True` to enable text-to-speech voice output, `False` to disable.
    *   `listen`: `True` to enable speech-to-text voice input (CLI mode only), `False` to disable.
    *   `work_dir`: **Crucial:** The directory where AgenticSeek will read/write files. **Ensure this path is valid and accessible on your system.**
    *   `jarvis_personality`: `True` to use a more "Jarvis-like" system prompt (experimental), `False` for the standard prompt.
    *   `languages`: A comma-separated list of languages (e.g., `en, zh, fr`). Used for TTS voice selection (defaults to the first) and can assist the LLM router. Avoid too many or very similar languages for router efficiency.
*   **`[BROWSER]` Section:**
    *   `headless_browser`: `True` to run the automated browser without a visible window (recommended for web interface or non-interactive use). `False` to show the browser window (useful for CLI mode or debugging).
    *   `stealth_mode`: `True` to enable measures to make browser automation harder to detect. May require manual installation of browser extensions like anticaptcha.


This section summarizes the supported LLM provider types. Configure them in `config.ini`.

**Local Providers (Run on Your Own Hardware):**

| Provider Name in `config.ini` | `is_local` | Description                                                                 | Setup Section                                                    |
|-------------------------------|------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|
| `ollama`                      | `True`     | Use Ollama to serve local LLMs.                                             | [Setup for running LLM locall

## limitations

## ChromeDriver Issues

**Error Example:** `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XXX`

### Root Cause
ChromeDriver version incompatibility occurs when:
1. Your installed ChromeDriver version doesn't match your Chrome browser version
2. In Docker environments, `undetected_chromedriver` may download its own ChromeDriver version, bypassing the mounted binary

### Solution Steps

#### 1. Check Your Chrome Version
Open Google Chrome → `Settings > About Chrome` to find your version (e.g., "Version 134.0.6998.88")

#### 2. Download Matching ChromeDriver

**For Chrome 115 and newer:** Use the [Chrome for Testing API](https://googlechromelabs.github.io/chrome-for-testing/)
- Visit the Chrome for Testing availability dashboard
- Find your Chrome version or the closest available match
- Download the ChromeDriver for your OS (Linux64 for Docker environments)

**For older Chrome versions:** Use the [legacy ChromeDriver downloads](https://chromedriver.chromium.org/downloads)

![Download ChromeDriver from Chrome for Testing](./media/chromedriver_readme.png)

#### 3. Install ChromeDriver (Choose One Method)

**Method A: Project Root Directory (Recommended for Docker)**
```bash
# Place the downloaded chromedriver binary in your project root
cp path/to/downloaded/chromedriver ./chromedriver
chmod +x ./chromedriver  # Make executable on Linux/macOS
```

**Method B: System PATH**
```bash
# Linux/macOS
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Windows: Place chromedriver.exe in a folder that's in your PATH
```

#### 4. Verify Installation
```bash
# Test the ChromeDriver version
./chromedriver --version
# OR if in PATH:
chromedriver --version
```

### Docker-Specific Notes

⚠️ **Important for Docker Users:**
- The Docker volume mount approach may not work with stealth mode (`undetected_chromedriver`)
- **Solution**: Place ChromeDriver in the project root directory as `./chromedriver`
- The application will automatically detect and use this binary
- You should see: `"Using ChromeDriver from project root: ./chromedriver"` in the logs

### Troubleshooting Tips

1. **Still getting version mismatch?**
   - Verify the ChromeDriver is executable: `ls -la ./chromedriver`
   - Check the ChromeDriver version: `./chromedriver --version`
   - Ensure it matches your Chrome browser version

2. **Docker container issues?**
   - Check backend logs: `docker logs backend`
   - Look for the message: `"Using ChromeDriver from project root"`
   - If not found, verify the file exists and is executable

3. **Chrome for Testing versions**
   - Use the exact version match when possible
   - For version 134.0.6998.88, use ChromeDriver 134.0.6998.165 (closest available)
   - Major version numbers must match (134 = 134)

### Version Compatibility Matrix

| Chrome Version | ChromeDriver Version | Status |
|----------------|---------------------|---------|
| 134.0.6998.x   | 134.0.6998.165     | ✅ Works |
| 133.0.6943.x   | 133.0.6943.141     | ✅ Works |
| 132.0.6834.x   | 132.0.6834.159     | ✅ Works |

*For the latest compatibility, check the [Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/)*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

This happen if there is a mismatch between your browser and chromedriver version.

You need to navigate to download the latest version:

https://developer.chrome.com/docs/chromedriver/downloads

If you're using Chrome version 115 or newer go to:

https://googlechromelabs.github.io/chrome-for-testing/

And download the chromedriver version matching your OS.

![alt text](./media/chromedriver_readme.png)

If this section is incomplete please raise an issue.

## Ollama connection failed from Docker backend

```
An error occurred: Provider ollama f
