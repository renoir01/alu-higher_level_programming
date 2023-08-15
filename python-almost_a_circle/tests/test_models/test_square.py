#!/usr/bin/python3
"""unittest for the models/square.py
"""

import unittest
from models.square import Square


class TesSquare(unittest.TestCase):
    """
    Our unittest class

    inheriting from the unittest.TestCase

    class.
    """
    def test_square_with_incomplete_correct_args(self):
        self.base1 = Square(1)
        self.base2 = Square(1, 2)
        self.base3 = Square(1, 2, 3)
        self.assertEqual(self.base1.id, 7)
        self.assertEqual(self.base2.id, 8)
        self.assertEqual(self.base3.id, 9)
        
    def test_square_for_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_with_complete_correct_args(self):
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_square_for_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_string_display(self):
        self.assertEqual(Square(5).__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(Square(2, 2).__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(Square(3, 1, 3).__str__(), "[Square] (3) 1/3 - 3")
        self.assertEqual(Square(3, 1, 3, 6).__str__(), "[Square] (6) 1/3 - 3")

    def test_square_update(self):
        s1 = Square(5)
        self.assertEqual(s1.update(10), 0)
        self.assertEqual(s1.update(1, 2), 0)
        self.assertEqual(s1.update(1, 2, 3), 0)
        self.assertEqual(s1.update(1, 2, 3, 4), 0)
        self.assertEqual(s1.update(), 1)
        self.assertEqual(s1.update(**{ 'id': 89 }), 0)
        self.assertEqual(s1.update(**{ 'id': 89, 'size': 1 }), 0)
        self.assertEqual(s1.update(**{ 'id': 89, 'size': 1, 'x': 2 }), 0)
        self.assertEqual(s1.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }), 0)
        self.assertEqual(s1.update(10, 3, x=1, size=2, y=3), 0)

    def test_square_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        self.assertDictEqual(s1.to_dictionary(), s1.to_dictionary())
        self.assertDictEqual(s2.to_dictionary(), s2.to_dictionary())
