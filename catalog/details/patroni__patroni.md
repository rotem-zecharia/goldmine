# patroni/patroni

A template for PostgreSQL High Availability with Etcd, Consul, ZooKeeper, or Kubernetes

## requirements

Install the requirements on macOS with Homebrew:

::

    brew install postgresql etcd haproxy libyaml python

Psycopg choices
^^^^^^^^^^^^^^^

Patroni requires a PostgreSQL Python driver. Recent versions of `psycopg2 <http://initd.org/psycopg/articles/2019/04/04/psycopg-28-released/>`__
no longer install a binary package by default, which means building from source may require a C compiler and development libraries.

Options:

1. Install using the package manager from your Linux distribution:

::

    sudo apt-get install python3-psycopg2
    sudo yum install python3-psycopg2

2. Install one of the supported Python packages with pip:

- `psycopg`
- `psycopg2`
- `psycopg2-binary`

Installing with pip
^^^^^^^^^^^^^^^^^^

Install Patroni with optional dependency groups:

::

    pip install patroni[dependencies]

Available dependency extras:

- ``etcd`` or ``etcd3``: `python-etcd` for Etcd as DCS
- ``consul``: `py-consul` for Consul as DCS
- ``zookeeper``: `kazoo` for ZooKeeper as DCS
- ``exhibitor``: `kazoo` for Exhibitor as DCS
- ``kubernetes``: `kubernetes` for Kubernetes as DCS
- ``raft``: `pysyncobj` for the python Raft DCS
- ``aws``: `boto3` for AWS callbacks
- ``systemd``: `systemd-python` for sd_notify integration
- ``all``: all of the above (except psycopg family)
- ``psycopg3``: `psycopg[binary]>=3.0.0`
- ``psycopg2``: `psycopg2>=2.5.4`
- ``psycopg2-binary``: `psycopg2-binary`

For example:

::

    pip install patroni[psycopg3,etcd3,aws]

Note: external tools used by bootstrap or replica creation scripts (for example WAL-G) must be installed separately.

## configuration

A minimal cluster can be started from different terminals:

::

    > etcd --data-dir=data/etcd --enable-v2=true
    > ./patroni.py postgres0.yml
    > ./patroni.py postgres1.yml

Then verify cluster behavior and experiment with the YAML configuration files.

Add more ``postgres*.yml`` files to scale the cluster.

Memory issue on Python 3.11+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you run Patroni on a system with strict memory limits, for example with ``vm.overcommit_memory=2`` (recommended for PostgreSQL), and use Python 3.11 or newer, you may observe unexpected behavior:

- Patroni appears healthy
- PostgreSQL continues to run
- Patroni **REST API becomes unresponsive**
- the operating system reports that Patroni is listening on the REST API port
- Patroni logs look normal; however, following messages may appear once: ``Exception ignored in thread started by: <object repr() failed>``, ``MemoryError``
- kernel logs may contain messages such as   ``not enough memory for the allocation``

This is caused by a `Python 3.11+ issue <https://github.com/python/cpython/issues/140746>`__.
Under strict memory conditions, starting a new thread may hang indefinitely when there is not enough free memory.

Recommended solution
""""""""""""""""""""

Recent Patroni releases (4.1.1+, 4.0.8+) reduce the impact of this issue by starting all required threads early in startup before memory pressure builds.

Additional recommendations (Linux, glibc)
"""""""""""""""""""""""""""""""""""""""""

When running with ``vm.overcommit_memory=2`` (recommended for PostgreSQL), we also recommend starting Patroni with the following environment variables configured:

- ``MALLOC_ARENA_MAX=1`` - reduces the amount of virtual memory allocated by glibc for multi-threaded
  applications
- ``PG_MALLOC_ARENA_MAX=`` - resets the value of ``MALLOC_ARENA_MAX`` for PostgreSQL processes started by Patroni.

In addition, you may tune the following Patroni configuration parameters:

- ``thread_stack_size`` - stack size used for threads started by Patroni. Lowering this value reduces memory usage of the Patroni process. The default value set by Patroni is ``512kB``. Increase ``thread_stack_size`` if Patroni experience stack-related crashes; otherwise the default value is sufficient.
- ``thread_pool_size`` - size of the thread pool used by Patroni for asynchronous tasks and REST API communication with other members during leader race or failsafe checks. The default value is ``5``, which is sufficient for three-node clusters.
- ``restapi.thread_pool_size`` - size of the thread pool used to process REST API requests. The default value is ``5``, allowing up to five parallel REST API requests. Note that requests involving SQL queries are effectively serialized because a single database connection is used, so increasing this value typically provides no benefit.

HAProxy support
^^^^^^^^^^^^^^^

Patroni includes an `HAProxy <http://www.haproxy.org/>`__ configuration for a single application endpoint.
Start it with:

::

    > haproxy -f haproxy.cfg

Then connect with:

::

    > psql --host 127.0.0.1 --port 5000 postgres

Configuration References
------------------------

YAML configuration
^^^^^^^^^^^^^^^^^^

For complete YAML options, see
`docs/dynamic_configuration.rst <https://github.com/patroni/patroni/blob/master/docs/dynamic_configuration.rst>`__
and the example file `postgres0.yml <https://github.com/patroni/patroni/blob/master/postgres0.yml>`__.

Environment configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

For environment variable configuration, see
`docs/ENVIRONMENT.rst <https://github.com/patroni/patroni/blob/master/docs/ENVIRONMENT.rst>`__.

Replication choices
^^^^^^^^^^^^^^^^^^^

Patroni uses PostgreSQL streaming replication. It supports:

- asynchronous replication with ``maximum_lag_on_failover``
- synchronous replication for stronger durability guarantees

See the `replication modes documentation <https://github.com/patroni/patroni/blob/master/docs/replication_modes.rst>`__ for det
