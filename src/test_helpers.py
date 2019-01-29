#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backports.configparser.helpers import _ChainMap
import copy
import pickle

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestChainMap(unittest.TestCase):

    def test_basics(self):
        c = _ChainMap()
        c['a'] = 1
        c['b'] = 2
        d = c.new_child()
        d['b'] = 20
        d['c'] = 30
        # check internal state
        self.assertEqual(d.maps, [{'b': 20, 'c': 30}, {'a': 1, 'b': 2}])
        # check items/iter/getitem
        self.assertEqual(d.items(), dict(a=1, b=20, c=30).items())
        # check len
        self.assertEqual(len(d), 3)
        # check contains
        for key in 'abc':
            self.assertIn(key, d)
        # check get
        for k, v in dict(a=1, b=20, c=30, z=100).items():
            self.assertEqual(d.get(k, 100), v)

        # unmask a value
        del d['b']
        # check internal state
        self.assertEqual(d.maps, [{'c': 30}, {'a': 1, 'b': 2}])
        # check items/iter/getitem
        self.assertEqual(d.items(), dict(a=1, b=2, c=30).items())
        # check len
        self.assertEqual(len(d), 3)
        # check contains
        for key in 'abc':
            self.assertIn(key, d)
        # check get
        for k, v in dict(a=1, b=2, c=30, z=100).items():
            self.assertEqual(d.get(k, 100), v)
        # check repr
        self.assertIn(repr(d), [
            type(d).__name__ + "({'c': 30}, {'a': 1, 'b': 2})",
            type(d).__name__ + "({'c': 30}, {'b': 2, 'a': 1})"
        ])

# check shallow copies
        for e in d.copy(), copy.copy(d):
            self.assertEqual(d, e)
            self.assertEqual(d.maps, e.maps)
            self.assertIsNot(d, e)
            self.assertIsNot(d.maps[0], e.maps[0])
            for m1, m2 in zip(d.maps[1:], e.maps[1:]):
                self.assertIs(m1, m2)

        # check deep copies
        for e in [pickle.loads(pickle.dumps(d)),
                  copy.deepcopy(d),
                  eval(repr(d))
                  ]:
            self.assertEqual(d, e)
            self.assertEqual(d.maps, e.maps)
            self.assertIsNot(d, e)
            for m1, m2 in zip(d.maps, e.maps):
                self.assertIsNot(m1, m2, e)

        d = d.new_child()
        d['b'] = 5
        self.assertEqual(d.maps, [{'b': 5}, {'c': 30}, {'a': 1, 'b': 2}])
        # check parents
        self.assertEqual(d.parents.maps, [{'c': 30}, {'a': 1, 'b': 2}])
        # find first in chain
        self.assertEqual(d['b'], 5)
        # look beyond maps[0]
        self.assertEqual(d.parents['b'], 2)

    def test_contructor(self):
        # no-args --> one new dict
        self.assertEqual(_ChainMap().maps, [{}])
        # 1 arg --> list
        self.assertEqual(_ChainMap({1: 2}).maps, [{1: 2}])

    def test_missing(self):
        class DefaultChainMap(_ChainMap):
            def __missing__(self, key):
                return 999
        d = DefaultChainMap(dict(a=1, b=2), dict(b=20, c=30))
        for k, v in dict(a=1, b=2, c=30, d=999).items():
            # check __getitem__ w/missing
            self.assertEqual(d[k], v)
        for k, v in dict(a=1, b=2, c=30, d=77).items():
            # check get() w/ missing
            self.assertEqual(d.get(k, 77), v)
        for k, v in dict(a=True, b=True, c=True, d=False).items():
            # check __contains__ w/missing
            self.assertEqual(k in d, v)
        self.assertEqual(d.pop('a', 1001), 1, d)
        # check pop() w/missing
        self.assertEqual(d.pop('a', 1002), 1002)
        # check popitem() w/missing
        self.assertEqual(d.popitem(), ('b', 2))
        with self.assertRaises(KeyError):
            d.popitem()

    def test_dict_coercion(self):
        d = _ChainMap(dict(a=1, b=2), dict(b=20, c=30))
        self.assertEqual(dict(d), dict(a=1, b=2, c=30))
        self.assertEqual(dict(d.items()), dict(a=1, b=2, c=30))
