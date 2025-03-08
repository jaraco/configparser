import contextlib
import pathlib
import sys
import types

import test.support  # type: ignore[import-untyped, unused-ignore, import-not-found]


def check__all__(*args, **kwargs):
    if sys.version_info < (3, 10):  # pragma: no cover
        with contextlib.suppress(KeyError):
            kwargs.update(blacklist=kwargs.pop('not_exported'))
    return test.support.check__all__(*args, **kwargs)


support = types.SimpleNamespace(**dict(vars(test.support), check__all__=check__all__))


try:
    from test.support import os_helper
except ImportError:  # pragma: no cover
    # Python 3.9
    import test.support as os_helper  # noqa: F401


def find_file(filename, subdir=None):
    """
    Replacement for support.findfile to find the files locally.
    """
    return str(pathlib.Path('tests') / filename)


support.findfile = find_file
