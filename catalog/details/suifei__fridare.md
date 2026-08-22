# suifei/fridare

强大的 Frida 重打包工具，用于 iOS 和 Android。轻松修改 Frida 特征，增强隐蔽性，绕过检测。简化逆向工程和安全测试。Powerful Frida repackaging tool for iOS and Android. Easily modify Frida servers to enhance stealth and bypass detection. Streamli

## features

- Dual-track Frida mods · Fyne GUI · Windows native deb · multi-arch static CLI  
- Magic name: **exactly 5 lowercase a–z** end-to-end  
- Optional local rebuild: `cd ui && ./build.sh` or `.\build.ps1` (CGO for GUI)

### Historical English changelog notes

## [v3.1.4] - 2024-07-18

### Added
- Introduced new `patch-tools` command for modifying the frida-tools module
- Implemented `render_markdown` function to display simple Markdown formatting in the terminal
- Added `generate_random_name` function to create random Frida modification names
- Created `move_file` function to handle "are identical" errors during file moves

### Improved
- Enhanced `list_frida_versions` function to render Markdown-formatted version descriptions
- Upgraded `build_frida` function to support building from local deb files
- Expanded functionality and error handling in `patch_frida_tools` and `restore_frida_tools` functions
- Optimized `modify_frida_tools` function for more reliable frida-tools modifications
- Enhanced `download_frida_module` function with support for specific OS and architecture

### Fixed
- Resolved issues with incorrect Frida path detection in certain scenarios
- Addressed "are identical" errors that could occur during file moves

### Changed
- Updated `show_main_usage` and other usage instruction functions to reflect new features
- Adjusted `parse_arguments` function to accommodate the new `patch-tools` command
- Modified configuration file handling to include support for `FRIDA_NAME`

### Other
- Improved overall code structure for better readability and maintainability
- Added more detailed log outputs for enhanced execution information
- Updated version number to 3.1.4

### New Features v3.0.0
- Added `fridare.sh` script, integrating all functionalities and providing a more complete command-line interface
- Added `build`, `ls`, `download`, `lm`, `setup`, `config`, and `help` commands
- Added configuration file support for saving and loading user settings
- Added color output to enhance user experience
- Added automatic dependency checking and installation
- Added functionality to download specific Frida modules
- Added listing of available Frida versions and modules

### New Features v2.2.0 (Tested only on macOS arm architecture, other architectures not tested)
- Added frida-tools patch, adapting to `frida:rpc` feature modification
   - Resolves the issue of Android memory scanning for this string
   - Automatically scans the local pip installation location of frida-tools, modifies the `core.py` file, and modifies the `_frida.abi3.so` file
- Added frida-agent.dylib modification, hiding from filename and load location
   - Resolves the issue of unhidden agent loading

### New Features v2.1.1

- Introduced `autoinstall.sh` script for automatic deployment of Frida plugins.
- Introduced `Makefile` to simplify the project build and deployment process.
- Before running, please ensure that the [issh](https://github.com/4ch12dy/issh) command is installed on your machine. And configure password-free SSH login.
   > Configure password-free SSH login for issh
   ```shell
   # Generate keygen, skip if already generated
   ssh-keygen -t rsa -b 4096 -C "<EMAIL>"
   # Configure iPhone IP, can be skipped if using USB connection
   issh ip set <iPhone-IP>     
   # Copy public key to /var/root on the phone, requires root password alpine
   issh scp ~/.ssh/id_rsa.pub  
   # Add public key to authorized_keys file on remote server
   issh run "mkdir -p ~/.ssh && cat /var/root/id_rsa.pub >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && chmod 700 ~/.ssh"
   ```

## Features

- **🎉 Brand New GUI Version**: Modern graphical user interface based on Fyne framework
- **🖥️ Cross-Platform Support**: Native GUI applications for Windows, macOS, Linux
- **📱 Intuitive Operation**: Visual Frida server modification and configuration management
- **📊 Real-time Feedback**: Graphical log display and progress bar visualization
- **🔧 Windows deb Packag

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

### Command List

1. `build`: Repackage Frida
2. `ls` or `list`: List available Frida versions
3. `download`: Download a specific version of Frida
4. `lm` or `list-modules`: List available Frida modules
5. `setup`: Check and install system dependencies
6. `config`: Set configuration options
7. `help`: Display help information

### Usage Examples

1. Build a modified version of Frida
```shell
./fridare.sh build -v 16.0.19 -p 8899 -y
```
This command will build Frida version 16.0.19, set the port to 8899, and automatically confirm all prompts.

2. List available Frida versions
```shell
./fridare.sh ls
```

3. Download a specific version of Frida
```shell
./fridare.sh download -v 16.0.19 -m frida-server ./output
```
This command will download the frida-server module of version 16.0.19 to the ./output directory.

4. Download all Frida modules of the latest version
```shell
./fridare.sh download -latest -all ./output
```

5. List available Frida modules
```shell
./fridare.sh lm
```

6. Set up the environment
```shell
./fridare.sh setup
```
This command will check and install the required system dependencies.

7. Configure settings
```shell
./fridare.sh config set proxy http://127.0.0.1:7890
./fridare.sh config set port 9999
./fridare.sh config set frida-name abcde
```
These commands set the proxy, port, and Frida modification name respectively.

8. List current configuration
```shell
./fridare.sh config ls
```

9. Get help information for a specific command
```shell
./fridare.sh help build
```
This command will display detailed usage for the build command.

10. Build Frida using the latest version
```shell
./fridare.sh build -latest -p 9999 -y
```
This command will build using the latest version of Frida, set the port to 9999, and automatically confirm all prompts.

11. Download but don't extract Frida module
```shell
./fridare.sh download -latest -m frida-gadget --no-extract ./output
```
This command will download the latest version of the frida-gadget module to the ./output directory but won't automatically extract it.

12. Install frida-tools
```shell
./fridare.sh config frida-tools
```
This command will install or update frida-tools.

13. Transfer the generated .deb package to your iOS device:
```shell
scp ./dist/frida_16.3.3_iphoneos-arm_tcp.deb root@<iPhone-IP>:/var/root/
```

14. SSH into your iOS device and install the modified package:
```shell
ssh root@<iPhone-IP>
dpkg -i /var/root/frida_16.3.3_iphoneos-arm_tcp.deb
```

These examples cover the main functionalities and common usage scenarios of the script. They can help you quickly get started with using it.
