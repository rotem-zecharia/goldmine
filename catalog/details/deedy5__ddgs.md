# deedy5/ddgs

A metasearch library that aggregates results from diverse web search services

## installation

```python
pip install -U ddgs       # Base install
pip install -U ddgs[api]  # API server (FastAPI)
pip install -U ddgs[mcp]  # MCP server (stdio)
```

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
