import pathlib
import types
import unittest

import test.support  # type: ignore[import-untyped, unused-ignore, import-not-found]
from test.support import os_helper  # noqa: F401

support = types.SimpleNamespace(**vars(test.support))


def find_file(filename, subdir=None):
    """
    Replacement for support.findfile to find the files locally.
    """
    return str(pathlib.Path('tests') / filename)


support.findfile = find_file


def assert_starts_with(self, s, prefix, msg=None):  # pragma: no cover
    """
    Replacement for TestCase.assertStartsWith as found in Python 3.14.
    """
    if not s.startswith(prefix):
        self.fail(msg or f'{s!r} does not start with {prefix!r}')


if not hasattr(unittest.TestCase, 'assertStartsWith'):  # pragma: no cover
    unittest.TestCase.assertStartsWith = assert_starts_with
