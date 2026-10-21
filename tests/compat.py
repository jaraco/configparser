import functools
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


def sub_tests(arg_names, arg_values, /, *, _do_cleanups=False):  # pragma: no cover
    """
    Replacement for support.subTests as found in Python 3.14.
    """
    single_param = isinstance(arg_names, str) and len(arg_names.split()) == 1
    if isinstance(arg_names, str):
        arg_names = arg_names.replace(',', ' ').split()
    arg_values = tuple(arg_values)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, /, *args, **kwargs):
            for values in arg_values:
                if single_param:
                    values = (values,)
                subtest_kwargs = dict(zip(arg_names, values))
                with self.subTest(**subtest_kwargs):
                    func(self, *args, **kwargs, **subtest_kwargs)
                if _do_cleanups:
                    self.doCleanups()

        return wrapper

    return decorator


if not hasattr(support, 'subTests'):  # pragma: no cover
    support.subTests = sub_tests
