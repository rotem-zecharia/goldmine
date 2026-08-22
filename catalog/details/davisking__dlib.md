# davisking/dlib

A toolkit for making real world machine learning and data analysis applications in C++

## tools

Either fetch the latest stable release of dlib from PyPi and install that:
```bash
pip install dlib
```
Or fetch the very latest version from github and install that:
```bash
git clone https://github.com/davisking/dlib.git
cd dlib
pip install .
```

It's possible to change build settings by passing parameters to `setup.py` or `DLIB_*` environment variables.
For example, setting the environment variable `DLIB_NO_GUI_SUPPORT` to `ON` will add the cmake option
`-DDLIB_NO_GUI_SUPPORT=ON`.
