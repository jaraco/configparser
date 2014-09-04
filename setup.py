#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This library brings the updated configparser from Python 3.5 to Python 2.6-3.5."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
import os
import sys
from setuptools import setup, find_packages

readme_filename = os.path.join(os.path.dirname(__file__), 'README.rst')
with codecs.open(readme_filename, encoding='utf8') as ld_file:
    long_description = ld_file.read()

author = 'Łukasz Langa'
modules = []
requirements = ['future>=0.13.0']
if sys.version_info[:2] < (2, 7):
    requirements.append('ordereddict')
    author = 'Lukasz Langa'
if sys.version_info[0] == 2:
    # enable `import configparser` for Python 2
    modules.append('configparser')

setup(
    name='configparser',
    version='3.5.0',
    author=author,
    author_email='lukasz@langa.pl',
    description=__doc__,
    long_description=long_description,
    url='http://docs.python.org/3/library/configparser.html',
    keywords='configparser ini parsing conf cfg configuration file',
    platforms=['any'],
    license='MIT',
    py_modules=modules,
    packages=find_packages('.'),
    namespace_packages=['backports'],
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
