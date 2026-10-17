import pathlib
import types

import test.support  # type: ignore[import-untyped, unused-ignore, import-not-found]
from test.support import os_helper  # noqa: F401

support = types.SimpleNamespace(**vars(test.support))


def find_file(filename, subdir=None):
    """
    Replacement for support.findfile to find the files locally.
    """
    return str(pathlib.Path('tests') / filename)


support.findfile = find_file
