#!/usr/bin/python3
"""
Unittest classes
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """ test for class rectangle
    """

    @classmethod
    def setUpClass(cls):
        Base.__Base__nb_objects = 0
        cls.a = Rectangle(5, 5)
        cls.b = Rectangle(1, 2, 3)

    def test_no_arg(self):
        """ test with no arg """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_id(self):
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)

    def test_rect(self):
        """ test rectangle """
        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)

    def test_one_arg(self):
        """ test one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_base(self):
        """ test rectangle base """
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_none_id(self):
        """ test none id """
        self.assertEqual(Base(None).id, Base(None).id - 1)
