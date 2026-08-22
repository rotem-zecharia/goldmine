# opendataloader-project/opendataloader-pdf

PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

## installation

### Python

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

### Node.js

```bash
npm install @opendataloader/pdf
```

```typescript
import { convert } from '@opendataloader/pdf';

await convert(['file1.pdf', 'file2.pdf', 'folder/'], {
  outputDir: 'output/',
  format: 'markdown,json'
});
```

### Java

```xml
<dependency>
  <groupId>org.opendataloader</groupId>
  <artifactId>opendataloader-pdf-core</artifactId>
</dependency>
```

[Python Quick Start](https://opendataloader.org/docs/quick-start-python) | [Node.js Quick Start](https://opendataloader.org/docs/quick-start-nodejs) | [Java Quick Start](https://opendataloader.org/docs/quick-start-java)

## Hybrid Mode: #1 Accuracy for Complex PDFs

Hybrid mode combines fast local Java processing with AI backends. Simple pages stay local (0.02s); complex pages route to AI for +90% table accuracy.

> **Don't combine with `--use-struct-tree` on tagged PDFs.** `--use-struct-tree` takes precedence, so the hybrid backend is **not** called (a warning is logged). If you want the hybrid backend, drop `--use-struct-tree`.

```bash
pip install -U "opendataloader-pdf[hybrid]"
```

**Terminal 1** — Start the backend server:

```bash
opendataloader-pdf-hybrid --port 5002
```

**Terminal 2** — Process PDFs:

```bash
# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/
```

**Python:**

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    hybrid="docling-fast"
)
```

### OCR for Scanned PDFs

Start the backend with `--force-ocr` for image-based PDFs with no selectable text:

```bash
opendataloader-pdf-hybrid --port 5002 --force-ocr
```

For non-English documents, specify the language:

```bash
opendataloader-pdf-hybrid --port 5002 --force-ocr --ocr-lang "ko,en"
```

Supported languages: `en`, `ko`, `ja`, `ch_sim`, `ch_tra`, `de`, `fr`, `ar`, and more.

### Formula Extraction (LaTeX)

Extract mathematical formulas as LaTeX from scientific PDFs:

```bash
# Server: enable formula enrichment
opendataloader-pdf-hybrid --enrich-formula

# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/
```

Output in JSON:
```json
{
  "type": "formula",
  "page number": 1,
  "bounding box": [226.2, 144.7, 377.1, 168.7],
  "content": "\\frac{f(x+h) - f(x)}{h}"
}
```

> **Note**: Formula and picture description enrichments require `--hybrid-mode full` on the client side.

### Chart & Image Description

Generate AI descriptions for charts and images — useful for RAG search and accessibility alt text:

```bash
# Server
opendataloader-pdf-hybrid --enrich-picture-description

# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/
```

Output in JSON:
```json
{
  "type": "picture",
  "page number": 1,
  "bounding box": [72.0, 400.0, 540.0, 650.0],
  "description": "A bar chart showing waste generation by region from 2016 to 2030..."
}
```

> Uses SmolVLM (256M), a lightweight vision model. Custom prompts supported via `--picture-description-prompt`.

### Hancom Data Loader Integration — Coming Soon

Enterprise-grade AI document analysis via [Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf) — customer-customized models trained on your domain-specific do

## features

### Tagged PDF Support

When a PDF has structure tags, OpenDataLoader extracts the **exact layout** the author intended — no guessing, no heuristics. Headings, lists, tables, and reading order are preserved from the source.

> **Output quality depends on tag quality.** Not all tagged PDFs are well-tagged. For PDFs with sparse or incorrect tags, the default heuristic mode or `--hybrid docling-fast` often produces better results.

> **`--use-struct-tree` takes precedence over `--hybrid`.** If both are set on a tagged PDF, the structure tree is used and the hybrid backend is **not** called (a well-tagged PDF already carries reading order and structure). Drop `--use-struct-tree` if you want the hybrid backend instead.

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    use_struct_tree=True           # Use native PDF structure tags
)
```

Most PDF parsers ignore structure tags entirely. [Learn more](https://opendataloader.org/docs/tagged-pdf)

### AI Safety: Prompt Injection Protection

PDFs can contain hidden prompt injection attacks. OpenDataLoader automatically filters:

- Hidden text (transparent, zero-size fonts)
- Off-page content
- Suspicious invisible layers

To sanitize sensitive data (emails, URLs, phone numbers → placeholders), enable it explicitly:

```bash
# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf file1.pdf file2.pdf folder/ --sanitize
```

[AI Safety Guide](https://opendataloader.org/docs/ai-safety)

### LangChain Integration

```bash
pip install -U langchain-opendataloader-pdf
```

```python
from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader

loader = OpenDataLoaderPDFLoader(
    file_path=["file1.pdf", "file2.pdf", "folder/"],
    format="text"
)
documents = loader.load()
```

[LangChain Docs](https://docs.langchain.com/oss/python/integrations/document_loaders/opendataloader_pdf) | [GitHub](https://github.com/opendataloader-project/langchain-opendataloader-pdf) | [PyPI](https://pypi.org/project/langchain-opendataloader-pdf/)

## configuration

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json,markdown,pdf",
    image_output="embedded",        # "off", "embedded" (Base64), or "external" (default)
    image_format="jpeg",            # "png" or "jpeg"
    use_struct_tree=True,           # Use native PDF structure
)
```

[Full CLI Options Reference](https://opendataloader.org/docs/reference/cli-options)

## PDF Accessibility & PDF/UA Conversion

**Problem**: Millions of existing PDFs lack structure tags, failing accessibility regulations (EAA, ADA/Section 508, Korea Digital Inclusion Act). Manual remediation costs $50–200 per document and doesn't scale.

**OpenDataLoader's approach**: Built in collaboration with [PDF Association](https://pdfa.org) and [Dual Lab](https://duallab.com) (developers of [veraPDF](https://verapdf.org), the industry-reference open-source PDF/A and PDF/UA validator). Auto-tagging follows the [Well-Tagged PDF specification](https://pdfa.org/resource/well-tagged-pdf/) and is validated programmatically using veraPDF — automated conformance checks against PDF accessibility standards, not manual review. No existing open-source tool generates Tagged PDFs end-to-end — most rely on proprietary SDKs for the tag-writing step. OpenDataLoader does it all under Apache 2.0. ([collaboration details](https://opendataloader.org/docs/tagged-pdf-collaboration))

| Regulation | Deadline | Requirement |
|------------|----------|-------------|
| **European Accessibility Act (EAA)** | June 28, 2025 | Accessible digital products across the EU |
| **ADA & Section 508** | In effect | U.S. federal agencies and public accommodations |
| **Digital Inclusion Act** | In effect | South Korea digital service accessibility |

### Standards & Validation

| Aspect | Detail |
|--------|--------|
| **Specification** | [Well-Tagged PDF](https://pdfa.org/resource/well-tagged-pdf/) by PDF Association |
| **Validation** | [veraPDF](https://verapdf.org) — industry-reference open-source PDF/A & PDF/UA validator |
| **Collaboration** | PDF Association + [Dual Lab](https://duallab.com) (veraPDF developers) co-develop tagging and validation |
| **License** | Auto-tagging → Tagged PDF: Apache 2.0 (free). PDF/UA export: Enterprise |

### Accessibility Pipeline

| Step | Feature | Status | Tier |
|------|---------|--------|------|
| 1. **Audit** | Read existing PDF tags, detect untagged PDFs | Shipped | Free |
| 2. **Auto-tag → Tagged PDF** | Generate structure tags for untagged PDFs | Shipped | Free (Apache 2.0) |
| 3. **Export PDF/UA** | Convert to PDF/UA-1 or PDF/UA-2 compliant files | 💼 Available | Enterprise |
| 4. **Visual editing** | Accessibility studio — review and fix tags | 💼 Available | Enterprise |

> **💼 Enterprise features** are available on request. [Contact us](https://opendataloader.org/contact) to get started.

### Auto-Tagging

Generate Tagged PDFs from untagged PDFs — output is a screen-reader-ready PDF with structure tags (headings, paragraphs, lists, tables, reading order).

```python
import opendataloader_pdf

# Untagged PDF in → Tagged PDF out
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="tagged-pdf"
)
```

```bash
# CLI
opendataloader-pdf --format tagged-pdf file1.pdf file2.pdf folder/
```

Combine with other formats: `format="json,tagged-pdf"`.

### End-to-End Compliance Workflow

```
Existing PDFs (untagged)
    │
    ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌──────────────────┐
│  1. Audit       │───>│  2. Auto-Tag     │───>│  3. Export      │───>│  4. Studio       │
│  (check tags)   │    │  (→ Tagged PDF)  │    │  (PDF/UA)       │    │  (visual editor) │
└─────────────────┘    └──────────────────┘    └─────────────────┘    └──────────────────┘
        │                       │       

## limitations

| Feature | Timeline | Tier |
|---------|----------|------|
| **[Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf)** — Enterprise AI document analysis, customer-customized models, VLM-based chart/image understanding, production-grade OCR | Q2-Q3 2026 | Planned |
| **Structure validation** — Verify PDF tag trees | Q3 2026 | Planned |

[Full Roadmap](https://opendataloader.org/docs/upcoming-roadmap)

## Frequently Asked Questions

### What is the best PDF parser for RAG?

For RAG pipelines, you need a parser that preserves document structure, maintains correct reading order, and provides element coordinates for citations. OpenDataLoader is designed specifically for this — it outputs structured JSON with bounding boxes, handles multi-column layouts with XY-Cut++, and runs locally without GPU. In hybrid mode, it ranks #1 overall (0.907) in benchmarks.

### What is the best open-source PDF parser?

OpenDataLoader PDF is the only open-source parser that combines: rule-based deterministic extraction (no GPU), bounding boxes for every element, XY-Cut++ reading order, built-in AI safety filters, native Tagged PDF support, and hybrid AI mode for complex documents. It ranks #1 in overall accuracy (0.907) while running locally on CPU.

### How do I extract tables from PDF for LLM?

OpenDataLoader detects tables using border analysis and text clustering, preserving row/column structure. For complex tables, enable hybrid mode for +90% accuracy improvement (0.489 to 0.928 TEDS score):

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json",
    hybrid="docling-fast"           # For complex tables
)
```

### How does it compare to docling, marker, or pymupdf4llm?

OpenDataLoader [hybrid] ranks #1 overall (0.907) across reading order, table, and heading accuracy. Key differences: docling (0.882) is strong but lacks bounding boxes and AI safety filters. marker (0.861) requires GPU and is 1000x slower (53.932s/page). pymupdf4llm (0.732) is fast but has poor table (0.401) and heading (0.412) accuracy. OpenDataLoader is the only parser that combines deterministic local extraction, bounding boxes for every element, and built-in prompt injection protection. See [full benchmark](https://github.com/opendataloader-project/opendataloader-bench).

### Can I use this without sending data to the cloud?

Yes. OpenDataLoader runs 100% locally. No API calls, no data transmission — your documents never leave your environment. The hybrid mode backend also runs locally on your machine. Ideal for legal, healthcare, and financial documents.

### Does it support OCR for scanned PDFs?

Yes, via hybrid mode. Install with `pip install "opendataloader-pdf[hybrid]"`, start the backend with `--force-ocr`, then process as usual. Supports multiple languages including Korean, Japanese, Chinese, Arabic, and more via `--ocr-lang`.

### Does it work with Korean, Japanese, or Chinese documents?

Yes. For digital PDFs, text extraction works out of the box. For scanned PDFs, use hybrid mode with `--force-ocr --ocr-lang "ko,en"` (or `ja`, `ch_sim`, `ch_tra`). Coming soon: [Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf) integration — enterprise-grade AI document analysis with built-in production-grade OCR and customer-customized models optimized for your specific document types and workflows.

### How fast is it?

Local mode processes 60+ pages per second on CPU (0.02s/page). Hybrid mode processes 2+ pages per second (0.46s/page) with significantly higher accuracy for complex documents. No GPU required. Benchmarked on Apple M4. [Full benchmark details](https://github.com/opendataloader-project/opendataloader-bench). With multi-process batch processing, thr
