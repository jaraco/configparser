"""
Sync files from upstream release.
"""

__requires__ = ['autocommand', 'requests_toolbelt']


import zipfile
import io

import autocommand
from requests_toolbelt import sessions


github = sessions.BaseUrlSession('https://github.com/python/cpython/')


file_map = {
    'Lib/configparser.py': 'src/backports/configparser/__init__.py',
    'Lib/test/test_configparser.py': 'src/test_configparser.py',
    'Doc/library/configparser.rst': 'configparser.rst',
}


@autocommand.autocommand(__name__)
def run(version):
    resp = github.get(f'archive/v{version}.zip')
    resp.raise_for_status()
    buf = io.BytesIO(resp.content)
    archive = zipfile.ZipFile(buf)
    prefix = archive.filelist[0].filename
    for src, dst in file_map.items():
        src_path = prefix + src
        with archive.open(src_path) as in_:
            with open(dst, 'wb') as out:
                out.write(in_.read())
