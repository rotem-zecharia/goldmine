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


## Running the unit test suite

Type the following to compile and run the dlib unit test suite:

```bash
cd dlib/test
mkdir build
cd build
cmake ..
cmake --build . --config Release
./dtest --runall
```

Note that on windows your compiler might put the test executable in a subfolder called `Release`. If that's the case then you have to go to that folder before running the test.

This library is licensed under the Boost Software License, which can be found in [dlib/LICENSE.txt](https://github.com/davisking/dlib/blob/master/dlib/LICENSE.txt).  The long and short of the license is that you can use dlib however you like, even in closed source commercial software.

## dlib sponsors

This research is based in part upon work supported by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA) under contract number 2014-14071600010. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of ODNI, IARPA, or the U.S. Government.
