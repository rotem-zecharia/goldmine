# ocrmypdf/OCRmyPDF

OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched

## features

- Generates a searchable [PDF/A](https://en.wikipedia.org/?title=PDF/A) file from a regular PDF
- Places OCR text accurately below the image to ease copy / paste
- Keeps the exact resolution of the original embedded images
- When possible, inserts OCR information as a "lossless" operation without disrupting any other content
- Optimizes PDF images, often producing files smaller than the input file
- If requested, deskews and/or cleans the image before performing OCR
- Validates input and output files
- Distributes work across all available CPU cores
- Uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) engine to recognize more than [100 languages](https://github.com/tesseract-ocr/tessdata)
- Keeps your private data private.
- Scales properly to handle files with thousands of pages.
- Battle-tested on millions of PDFs.

<img src="misc/screencast/demo.svg" alt="Demo of OCRmyPDF in a terminal session">

For details: please consult the [documentation](https://ocrmypdf.readthedocs.io/en/latest/).

## installation

Linux, Windows, macOS and FreeBSD are supported. Docker images are also available, for both x64 and ARM.

| Operating system              | Install command               |
| ----------------------------- | ------------------------------|
| Debian, Ubuntu                | ``apt install ocrmypdf``      |
| Windows Subsystem for Linux   | ``apt install ocrmypdf``      |
| Fedora                        | ``dnf install ocrmypdf``      |
| macOS (Homebrew)              | ``brew install ocrmypdf``     |
| macOS (MacPorts)              | ``port install ocrmypdf``     |
| macOS (nix)                   | ``nix-env -i ocrmypdf``       |
| LinuxBrew                     | ``brew install ocrmypdf``     |
| FreeBSD                       | ``pkg install py-ocrmypdf``   |
| OpenBSD                       | ``pkg_add ocrmypdf``          |
| Ubuntu Snap                   | ``snap install ocrmypdf``     |

For everyone else, [see our documentation](https://ocrmypdf.readthedocs.io/en/latest/installation.html) for installation steps.

## requirements

In addition to the required Python version, OCRmyPDF requires external program installations of Ghostscript and Tesseract OCR. OCRmyPDF is pure Python, and runs on pretty much everything: Linux, macOS, Windows and FreeBSD.
