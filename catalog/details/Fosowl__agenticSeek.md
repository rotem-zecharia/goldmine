# Fosowl/agenticSeek

Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity.

## features

* 🔒 Fully Local & Private - Everything runs on your machine — no cloud, no data sharing. Your files, conversations, and searches stay private.

* 🌐 Smart Web Browsing - AgenticSeek can browse the internet by itself — search, read, extract info, fill web form — all hands-free.

* 💻 Autonomous Coding Assistant - Need code? It can write, debug, and run programs in Python, C, Go, Java, and more — all without supervision.

* 🧠 Smart Agent Selection - You ask, it figures out the best agent for the job automatically. Like having a team of experts ready to help.

* 📋 Plans & Executes Complex Tasks - From trip planning to complex projects — it can split big tasks into steps and get things done using multiple AI agents.

* 🎙️ Voice-Enabled - Clean, fast, futuristic voice and speech to text allowing you to talk to it like it's your personal AI from a sci-fi movie. (In progress)

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
