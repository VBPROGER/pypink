#!/usr/bin/env python3
import unittest, pydoc
from os import path
def import_file(path: str = ''): return pydoc.importfile(path)
lib = import_file(path.abspath(path.expanduser(path.expandvars(('src/pypink.py')))))

class TestUtils(unittest.TestCase):
    def test_get_args(self):
        self.assertEqual(lib.get_args(7), (7,))
        self.assertEqual(lib.get_args([-12], '7566', -122.47), ([-12], '7566', -122.47))
    def test_is_empty(self):
        self.assertTrue(lib.is_empty(''))
        self.assertFalse(lib.is_empty('123'))
        self.assertFalse(lib.is_empty(567))
        self.assertFalse(lib.is_empty('abababa'))
        self.assertFalse(lib.is_empty(-17.56))
        self.assertFalse(lib.is_empty([555, 4132]))

if __name__ == '__main__':
    unittest.main()