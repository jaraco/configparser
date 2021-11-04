import test.support
import contextlib
import sys


def check__all__(*args, **kwargs):
    if sys.version_info < (3, 10):
        with contextlib.suppress(KeyError):
            kwargs.update(blacklist=kwargs.pop('not_exported'))
    return test.support.check__all__(*args, **kwargs)


try:
    from test.support import os_helper
except ImportError:
    # Python 3.9
    import test.support as os_helper  # noqa: F401
