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

3.2.0r1
~~~~~~~

* the first public release compatible with 3.2.0 + fixes for `#11324
  <http://bugs.python.org/issue11324>`_, `#11670
  <http://bugs.python.org/issue11670>`_ and `#11858
  <http://bugs.python.org/issue11858>`_.
