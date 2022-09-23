#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_onlypos_value(self):
        self.assertEqual(max_integer([1, 12, 9]), 12)

    def test_onlyneg_value(self):
        self.assertEqual(max_integer([-1, -12, -9]), -1)

    def test_oneneg(self):
        self.assertEqual(max_integer([1, 6, 300, -1, 500]), 500)

    def test_single(self):
        self.assertEqual(max_integer([22]), 22)

    def test_floatint(self):
        self.assertEqual(max_integer([5, 6, 3.2, 9.8]), 9.8)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)
