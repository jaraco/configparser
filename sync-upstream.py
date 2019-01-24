"""
Sync files from upstream release.
"""

__requires__ = ['autocommand', 'requests_toolbelt', 'packaging']


import subprocess

import autocommand
from packaging.version import Version
from requests_toolbelt import sessions


gh_content = sessions.BaseUrlSession(
    'https://raw.githubusercontent.com/python/cpython/')
gh_api = sessions.BaseUrlSession(
    'https://api.github.com/repos/python/cpython/')

file_map = {
    'Lib/configparser.py': 'src/backports/configparser/__init__.py',
    'Lib/test/test_configparser.py': 'src/test_configparser.py',
    'Doc/library/configparser.rst': 'configparser.rst',
}


def by_tag(tag):
    return Version(tag['name'])


def is_stable(tag):
    return not by_tag(tag).is_prerelease


@autocommand.autocommand(__name__)
def run():
    tags = gh_api.get('tags').json()
    tag = max(filter(is_stable, tags), key=by_tag)
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
