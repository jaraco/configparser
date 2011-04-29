#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Łukasz Langa

"""Does the conversion."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from lib3to2.fixes import fix_imports
from lib3to2.main import main
import sys

fix_imports.MAPPING['configparser'] = 'configparser'

fixers = ('annotations', 'bitlength', 'bool', 'bytes', 'classdecorator',
    'collections', 'dctsetcomp', 'division', 'except', 'features',
    'fullargspec', 'funcattrs', 'getcwd', 'imports', 'imports2', 'input',
    'intern', 'kwargs', 'memoryview', 'metaclass', 'methodattrs',
    'newstyle', 'next', 'numliterals', 'open', 'print', 'printfunction',
    'raise', 'range', 'reduce', 'setliteral', 'str', 'super', 'throw',
    'unittest', 'unpacking', 'with')

args = []

for fixer in fixers:
    args.append('-f')
    args.append(fixer)

args.extend(['-wn', '--no-diffs', 'configparser.py', 'configparser_helpers.py',
    'test_cfgparser.py', 'test_helpers.py'])

sys.exit(main("lib3to2.fixes", args))
