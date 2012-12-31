#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This library brings the updated configparser from Python 3.2+ to Python 2.6-2.7."""

from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

import os
import sys
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf8')

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as ld_file:
    long_description = ld_file.read()

requirements = []
if sys.version_info[:2] < (2, 7):
    requirements.append('ordereddict')

setup (
    name = 'configparser',
    version = '3.3.0r1',
    author = u'Łukasz Langa',
    author_email = 'lukasz@langa.pl',
    description = __doc__,
    long_description = long_description,
    url = 'http://docs.python.org/py3k/library/configparser.html',
    keywords = 'configparser ini parsing conf cfg configuration file',
    platforms = ['any'],
    license = 'MIT',
    py_modules = ('configparser', 'configparser_helpers'),
    zip_safe = True,
    install_requires = requirements,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
