# oomol-lab/pdf-craft

PDF craft can convert PDF files into various other formats. This project will focus on processing PDF files of scanned books.

## installation

### Installation

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pdf-craft
```

The above commands are for quick setup only. To actually use pdf-craft, you need to **install Poppler** for PDF parsing. Local OCR also requires a CUDA-capable PyTorch environment; vendor OCR does not. Please refer to the [Installation Guide](docs/INSTALLATION.md) for detailed instructions.

### Quick Start

#### Convert to Markdown

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    markdown_assets_path="images",
)
```

![mdmd](https://github.com/user-attachments/assets/d7082496-13b8-4728-9e79-44e2888e57fd)

#### Convert to EPUB

```python
from pdf_craft import transform_epub, BookMeta

transform_epub(
    pdf_path="input.pdf",
    epub_path="output.epub",
    book_meta=BookMeta(
        title="Book Title",
        authors=["Author"],
    ),
)
```

![20251218-162533](https://github.com/user-attachments/assets/7f6df04a-1fa7-48b3-aa5e-d2d056304ad6)

## tools

### Convert to Markdown

```python
from pdf_craft import DeepSeekOCRLocalConfig, transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    markdown_assets_path="images",
    analysing_path="temp",  # Optional: specify temporary folder
    ocr_size="gundam",  # Optional: tiny, small, base, large, gundam
    ocr=DeepSeekOCRLocalConfig(models_cache_path="models"),
    dpi=300,  # Optional: DPI for rendering PDF pages (default: 300)
    max_page_image_file_size=None,  # Optional: max image file size in bytes, auto-adjust DPI if exceeded
    includes_cover=False,  # Optional: include cover
    includes_footnotes=True,  # Optional: include footnotes
    ignore_pdf_errors=False,  # Optional: continue on PDF rendering errors
    ignore_ocr_errors=False,  # Optional: continue on OCR recognition errors
    generate_plot=False,  # Optional: generate visualization charts
    toc_llm=None,  # Optional: LLM instance for enhanced TOC extraction
    toc_assumed=False,  # Optional: whether to assume TOC pages exist (default: False)
)
```

### Convert to EPUB

```python
from pdf_craft import (
    BookMeta,
    LaTeXRender,
    DeepSeekOCRLocalConfig,
    TableRender,
    transform_epub,
)

transform_epub(
    pdf_path="input.pdf",
    epub_path="output.epub",
    analysing_path="temp",  # Optional: specify temporary folder
    ocr_size="gundam",  # Optional: tiny, small, base, large, gundam
    ocr=DeepSeekOCRLocalConfig(models_cache_path="models"),
    dpi=300,  # Optional: DPI for rendering PDF pages (default: 300)
    max_page_image_file_size=None,  # Optional: max image file size in bytes, auto-adjust DPI if exceeded
    includes_cover=True,  # Optional: include cover
    includes_footnotes=True,  # Optional: include footnotes
    ignore_pdf_errors=False,  # Optional: continue on PDF rendering errors
    ignore_ocr_errors=False,  # Optional: continue on OCR recognition errors
    generate_plot=False,  # Optional: generate visualization charts
    toc_llm=None,  # Optional: LLM instance for enhanced TOC extraction
    toc_assumed=True,  # Optional: whether to assume TOC pages exist (default: True for EPUB)
    book_meta=BookMeta(
        title="Book Title",
        authors=["Author 1", "Author 2"],
        publisher="Publisher",
        language="en",
    ),
    lan="en",  # Optional: language (zh/en)
    table_render=TableRender.HTML,  # Optional: table rendering method
    latex_render=LaTeXRender.MATHML,  # Optional: formula rendering method
    inline_latex=True,  # Optional: preserve inline LaTeX expressions
)
```

## configuration

pdf-craft supports every OCR backend exposed by `doc-page-extractor`:

- `DeepSeekOCRLocalConfig`: local DeepSeek OCR model. Real conversion requires CUDA.
- `DeepSeekOCR2LocalConfig`: local DeepSeek OCR 2 model. Real conversion requires CUDA.
- `UnlimitedOCRLocalConfig`: local Unlimited OCR model. Real conversion requires CUDA.
- `DeepSeekOCRVendorConfig`: DeepSeek OCR through an OpenAI-compatible endpoint.
- `DeepSeekOCR2VendorConfig`: DeepSeek OCR 2 through an OpenAI-compatible endpoint.
- `UnlimitedOCRVendorConfig`: Unlimited OCR cloud backend.

Pass one of these configs through the `ocr` parameter. The OCR mode strings are
`deepseek-ocr-local`, `deepseek-ocr2-local`, `unlimited-ocr-local`,
`deepseek-ocr-vendor`, `deepseek-ocr2-vendor`, and `unlimited-ocr-vendor`.
They are used only by this repository's manual scripts through `.env`; the
library API accepts configuration objects and does not read environment
variables.

```python
from pdf_craft import (
    DeepSeekOCR2VendorConfig,
    DeepSeekOCRVendorConfig,
    UnlimitedOCRVendorConfig,
    transform_markdown,
)

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ocr=DeepSeekOCRVendorConfig(
        base_url="https://example.com",
        api_key="...",
        model="deepseek-ocr",
    ),
)

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ocr=DeepSeekOCR2VendorConfig(
        base_url="https://example.com",
        api_key="...",
        model="deepseek-ocr2",
    ),
)

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ocr=UnlimitedOCRVendorConfig(
        ak="...",
        sk="...",
    ),
)
```

### Model Management

Local OCR models are automatically downloaded from Hugging Face on first run
when `local_only=False` (the default for the library configuration objects).
The repository's manual scripts default `DEEPSEEK_LOCAL_ONLY` and
`UNLIMITED_LOCAL_ONLY` to `true`, so set the relevant variable to `false` to
allow a missing model to download.
You can control model storage and loading behavior through the local OCR
configs. Unlimited OCR local supports the `base` and `gundam` `ocr_size`
presets.

#### Pre-download Models

In production environments, it is recommended to download models in advance to avoid downloading on first run:

```python
from pdf_craft import DeepSeekOCRLocalConfig, predownload_models

predownload_models(
    ocr=DeepSeekOCRLocalConfig(models_cache_path="models"),
    revision=None,  # Optional: specify model version
)
```

#### Specify Model Cache Path

By default, models are downloaded to the system's Hugging Face cache directory. You can customize the cache location through the `models_cache_path` parameter:

```python
from pdf_craft import DeepSeekOCRLocalConfig, transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ocr=DeepSeekOCRLocalConfig(models_cache_path="./my_models"),
)
```

#### Offline Mode

If you have pre-downloaded the models, you can use `local_only=True` to disable network downloads and ensure only local models are used:

```python
from pdf_craft import DeepSeekOCRLocalConfig, transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ocr=DeepSeekOCRLocalConfig(
        models_cache_path="./my_models",
        local_only=True,
    ),
)
```
