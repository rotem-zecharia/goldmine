# gyroflow/gyroflow

Video stabilization using gyroscope data

## features

- Real-time preview, parameter adjustments and all calculations
- GPU processing and rendering, all algorithms fully multi-threaded
- Rolling shutter correction
- [Video editor plugins](https://github.com/gyroflow/gyroflow-plugins) (Adobe Premiere/Ae, DaVinci Resolve, Final Cut Pro and more), allowing you to apply stabilization directly in a video editor without transcoding
- Supports full Sony metadata (recording params, automatic lens, support for IBIS, OIS, EIS - you can have IBIS enabled in camera and still apply Gyroflow on top)
- Supports already stabilized GoPro videos (captured with Hypersmooth enabled) (Hero 8 and up)
- Supports and renders 10-bit videos (up to 16-bit 4:4:4:4 for regular codecs and 32-bit float for OpenEXR - working directly on YUV data to maintain maximum quality)
- Customizable lens correction strength
- Render queue
- Keyframes
- Ability to create custom settings presets
- Visual chart with gyro data (displays gyro, accelerometer, magnetometer, and quaternions, including smoothed quaternions)
- Supports underwater footage (corrects underwater distortions)
- Modern responsive user interface with Dark and Light theme
- Adaptive zoom (dynamic cropping)
- Zoom limit
- Supports image sequences (PNG, OpenEXR, CinemaDNG)
- Based on [telemetry-parser](https://github.com/AdrianEddy/telemetry-parser) - supports all gyro sources out of the box
- Gyro low pass filter, arbitrary rotation (pitch, roll, yaw angles) and orientation
- Multiple gyro integration methods for orientation determination
- Multiple video orientation smoothing algorithms, including horizon levelling and per-axis smoothness adjustment.
- Cross-platform - works on Windows/Linux/Mac/Android/iOS
- Multiple UI languages
- Supports variable and high frame rate videos - all calculations are done on timestamps
- H.264/AVC, H.265/HEVC, ProRes, DNxHD, CineForm, PNG and OpenEXR outputs, with H.264 and H.265 fully GPU accelerated (ProRes also accelerated on Apple Silicon)
- Easy lens calibration process
- Fully zero-copy GPU preview rendering
- Core engine is a separate library without external dependencies (no Qt, no ffmpeg, no OpenCV), and can be used to create OpenFX and Adobe plugins (on the TODO list)
- Automatic updates of lens profile database
- Built-in official lens profiles for GoPro HERO 6-13; Sony; DJI; Insta360 action cameras; RunCam: Thumb series, 5 Orange
- Easy management of the video editor plugins from within the app
- Ability to add an additional 3D rotation (useful for framing vertical videos)

## requirements

- Windows 10 64-bit (1809 or later)
    - If you have Windows "N" install, go to `Settings` -> `Apps` -> `Optional features` -> `Add a feature` -> enable `Media Feature Pack`
- macOS 10.15 or later (both Intel and Apple Silicon are supported natively)
- Linux:
    - `.tar.gz` package (recommended): Debian 10+, Ubuntu 18.10+, CentOS 8.2+, openSUSE 15.3+. Other distros require glibc 2.28+ (`ldd --version` to check)
    - `.AppImage` should work everywhere
- Android 6+
- iOS 14+

## limitations

See the [open issues](https://github.com/gyroflow/gyroflow/issues) for a list of proposed features and known issues.
There's also a ton of TODO comments throughout the code.

## configuration

`Visual Studio Code` with `rust-analyzer` extension.

For working with QML I recommend to use Qt Creator and load all QML files there, as it has auto-complete and syntax highlighting.
The project also supports UI live reload, it's a super quick way of working with the UI. Just change `live_reload = true` in `gyroflow.rs` and it should work right away. Now every time you change any QML file, the app should reload it immediately.
