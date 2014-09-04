============
configparser
============

The ancient ``ConfigParser`` module available in the standard library 2.x has
seen a major update in Python 3.2. This is a backport of those changes so that
they can be used directly in Python 2.6 - 3.5.

To use the ``configparser`` backport instead of the built-in version on both
Python 2 and Python 3, simply import it explicitly as a backport::

  from backports import configparser

If you'd like to use the backport on Python 2 and the built-in version on
Python 3, use that invocation instead::

  import configparser

For detailed documentation consult the vanilla version at
http://docs.python.org/3/library/configparser.html.

Why you'll love ``configparser``
--------------------------------

Whereas almost completely compatible with its older brother, ``configparser``
sports a bunch of interesting new features:

* full mapping protocol access (`more info
  <http://docs.python.org/3/library/configparser.html#mapping-protocol-access>`_)::

    >>> parser = ConfigParser()
    >>> parser.read_string("""
    [DEFAULT]
    location = upper left
    visible = yes
    editable = no
    color = blue

    [main]
    title = Main Menu
    color = green

    [options]
    title = Options
    """)
    >>> parser['main']['color']
    'green'
    >>> parser['main']['editable']
    'no'
    >>> section = parser['options']
    >>> section['title']
    'Options'
    >>> section['title'] = 'Options (editable: %(editable)s)'
    >>> section['title']
    'Options (editable: no)'

* there's now one default ``ConfigParser`` class, which basically is the old
  ``SafeConfigParser`` with a bunch of tweaks which make it more predictable for
  users. Don't need interpolation? Simply use
  ``ConfigParser(interpolation=None)``, no need to use a distinct
  ``RawConfigParser`` anymore.

* the parser is highly `customizable upon instantiation
  <http://docs.python.org/3/library/configparser.html#customizing-parser-behaviour>`__
  supporting things like changing option delimiters, comment characters, the
  name of the DEFAULT section, the interpolation syntax, etc.

* you can easily create your own interpolation syntax but there are two powerful
  implementations built-in (`more info
  <http://docs.python.org/3/library/configparser.html#interpolation-of-values>`__):

  * the classic ``%(string-like)s`` syntax (called ``BasicInterpolation``)

  * a new ``${buildout:like}`` syntax (called ``ExtendedInterpolation``)

* fallback values may be specified in getters (`more info
  <http://docs.python.org/3/library/configparser.html#fallback-values>`__)::

    >>> config.get('closet', 'monster',
    ...            fallback='No such things as monsters')
    'No such things as monsters'

* ``ConfigParser`` objects can now read data directly `from strings
  <http://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_string>`__
  and `from dictionaries
  <http://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict>`__.
  That means importing configuration from JSON or specifying default values for
  the whole configuration (multiple sections) is now a single line of code. Same
  goes for copying data from another ``ConfigParser`` instance, thanks to its
  mapping protocol support.

* many smaller tweaks, updates and fixes

A few words about Unicode
-------------------------

``configparser`` comes from Python 3 and as such it works well with Unicode.
The library is generally cleaned up in terms of internal data storage and
reading/writing files.  There are a couple of incompatibilities with the old
``ConfigParser`` due to that. However, the work required to migrate is well
worth it as it shows the issues that would likely come up during migration of
your project to Python 3.

The design assumes that Unicode strings are used whenever possible [1]_.  That
gives you the certainty that what's stored in a configuration object is text.
Once your configuration is read, the rest of your application doesn't have to
deal with encoding issues. All you have is text [2]_. The only two phases when
you should explicitly state encoding is when you either read from an external
source (e.g. a file) or write back.

Versioning
----------

This backport is intended to keep 100% compatibility with the vanilla release in
Python 3.2+. To help maintaining a version you want and expect, a versioning
scheme is used where:

* the first two numbers indicate the version of Python 3 from which the
  backport is done

* a backport release number is provided as the final number (zero-indexed)

For example, ``3.5.2`` is the **third** backport release of the
``configparser`` library as seen in Python 3.5.  Note that ``3.5.2`` does
**NOT** necessarily mean this backport version is based on the standard library
of Python 3.5.2.

One exception from the 100% compatibility principle is that bugs fixed before
releasing another minor Python 3 bugfix version **will be included** in the
backport releases done in the mean time.

Maintenance
-----------

This backport is maintained on BitBucket by Łukasz Langa, the current vanilla
``configparser`` maintainer for CPython:

* `configparser Mercurial repository <https://bitbucket.org/ambv/configparser>`_

* `configparser issue tracker <https://bitbucket.org/ambv/configparser/issues>`_

Change Log
----------

3.5.0
~~~~~

* a complete rewrite of the backport; now single codebase working on Python
  2.6 - 3.5. To use on Python 3 import ``from backports import configparser``
  instead of the built-in version.

* compatible with 3.4.1 + fixes for `#19546
  <http://bugs.python.org/issue19546>`_

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
3.3.0r2
~~~~~~~

* updated the fix for `#16820 <http://bugs.python.org/issue16820>`_: parsers
  now preserve section order when using ``__setitem__`` and ``update``

3.3.0r1
~~~~~~~

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
~~~~~~~

* proper Python 2.6 support

  * explicitly stated the dependency on `ordereddict
    <http://pypi.python.org/pypi/ordereddict>`_

  * numbered all formatting braces in strings

* explicitly says that Python 2.5 support won't happen (too much work necessary
  without abstract base classes, string formatters, the ``io`` library, etc.)

* some healthy advertising in the README

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

* the ``3.x`` branch holds unchanged files synchronized from the upstream
  CPython repository. The synchronization is currently done by manually copying
  the required files and stating from which CPython changeset they come from.

* the ``3.x-clean`` branch holds a version of the ``3.x`` code with some tweaks
  that make it independent from libraries and constructions unavailable on 2.x.
  Code on this branch still *must* work on the corresponding Python 3.x. You
  can check this running the supplied unit tests.

* the ``default`` branch holds necessary changes which break unit tests on
  Python 3.2.  Additional files which are used by the backport are also stored
  here.

The process works like this:

1. I update the ``3.x`` branch with new versions of files. Commit.

2. I merge the new commit to ``3.x-clean``. Check unit tests. Commit.

3. If there are necessary changes that can be made in a 3.x compatible manner,
   I do them now (still on ``3.x-clean``), check unit tests and commit. If I'm
   not yet aware of any, no problem.

4. I merge the changes from ``3.x-clean`` to ``default``. Commit.

5. If there are necessary changes that *cannot* be made in a 3.x compatible
   manner, I do them now (on ``default``). Note that the changes should still
   be written using 3.x syntax. If I'm not yet aware of any required changes,
   no problem.

6. I run ``./convert.py`` which is a custom ``3to2`` runner for this project.

7. I run the unit tests with ``unittest2`` on Python 2.x. If the tests are OK,
   I can prepare a new release.  Otherwise, I revert the ``default`` branch to
   its previous state (``hg revert .``) and go back to Step 3.

**NOTE:** the ``default`` branch holds unconverted code. This is because keeping
the conversion step as the last (after any custom changes) helps managing the
history better. Plus, the merges are nicer and updates of the converter software
don't create nasty conflicts in the repository.

This process works well but if you have any tips on how to make it simpler and
faster, do enlighten me :)

Footnotes
---------

.. [1] To somewhat ease migration, passing bytestrings is still supported but
       they are converted to Unicode for internal storage anyway. This means
       that for the vast majority of strings used in configuration files, it
       won't matter if you pass them as bytestrings or Unicode. However, if you
       pass a bytestring that cannot be converted to Unicode using the naive
       ASCII codec, a ``UnicodeDecodeError`` will be raised. This is purposeful
       and helps you manage proper encoding for all content you store in
       memory, read from various sources and write back.

.. [2] Life gets much easier when you understand that you basically manage
       **text** in your application.  You don't care about bytes but about
       letters.  In that regard the concept of content encoding is meaningless.
       The only time when you deal with raw bytes is when you write the data to
       a file.  Then you have to specify how your text should be encoded.  On
       the other end, to get meaningful text from a file, the application
       reading it has to know which encoding was used during its creation.  But
       once the bytes are read and properly decoded, all you have is text.  This
       is especially powerful when you start interacting with multiple data
       sources.  Even if each of them uses a different encoding, inside your
       application data is held in abstract text form.  You can program your
       business logic without worrying about which data came from which source.
       You can freely exchange the data you store between sources.  Only
       reading/writing files requires encoding your text to bytes.
