# TheJoeFin/Text-Grab

Use OCR in Windows quickly and easily with Text Grab. With optional background process and notifications.

## features

![All Modes In Light Mode](images/All-Modes-Light.png)

Use Text Grab on Windows to capture text with OCR, clean it up quickly, and move it into the next step of your workflow.

When text gets trapped inside images, videos, PDFs, and parts of apps where you cannot select it, Text Grab helps you get it back out. You can take a screenshot or open a supported file, run it through the OCR engine, and send the result to the clipboard or straight into an editor. All OCR runs entirely on your device — no internet connection, no cloud service, and no per-use cost. Everything stays local and private. You can also do much more than copy text from images, because Text Grab gives you multiple modes for capture, post-grab cleanup, spreadsheet-style editing, and fast text reuse.

You can use it all day without friction. Launch it quickly from the taskbar, open specific modes from the command line, or enable the background process so global hotkeys work anywhere in Windows.

The Full-Screen Grab mode is also the basis of the [PowerToys Text Extractor](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor).

## requirements

- **Windows 10 or later** — required for all features using the Windows OCR API.
- **Windows 11 on a Copilot+ PC (Microsoft Store install)** — required for Windows AI features, which use the on-device Neural Processing Unit for higher-accuracy recognition.

## installation

### Official

- [Microsoft Store](https://www.microsoft.com/en-us/p/text-grab/9mznkqj7sl0b?cid=TextGrabGitHub)
- [GitHub Releases](https://github.com/TheJoeFin/Text-Grab/releases/latest)

### Community

- [scoop](https://scoop.sh/) — `scoop install text-grab`
- [choco](https://community.chocolatey.org) - `choco install text-grab`

## How to Build

Build and test Text Grab on Windows.

Get the code:
- Install Git: https://git-scm.com/download/win
    - `winget install git.git`
- `git clone https://github.com/TheJoeFin/Text-Grab.git`

### With Visual Studio 2022 or Visual Studio 2026
- Install Visual Studio (the free Community edition is sufficient).
    - Install the "Universal Windows Platform development" workload.
    - Install the ".NET desktop development" workload.
    - Install the ".NET cross-platform development" workload.
    - Install Windows 10 SDK `10.0.22621.0`
- Open `Text-Grab.sln` in Visual Studio.
- Set `Text-Grab-Package` as the startup project.
- Set the CPU target to `x64` or `ARM64`.
- Press `F5` or choose **Local Machine**.

### With the .NET SDK or Visual Studio Code
- Install the .NET 10 SDK: https://dotnet.microsoft.com/download/dotnet/10.0
- This repository pins SDK `10.0.100` in `global.json`.
- Optional for debugging: install Visual Studio Code https://code.visualstudio.com/ and the C# extension / C# Dev Kit.
- Open the `Text-Grab` folder in VS Code.
- Restore dependencies with `dotnet restore Text-Grab.sln`
- Build with `dotnet build Text-Grab\Text-Grab.csproj`
- Run tests with `dotnet test Tests\Tests.csproj`
- In VS Code, press `F5` to launch with the included debug configuration.

### UI automation

The Windows UI automation inventory, safe local release sign-off command, runner requirements, and opt-in system/package lanes are documented in [UiTests/README.md](UiTests/README.md).

## Choose from Four Modes

### 1. Full-Screen Mode (basis of [Text Extractor](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor))
![Select text from a region](images/FSG-V4.gif)

Use Full-Screen Mode when you want to select any region of the screen and copy the recognized text straight to your clipboard.

You can also click once to try to copy a single word. That works because the Windows OCR API draws a bounding box around each recognized word.

If you click or select an area with no text, the Text Grab window stays active so you can try again. To exit, press Escape, right-click and choose Cancel, or press Alt+F4.

### 2. Grab Frame Mode
![Grab Frame](images/3-2-GF-Editing-Table-2.gif)

Use Grab Frame when you want a movable OCR window you can keep over part of your screen. Position the frame over the text you want, then grab text by searching for it, clicking a word border, or clicking the Grab button.

Grab Frame uses the same OCR engine as Full-Screen Mode, so you get the same strengths and tradeoffs. OCR is not perfect, but you can often improve accuracy by adjusting the size and position of the frame.

### 3. Edit Text Window

Use the Edit Text Window to turn OCR results into clean, usable content. You can work in plain text, spreadsheet-style, or markdown mode depending on what you need. Grab text with Full-Screen Mode or Grab Frame, then keep refining it without leaving Text Grab.

Inside the Edit Text Window, you get tools that help you quickly fix, extract, and structure text.

**Clean OCR output**
- Make text into a single line
- Toggle between UPPERCASE, lowercase, and Titlecase
- Trim spaces and empty lines
- Remove duplicate lines
- Replace reserved characters (like spaces, /, %, etc.)
- Extract text based on patterns like phone numbers, emails, or customer patterns

**Search and extract**
- Find and replace
- Extract regular expressions
- Launch URLs

**Structure data**
- Convert stacked data to table format
- Continue working in Spreadsheet mode for row-and-column cleanup
- Transpose captured table data when OCR gives the right data in the wrong orientation

**Workflow helpers**
- List

## tools

The newest and most accurate option. The Windows AI API is available on Copilot+ PCs with Text Grab installed through the Microsoft Store, and runs on the dedicated Neural Processing Unit (NPU). Because inference happens on dedicated silicon, it is fast and power-efficient. It produces higher-quality results than traditional OCR, especially on handwriting, stylized fonts, and complex layouts. WinAI models support a wide range of languages automatically without requiring additional language packs. If your device supports it, Text Grab will offer this as an option automatically.

### WinRT OCR (Windows OCR API) — Windows 10 and later

The default capture method for most users. The Windows Runtime OCR API has shipped with Windows since Windows 10 and runs entirely on your device. It is fast, reliable, and produces excellent results for printed text in screenshots, documents, and images. Recognized languages depend on the language packs installed in Windows — add languages through Windows Settings to enable recognition in those languages.

### Tesseract

An open-source OCR engine that Text Grab can use as an alternative to the WinRT API. Tesseract has been around for decades, is highly configurable, and supports a very large range of languages through downloadable language data files available in the [tessdata repository](https://github.com/tesseract-ocr/tessdata). It can be a good choice when you need more control over recognition parameters or when working with image types where you want to compare output between engines.

### Direct Text (UI Automation)

Sometimes OCR is not needed at all. When text is displayed in a native UI element — a text box, label, list, or document rendered by the operating system — Text Grab can read it directly using Windows UI Automation without running any OCR. This approach is faster, perfectly accurate, and works regardless of display resolution or font. Use it when the text is selectable in theory but not easily accessible through normal copy and paste.

## Command Line Interface

Use these arguments with `Text-Grab.exe`:
- `Fullscreen` launches into Fullscreen Grab mode
- `GrabFrame` launches a new Grab Frame
- `EditText` launches a new Edit Text Window
- `QuickLookup` launches Quick Simple Lookup
- `Settings` opens Text Grab settings
- `--grabframe "file path"` opens a supported image or PDF directly in Grab Frame
- `--windowless "file path"` reads or OCRs a file and copies the resulting text without opening a window
- `"file path"` opens text files in Edit Text and opens supported image or PDF files in Grab Frame
- `"folder path"` e.g. `.\Text-Grab.exe "C:\Users\myPC\Downloads"` opens a new Edit Text Window and scans the images in that directory

### Bulk processing folders of images

You are not limited to one screenshot at a time. You can also bulk process a folder full of images or PDFs and collect the OCR output in the Edit Text Window for review, cleanup, and export.

Use this when you have a batch of scans, receipts, product labels, screenshots, or archived documents that all need text extracted in one pass. Instead of opening files one by one, point Text Grab at the folder and let it process the supported files it finds.

Use bulk folder OCR to:
- Scan every supported image or PDF in a selected folder
- Open a folder directly from the command line
- Optionally include file names, headers, and footers in the output
- Process subfolders recursively when needed
- Apply a grab template while processing a batch
- Write `.txt` output files for the processed items

After the batch OCR finishes, you can continue cleaning the combined results in the Edit Text Window, use find and replace or regex extraction, convert stacked data into table form, or move the result into Spreadsheet mode for final cleanup before sending it elsewhere in your workflow.

### Patterns (Regular Expressions / RegEx)

Patterns, also known as regular expressions or RegEx, help you make text cleanup more robust, accurate, 
