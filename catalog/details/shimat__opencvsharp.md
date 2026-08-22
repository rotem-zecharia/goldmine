# shimat/opencvsharp

OpenCV wrapper for .NET

## installation

### Windows (x64)
```bash
dotnet add package OpenCvSharp5.Windows
```

### Windows (ARM64 — Snapdragon X and other arm64 devices)
```bash
dotnet add package OpenCvSharp5
dotnet add package OpenCvSharp5.runtime.win-arm64
```

### Linux / Ubuntu
```bash
dotnet add package OpenCvSharp5
dotnet add package OpenCvSharp5.official.runtime.linux-x64
# optional headless profile (full module set, no GTK3/X11 dependency)
# dotnet add package OpenCvSharp5.official.runtime.linux-x64.headless
# optional slim profile (smaller native dependency surface)
# dotnet add package OpenCvSharp5.official.runtime.linux-x64.slim
```

### macOS
```bash
dotnet add package OpenCvSharp5
# Intel (x64):
dotnet add package OpenCvSharp5.runtime.osx.x64
# Apple Silicon (arm64):
dotnet add package OpenCvSharp5.runtime.osx.arm64
```

For more installation options, see the [Installation](#installation) section below, or the full [NuGet package list](#nuget).

## features

* OpenCvSharp is modeled on the native OpenCV C++ API as closely as practical.
* Many classes of OpenCvSharp implement IDisposable. Unsafe resources are managed automatically. 
* OpenCvSharp does not force object-oriented programming style on you. You can also call native-style OpenCV functions.
* OpenCvSharp provides functions for converting from `Mat` to `Bitmap` (GDI+) or `WriteableBitmap` (WPF).

## Target OpenCV
* **OpenCvSharp5**: [OpenCV 5.0.x](https://opencv.org/) with [opencv_contrib](https://github.com/opencv/opencv_contrib)
* **OpenCvSharp4**: [OpenCV 4.13.0](https://opencv.org/) with [opencv_contrib](https://github.com/opencv/opencv_contrib)

## requirements

* **OpenCvSharp5**: [.NET 8](https://www.microsoft.com/net/download) or later
* **OpenCvSharp4**: .NET 8+, .NET Standard 2.0 / 2.1, or .NET Framework 4.6.1+ (WpfExtensions also directly targets .NET Framework 4.8)
* (Windows Server) Media Foundation
```
PS1> Install-WindowsFeature Server-Media-Foundation
```
* (Linux) The official `OpenCvSharp5.official.runtime.linux-x64` package is built on manylinux_2_28 and works on Ubuntu 20.04+, Debian 10+, RHEL/AlmaLinux 8+, and other Linux distributions with glibc 2.28+. The full package includes FFmpeg (LGPL v2.1) and Tesseract statically linked.
  * The **full** package uses GTK3 for `highgui` support (`Cv2.ImShow`, `Cv2.WaitKey`, etc.). GTK3 is pre-installed on standard Ubuntu/Debian/RHEL environments. In minimal or container environments where it is absent, install it manually (`apt-get install libgtk-3-0` or `dnf install gtk3`), or use the **headless** or **slim** profile instead.
  * The **headless** package (`OpenCvSharp5.official.runtime.linux-x64.headless`) keeps the full module set (`videoio`, `dnn`, `ml`, `contrib`, `stitching`, `barcode`, ...) but disables `highgui`, so it has no GTK3/X11 dependency — suitable for containerized services that need more than the slim module set below.
  * The **slim** package (`OpenCvSharp5.official.runtime.linux-x64.slim`) disables `highgui` and reduces the module set — also has no GUI dependencies.


**OpenCvSharp won't work on Unity and Xamarin platforms.** For Unity, please consider using [OpenCV for Unity](https://assetstore.unity.com/packages/tools/integration/opencv-for-unity-21088) or some other solutions.

**OpenCvSharp does not support CUDA.** If you want to use CUDA features, you need to customize the native bindings yourself.

OpenCV's OpenCL Transparent API can be used through `UMat`. See [OpenCL Acceleration with UMat](docs/docfx/articles/guides/opencl-and-umat.md) for runtime diagnostics and benchmarking guidance.

## tools

For step-by-step guides, package selection, and troubleshooting, see the **[OpenCvSharp documentation](https://shimat.github.io/opencvsharp/)**. More complete programs are available in the **[samples repository](https://github.com/shimat/opencvsharp_samples/)**.

**Always remember to release Mat and other IDisposable resources using the `using` syntax:**
```C#
// Edge detection by Canny algorithm
using OpenCvSharp;

using var src = new Mat("lenna.png", ImreadModes.Grayscale);
using var dst = new Mat();

Cv2.Canny(src, dst, 50, 200);
using (new Window("src image", src))
using (new Window("dst image", dst))
{
    Cv2.WaitKey();
}
```

<details>
<summary><b>Note: chained Mat arithmetic is leak-free</b></summary>

`Mat` arithmetic operators (`+`, `-`, `*`, `/`, the comparison and bitwise operators, `T()`, `Inv()`, `Mul()`, `Abs()`, `Eye`/`Zeros`/`Ones`, ...) return a purely managed, lazily-evaluated expression tree (`MatExpr`) that holds **no** unmanaged resources. The native `cv::MatExpr` chain is built only when the expression is materialized — when it is assigned to a `Mat`, or passed where a `Mat`/`InputArray` is expected — and every native intermediate is disposed immediately during that evaluation.

As a result, chained expressions never leak: you only need `using` on your inputs and on the final `Mat`. The intermediate expression nodes require no disposal.

```C#
using var src = new Mat("lenna.png", ImreadModes.Grayscale);

// The intermediate (src * 0.8) holds no native resource; nothing leaks.
using Mat dst = 255 - src * 0.8;
```

```C#
using var mat1 = new Mat(new Size(100, 100), MatType.CV_8UC3, new Scalar(0));
using Mat mat3 = 255 - mat1 * 0.8;

using var canny = new Mat();
Cv2.Canny(src, canny, 50, 200);   // an expression can be passed directly to a Cv2 method
```

</details>

## Code samples
https://github.com/shimat/opencvsharp_samples/

Interactive browser-based samples (Blazor WebAssembly) are maintained separately at https://github.com/shimat/opencvsharp_blazor_sample/, with a [live demo](https://shimat.github.io/opencvsharp_blazor_sample/).

## Documentation
https://shimat.github.io/opencvsharp/

## NuGet

> Packages are published in two parallel families: **`OpenCvSharp5.*`** (OpenCV 5.x, .NET 8+) and **`OpenCvSharp4.*`** (OpenCV 4.13.0; also supports .NET Framework / .NET Standard). The tables below list the OpenCvSharp5 packages — each has an identically-named `OpenCvSharp4.*` counterpart.

### Managed libraries

| Package | Description |
|---------|-------------|
|**[OpenCvSharp5](https://www.nuget.org/packages/OpenCvSharp5/)**| OpenCvSharp core libraries |
|**[OpenCvSharp5.GdipExtensions](https://www.nuget.org/packages/OpenCvSharp5.GdipExtensions/)**| GDI+ (System.Drawing) Extensions |
|**[OpenCvSharp5.WpfExtensions](https://www.nuget.org/packages/OpenCvSharp5.WpfExtensions/)**| WPF Extensions |
|**[OpenCvSharp5.AvaloniaExtensions](https://www.nuget.org/packages/OpenCvSharp5.AvaloniaExtensions/)**| Avalonia Extensions (cross-platform) |
|**[OpenCvSharp5.Windows](https://www.nuget.org/packages/OpenCvSharp5.Windows/)**| All-in-one package for Windows |
|**[OpenCvSharp5.Windows.Slim](https://www.nuget.org/packages/OpenCvSharp5.Windows.Slim/)**| All-in-one slim package for Windows |

<details>
<summary><h3>Native bindings</h3></summary>

| Package | Description |
|---------|-------------|
|**[OpenCvSharp5.runtime.win](https://www.nuget.org/packages/OpenCvSharp5.runtime.win/)**| Native bindings for Windows x64 |
|**[OpenCvSharp5.runtime.win.slim](https://www.nuget.org/packages/OpenCvSharp5.runtime.win.slim/)**| Slim native bindings for Windows x64, with `core,imgproc,imgcodecs,calib3d,features2d,flann,objdetect,photo,ml,video,barcode` enabled |
|**[OpenCvSharp5.runtime.win-arm64](https://www.nuget.org/packages/OpenCvSharp5.runtime.win-arm64/)**| Native bindings for Windows ARM64 (Snapdragon X and other arm64 devices). FFmpeg not included. |
|**[OpenCvSharp5.runtime.win-arm64.slim](https://www.nuget.org/packages
