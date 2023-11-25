#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_Regular(self):
        """ Testing with a list (regular) """
        g = [1, 2, 3, 4, 5]
        RES = max_integer(g)
        self.assertEqual(RES, 5)

    def test_not_integer(self):
        """ Testing with a list with no integers """
        g = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, g)

    def test_EMPTY(self):
        """ Test with an empty list """
        g = []
        RES = max_integer(g)
        self.assertEqual(RES, None)

    def test_unique(self):
        """ Test with a list of one int """
        g = [41]
        RES = max_integer(g)
        self.assertEqual(RES, 41)

    def test_NEGATIVE(self):
        """ Test with negative values """
        g = [-2, -6, -1]
        RSA = max_integer(g)
        self.assertEqual(RSA, -1)

    def test_NOT_LIST(self):
        """  with a parameter that's not a list """
        self.assertRaises(TypeError, max_integer, 7)

    def test_IDENTICAL_VALUES(self):
        """ Test with a list of identical values """
        g = [8, 8, 8, 8, 8]
        RES = max_integer(g)
        self.assertEqual(RES, 8)

    def test_STRINGS(self):
        """ Test with a list of strings """
        g = ["hi", "hello"]
        RES = max_integer(g)
        self.assertEqual(RES, "hi")

    def test_FLOAT(self):
        """ Test with ints and floats """
        g = [3, 1.5, 2]
        REA = max_integer(g)
        self.assertEqual(REA, 1.5)

    def test_NONE(self):
        """ Test with a None """
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
