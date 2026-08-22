# go-vgo/robotgo

RobotGo, Go Native cross-platform RPA, GUI automation, Auto test and Computer use @vcaesar

## requirements

Now, Please make sure `Golang, GCC` is installed correctly before installing RobotGo.

### ALL:

```
Golang

GCC
```

#### For MacOS:

```
brew install go
```

Xcode Command Line Tools; <br>
And Privacy setting, add Screen Recording and Accessibility under: <br>
`System Settings > Privacy & Security > Accessibility, Screen & System Audio Recording`.

```
xcode-select --install
```

#### For Windows:

```
winget install Golang.go
```

[llvm-mingw](https://github.com/mstorsjo/llvm-mingw)

```
winget install MartinStorsjo.LLVM-MinGW.UCRT
```

or [Mingw-w64](https://sourceforge.net/projects/mingw-w64/files)

```
winget install BrechtSanders.WinLibs.POSIX.UCRT
```

Or Download the [Mingw-w64](https://sourceforge.net/projects/mingw-w64/files) and the others gcc, then set system environment variables like `C:\mingw64\bin` to the env `Path`.
[Set environment variables to run GCC from command line](https://www.youtube.com/results?search_query=Set+environment+variables+to+run+GCC+from+command+line).

`Or The others GCC` (Except the Mingw-w64, you should compile the "libpng" with yourself when use the [bitmap](https://github.com/vcaesar/bitmap).)

#### For everything else:

```
GCC

X11 with the XTest extension (the Xtst library)

"Clipboard": xsel xclip

"Bitmap": libpng (Just used by the "bitmap".)

"Event-Gohook": xcb, xkb, libxkbcommon (Just used by the "hook".)
```

##### Ubuntu:

```yml

## installation

sudo snap install go  --classic

# gcc
sudo apt install gcc libc6-dev

# x11
sudo apt install libx11-dev xorg-dev libxtst-dev

# Clipboard
sudo apt install xsel xclip

# Bitmap
sudo apt install libpng++-dev

# GoHook
sudo apt install xcb libxcb-xkb-dev x11-xkb-utils libx11-xcb-dev libxkbcommon-x11-dev libxkbcommon-dev
```

##### Fedora:

```yml
# x11
sudo dnf install libXtst-devel

# Clipboard
sudo dnf install xsel xclip

# Bitmap
sudo dnf install libpng-devel

# GoHook
sudo dnf install libxkbcommon-devel libxkbcommon-x11-devel xkbcomp-devel
xorg-x11-xkb-utils-devel (< Fedora 34)
```

#### Wayland

The Wayland backend is a **pure-Go (Cgo-free)** implementation, so no system C
libraries are required. It needs a wlroots-based compositor (Sway, Hyprland,
Wayfire, ...) that supports the following protocols:

```
zwlr_virtual_pointer_v1            (mouse control)
zwp_virtual_keyboard_v1            (keyboard control)
zwlr_screencopy_v1                 (screen capture)
zwlr_foreign_toplevel_management_v1 (window management)
```

GNOME and KDE do **not** support these protocols natively.

#### libei (GNOME / KDE)

The libei backend is also a **pure-Go (Cgo-free)** implementation. It drives input
through the freedesktop `xdg-desktop-portal` RemoteDesktop interface, so it works
on GNOME and KDE (unlike the wlroots Wayland backend). It requires:

```
xdg-desktop-portal               (the portal D-Bus service)
xdg-desktop-portal-gnome / -kde  (your desktop's portal backend)
```

Note: the libei backend handles mouse and keyboard input only. Screen capture and
window management report `ErrNotSupported`.

## Installation:

With Go module support (Go 1.11+), just import:

```go
import "github.com/go-vgo/robotgo"
```

Otherwise, to install the robotgo package, run the command:

```
go get github.com/go-vgo/robotgo
```

png.h: No such file or directory? Please see [issues/47](https://github.com/go-vgo/robotgo/issues/47).

## Update:

```
go get -u github.com/go-vgo/robotgo
```

Note go1.10.x C file compilation cache problem, [golang #24355](https://github.com/golang/go/issues/24355).
`go mod vendor` problem, [golang #26366](https://github.com/golang/go/issues/26366).

## Cgo-free Builds:

RobotGo ships **pure-Go (Cgo-free)** backends for Windows, macOS, X11, Wayland
and libei (Linux), it's experimental. They expose the same `robotgo` API, so your code needs no changes —
only a build tag. These backends cross-compile with `CGO_ENABLED=0` (no GCC,
MinGW, Xcode, or X11 headers required).

| Backend                          | Build tag | Go package                          |
| -------------------------------- | --------- | ----------------------------------- |
| Windows (Cgo-free)               | `win`     | `github.com/go-vgo/robotgo/win`     |
| macOS (Quartz via purego)        | `mac`     | `github.com/go-vgo/robotgo/darwin`  |
| X11 (Linux, pure-Go X protocol)  | `x11`     | `github.com/go-vgo/robotgo/x11`     |
| Wayland (Linux, wlroots)         | `wayland` | `github.com/go-vgo/robotgo/wayland` |
| libei (Linux, GNOME/KDE portal)  | `libei`   | `github.com/go-vgo/robotgo/libei`   |
| Pure-Go default (all platforms)  | `purego`  | selects `mac`/`win`/`wayland` above |

```sh
# Pure-Go default backend per platform, one tag for all targets:
# macOS -> mac, Windows -> win, Linux -> wayland (combine with x11/libei to override)
go build -tags purego .
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags "purego,x11" .

# Windows, no Cgo / no MinGW required
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -tags win .

# macOS, Quartz/CoreGraphics loaded at runtime via purego (no Xcode required)
CGO_ENABLED=0 GOOS=darwin GOARCH=arm64 go build -tags mac .

# X11, pure-Go X protocol (XTEST) — no X11 headers required
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags x11 .

# Wayland, wlroots-based compositor (Sway, Hyprland, Wayfire, ...)
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags wayland .

# libei, GNOME/KDE via xdg-desktop-portal RemoteD

## tools

#### [Mouse](https://github.com/go-vgo/robotgo/blob/master/examples/mouse/main.go)

```Go
package main

import (
  "fmt"
  "github.com/go-vgo/robotgo"
)

func main() {
  robotgo.MouseSleep = 300

  robotgo.Move(100, 100)
  fmt.Println(robotgo.Location())
  robotgo.Move(100, -200) // multi screen supported
  robotgo.MoveSmooth(120, -150)
  fmt.Println(robotgo.Location())

  robotgo.ScrollDir(10, "up")
  robotgo.ScrollDir(20, "right")

  robotgo.Scroll(0, -10)
  robotgo.Scroll(100, 0)

  robotgo.MilliSleep(100)
  robotgo.ScrollSmooth(-10, 6)
  // robotgo.ScrollRelative(10, -100)

  robotgo.Move(10, 20)
  robotgo.MoveRelative(0, -10)
  robotgo.DragSmooth(10, 10)

  robotgo.Click("wheelRight")
  robotgo.Click("left", true)
  robotgo.MoveSmooth(100, 200, 1.0, 10.0)

  robotgo.Toggle("left")
  robotgo.Toggle("left", "up")
}
```

#### [Keyboard](https://github.com/go-vgo/robotgo/blob/master/examples/key/main.go)

```Go
package main

import (
  "fmt"

  "github.com/go-vgo/robotgo"
)

func main() {
  robotgo.Type("Hello World")
  robotgo.Type("だんしゃり", 0, 1)
  // robotgo.Type("テストする")

  robotgo.Type("Hi, Seattle space needle, Golden gate bridge, One world trade center.")
  robotgo.Type("Hi galaxy, hi stars, hi MT.Rainier, hi sea. こんにちは世界.")
  robotgo.Sleep(1)

  // ustr := uint32(robotgo.CharCodeAt("Test", 0))
  // robotgo.UnicodeType(ustr)

  robotgo.KeySleep = 100
  robotgo.KeyTap("enter")
  // robotgo.Type("en")
  robotgo.KeyTap("i", "alt", "cmd")

  arr := []string{"alt", "cmd"}
  robotgo.KeyTap("i", arr)

  robotgo.MilliSleep(100)
  robotgo.KeyToggle("a")
  robotgo.KeyToggle("a", "up")

  robotgo.WriteAll("Test")
  text, err := robotgo.ReadAll()
  if err == nil {
    fmt.Println(text)
  }
}
```

#### [Screen](https://github.com/go-vgo/robotgo/blob/master/examples/screen/main.go)

```Go
package main

import (
  "fmt"
  "strconv"

  "github.com/go-vgo/robotgo"
  "github.com/vcaesar/imgo"
)

func main() {
  x, y := robotgo.Location()
  fmt.Println("pos: ", x, y)

  color := robotgo.GetPixelColor(100, 200)
  fmt.Println("color---- ", color)

  sx, sy := robotgo.GetScreenSize()
  fmt.Println("get screen size: ", sx, sy)

  bit := robotgo.CaptureScreen(10, 10, 30, 30)
  defer robotgo.FreeBitmap(bit)

  img := robotgo.ToImage(bit)
  imgo.Save("test.png", img)

  num := robotgo.DisplaysNum()
  for i := 0; i < num; i++ {
    robotgo.DisplayID = i
    img1, _ := robotgo.CaptureImg()
    path1 := "save_" + strconv.Itoa(i)
    robotgo.Save(img1, path1+".png")
    robotgo.SaveJpeg(img1, path1+".jpeg", 50)

    img2, _ := robotgo.CaptureImg(10, 10, 20, 20)
    robotgo.Save(img2, "test_"+strconv.Itoa(i)+".png")

    x, y, w, h := robotgo.GetDisplayBounds(i)
    img3, err := robotgo.CaptureImg(x, y, w, h)
    fmt.Println("Capture error: ", err)
    robotgo.Save(img3, path1+"_1.png")
  }
}
```

#### [Bitmap](https://github.com/vcaesar/bitmap/blob/main/examples/main.go)

```Go
package main

import (
  "fmt"

  "github.com/go-vgo/robotgo"
  "github.com/vcaesar/bitmap"
)

func main() {
  bit := robotgo.CaptureScreen(10, 20, 30, 40)
  // use `defer robotgo.FreeBitmap(bit)` to free the bitmap
  defer robotgo.FreeBitmap(bit)

  fmt.Println("bitmap...", bit)
  img := robotgo.ToImage(bit)
  // robotgo.SavePng(img, "test_1.png")
  robotgo.Save(img, "test_1.png")

  bit2 := robotgo.ToCBitmap(robotgo.ImgToBitmap(img))
  fx, fy := bitmap.Find(bit2)
  fmt.Println("FindBitmap------ ", fx, fy)
  robotgo.Move(fx, fy)

  arr := bitmap.FindAll(bit2)
  fmt.Println("Find all bitmap: ", arr)

  fx, fy = bitmap.Find(bit)
  fmt.Println("FindBitmap------ ", fx, fy)

  bitmap.Save(bit, "test.png")
}
```

#### [OpenCV](https://github.com/vcaesar/gcv)

```Go
package main

import (
  "fmt"
  "math/rand"

  "github.com/go-vgo/robotgo"
  "github.com/vcaesar/gcv"
  "github.com/vcaesar/bitmap"
)

func main() {
  opencv()
}

func opencv() {
  name := "test.png"
  name1 := "test_001.png"
  robotgo.SaveCapture(name1, 10, 10, 30, 30)
  robotgo.SaveCapture(name)

  fmt.Print("gcv fin
