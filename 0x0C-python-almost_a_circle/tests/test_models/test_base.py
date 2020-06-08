#!/usr/bin/python3
"""
    Tests for the Base class
"""

import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """  Class containing functions to
        test on the Bass class
    """
    def setUp(self):
        """ Method to set the start point  """
        Base._Base__nb_objects = 0

    def test_b0(self):
        """
            Instance creation verification,
            with its respective id
        """
        base_0 = Base()
        base_1 = Base(23)
        base_2 = Base()

        self.assertEqual(base_0.id, 1)
        self.assertEqual(base_1.id, 23)
        self.assertEqual(base_2.id, 2)

    if __name__ == '__main__':
        unittest.main()
