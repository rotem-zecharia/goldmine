# suifei/fridare

强大的 Frida 重打包工具，用于 iOS 和 Android。轻松修改 Frida 特征，增强隐蔽性，绕过检测。简化逆向工程和安全测试。Powerful Frida repackaging tool for iOS and Android. Easily modify Frida servers to enhance stealth and bypass detection. Streamli

## features

- Dual-track Frida mods · Fyne GUI · Windows native deb · multi-arch static CLI  
- Magic name: **exactly 5 lowercase a–z** end-to-end  
- Optional local rebuild: `cd ui && ./build.sh` or `.\build.ps1` (CGO for GUI)

## requirements

- macOS operating system (for running build scripts)
- Homebrew
- Python 3
- Go (for compiling the hexreplace tool)
- Jailbroken iOS device
- OpenSSH installed on iOS device

## installation

1. Clone this repository:
```shell
git clone https://github.com/suifei/fridare.git
cd fridare
```

2. Run the setup command:
```shell
./fridare.sh setup
```
This command will check and install the required dependencies.

3. View the help information:
```shell
./fridare.sh help
```

## tools

Fridare provides multiple commands to meet different needs:
