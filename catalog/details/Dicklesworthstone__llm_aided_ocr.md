# Dicklesworthstone/llm_aided_ocr

Enhances Tesseract OCR output using LLMs (local or API) for error correction, smart chunking, and markdown formatting of scanned PDFs

## features

- PDF to image conversion
- OCR using Tesseract
- Advanced error correction using LLMs (local or API-based)
- Smart text chunking for efficient processing
- Markdown formatting option
- Header and page number suppression (optional)
- Quality assessment of the final output
- Support for both local LLMs and cloud-based API providers (OpenAI, Anthropic)
- Asynchronous processing for improved performance
- Detailed logging for process tracking and debugging
- GPU acceleration for local LLM inference

## configuration

The project uses a `.env` file for easy configuration. Key settings include:

- LLM selection (local or API-based)
- API provider selection
- Model selection for different providers
- Token limits and buffer sizes
- Markdown formatting options

## requirements

- Python 3.12+
- Tesseract OCR engine
- PDF2Image library
- PyTesseract
- OpenAI API (optional)
- Anthropic API (optional)
- Local LLM support (optional, requires compatible GGUF model)

## installation

1. Install Pyenv and Python 3.12 (if needed):

```bash

## tools

1. Place your PDF file in the project directory.

2. Update the `input_pdf_file_path` variable in the `main()` function with your PDF filename.

3. Run the script:
   ```
   python llm_aided_ocr.py
   ```

4. The script will generate several output files, including the final post-processed text.

## limitations

- The system's performance is heavily dependent on the quality of the LLM used.
- Processing very large documents can be time-consuming and may require significant computational resources.
