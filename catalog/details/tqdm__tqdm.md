# tqdm/tqdm

:zap: A Fast, Extensible Progress Bar for Python and CLI

## tools

``tqdm`` is very versatile and can be used in a number of ways.
The three main ones are given below.

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
