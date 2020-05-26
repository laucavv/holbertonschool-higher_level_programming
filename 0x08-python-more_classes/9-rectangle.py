#!/usr/bin/python3
"""
    create an class called rectangle
    # width must be an integer, otherwise raise a TypeError exception with
    the message width must be an integer
    # if width is less than 0, raise a ValueError exception with
    the message width must be >= 0
    # height must be an integer, otherwise raise a TypeError exception with
    the message height must be an integer
    # if height is less than 0, raise a ValueError exception with
    the message height must be
"""


class Rectangle:
    """ Class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init method to initialize in constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ repesentation rectangle"""
        rec_re = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rec_re += "#" * self.__width
                rec_re += "\n"
            rec_re = rec_re[:-1]
        return rec_re

    def __repr__(self):
        """ return rectangle"""
        return 'Rectangle(' + str(self.__width) + \
            ',' + str(self.__height) + ')'

    def __del__(self):
        """ prints a messge when delete instance
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance"""
        return cls(size, size)