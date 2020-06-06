""" 
"""

import unittest
from models.base import Base

class TestClassBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_b0(self):
        base_0 = Base()
        base_1 = Base(23)
        base_2 = Base()

        self.assertEqual(base_0.id, 1)
        self.assertEqual(base_1.id, 23)
        self.assertEqual(base_2.id, 2)
    
    if __name__ == '__main__':
        unittest.main()
