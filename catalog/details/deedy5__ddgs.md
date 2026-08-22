# deedy5/ddgs

A metasearch library that aggregates results from diverse web search services

## installation

```python
pip install -U ddgs       # Base install
pip install -U ddgs[api]  # API server (FastAPI)
pip install -U ddgs[mcp]  # MCP server (stdio)
```

## CLI version

```python3
ddgs - -help
```

[Go To TOP](#TOP)
___

## tools

-- **Install**
```bash
pip install -U ddgs[api]
```

-- **CLI**
```bash
ddgs api              # Start server in foreground
ddgs api -d           # Start in detached mode (background)
ddgs api -s           # Stop detached server
ddgs api --host 127.0.0.1 --port 4479  # Default port 4479
ddgs api -pr socks5h://127.0.0.1:9150  # With proxy
```

-- **Docker compose**
```bash
git clone https://github.com/deedy5/ddgs && cd ddgs
docker-compose up --build
```

-- **Bash script**
```bash
git clone https://github.com/deedy5/ddgs && cd ddgs
chmod +x start_api.sh
./start_api.sh
```

#### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/search/text` | GET, POST | Text search |
| `/search/images` | GET, POST | Image search |
| `/search/news` | GET, POST | News search |
| `/search/videos` | GET, POST | Video search |
| `/search/books` | GET, POST | Book search |
| `/extract` | GET, POST | Extract content from URL |
| `/health` | GET | Health check |
| `/docs` | GET | Swagger UI |
| `/redoc` | GET | ReDoc documentation |

[Go To TOP](#TOP)
___

## MCP Server

- **Install**
```bash
pip install -U ddgs[mcp]
```

- **CLI**
```bash
ddgs mcp    # Start MCP server (stdio transport)
ddgs mcp -pr socks5h://127.0.0.1:9150  # With proxy
```

#### Available Tools

| Tool | Description |
|------|-------------|
| `search_text` | Web text search |
| `search_images` | Image search |
| `search_news` | News search |
| `search_videos` | Video search |
| `search_books` | Book search |
| `extract_content` | Extract content from a URL |

#### Client Configuration

For MCP clients like Cursor or Claude Desktop:
```json
{
  "mcpServers": {
    "ddgs": {
      "command": "ddgs",
      "args": ["mcp"]
    }
  }
}
```

[Go To TOP](#TOP)
___

## Engines

| DDGS function | Available backends |
| --------------|:-------------------|
| text()        | `bing`, `brave`, `duckduckgo`, `google`, `grokipedia`, `mojeek`, `startpage`, `yandex`, `yahoo`, `wikipedia`|
| images()      | `bing`, `duckduckgo` |
| videos()      | `duckduckgo` |
| news()        | `bing`, `duckduckgo`, `yahoo` |
| books()       | `annasarchive` |

[Go To TOP](#TOP)

## DDGS class

DDGS class is lazy-loaded.

```python3
class DDGS:
    """Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services.

    Args:
        proxy (str, optional): proxy for the HTTP client, supports http/https/socks5 protocols.
            example: "http://user:pass@example.com:3128". Defaults to None.
        timeout (int, optional): Timeout value for the HTTP client. Defaults to 5.
        verify: (bool | str):  True to verify, False to skip, or a str path to a PEM file. Defaults to True.
    """
```

Here is an example of initializing the DDGS class.
```python3
from ddgs import DDGS

results = DDGS().text("python programming", max_results=5)
print(results)
```

[Go To TOP](#TOP)

## 1. text()

```python
def text(
    query: str,
    region: str = "us-en",
    safesearch: str = "moderate",
    timelimit: str | None = None,
    max_results: int | None = 10,
    page: int = 1,
    backend: str = "auto",
) -> list[dict[str, str]]:
    """DDGS text metasearch.

    Args:
        query: text search query.
        region: us-en, uk-en, ru-ru, etc. Defaults to us-en.
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: d, w, m, y. Defaults to None.
        max_results: maximum number of results. Defaults to 10.
        page: page of results. Defaults to 1.
        backend: A single or comma-delimited backends. Defaults to "auto".

    Returns:
        List of dictionaries with search results.
    """
```
***Example***
```python
results = DDGS().text("live free or die", region="us-en", safesearch="off", timelimit="y", page=1, backend="auto")
# Searching for pdf files
results = DDGS().text("russia filetype:pdf", region="us-en", safesearch="off", timelimit="y", page=1, backend="auto")
print(results)
[
    {
        "title"
