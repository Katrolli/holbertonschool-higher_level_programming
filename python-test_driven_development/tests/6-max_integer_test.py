#!/usr/bin/python3
import unittest
''' Module used for testing in the unittest format'''


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 5, 6, 7]), 7)
        self.assertAlmostEqual(max_integer([1, 8, 7, 2]), 8)
        self.assertAlmostEqual(max_integer([-1, 5, 9, 3]), 9)
        self.assertAlmostEqual(max_integer([-1, -5, -6, -7]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
