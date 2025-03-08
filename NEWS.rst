v7.2.0
======

Features
--------

- Refreshed with implementation from CPython main (3.14).


v7.1.0
======

Features
--------

- Refreshed with implementation from CPython main (3.14).


v7.0.1
======

Bugfixes
--------

- Refreshed with implementation from CPython 3.13.0rc1.


v7.0.0
======

Deprecations and Removals
-------------------------

- Refreshed with implementation from CPython 3.13.0a6.
- Remove 'configparser' as a top-level name, as it's already masked by the stdlib on all supported Pythons.


v6.0.1
======

Bugfixes
--------

- Fixed failing tests introduced by upstream test suite changes. (#70)


v6.0.0
======

Features
--------

- Require Python 3.8 or later.


Deprecations and Removals
-------------------------

- Synced with CPython 3.12.0b2. Removes ``SafeConfigParser`` and ``filename`` parameter.


v5.3.0
======

* Synced with Python 3.11.0rc1.
* Packaging refresh.
* Requires Python 3.7 or later.

v5.2.0
======

* Project now uses PEP 420 (native) namespace package for
  ``backports`` package.

v5.1.0
======

* Synced with Python 3.10.0.
* Packaging refresh.
* Tests now run on Python 3.10.
* Modernized code relying on Python 3.6.

v5.0.2
======

* Packaging refresh.

v5.0.1
======

* Synced with Python 3.9.0.
* Refreshed package metadata.

v5.0.0
======

* Require Python 3.6 or later. For Python 2.6-3.5, use
  ``configparser < 5`` (selection should be automatic
  when installed using pip 9 from PyPI). The ``4.x`` line
  remains supported for bug fixes but will no longer
  be updated for future releases.

v4.0.2
======

* Re-release after pulling 4.0.0 and 4.0.1 due to #45.

v4.0.1
======

* Cleaned up broken badges and release notes publishing.

v4.0.0
======

* Switched to
  `semver <https://semver.org/spec/v2.0.0.html>`_
  for versioning this backport.

* Project now uses ``setuptools_scm`` for tagging releases.

3.8.1
=====

* Synced with `Python 3.8.0b3
  <https://docs.python.org/3.8/whatsnew/changelog.html#python-3-8-0-beta-3>`_.

3.7.5
=====

* Synced project with Python 3.7.4 (no meaningful changes).

3.7.4
=====

* Project is now officially supported through
  `Tidelift <https://tidelift.com/subscription/pkg/pypi-configparser?utm_source=pypi-configparser&utm_medium=readme>`_.

3.7.3
=====

* Issue #34: Temporarily degrade to use ASCII for author's name.

3.7.2
=====

(also released as 3.8.0)

* Repackaged using setuptools_scm for file discovery and other features
  from `skeleton <https://pypi.org/project/skeleton>`_. Fixes #33.

* Package now unconditionally installs the  ``configparser`` module.
  Doing so allowed for the project to release a universal wheel for
  Python 2 and Python 3. Even though the ``configparser`` module is
  installed unconditionally on Python 3, it's expected that it will be
  masked in that environment by the module in stdlib, so the same
  interface applies. Ref #31.

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

* Project now uses declarative config for package metadata, meaning it
  requires install from wheel or build using Setuptools 30.4 or later.

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

* fixes #1: versioning non-compliant with PEP 386

* fixes #3: ``reload(sys); sys.setdefaultencoding('utf8')`` in setup.py

* fixes #5: Installing the backport on Python 3 breaks virtualenv

* fixes #6: PyPy compatibility

3.5.0b2
=======

* second beta of 3.5.0, not using any third-party futurization libraries

3.5.0b1
=======

* first beta of 3.5.0, using python-future

* for the full feature list, see `3.5.0`_

3.3.0r2
=======

* updated the fix for Python #16820: parsers
  now preserve section order when using ``__setitem__`` and ``update``

3.3.0r1
=======

* compatible with 3.3.0 + fixes for Python #15803
  and Python #16820

* fixes #4: ``read()`` properly
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

* the first public release compatible with 3.2.0 + fixes for
  Python #11324, Python #11670, and Python #11858.
