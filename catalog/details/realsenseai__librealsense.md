# realsenseai/librealsense

RealSense SDK

## features

- **High-resolution color and depth** at close and long ranges
- **Open source SDK** with rich examples and wrappers (Python, ROS, C#, Unity and [more...](https://github.com/realsenseai/librealsense/tree/master/wrappers))
- **Active developer community and defacto-standard 3D stereo camera for robotics**
- **Cross-platform** support: Windows, Linux, macOS, Android, and Docker

## Product Line

RealSense stereo depth products use stereo vision to calculate depth, providing high-quality performance in various lighting and environmental conditions.

Here are some examples of the supported models:

| Product | Image | Description |
|---------|-------|-------------|
| [**D555 PoE**](https://realsenseai.com/ruggedized-industrial-stereo-depth/d555-poe/) | <img src="https://realsenseai.com/wp-content/uploads/2025/07/D555.png" width="1000"> | The RealSense™ Depth Camera D555 introduces Power over Ethernet (PoE) interface on chip, expanding our portfolio of USB and GMSL/FAKRA products. |
| [**D457 GMSL/FAKRA**](https://realsenseai.com/ruggedized-industrial-stereo-depth/d457-gmsl-fakra/) | <img src="https://realsenseai.com/wp-content/uploads/2025/07/D457.png" width="1000"> | The RealSense™ Depth Camera D457 is our first GMSL/FAKRA high bandwidth stereo camera. The D457 has an IP65 grade enclosure protecting it from dust ingress and projected water. |
| [**D455**](https://realsenseai.com/stereo-depth-cameras/real-sense-depth-camera-d455/) | <img src="https://www.realsenseai.com/wp-content/uploads/2021/11/455.png" width="1000"> | The RealSense D455 is a long-range stereo depth camera with a 95 mm baseline, global-shutter depth sensors, an RGB sensor, and a built-in IMU, delivering accurate depth at distances up to 10 m.. |
| [**D435if**](https://realsenseai.com/stereo-depth-cameras/depth-camera-d435i/) | <img src="https://realsenseai.com/wp-content/uploads/2025/06/D435if-a.png" width="1000"> | The D435if is one of [RealSense™ Depth Camera with IR pass filter family](https://realsenseai.com/stereo-depth-with-ir-pass-filter/) expanding our portfolio targeting the growing robotic market. The D400f family utilizes an IR pass filter to enhance depth quality and performance range in many robotic environments.|
| [**D405**](https://realsenseai.com/stereo-depth-cameras/stereo-depth-camera-d405/) | <img src="https://realsenseai.com/wp-content/uploads/2025/07/D-405.png" width="1000"> | The RealSense™ Depth Camera D405 is a short-range stereo camera providing sub-millimeter accuracy for your close-range computer vision needs. |


> 🛍️ [Explore more stereo products](https://store.realsenseai.com/)

## installation

Start developing with RealSense in minutes using either method below.

### 1️. Precompiled SDK

This is the best option if you want to plug in your camera and get started right away.
1. Download the latest SDK bundle from the [Releases page](https://github.com/realsenseai/librealsense/releases).
2. Connect your RealSense camera.
3. Run the included tools:
    - [RealSense Viewer](./tools/realsense-viewer/): View streams, tune settings, record and playback.
    - [Depth Quality Tool](./tools/depth-quality/): Measure accuracy and fill rate.

### Setup Guides - precompiled SDK

<a href="./doc/distribution_linux.md"><img src="https://img.shields.io/badge/Ubuntu_Guide-333?style=flat&logo=ubuntu&logoColor=white" style="margin: 5px;" alt="Linux\Jetson Guide"/></a>
<a href="./doc/distribution_windows.md"><img src="https://custom-icon-badges.demolab.com/badge/Windows_Guide-333?logo=windows11&logoColor=white" style="margin: 5px;" alt="Windows Guide"/></a>

> **Note:** For **minor releases**, we publish Debian packages as release artifacts that you can download and install directly.

### 2️. Build from Source
For a more custom installation, follow these steps to build the SDK from source.
1. Clone the repository and create a build directory:
   ```bash
   git clone https://github.com/realsenseai/librealsense.git
   cd librealsense
   mkdir build && cd build
   ```
2. Run CMake to configure the build:
    ```bash
    cmake ..
    ```
3. Build the project:
    ```bash
    cmake --build .
    ```

### Setup Guides - build from source

<a href="./doc/installation.md"><img src="https://img.shields.io/badge/Ubuntu_Guide-333?style=flat&logo=ubuntu&logoColor=white" style="margin: 5px;" alt="Linux Guide"/></a>
<a href="./doc/installation_jetson.md"><img src="https://img.shields.io/badge/Jetson_Guide-333?style=flat&logo=nvidia&logoColor=white" style="margin: 5px;" alt="Jetson Guide"/></a>
<a href="./doc/installation_windows.md"><img src="https://custom-icon-badges.demolab.com/badge/Windows_Guide-333?logo=windows11&logoColor=white" style="margin: 5px;" alt="Windows Guide"/></a>
<a href="./doc/installation_osx.md"><img src="https://img.shields.io/badge/macOS_Guide-333?style=flat&logo=apple&logoColor=white" style="margin: 5px;" alt="macOS Guide"/></a>


## Python Packages
[![pyrealsense2](https://img.shields.io/pypi/v/pyrealsense2.svg?label=pyrealsense2&logo=pypi)](https://pypi.org/project/pyrealsense2/)
[![PyPI - pyrealsense2-beta](https://img.shields.io/pypi/v/pyrealsense2-beta.svg?label=pyrealsense2-beta&logo=pypi)](https://pypi.org/project/pyrealsense2-beta/)

**Which should I use?**
- **Stable:** `pyrealsense2` — validated releases aligned with SDK tags (Recommended for most users).  
- **Beta:** `pyrealsense2-beta` — fresher builds for early access and testing. Expect faster updates.  

### Install
```bash
pip install pyrealsense2 # Stable
pip install pyrealsense2-beta # Beta
```
> Both packages import as `pyrealsense2`. Install **only one** at a time.

## Ready to Hack!

Our library offers a high level API for using RealSense depth cameras (in addition to lower level ones).
The following snippets show how to start streaming frames and extracting the depth value of a pixel:

**C++**
```cpp
#include <librealsense2/rs.hpp>
#include <iostream>

int main() {
    rs2::pipeline p;                 // Top-level API for streaming & processing frames
    p.start();                       // Configure and start the pipeline

    while (true) {
        rs2::frameset frames = p.wait_for_frames();        // Block until frames arrive
        rs2::depth_frame depth = frames.get_depth_frame(); // Get depth frame
        if (!depth) continue;

        int w = depth.get_width(), h = depth.get_height();
        float dist = depth.get_distance(w/2, h/2);         // Distance to center pixel
        std::cout << "The camera is facing an object " << dist << " meters away\r";
    }
}
```

**Python**
```python
import pyrealsense2 as rs

pipeline = rs.pipeline() # Create 
