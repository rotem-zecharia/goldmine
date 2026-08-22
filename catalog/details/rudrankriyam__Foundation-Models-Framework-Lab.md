# rudrankriyam/Foundation-Models-Framework-Lab

A practical lab for building, testing, and evaluating apps with Apple's Foundation Models framework.

## requirements

- iOS 26.0+ or macOS 26.0+
- Apple Silicon for on-device model execution
- Apple Intelligence enabled for live model runs
- Xcode 26.6 or Xcode 27

The project builds with both Xcode 26.6 and Xcode 27. APIs introduced with the
OS 27 SDK are compiler- and availability-gated, so the core app remains usable
with Xcode 26 while Xcode 27 exposes the newest labs.

## installation

```bash
git clone https://github.com/rudrankriyam/Foundation-Models-Framework-Lab.git
cd Foundation-Models-Framework-Lab
open FoundationLab.xcodeproj
```

Build from the command line:

```bash
xcodebuild \
  -project FoundationLab.xcodeproj \
  -scheme 'Foundation Lab' \
  -destination 'generic/platform=macOS' \
  CODE_SIGNING_ALLOWED=NO \
  build

xcodebuild \
  -project FoundationLab.xcodeproj \
  -scheme 'Foundation Lab' \
  -destination 'generic/platform=iOS Simulator' \
  CODE_SIGNING_ALLOWED=NO \
  build
```

Live model execution requires a compatible physical device. Simulator builds
remain useful for compilation and interface validation.

## features

### Experiments and conversations

- Streaming multi-turn conversations with context-window management
- Editable instructions, sampling, response limits, runtime, and reasoning controls
- Saved experiment configurations and persistent run history
- Swift export for Playground configurations
- Speech recognition and synthesis integrated into Playground

## tools

Nine ready-made tool recipes use the shared `FoundationModelsTools` package:

- Weather through Open-Meteo
- Keyless Search1 web search
- Contacts
- Calendar
- Reminders
- Location and place search
- Authorized HealthKit data
- Apple Music
- Web metadata

Tool recipes open in Playground, where tools can be combined or removed. Tools
that can change user data require confirmation through the app-owned workflow.

### Structured output and applied projects

- `@Generable` models and `@Guide` constraints
- Dynamic schemas, nested objects, unions, forms, and invoice extraction
- Multilingual sessions and supported-language inspection
- RAG document indexing and semantic retrieval with LumoKit and VecturaKit
- A HealthKit dashboard and chat grounded only in authorized Health data

### Xcode 27 labs

When built with Xcode 27, Foundation Lab also demonstrates:

- `PrivateCloudComputeLanguageModel`
- Shared `LanguageModel` execution
- Image attachments and references
- Explicit tool-calling modes
- Dynamic profiles and reasoning controls
- Transcript inspection and history transforms
- Context-budget visualization
- Custom model executors, including a video-capable provider bridge

The image-input probe under [`Tools/ImageInputProbe`](Tools/ImageInputProbe)
can measure the current SDK's practical decoded-buffer boundary.

## Workspaces

### Adapter Comparison

On macOS, import a `.fmadapter` package and run the same prompt through fresh
base-model and adapter sessions. The workspace shows both streams and diagnostic
time-to-first-token and total-duration measurements.

Training and export remain in the companion `fmas` CLI:

```bash
python3.11 -m venv .venv-fmas
source .venv-fmas/bin/activate
python -m pip install -e Tools/AdapterStudio
fmas init
fmas setup
fmas train-adapter --help
fmas export --help
```

See [`Tools/AdapterStudio`](Tools/AdapterStudio) for the full workflow.

## Command-Line Interface

The `afm` CLI now ships from the standalone
[`rudrankriyam/Foundation-Models-Framework-CLI`](https://github.com/rudrankriyam/Foundation-Models-Framework-CLI)
repository. It uses the public `FoundationModelsKit` package and keeps CLI
releases independent from Foundation Lab app releases.

```bash
brew tap rudrankriyam/tap
brew install afm
```

See the CLI repository for source, documentation, release automation, and
server-mode implementation.

## Repository Map

| Surface | Location | Purpose |
| --- | --- | --- |
| Foundation Lab | [`Foundation Lab`](Foundation%20Lab) | Native Library, Playground, Runs, guided labs, and workspaces |
| FoundationLabCore | [`FoundationLabCore`](FoundationLabCore) | UI-independent requests, results, use cases, providers, and experiment models |
| FoundationModelsKit | [`rryam/FoundationModelsKit`](https://github.com/rryam/FoundationModelsKit) | External transcript, context, history, and system-tool package |
| AFM CLI | [`rudrankriyam/Foundation-Models-Framework-CLI`](https://github.com/rudrankriyam/Foundation-Models-Framework-CLI) | Scriptable Foundation Models workflows |
| FoundationModelsBench | [`rudrankriyam/FoundationModelsBench`](https://github.com/rudrankriyam/FoundationModelsBench) | External quality, safety, tool-use, on-device, and Private Cloud Compute benchmark |
| Adapter tooling | [`Tools/AdapterStudio`](Tools/AdapterStudio) | Adapter training and export with `fmas` |
| Book playgrounds | [`BookPlaygrounds`](BookPlaygrounds) | Chapter-oriented `#Playground` examples |

FoundationModelsBench and the AFM CLI are developed and released from their
standalone repositories. Foundation Lab keeps the native app, app runtime, and
adapter tooling here.

## Swift Package Products

`FoundationModelsKit` and `FoundationModelsTools` are defined in the external
[`rryam/FoundationModelsKit`](https://github.com/rryam/FoundationModelsKit)
package. Local package consumers should depend on that package URL directly
rather than requesting those products from this repository's root manifest.

- `FoundationMode
