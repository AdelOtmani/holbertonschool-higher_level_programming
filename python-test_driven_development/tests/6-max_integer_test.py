#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def onlypos_valuetest(self):
        self.assertEqual(max_integer([1, 12, 9]), 12)

    def onlyneg_value_test(self):
        self.assertEqual(max_integer([-1, -12, -9]), -1)

    def oneneg_test(self):
        self.assertEqual(max_integer([1, 6, 300, -1, 500]), 500)

    def single_test(self):
        self.assertEqual(max_integer([22]), 22)

    def floatint_test(self):
        self.assertEqual(max_integer([5, 6, 3.2, 9.8]), 9.8)

    def emptylist_test(self):
        self.assertEqual(max_integer([]), None)
