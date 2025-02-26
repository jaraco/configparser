.. image:: https://img.shields.io/pypi/v/configparser.svg
   :target: https://pypi.org/project/configparser

.. image:: https://img.shields.io/pypi/pyversions/configparser.svg

.. image:: https://github.com/jaraco/configparser/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/configparser/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://readthedocs.org/projects/configparser/badge/?version=latest
   :target: https://configparser.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

.. image:: https://tidelift.com/badges/package/pypi/configparser
   :target: https://tidelift.com/subscription/pkg/pypi-configparser?utm_source=pypi-configparser&utm_medium=readme


This package is a backport of the refreshed and enhanced ConfigParser from
later Python versions. To use the backport instead of the built-in version,
simply import it explicitly as a backport::

  from backports import configparser

For detailed documentation consult the vanilla version at
http://docs.python.org/3/library/configparser.html.


Versioning
==========

This project uses `semver <https://semver.org/spec/v2.0.0.html>`_ to
communicate the impact of various releases while periodically syncing
with the upstream implementation in CPython.
The `history <https://configparser.readthedocs.io/en/latest/history.html>`_
serves as a reference indicating which versions incorporate
which upstream functionality.

Prior to the ``4.0.0`` release, `another scheme
<https://github.com/jaraco/configparser/blob/3.8.1/README.rst#versioning>`_
was used to associate the CPython and backports releases.

Maintenance
===========

This backport was originally authored by Łukasz Langa, the current vanilla
``configparser`` maintainer for CPython and is currently maintained by
Jason R. Coombs:

* `configparser repository <https://github.com/jaraco/configparser>`_

* `configparser issue tracker <https://github.com/jaraco/configparser/issues>`_

Conversion Process
==================

This section is technical and should bother you only if you are wondering how
this backport is produced. If the implementation details of this backport are
not important for you, feel free to ignore the following content.

The project takes the following branching approach:

* The ``cpython`` branch holds unchanged files synchronized from the upstream
  CPython repository. The synchronization is currently done by manually copying
  the required files and stating from which CPython changeset they come.

* The ``main`` branch holds a version of the ``cpython`` code with some tweaks
  that make it compatible with older Pythons. Code on this branch must work
  on all supported Python versions. Test with ``tox`` or in CI.

The process works like this:

1. In the ``cpython`` branch, run ``./sync-upstream``, which
   downloads the latest stable release of Python and copies the relevant
   files from there into their new locations and then commits those
   changes with a nice reference to the relevant upstream commit hash.

2. Merge the new commit to ``main``.

3. Check for new names in ``__all__`` and update imports in
   ``configparser/__init__.py`` accordingly. Run tests. Commit.

4. Make any compatibility changes on ``main``. Run tests. Commit.

5. Update the docs and release the new version.


For Enterprise
==============

Available as part of the Tidelift Subscription.

This project and the maintainers of thousands of other packages are working with Tidelift to deliver one enterprise subscription that covers all of the open source you use.

`Learn more <https://tidelift.com/subscription/pkg/pypi-configparser?utm_source=pypi-configparser&utm_medium=referral&utm_campaign=github>`_.
