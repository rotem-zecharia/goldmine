# tesseract-ocr/tesseract

Tesseract Open Source OCR Engine (main repository)

## installation

You can either [Install Tesseract via pre-built binary package](https://tesseract-ocr.github.io/tessdoc/Installation.html)
or [build it from source](https://tesseract-ocr.github.io/tessdoc/Compiling.html).

Before building Tesseract from source, please check that your system has a compiler which is one of the [supported compilers](https://tesseract-ocr.github.io/tessdoc/supported-compilers.html).

## requirements

Tesseract uses [Leptonica library](https://github.com/DanBloomberg/leptonica)
for opening input images (e.g. not documents like pdf).
It is suggested to use leptonica with built-in support for [zlib](https://zlib.net),
[png](https://sourceforge.net/projects/libpng) and
[tiff](http://www.simplesystems.org/libtiff) (for multipage tiff).
