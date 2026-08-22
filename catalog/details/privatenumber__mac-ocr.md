# privatenumber/mac-ocr

macOS CLI for OCR and searchable PDFs using Apple's Vision framework

## features

- **Read text from an image:** `mac-ocr photo.png`
- **Read text from many images:** `mac-ocr *.png`
- **Stream text from a PDF, page by page:** `mac-ocr scan.pdf --format jsonl`
- **Read document structure on macOS 26+:** `mac-ocr document receipt.jpg --format json`
- **Turn an image into a searchable PDF:** `mac-ocr searchable-pdf photo.png` → `photo.ocr.pdf`
- **Add a selectable text layer to a scanned PDF:** `mac-ocr searchable-pdf scan.pdf` → `scan.ocr.pdf`

## installation

```sh
npm install -g mac-ocr
```

Or run it without installing:

```sh
npx mac-ocr receipt.jpg
```

**Requirements:** macOS 10.15+. The npm package ships a prebuilt universal binary, so no Xcode or Swift toolchain is needed.

## configuration

Both OCR and `searchable-pdf` accept the recognition options:

| Flag | Effect |
|------|--------|
| `--fast` | Faster, lower-accuracy recognition ([details](docs/CLI.md#recognition-levels)) |
| `--password <password>` | Password for an encrypted PDF (or set `MAC_OCR_PDF_PASSWORD`) |
| `-l, --language <code>` | Recognition language (BCP-47, repeatable). e.g. `-l en-US -l ja-JP` |
| `-c, --confidence <0–1>` | Drop observations below this confidence |
| `-w, --custom-words <word>` | Add custom vocabulary (repeatable) |
| `--custom-words-file <path>` | Custom vocabulary file, one word per line |
| `--no-language-correction` | Disable language correction |
| `--min-text-height <0–1>` | Ignore text shorter than this fraction of image height |
| `--pdf-dpi <auto\|72–600>` | PDF rasterization DPI (default `auto`) |
| `--roi <x,y,w,h>` | Region of interest: restrict recognition to a normalized region (top-left origin) |

## tools

The same package exposes a typed, promise-based API that wraps the binary. Inputs are image or PDF **bytes** — read files or fetch URLs in your own code and pass the bytes:

```sh
npm install mac-ocr
```

```ts
import fs from 'node:fs/promises'
import {
    ocr, ocrDocument, createSearchablePdf, supportedLanguages
} from 'mac-ocr'

// Recognize text in an image or single-page PDF
const result = await ocr(await fs.readFile('receipt.jpg'))
console.log(result.text)
for (const { text, confidence, boundingBox } of result.observations) { /* … */ }

// Multi-page PDF: stream pages as they finish…
for await (const page of ocr.pages(await fs.readFile('book.pdf'))) {
    console.log(page.page, '/', page.pageCount, page.text)
}
// …or collect the whole thing into an array
const pages = await Array.fromAsync(ocr.pages(await fs.readFile('book.pdf')))

// Extract structured paragraphs, tables, and lists on macOS 26+
const document = await ocrDocument(await fs.readFile('receipt.jpg'), {
    languages: ['en']
})
console.log(document.documents[0]?.content.tables)
for await (const page of ocrDocument.pages(await fs.readFile('book.pdf'))) {
    console.log(page.page, page.text)
}

// Build a searchable PDF (returns the PDF bytes)
const pdf = await createSearchablePdf(await fs.readFile('scan.pdf'), { fast: true })
await fs.writeFile('scan.ocr.pdf', pdf)

// Recognition languages supported on this macOS version (for ocr and createSearchablePdf)
const languages = await supportedLanguages()
```

Options mirror the CLI flags (like `{ fast: true }` above), plus an `AbortSignal` for cancellation. Failures throw a `MacOcrError` with a `kind` you can branch on. See [docs/NODE.md](docs/NODE.md) for every option, the result types, and error handling.
