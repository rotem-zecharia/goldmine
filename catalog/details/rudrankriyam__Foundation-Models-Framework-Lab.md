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
