# fail2ban/fail2ban

Daemon to ban hosts that cause multiple authentication errors

## installation

Fail2Ban is likely already packaged for your Linux distribution and [can be installed with a simple command](https://github.com/fail2ban/fail2ban/wiki/How-to-install-fail2ban-packages).

If your distribution is not listed, you can install from GitHub:

Required:
- [Python >= 3.5](https://www.python.org) or [PyPy3](https://pypy.org)
- python-setuptools (or python3-setuptools) for installation from source

Optional:
- [pyinotify >= 0.8.3](https://github.com/seb-m/pyinotify), may require:
  * Linux >= 2.6.13
- [systemd >= 204](http://www.freedesktop.org/wiki/Software/systemd) and python bindings:
  * [python-systemd package](https://www.freedesktop.org/software/systemd/python-systemd/index.html)
- [dnspython](http://www.dnspython.org/)
- [pyasyncore](https://pypi.org/project/pyasyncore/) and [pyasynchat](https://pypi.org/project/pyasynchat/) (normally bundled-in within fail2ban, for python 3.12+ only)


To install:

    tar xvfj fail2ban-master.tar.bz2
    cd fail2ban-master
    sudo python setup.py install
   
Alternatively, you can clone the source from GitHub to a directory of your choice, and do the install from there. Pick the correct branch, for example, master or 0.11

    git clone https://github.com/fail2ban/fail2ban.git
    cd fail2ban
    sudo python setup.py install 
    
This will install Fail2Ban into the python library directory. The executable
scripts are placed into `/usr/bin`, and configuration in `/etc/fail2ban`.

Fail2Ban should be correctly installed now. Just type:

    fail2ban-client -h

to see if everything is alright. You should always use fail2ban-client and
never call fail2ban-server directly.
You can verify that you have the correct version installed with 

    fail2ban-client version

Please note that the system init/service script is not automatically installed.
To enable fail2ban as an automatic service, simply copy the script for your
distro from the `files` directory to `/etc/init.d`. Example (on a Debian-based
system):

    cp files/debian-initd /etc/init.d/fail2ban
    update-rc.d fail2ban defaults
    service fail2ban start

## configuration

You can configure Fail2Ban using the files in `/etc/fail2ban`. It is possible to
configure the server using commands sent to it by `fail2ban-client`. The
available commands are described in the fail2ban-client(1) manpage.  Also see
fail2ban(1) and jail.conf(5)  manpages for further references.

Code status:
------------

* [![CI](https://github.com/fail2ban/fail2ban/actions/workflows/main.yml/badge.svg)](https://github.com/fail2ban/fail2ban/actions/workflows/main.yml)

Contact:
--------

## features

See [CONTRIBUTING.md](https://github.com/fail2ban/fail2ban/blob/master/CONTRIBUTING.md)

### You just appreciate this program:
Send kudos to the original author ([Cyril Jaquier](mailto:cyril.jaquier@fail2ban.org))
or *better* to the [mailing list](https://lists.sourceforge.net/lists/listinfo/fail2ban-users)
since Fail2Ban is "community-driven" for years now.

Thanks:
-------

See [THANKS](https://github.com/fail2ban/fail2ban/blob/master/THANKS) file.

License:
--------

Fail2Ban is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

Fail2Ban is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
Fail2Ban; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA 02110, USA
