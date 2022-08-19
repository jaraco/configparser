"""
Sync files from upstream release.
"""

__requires__ = ['autocommand', 'requests_toolbelt', 'packaging']


import subprocess

import autocommand
import packaging.version
from requests_toolbelt import sessions


gh_content = sessions.BaseUrlSession(
    'https://raw.githubusercontent.com/python/cpython/')
gh_api = sessions.BaseUrlSession(
    'https://api.github.com/repos/python/cpython/')

file_map = {
    'Lib/configparser.py': 'src/backports/configparser/__init__.py',
    'Lib/test/test_configparser.py': 'src/test_configparser.py',
    'Lib/test/cfgparser.1': 'src/cfgparser.1',
    'Lib/test/cfgparser.2': 'src/cfgparser.2',
    'Lib/test/cfgparser.3': 'src/cfgparser.3',
    'Doc/library/configparser.rst': 'configparser.rst',
}


class Version(packaging.version.Version):
    @property
    def is_stable(self):
        """
        Include release candidates in stable.
        """
        return not self.is_prerelease or self.is_rc

    @property
    def is_rc(self):
        return self.pre[1:] == ['rc']


def by_tag(tag):
    return Version(tag['name'])


def is_stable(tag):
    return not by_tag(tag).is_stable


@autocommand.autocommand(__name__)
def run(pre=False):
    tags = gh_api.get('tags').json()
    filtered = tags if pre else filter(is_stable, tags)
    tag = max(filtered, key=by_tag)
    version = tag['name']
    for src, dst in file_map.items():
        resp = gh_content.get(f'{version}/{src}')
        resp.raise_for_status()
        with open(dst, 'wb') as out:
            out.write(resp.content)
    cmd = [
        'git', 'commit',
        '-a',
        '-m', f'cpython-{version} rev={tag["commit"]["sha"][:12]}',
    ]
    subprocess.run(cmd)
