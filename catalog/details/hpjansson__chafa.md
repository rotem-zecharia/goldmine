# hpjansson/chafa

📺🗿 Terminal graphics for the 21st century.

## installation

Chafa is most likely packaged for your distribution, so if you're not
going to hack on it, you're better off using
[official packages](https://hpjansson.org/chafa/download/). If you want to
build the latest and greatest yourself, read on.

You will need GCC, make, Autoconf, Automake, Libtool and the GLib
development package installed to compile Chafa from its git repository. If
you want to build the command-line tool `chafa` and not just the library,
you will additionally need development packages for:

* FreeType2. Often packaged as `libfreetype6-dev` or `freetype2-devel`.
* libjpeg (optional). Look for `libjpeg-dev`, `libjpeg62-devel` or `libjpeg8-devel`.
* librsvg (optional). Look for `librsvg2-dev` or `librsvg-devel`.
* libtiff (optional). Look for `libtiff5-dev` or `libtiff-devel`.
* libwebp (optional). Look for `libwebp-dev` or `libwebp-devel`.

If you want to build documentation, you will also need gtk-doc.

Start by cloning the repository:

```sh
$ git clone https://github.com/hpjansson/chafa.git
```

Then cd to the toplevel directory and issue the following shell commands:

```sh
$ ./autogen.sh
$ make
$ sudo make install
```

That should do it!
