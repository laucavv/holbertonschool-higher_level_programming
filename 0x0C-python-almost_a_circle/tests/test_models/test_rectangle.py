import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestClassRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4,6,2,2)

    def test_r0(self):
        """Normal Cases"""
        rec_1 = Rectangle(2, 6)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 6)
        rec_2 = Rectangle(8, 3, 1, 2)
        self.assertEqual(rec_2.width, 8)
        self.assertEqual(rec_2.height, 3)
        self.assertEqual(rec_2.x, 1)
        self.assertEqual(rec_2.y, 2)
    def test_r1(self):
        self.assertRaises(TypeError,Rectangle, "a", 2, 7, 8)
        self.assertRaises(TypeError,Rectangle, 2, 3, "3", 9)
        self.assertRaises(TypeError,Rectangle, 2,"3", 5, 9)
        self.assertRaises(TypeError,Rectangle, 8, 6, 3, "9")
    def test_r2(self):
        self.assertRaises(TypeError,Rectangle, [1,2], 2, 7, 8)
        self.assertRaises(TypeError,Rectangle, 2, 3, 3.5, 9)
        self.assertRaises(TypeError,Rectangle, 2, {1,2},5 ,9)
        self.assertRaises(TypeError,Rectangle, 8,6,3, (1,2))
    def test_r3(self):
        self.assertRaises(ValueError,Rectangle, -8, 2, 7, 8)
        self.assertRaises(ValueError,Rectangle, 2, 3, -5, 9)
        self.assertRaises(ValueError,Rectangle, 2, -8, 5, 9)
        self.assertRaises(ValueError,Rectangle, 8, 6, 3, -5)
    def test_r4(self):
        self.assertRaises(TypeError, Rectangle, None, 3, 6, 8, 9)
        self.assertRaises(TypeError, Rectangle, 222, 197, 5j, 19)
        self.assertRaises(TypeError, Rectangle, 2, float("inf"), 8, 1)
        self.assertRaises(TypeError, Rectangle, 222, 197, "lau", 2398)
        self.assertRaises(TypeError, Rectangle)

if __name__ == '__main__':
    unittest.main()