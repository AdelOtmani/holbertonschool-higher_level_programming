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

    def test_type(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            c = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            c = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            c = Rectangle(1, 2, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            c = Rectangle(1, 2, 3, "1")



    def test_rect(self):
        """ test rectangle """
        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)

    def test_one_arg(self):
        """ test one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        """test value widht
        """
        self.assertEqual(self.a.width, 5)
        self.assertEqual(self.b.width, 1)

    def test_height(self):
        """test value height
        """
        self.assertEqual(self.a.height, 5)
        self.assertEqual(self.b.height, 2)

    def test_x(self):
        """test value x
        """
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.b.x, 3)

    def test_y(self):
        """test value y
        """
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.y, 0)

    def test_rectangle_base(self):
        """ test rectangle base """
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_none_id(self):
        """ test none id """
        self.assertEqual(Base(None).id, Base(None).id - 1)
