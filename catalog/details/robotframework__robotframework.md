# robotframework/robotframework

Generic automation framework for acceptance testing and RPA

## installation

If you already have Python_ with `pip <https://pip.pypa.io>`_ installed,
you can simply run::

    pip install robotframework

For more detailed installation instructions, including installing Python, see
`<INSTALL.rst>`__.

Robot Framework requires Python 3.8 or newer and runs also on `PyPy <http://pypy.org>`_.
The latest version that supports Python 3.6 and 3.7 is `Robot Framework 6.1.1`__.
If you need to use Python 2, `Jython <http://jython.org>`_ or
`IronPython <http://ironpython.net>`_, you can use `Robot Framework 4.1.3`__.

__ https://github.com/robotframework/robotframework/tree/v6.1.1#readme
__ https://github.com/robotframework/robotframework/tree/v4.1.3#readme

## tools

Tests (or tasks) are executed from the command line using the ``robot``
command or by executing the ``robot`` module directly like ``python -m robot`` .

The basic usage is giving a path to a test (or task) file or directory as an
argument with possible command line options before the path::

    robot tests.robot
    robot --variable BROWSER:Firefox --outputdir results path/to/tests/

Additionally, there is the ``rebot`` tool for combining results and otherwise
post-processing outputs::

    rebot --name Example output1.xml output2.xml

Run ``robot --help`` and ``rebot --help`` for more information about the command
line usage. For a complete reference manual see `Robot Framework User Guide`_.
