#!/usr/bin/python3
"""test_unittest base
    """
import unittest
import json
from os.path import exists
from models.base import Base
from models.rectangle import Rectangle


class Test_instentiation(unittest.TestCase):

    def test_all_and_no_arg(self):
        """test when base have arg and
        when it's equal to none"""
        Base.__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

        b = Base()
        self.assertEqual(b.id, 5)

    def test_input(self):
        """test for valid input for positive int or negativ and float
        """
        b_pos = Base(12)
        self.assertEqual(b_pos.id, 12)

        b_neg = Base(-12)
        self.assertEqual(b_neg.id, -12)

        b_float = Base(6.8)
        self.assertEqual(b_float.id, 6.8)

    def test_pub_id(self):
        """test for public id
        """
        b = Base(12)
        b.id = 21
        self.assertEqual(21, b.id)

    def test_str(self):
        """test string
        """
        b_str = Base("school")
        self.assertEqual(b_str.id, "school")

    def test_num_private(self):
        """test for private number object
        """
        b = Base(5)
        with self.assertRaises(AttributeError):
            print(b.nb__objects)

    def test_json_str(self):
        Base._Base__nb_objects = 0
        l1 = {"id": 5, "width": 5, "height": 6, "x": 8, "y": 9}
        l2 = {"id": 6, "width": 7, "height": 7, "x": 9, "y": 8}
        new_json = Base.to_json_string([l1, l2])
        self.assertTrue(type(new_json) is str)
        list = json.loads(new_json)
        self.assertEqual(list, [l1, l2])

    def test_from_json_file(self):
        """test for normal from json file
        """
        str = '[{"id": 5, "width": 5, "height": 6, "x": 8, "y": 9}, \
            {"id": 6, "width": 7, "height": 7, "x": 9, "y": 8}]'
        json_file = Base.from_json_string(str)
        self.assertTrue(type(json_file) is list)
        self.assertEqual(len(json_file), 2)
        self.assertTrue(type(json_file[0]) is dict)
        self.assertTrue(type(json_file[1]) is dict)
        self.assertEqual(json_file[0],
                         {"id": 5, "width": 5, "height": 6, "x": 8, "y": 9})
        self.assertEqual(json_file[1],
                         {"id": 6, "width": 7, "height": 7, "x": 9, "y": 8})


if __name__ == '__main__':
    unittest.main()
