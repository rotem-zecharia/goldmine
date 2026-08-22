# ceph/ceph

Ceph is a distributed object, block, and file storage platform

## requirements

*section last updated 06 Sep 2024*

We provide the Debian and Ubuntu ``apt`` commands in this procedure. If you use
a system with a different package manager, then you will have to use different
commands. 

#. Install ``curl``:

    apt install curl

#. Install package dependencies by running the ``install-deps.sh`` script:

	./install-deps.sh

#. Install the ``python3-routes`` package:

    apt install python3-routes

## configuration

The `-D` flag can be used with `cmake` to speed up the process of building Ceph
and to customize the build.

#### Building without RADOS Gateway

The RADOS Gateway is built by default. To build Ceph without the RADOS Gateway,
run a command of the following form:

	cmake -DWITH_RADOSGW=OFF [path to top-level ceph directory]

#### Building with debugging and arbitrary dependency locations 

Run a command of the following form to build Ceph with debugging and alternate
locations for some external dependencies:

	cmake -DCMAKE_INSTALL_PREFIX=/opt/ceph -DCMAKE_C_FLAGS="-Og -g3 -gdwarf-4" \
	..

Ceph has several bundled dependencies such as Boost, RocksDB and Arrow. By
default, `cmake` builds these bundled dependencies from source instead of using
libraries that are already installed on the system. You can opt to use these
system libraries, as long as they meet Ceph's version requirements. To use
system libraries, use `cmake` options like `WITH_SYSTEM_BOOST`, as in the
following example:

	cmake -DWITH_SYSTEM_BOOST=ON [...]

To view an exhaustive list of -D options, invoke `cmake -LH`:

	cmake -LH

#### Preserving diagnostic colors

If you pipe `ninja` to `less` and would like to preserve the diagnostic colors
in the output in order to make errors and warnings more legible, run the
following command:  

	cmake -DDIAGNOSTICS_COLOR=always ...

The above command works only with supported compilers.

The diagnostic colors will be visible when the following command is run: 

	ninja | less -R

Other available values for `DIAGNOSTICS_COLOR` are `auto` (default) and
`never`.
