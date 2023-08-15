#!/usr/bin/python3
"""unittest for the models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Our unittest class

    inheriting from the unittest.TestCase

    class.
    """

    def test_rectangle_base_with_incomplete_correct_args(self):
        self.base1 = Rectangle(1, 2)
        self.base2 = Rectangle(1, 2, 3)
        self.base3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.base1.id, 3)
        self.assertEqual(self.base2.id, 4)
        self.assertEqual(self.base3.id, 5)

    def test_rectangle_for_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_reactangle_with_complete_correct_args(self):
        self.base4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.base4.id, 5)

    def test_rectangle_for_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_rectangle_display(self):
        self.assertEqual(Rectangle(4, 6).display(), 0)
        self.assertEqual(Rectangle(2, 2).display(), 0)
        self.assertEqual(Rectangle(2, 3, 2, 2).display(), 0)
        self.assertEqual(Rectangle(3, 2, 1, 0).display(), 0)
        self.assertEqual(Rectangle(3, 2, 4).display(), 0)
        self.assertEqual(Rectangle(3, 2, 5).display(), 0)
        self.assertEqual(Rectangle(3, 2, y=4).display(), 0)
        self.assertEqual(Rectangle(3, 2, y=3).display(), 0)

    def test_rectangle_string_display(self):
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(Rectangle(5, 5, 1).__str__(), "[Rectangle] (14) 1/0 - 5/5")

    def test_rectangle_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.update(), 1)
        self.assertEqual(r1.update(89), 0)
        self.assertEqual(r1.update(89, 2), 0)
        self.assertEqual(r1.update(89, 2, 3), 0)
        self.assertEqual(r1.update(89, 2, 3, 4), 0)
        self.assertEqual(r1.update(89, 2, 3, 4, 5), 0)
        self.assertEqual(r1.update(**{ 'id': 89 }), 0)
        self.assertEqual(r1.update(**{ 'id': 89, 'width': 1 }), 0)
        self.assertEqual(r1.update(**{ 'id': 89, 'width': 1, 'height': 2 }), 0)
        self.assertEqual(r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }), 0)
        self.assertEqual(r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }), 0)
        self.assertEqual(r1.update(22, x=1, height=2, y=3, width=4), 0)
        self.assertEqual(r1.update(13, 2, x=1, height=2, y=3, width=4), 0)
        self.assertEqual(r1.update(10, 3, 10, x=1, height=2, y=3, width=4), 0)
        self.assertEqual(r1.update(35, 3, 4, 3, x=1, height=2, y=3, width=4), 0)
        self.assertEqual(r1.update(25, 7, 5, 1, 2, x=1, height=2, y=3, width=4), 0)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertDictEqual(r1.to_dictionary(), r1.to_dictionary())

