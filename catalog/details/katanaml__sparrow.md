# katanaml/sparrow

Structured data extraction, instruction calling and agentic workflows with ML, LLM and Vision LLM

## features

The web UI provides a visual interface on top of the same API:

- **Drag & Drop**: Upload documents directly
- **Real-time Processing**: See results instantly
- **Data Query**: JSON based schema for data query
- **Structured Output**: JSON structured output

## requirements

- **Python 3.12.10+** (use `pyenv` for version management)
- **macOS** (for MLX backend) or **Linux/Windows** (for other backends)
- **GPU** (make sure GPU have enough memory to run selected Vision LLM)

## installation

```bash

## configuration

python -m venv .env_sparrow_parse
source .env_sparrow_parse/bin/activate  # Linux/Mac

## tools

python api.py
```

Before running `pip install -r requirements_sparrow_parse.txt`, check your platform. If you are on macOS and want to run MLX backend, go to `requirements_sparrow_parse.txt` and make sure `sparrow-parse[mlx]` libary reference is defined. If you are running Sparrow on Linux/Windows, make sure to use `sparrow-parse` library reference, this will skip MLX related libraries.
