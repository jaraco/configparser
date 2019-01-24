"""
Sync files from upstream release.
"""

__requires__ = ['autocommand', 'requests_toolbelt']


import autocommand
from requests_toolbelt import sessions


github = sessions.BaseUrlSession(
    'https://raw.githubusercontent.com/python/cpython/')

file_map = {
    'Lib/configparser.py': 'src/backports/configparser/__init__.py',
    'Lib/test/test_configparser.py': 'src/test_configparser.py',
    'Doc/library/configparser.rst': 'configparser.rst',
}


@autocommand.autocommand(__name__)
def run(version):
    for src, dst in file_map.items():
        resp = github.get(f'v{version}/{src}')
        resp.raise_for_status()
        with open(dst, 'wb') as out:
            out.write(resp.content)
