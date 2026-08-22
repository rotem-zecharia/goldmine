# ScrapeGraphAI/Scrapegraph-ai

Python scraper based on AI

## installation

The reference page for Scrapegraph-ai is available on the official page of PyPI: [pypi](https://pypi.org/project/scrapegraphai/).

```bash
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

**Note**: it is recommended to install the library in a virtual environment to avoid conflicts with other libraries 🐱

## tools

There are multiple standard scraping pipelines that can be used to extract information from a website (or local file).

The most common one is the `SmartScraperGraph`, which extracts information from a single page given a user prompt and a source URL.


```python
from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> For OpenAI and other models you just need to change the llm config!
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


The output will be a dictionary like the following:

```python
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```
There are other pipelines that can be used to extract information from multiple pages, generate Python scripts, or even generate audio files.

| Pipeline Name           | Description                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | Single-page scraper that only needs a user prompt and an input source.                                           |
| SearchGraph             | Multi-page scraper that extracts information from the top n search results of a search engine.                  |
| SpeechGraph             | Single-page scraper that extracts information from a website and generates an audio file.                       |
| ScriptCreatorGraph      | Single-page scraper that extracts information from a website and generates a Python script.                     |
| SmartScraperMultiGraph  | Multi-page scraper that extracts information from multiple pages given a single prompt and a list of sources.    |
| ScriptCreatorMultiGraph | Multi-page scraper that generates a Python script for extracting information from multiple pages and sources.     |

For each of these graphs there is the multi version. It allows to make calls of the LLM in parallel.

It is possible to use different LLM through APIs, such as **OpenAI**, **Groq**, **Azure**, **Gemini**, **[MiniMax](docs/minimax.md)** and more, or local models using **Ollama**.

Remember to have [Ollama](https://ollama.com/) installed and download the models using the **ollama pull** command, if you want to use local models.


## 📖 Documentation
