# oomol-lab/pdf-craft

PDF craft can convert PDF files into various other formats. This project will focus on processing PDF files of scanned books.

## installation

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pdf-craft
```

The above commands are for quick setup only. To actually use pdf-craft, you need to **install Poppler** for PDF parsing. Local OCR also requires a CUDA-capable PyTorch environment; vendor OCR does not. Please refer to the [Installation Guide](docs/INSTALLATION.md) for detailed instructions.

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
