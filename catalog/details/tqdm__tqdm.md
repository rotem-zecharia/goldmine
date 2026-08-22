# tqdm/tqdm

:zap: A Fast, Extensible Progress Bar for Python and CLI

## installation

Latest PyPI stable release
~~~~~~~~~~~~~~~~~~~~~~~~~~

|Versions| |PyPI-Downloads| |Libraries-Dependents|

.. code:: sh

    pip install tqdm

Latest development release on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GitHub-Status| |GitHub-Stars| |GitHub-Commits| |GitHub-Forks| |GitHub-Updated|

Pull and install pre-release ``devel`` branch:

.. code:: sh

    pip install "git+https://github.com/tqdm/tqdm.git@devel#egg=tqdm"

Latest Conda release
~~~~~~~~~~~~~~~~~~~~

|Conda-Forge-Status|

.. code:: sh

    conda install -c conda-forge tqdm

Latest Snapcraft release
~~~~~~~~~~~~~~~~~~~~~~~~

|Snapcraft|

There are 3 channels to choose from:

.. code:: sh

    snap install tqdm  # implies --stable, i.e. latest tagged release
    snap install tqdm  --candidate  # master branch
    snap install tqdm  --edge  # devel branch

Note that ``snap`` binaries are purely for CLI use (not ``import``-able), and
automatically set up ``bash`` tab-completion.

Latest Docker release
~~~~~~~~~~~~~~~~~~~~~

|Docker|

.. code:: sh

    docker pull tqdm/tqdm
    docker run -i --rm tqdm/tqdm --help

Other
~~~~~

There are other (unofficial) places where ``tqdm`` may be downloaded, particularly for CLI use:

|Repology|

.. |Repology| image:: https://repology.org/badge/tiny-repos/python:tqdm.svg
   :target: https://repology.org/project/python:tqdm/versions

Changelog
---------

The list of all changes is available either on GitHub's Releases:
|GitHub-Status|, on the
`wiki <https://github.com/tqdm/tqdm/wiki/Releases>`__, or on the
`website <https://tqdm.github.io/releases>`__.

## tools

``tqdm`` is very versatile and can be used in a number of ways.
The three main ones are given below.

Iterable-based
~~~~~~~~~~~~~~

Wrap ``tqdm()`` around any iterable:

.. code:: python

    from tqdm import tqdm
    from time import sleep

    text = ""
    for char in tqdm(["a", "b", "c", "d"]):
        sleep(0.25)
        text = text + char

``trange(i)`` is a special optimised instance of ``tqdm(range(i))``:

.. code:: python

    from tqdm import trange

    for i in trange(100):
        sleep(0.01)

Instantiation outside of the loop allows for manual control over ``tqdm()``:

.. code:: python

    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        sleep(0.25)
        pbar.set_description("Processing %s" % char)

Manual
~~~~~~

Manual control of ``tqdm()`` updates using a ``with`` statement:

.. code:: python

    with tqdm(total=100) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update(10)

If the optional variable ``total`` (or an iterable with ``len()``) is
provided, predictive stats are displayed.

``with`` is also optional (you can just assign ``tqdm()`` to a variable,
but in this case don't forget to ``del`` or ``close()`` at the end:

.. code:: python

    pbar = tqdm(total=100)
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
    pbar.close()

Module
~~~~~~

Perhaps the most wonderful use of ``tqdm`` is in a script or on the command
line. Simply inserting ``tqdm`` (or ``python -m tqdm``) between pipes will pass
through all ``stdin`` to ``stdout`` while printing progress to ``stderr``.

The example below demonstrate counting the number of lines in all Python files
in the current directory, with timing information included.

.. code:: sh

    $ time find . -name '*.py' -type f -exec cat \{} \; | wc -l
    857365

    real    0m3.458s
    user    0m0.274s
    sys     0m3.325s

    $ time find . -name '*.py' -type f -exec cat \{} \; | tqdm | wc -l
    857366it [00:03, 246471.31it/s]
    857365

    real    0m3.585s
    user    0m0.862s
    sys     0m3.358s

Note that the usual arguments for ``tqdm`` can also be specified.

.. code:: sh

    $ find . -name '*.py' -type f -exec cat \{} \; |
        tqdm --unit loc --unit_scale --total 857366 >> /dev/null
    100%|█████████████████████████████████| 857K/857K [00:04<00:00, 246Kloc/s]

Backing up a large directory?

.. code:: sh

    $ tar -zcf - docs/ | tqdm --bytes --total `du -sb docs/ | cut -f1` \
      > backup.tgz
     44%|██████████████▊                   | 153M/352M [00:14<00:18, 11.0MB/s]

This can be beautified further:

.. code:: sh

    $ BYTES=$(du -sb docs/ | cut -f1)
    $ tar -cf - docs/ \
      | tqdm --bytes --total "$BYTES" --desc Processing | gzip \
      | tqdm --bytes --total "$BYTES" --desc Compressed --position 1 \
      > ~/backup.tgz
    Processing: 100%|██████████████████████| 352M/352M [00:14<00:00, 30.2MB/s]
    Compressed:  42%|█████████▎            | 148M/352M [00:14<00:19, 10.9MB/s]

Or done on a file level using 7-zip:

.. code:: sh

    $ 7z a -bd -r backup.7z docs/ | grep Compressing \
      | tqdm --total $(find docs/ -type f | wc -l) --unit files \
      | grep -v Compressing
    100%|██████████████████████████▉| 15327/15327 [01:00<00:00, 712.96files/s]

Pre-existing CLI programs already outputting basic progress information will
benefit from ``tqdm``'s ``--update`` and ``--update_to`` flags:

.. code:: sh

    $ seq 3 0.1 5 | tqdm --total 5 --update_to --null
    100%|████████████████████████████████████| 5.0/5 [00:00<00:00, 9673.21it/s]
    $ seq 10 | tqdm --update --null  # 1 + 2 + ... + 10 = 55 iterations
    55it [00:00, 90006.52it/s]

## limitations

|GitHub-Issues|

The most common issues relate to excessive output on multiple lines, instead
of a neat one-line progress bar.

- Consoles in general: require support for carriage return (``CR``, ``\r``).

  * Some cloud logging consoles which don't support ``\r`` properly
    (`cloudwatch <https://github.com/tqdm/tqdm/issues/966>`__,
    `K8s <https://github.com/tqdm/tqdm/issues/1319>`__) may benefit from
    ``export TQDM_POSITION=-1``.

- Nested progress bars:

  * Consoles in general: require support for moving cursors up to the
    previous line. For example,
    `IDLE <https://github.com/tqdm/tqdm/issues/191#issuecomment-230168030>`__,
    `ConEmu <https://github.com/tqdm/tqdm/issues/254>`__ and
    `PyCharm <https://github.com/tqdm/tqdm/issues/203>`__ (also
    `here <https://github.com/tqdm/tqdm/issues/208>`__,
    `here <https://github.com/tqdm/tqdm/issues/307>`__, and
    `here <https://github.com/tqdm/tqdm/issues/454#issuecomment-335416815>`__)
    lack full support.
  * Windows: additionally may require the Python module ``colorama``
    to ensure nested bars stay within their respective lines.

- Unicode:

  * Environments which report that they support unicode will have solid smooth
    progress bars. The fallback is an ``ascii``-only bar.
  * Windows consoles often only partially support unicode and thus
    `often require explicit ascii=True <https://github.com/tqdm/tqdm/issues/454#issuecomment-335416815>`__
    (also `here <https://github.com/tqdm/tqdm/issues/499>`__). This is due to
    either normal-width unicode characters being incorrectly displayed as
    "wide", or some unicode characters not rendering.

- Wrapping generators:

  * Generator wrapper functions tend to hide the length of iterables.
    ``tqdm`` does not.
  * Replace ``tqdm(enumerate(...))`` with ``enumerate(tqdm(...))`` or
    ``tqdm(enumerate(x), total=len(x), ...)``.
    The same applies to ``numpy.ndenumerate``.
  * Replace ``tqdm(zip(a, b))`` with ``zip(tqdm(a), b)`` or even
    ``zip(tqdm(a), tqdm(b))``.
  * The same applies to ``itertools``.
  * Some useful convenience functions can be found under ``tqdm.contrib``.

- `No intermediate output in docker-compose <https://github.com/tqdm/tqdm/issues/771>`__:
  use ``docker-compose run`` instead of ``docker-compose up`` and ``tty: true``.

- Overriding defaults via environment variables:
  e.g. in CI/cloud jobs, ``export TQDM_MININTERVAL=5`` to avoid log spam.
  This override logic is handled by the ``tqdm.utils.envwrap`` decorator
  (useful independent of ``tqdm``).

If you come across any other difficulties, browse and file |GitHub-Issues|.

Documentation
-------------

|Py-Versions| |README-Hits| (Since 19 May 2016)

.. code:: python

    class tqdm():
      """
      Decorate an iterable object, returning an iterator which acts exactly
      like the original iterable, but prints a dynamically updating
      progress bar every time a value is requested.
      """

      @envwrap("tqdm")  # override defaults via env vars
      def __init__(self, iterable=None, desc=None, total=None, leave=True,
                   file=None, ncols=None, mininterval=0.1,
                   maxinterval=10.0, miniters=None, ascii=None, disable=False,
                   unit='it', unit_scale=False, dynamic_ncols=False,
                   smoothing=0.3, bar_format=None, initial=0, position=None,
                   postfix=None, unit_divisor=1000, write_bytes=False,
                   lock_args=None, nrows=None, colour=None, delay=0):

Parameters
~~~~~~~~~~

* iterable  : iterable, optional  
    Iterable to decorate with a progress bar.
    Leave blank to manually manage the updates.
* desc  : str, optional  
    Prefix for the progress bar.
* total  : int or float, optional  
    The number of expected iterations. If unspecified,
    len(iterable) is used if possible. If float("inf") or as a last
    resort, only basic progress statistics are displayed
    (no ETA, no progress bar).
    If ``gui`` is True a

## configuration

* delim  : chr, optional  
    Delimiting character [default: '\n']. Use '\0' for null.
    N.B.: on Windows systems, Python converts '\n' to '\r\n'.
* buf_size  : int, optional  
    String buffer size in bytes [default: 256]
    used when ``delim`` is specified.
* bytes  : bool, optional  
    If true, will count bytes, ignore ``delim``, and default
    ``unit_scale`` to True, ``unit_divisor`` to 1024, and ``unit`` to 'B'.
* tee  : bool, optional  
    If true, passes ``stdin`` to both ``stderr`` and ``stdout``.
* update  : bool, optional  
    If true, will treat input as newly elapsed iterations,
    i.e. numbers to pass to ``update()``. Note that this is slow
    (~2e5 it/s) since every input must be decoded as a number.
* update_to  : bool, optional  
    If true, will treat input as total elapsed iterations,
    i.e. numbers to assign to ``self.n``. Note that this is slow
    (~2e5 it/s) since every input must be decoded as a number.
* null  : bool, optional  
    If true, will discard input (no stdout).
* manpath  : str, optional  
    Directory in which to install tqdm man pages.
* comppath  : str, optional  
    Directory in which to place tqdm completion.
* log  : str, optional  
    CRITICAL|FATAL|ERROR|WARN(ING)|[default: 'INFO']|DEBUG|NOTSET.

Returns
~~~~~~~

* out  : decorated iterator.  

.. code:: python

    class tqdm():
      def update(self, n=1):
          """
          Manually update the progress bar, useful for streams
          such as reading files.
          E.g.:
          >>> t = tqdm(total=filesize) # Initialise
          >>> for current_buffer in stream:
          ...    ...
          ...    t.update(len(current_buffer))
          >>> t.close()
          The last line is highly recommended, but possibly not necessary if
          `t.update()` will be called in such a way that `filesize` will be
          exactly reached and printed.

          Parameters
          ----------
          n  : int or float, optional
              Increment to add to the internal counter of iterations
              [default: 1]. If using float, consider specifying `{n:.3f}`
              or similar in `bar_format`, or specifying `unit_scale`.

          Returns
          -------
          out  : bool or None
              True if a `display()` was triggered.
          """

      def close(self):
          """Cleanup and (if leave=False) close the progress bar."""

      def clear(self, nomove=False):
          """Clear current bar display."""

      def refresh(self):
          """
          Force refresh the display of this bar.

          Parameters
          ----------
          nolock  : bool, optional
              If `True`, does not lock.
              If [default: `False`]: calls `acquire()` on internal lock.
          lock_args  : tuple, optional
              Passed to internal lock's `acquire()`.
              If specified, will only `display()` if `acquire()` returns `True`.
          """

      def unpause(self):
          """Restart tqdm timer from last print time."""

      def reset(self, total=None):
          """
          Resets to 0 iterations for repeated use.

          Consider combining with `leave=True`.

          Parameters
          ----------
          total  : int or float, optional. Total to use for the new bar.
          """

      def set_description(self, desc=None, refresh=True):
          """
          Set/modify description of the progress bar.

          Parameters
          ----------
          desc  : str, optional
          refresh  : bool, optional
              Forces refresh [default: True].
          """

      def set_postfix(self, ordered_dict=None, refresh=True, **tqdm_kwargs):
          """
          Set/modify postfix (additional stats)
          with automatic formatting based on datatype.

          Parameters
          ----------
          ordered_dict  : dict or OrderedDict, optional
          refresh  : bool, optional
              Forces refresh [default: True]
