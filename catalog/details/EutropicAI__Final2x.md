# EutropicAI/Final2x

a cross-platform image super-resolution tool

## installation

##### [Download the latest release from here.](https://github.com/EutropicAI/Final2x/releases)

#### Windows

You can also use a package manager like winget or scoop to install and upgrade. Please note that the versions available through package managers may not always be the latest.

#### MacOS

```bash
sudo spctl --master-disable
# Disable Gatekeeper, then allow applications downloaded from anywhere in System Preferences > Security & Privacy > General
xattr -cr /Applications/Final2x.app
```

In first time, you need to run the command above in terminal to allow the app to run.

#### Linux

For Linux User, you need to install the dependencies first.

Make sure you have Python >= 3.9 and PyTorch >= 2.0 installed

```bash
pip install Final2x-core
Final2x-core -h # check if the installation is successful
apt install -y libomp5 xdg-utils
```

### Reference

The Python CLI and desktop backend now live in [`core`](./core) and are released with the desktop app under the same version number.

The following references were referenced in the development of this project:

- [naive-ui](https://github.com/tusen-ai/naive-ui)
- [electron-vite](https://github.com/alex8088/electron-vite)

### License

This project is licensed under the BSD 3-Clause - see
the [LICENSE file](./LICENSE) for details.

### Acknowledgements

Feel free to reach out to the project maintainers with any questions or concerns~
