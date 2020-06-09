#!/usr/bin/python3
""" Tests for the Rectangle class """


import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
import sys
from io import StringIO
import pep8


class TestRecDocs(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


class TestRectanglePep8(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ test rectangle and test_rectangle
            for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestClassRectangle(unittest.TestCase):
    """
        Class containing functions to
        test on the Rectangle class
    """
    def setUp(self):
        """ Method to set the start point """
        self.rectangle = Rectangle(4, 6, 2, 2, 1)
        self.rectangle_1 = Rectangle(1, 7, 0, 0, 2)
        self.rectangle_2 = Rectangle(2, 4, 0, 3, 3)
        self.rectangle_3 = Rectangle(2, 5, 0, 0, 4)
        self.rectangle_4 = Rectangle(2, 4, 0, 0, 5)
        sys.stdout = StringIO()

    def tearDown(self):
        """
            Method to cleans everything up after running setup.
        """
        sys.stdout = sys.__stdout__

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
        """ TypeError cases with string """
        self.assertRaises(TypeError, Rectangle, "a", 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2, 3, "3", 9)
        self.assertRaises(TypeError, Rectangle, 2, "3", 5, 9)
        self.assertRaises(TypeError, Rectangle, 8, 6, 3, "9")

    def test_r2(self):
        """ TypeError cases"""
        self.assertRaises(TypeError, Rectangle, [1, 2], 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2, 3, 3.5, 9)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2}, 5, 9)
        self.assertRaises(TypeError, Rectangle, 8, 6, 3, (1, 2))

    def test_r3(self):
        """ValueError cases """
        self.assertRaises(ValueError, Rectangle, -8, 2, 7, 8)
        self.assertRaises(ValueError, Rectangle, 2, 3, -5, 9)
        self.assertRaises(ValueError, Rectangle, 2, -8, 5, 9)
        self.assertRaises(ValueError, Rectangle, 8, 6, 3, -5)

    def test_r4(self):
        """ More TypeError cases """
        self.assertRaises(TypeError, Rectangle, None, 3, 6, 8, 9)
        self.assertRaises(TypeError, Rectangle, 222, 197, 5j, 19)
        self.assertRaises(TypeError, Rectangle, 2, float("inf"), 8, 1)
        self.assertRaises(TypeError, Rectangle, 222, 197, "lau", 2398)
        self.assertRaises(TypeError, Rectangle)

    def test_area(self):
        """Test the area method. """
        self.assertEqual(self.rectangle.area(), 24)
        self.assertEqual(self.rectangle_1.area(), 7)
        self.assertEqual(self.rectangle_2.area(), 8)
        self.assertEqual(self.rectangle_3.area(), 10)

    def test_display(self):
        """Test display method without x and y """
        repre = "##\n" \
                "##\n" \
                "##\n" \
                "##\n"
        self.rectangle_4.display()
        self.assertEqual(sys.stdout.getvalue(), repre)

    def test_str(self):
        """ Test that __str__ method produces correct output. """
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (1)"
                                                   " 2/2 - 4/6")
        self.assertEqual(self.rectangle_1.__str__(), "[Rectangle] (2)"
                                                     " 0/0 - 1/7")
        self.assertEqual(self.rectangle_2.__str__(), "[Rectangle] (3)"
                                                     " 0/3 - 2/4")
        self.assertEqual(self.rectangle_3.__str__(), "[Rectangle] (4)"
                                                     " 0/0 - 2/5")

    def test_display2(self):
        """  Test display method with 'x' and 'y' position. """
        repre = "\n\n\n##\n" \
                "##\n" \
                "##\n" \
                "##\n"
        self.rectangle_2.display()
        self.assertEqual(sys.stdout.getvalue(), repre)

    def test_update(self):
        """ Tests that the update method uses setter with *args. """
        self.rectangle_2.update(5, 4, 1, 9, 23)
        self.assertEqual(self.rectangle_2.__str__(), "[Rectangle] (5)"
                                                     " 9/23 - 4/1")

    def test_update2(self):
        """ Tests that the update method uses setter with **kwargs. """
        self.rectangle_4.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.rectangle_4.__str__(), "[Rectangle] (5)"
                                                     " 1/3 - 4/2")

    def test_dic(self):
        """ Test regular to_dictionary """
        dic = {'x': 0, 'id': 2, 'height': 7, 'width': 1, 'y': 0}
        self.assertEqual(self.rectangle_1.to_dictionary(), dic)
