# pymupdf/PyMuPDF

PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.

## features

- **Fast** — powered by [MuPDF](https://mupdf.com?utm_source=github&utm_medium=referral&utm_campaign=pymupdf_github&utm_content=body&utm_term=mupdf), a best-in-class C rendering engine
- **Accurate** — pixel-perfect text extraction with font, color, and position metadata
- **Versatile** — read, write, annotate, redact, merge, split, and convert documents
- **LLM-ready** — native Markdown output via [PyMuPDF4LLM](https://pdf4llm.com?utm_source=github&utm_medium=referral&utm_campaign=pymupdf_github&utm_content=body&utm_term=pymupdf4llm) for RAG and AI pipelines
- **No mandatory dependencies** — `pip install pymupdf` and you're done

---

## installation

```bash
pip install pymupdf
```

Wheels are available for **Windows**, **macOS**, and **Linux** on Python 3.10–3.14. If no pre-built wheel exists for your platform, pip will compile from source (requires a C/C++ toolchain).

### Optional extras

| Package | Purpose |
|---|---|
| `pymupdf-fonts` | Extended font collection for text output |
| `pymupdf4llm` | LLM/RAG-optimised Markdown and JSON extraction |
| `pymupdfpro` | Adds Office document support |
| `tesseract-ocr` | OCR for scanned pages and images (separate install) |

```bash
# More fonts
pip install pymupdf-fonts

# LLM-ready extraction
pip install pymupdf4llm

# Office support
pip install pymupdfpro

# OCR (Tesseract must be installed separately)
# macOS
brew install tesseract

# Ubuntu / Debian
sudo apt install tesseract-ocr
```

---

## Supported File Formats

### Input

| Category | Formats |
|---|---|
| PDF & derivatives | PDF, XPS, EPUB, CBZ, MOBI, FB2, SVG, TXT, MD |
| Images | PNG, JPEG, BMP, TIFF, GIF, and more |
| Microsoft Office *(Pro)* | DOC, DOCX, XLS, XLSX, PPT, PPTX |
| Korean Office *(Pro)* | HWP, HWPX |

### Output

| Format | Notes |
|---|---|
| PDF | Full fidelity conversion from Office formats |
| SVG | Vector page rendering |
| Image (PNG, JPEG, …) | Page rasterisation at any DPI |
| Markdown | Structure-aware, LLM-ready |
| JSON | Bounding boxes, layout data, per-element detail |
| Plain text | Fast, lightweight extraction |

---


## Quick start

### Extract text

```python
import pymupdf

doc = pymupdf.open("document.pdf")
for page in doc:
    print(page.get_text())
```

### Extract text with layout metadata

```python
import pymupdf

doc = pymupdf.open("document.pdf")
page = doc[0]

blocks = page.get_text("dict")["blocks"]
for block in blocks:
    if block["type"] == 0:  # text block
        for line in block["lines"]:
            for span in line["spans"]:
                print(f"{span['text']!r}  font={span['font']}  size={span['size']:.1f}")
```

### Extract tables

```python
import pymupdf

doc = pymupdf.open("spreadsheet.pdf")
page = doc[0]

tables = page.find_tables()
for table in tables:
    print(table.to_markdown())

    # or get as Pandas DataFrame
    df = table.to_pandas()
```

### Render a page to an image

```python
import pymupdf

doc = pymupdf.open("document.pdf")
page = doc[0]

pixmap = page.get_pixmap(dpi=150)
pixmap.save("page_0.png")
```

### OCR a scanned document

```python
import pymupdf

doc = pymupdf.open("scanned.pdf")
page = doc[0]

# Requires Tesseract installed and on PATH
text = page.get_textpage_ocr(language="eng").extractText()
print(text)
```

### Convert Markdown to PDF

```python
import pymupdf

md_doc = pymupdf.open("example.md")
md_doc.save("example.pdf")
```

### Convert to Markdown for LLMs

```python
import pymupdf4llm

md = pymupdf4llm.to_markdown("report.pdf")
# Pass directly to your LLM or vector store
print(md)
```

### Annotate and redact

```python
import pymupdf

doc = pymupdf.open("contract.pdf")
page = doc[0]

# Add a highlight annotation
rect = pymupdf.Rect(72, 100, 400, 120)
page.add_highlight_annot(rect)

# Add a redaction and apply it
page.add_redact_annot(rect)
page.apply_redactions()

doc.save("contract_redacted.pdf")
```

### Merge PDFs

```python
import pymupdf

merger = pymupdf.open()
for path in ["part1.pdf", "part2.pdf", "part3.pdf"]:
    merger.insert_pdf(pymupdf.open(path))

merger.save("merged.pdf")
```

### Convert an Office document to PDF

```python
import pymupdf.pro

pymupdf.pro.unlock("YOUR-LICENSE-KEY")

doc = pymupdf.open("presentation.pptx")
pdf_bytes = doc.convert_to_pdf()

with open("output.pdf", "wb") as f:
    f.write(pdf_bytes)
```

### Extract LLM-ready Markdown from a Word document

```python
import pymupdf4llm
import pymupdf.pro

pymupdf.pro.unlock("YOUR-LICENSE-KEY")

md = pymupdf4llm.to_markdown("document.docx")
print(md)
```

---
