# shimat/opencvsharp

OpenCV wrapper for .NET

## features

* OpenCvSharp is modeled on the native OpenCV C++ API as closely as practical.
* Many classes of OpenCvSharp implement IDisposable. Unsafe resources are managed automatically. 
* OpenCvSharp does not force object-oriented programming style on you. You can also call native-style OpenCV functions.
* OpenCvSharp provides functions for converting from `Mat` to `Bitmap` (GDI+) or `WriteableBitmap` (WPF).

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
