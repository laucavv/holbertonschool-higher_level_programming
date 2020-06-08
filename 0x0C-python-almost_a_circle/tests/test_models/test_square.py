#!/usr/bin/python3
""" Tests for the Square class """


import unittest
from models.square import Square


class TestClassSquare(unittest.TestCase):
    """
        Class containing functions to
        test on the Square class
    """
    def setUp(self):
        """ Method to set the start point """
        self.square = Square(4, 8, 6, 1)
        self.square_1 = Square(1, 3, 4, 2)
        self.square_2 = Square(2, 4, 4, 3)

    def test_s0(self):
        """instantiation"""
        self.assertEqual(self.square.size, 4)
        self.assertRaises(TypeError, Square, [1, 2], 2, 7)
        self.assertRaises(TypeError, Square, 2, 3.5, 12)
        self.assertRaises(TypeError, Square, 8, 6, {1, 2})
        self.assertRaises(ValueError, Square, -8, 2, 7)
        self.assertRaises(ValueError, Square, 2, 3, -5)
        self.assertRaises(ValueError, Square, 2, -8, 5)

    def test_str(self):
        """Test that __str__ method produces correct output.  """
        self.assertEqual(self.square.__str__(), "[Square] (1)"
                                                " 8/6 - 4")

    def test_dic(self):
        """ Test regular to_dictionary """
        dic = {'x': 4, 'id': 3, 'size': 2, 'y': 4}
        self.assertEqual(self.square_2.to_dictionary(), dic)


if __name__ == '__main__':
    unittest.main()
