# opendatalab/MinerU

Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.

## features

- Support `PDF`, image, `DOCX`, `PPTX`, and `XLSX` inputs.
- Remove headers, footers, footnotes, page numbers, etc., to ensure semantic coherence.
- Output text in human-readable order, suitable for single-column, multi-column, and complex layouts.
- Preserve the structure of the original document, including headings, paragraphs, lists, etc.
- Extract images, image descriptions, tables, table titles, and footnotes.
- Automatically recognize and convert formulas in the document to LaTeX format.
- Automatically recognize and convert tables in the document to HTML format.
- Automatically detect scanned PDFs and garbled PDFs and enable OCR functionality.
- OCR supports detection and recognition of 109 languages.
- Supports multiple output formats, such as multimodal and NLP Markdown, JSON sorted by reading order, and rich intermediate formats.
- Supports various visualization results, including layout visualization and span visualization, for efficient confirmation of output quality.
- Built-in CLI, FastAPI, Gradio WebUI, for local orchestration and multi-service deployment.
- Supports running in a pure CPU environment, and also supports GPU/MPS acceleration
- Compatible with Windows, Linux, and Mac platforms.

## installation

Document parsing is a difficult and complex task. In scenarios such as complex layouts, scanned pages, and handwritten content, the parsing results may fall short of expectations. We recommend trying the online demo first to evaluate MinerU's parsing quality and suitability before choosing an appropriate deployment method based on your actual needs.
If you have **document** samples with unsatisfactory parsing results, feel free to share them in an [issue](https://github.com/opendatalab/MinerU/issues). We will continue improving the parsing capabilities.
If you encounter any installation issues, please first consult the <a href="#faq">FAQ</a>.
