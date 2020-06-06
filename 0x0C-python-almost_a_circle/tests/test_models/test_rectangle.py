import unittest
from models.base import Base
from models.rectangle import Rectangle
class TestClassRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4, 6, 2, 2)
        self.rectangle_1 = Rectangle(1, 7)
        self.rectangle_2 = Rectangle(2, 4, 0, 3)
        self.rectangle_3 = Rectangle(2, 5)



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
    def test_area(self):
        self.assertEqual(self.rectangle.area(), 24)
        self.assertEqual(self.rectangle_1.area(), 7)
        self.assertEqual(self.rectangle_2.area(), 8)
        self.assertEqual(self.rectangle_3.area(), 10)
    def test_display(self):
        pass
    def test_str(self):
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (46) 2/2 - 4/6")
        self.assertEqual(self.rectangle_1.__str__(), "[Rectangle] (47) 0/0 - 1/7")
        self.assertEqual(self.rectangle_2.__str__(), "[Rectangle] (48) 0/3 - 2/4")
        self.assertEqual(self.rectangle_3.__str__(), "[Rectangle] (49) 0/0 - 2/5")



if __name__ == '__main__':
    unittest.main()