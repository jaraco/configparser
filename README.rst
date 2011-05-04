============
configparser
============

The ancient ``ConfigParser`` module available in the standard library 2.x has
seen a major update in Python 3.2. This is a backport of those changes so that
they can be used directly in Python 2.5 - 2.7.

To use ``configparser`` instead of ``ConfigParser``, simply replace::
  
  import ConfigParser

with::

  import configparser

For detailed documentation consult the vanilla version at
http://docs.python.org/py3k/library/configparser.html.

Versioning
----------

This backport is intended to keep 100% compatibility with the vanilla release in
Python 3.2+. To help maintaining a version you want and expect, a versioning
scheme is used where:

* the first three numbers indicate the version of Python 3.x from which the
  backport is done

* a backport release number is provided after the ``r`` letter

For example, ``3.2.0r1`` is the **first** release of ``configparser`` compatible
with the library found in Python **3.2.0**.

A single exception from the 100% compatibility principle is that bugs fixed
before releasing another minor Python 3.x.y version **will be included** in the
backport releases done in the mean time. This rule applies to bugs only.

Maintenance
-----------

This backport is maintained on BitBucket by Łukasz Langa, the current vanilla
``configparser`` maintainer for CPython:

* `configparser Mercurial repository <https://bitbucket.org/langacore/configparser>`_

* `configparser issue tracker <https://bitbucket.org/langacore/configparser/issues>`_ 

Change Log
----------

3.2.0r2
~~~~~~~

* a backport-specific change: for convenience and basic compatibility with the
  old ConfigParser, bytestrings are now accepted as section names, options and
  values.  Those strings are still converted to Unicode for internal storage so
  in any case when such conversion is not possible (using the 'ascii' codec),
  UnicodeDecodeError is raised.

3.2.0r1
~~~~~~~

* the first public release compatible with 3.2.0 + fixes for `#11324
  <http://bugs.python.org/issue11324>`_, `#11670
  <http://bugs.python.org/issue11670>`_ and `#11858
  <http://bugs.python.org/issue11858>`_.

Conversion Process
------------------

This section is technical and should bother you only if you are wondering how
this backport is produced. If the implementation details of this backport are
not important for you, feel free to ignore the following content.

``configparser`` is converted using `3to2 <http://pypi.python.org/pypi/3to2>`_.
Because a fully automatic conversion was not doable, I took the following
branching approach:

* the ``3.2`` branch holds unchanged files synchronized from the upstream
  CPython repository. The synchronization is currently done by manually copying
  the required files and stating from which CPython changeset they come from.

* the ``3.2-clean`` branch holds a version of the ``3.2`` code with some tweaks
  that make it independent from libraries and constructions unavailable on 2.x.
  Code on this branch still *must* work on Python 3.2. You can check this
  running the supplied unit tests.

* the ``default`` branch holds necessary changes which break unit tests on
  Python 3.2.  Additional files which are used by the backport are also stored
  here.

The process works like this:

1. I update the ``3.2`` branch with new versions of files. Commit.

2. I merge the new commit to ``3.2-clean``. Check unit tests. Commit.

3. If there are necessary changes that can be made in a 3.2 compatible manner,
   I do them now (still on ``3.2-clean``), check unit tests and commit. If I'm
   not yet aware of any, no problem.

4. I merge the changes from ``3.2-clean`` to ``default``. Commit.

5. If there are necessary changes that cannot be made in a 3.2 compatible
   manner, I do them now (on ``default``). Note that the changes should still be
   written using 3.x syntax. If I'm not yet aware of any required changes, no
   problem.

6. I run ``./convert.py`` which is a custom ``3to2`` runner for this project.

7. I run the unit tests with ``unittest2`` on Python 2.x. If the tests are OK,
   I can prepare a new release.  Otherwise, I revert the ``default`` branch to
   its previous state (``hg revert .``) and go back to Step 3.

**NOTE:** the ``default`` branch holds unconverted code. This is because keeping
the conversion step as the last (after any custom changes) helps managing the
history better. Plus, the merges are nicer and updates of the converter software
don't create nasty conflicts in the repository.

This process works quite well but if you have any tips on how to make it simpler
and faster, do enlighten me :)
