3.7.1
=====

* Issue #30: Fixed issue on Python 2.x when future is present.

3.7.0
=====

* Merge functionality from Python 3.7.2. Now ConfigParser accepts bytes
  paths as well as any
  `PathLike <https://docs.python.org/3/library/os.html#os.PathLike>`_
  object, including those found in the `pathlib2 backport
  <https://pypi.org/project/pathlib2/>`.

3.5.3
=====

* Issue #27: Reverted the limit on DeprecationWarning, as it had unintended
  consequences.

3.5.2
=====

* Issue #23: Use environment markers to indicate the 'ordereddict' dependency
  for Python 2.6.

* Issue #24: Limit DeprecationWarning when a filename is indicated as a
  bytestring on Python 2. Now the warning is only emitted when py3kwarning
  is indicated.

3.5.1
=====

* jaraco adopts the package.

* Moved hosting to GitHub.

* Issue #21: Updated ``backports`` namespace package to conform with other
  packages sharing the namespace.

3.5.0
=====

* a complete rewrite of the backport; now single codebase working on Python
  2.6 - 3.5. To use on Python 3 import ``from backports import configparser``
  instead of the built-in version.

* compatible with 3.5.1

* fixes `BitBucket issue #1
  <https://bitbucket.org/ambv/configparser/issue/1>`_: versioning non-compliant
  with PEP 386

* fixes `BitBucket issue #3
  <https://bitbucket.org/ambv/configparser/issue/3>`_: ``reload(sys);
  sys.setdefaultencoding('utf8')`` in setup.py

* fixes `BitBucket issue #5
  <https://bitbucket.org/ambv/configparser/issue/5>`_: Installing the backport
  on Python 3 breaks virtualenv

* fixes `BitBucket issue #6
  <https://bitbucket.org/ambv/configparser/issue/6>`_: PyPy compatibility

3.5.0b2
=======

* second beta of 3.5.0, not using any third-party futurization libraries

3.5.0b1
=======

* first beta of 3.5.0, using python-future

* for the full feature list, see `3.5.0`_

3.3.0r2
=======

* updated the fix for `#16820 <http://bugs.python.org/issue16820>`_: parsers
  now preserve section order when using ``__setitem__`` and ``update``

3.3.0r1
=======

* compatible with 3.3.0 + fixes for `#15803
  <http://bugs.python.org/issue15803>`_ and `#16820
  <http://bugs.python.org/issue16820>`_

* fixes `BitBucket issue #4
  <https://bitbucket.org/ambv/configparser/issue/4>`_: ``read()`` properly
  treats a bytestring argument as a filename

* `ordereddict <http://pypi.python.org/pypi/ordereddict>`_ dependency required
  only for Python 2.6

* `unittest2 <http://pypi.python.org/pypi/unittest2>`_ explicit dependency
  dropped. If you want to test the release, add ``unittest2`` on your own.

3.2.0r3
=======

* proper Python 2.6 support

  * explicitly stated the dependency on `ordereddict
    <http://pypi.python.org/pypi/ordereddict>`_

  * numbered all formatting braces in strings

* explicitly says that Python 2.5 support won't happen (too much work necessary
  without abstract base classes, string formatters, the ``io`` library, etc.)

* some healthy advertising in the README

3.2.0r2
=======

* a backport-specific change: for convenience and basic compatibility with the
  old ConfigParser, bytestrings are now accepted as section names, options and
  values.  Those strings are still converted to Unicode for internal storage so
  in any case when such conversion is not possible (using the 'ascii' codec),
  UnicodeDecodeError is raised.

3.2.0r1
=======

* the first public release compatible with 3.2.0 + fixes for `#11324
  <http://bugs.python.org/issue11324>`_, `#11670
  <http://bugs.python.org/issue11670>`_ and `#11858
  <http://bugs.python.org/issue11858>`_.
