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

## features

See [CONTRIBUTING.md](https://github.com/fail2ban/fail2ban/blob/master/CONTRIBUTING.md)
