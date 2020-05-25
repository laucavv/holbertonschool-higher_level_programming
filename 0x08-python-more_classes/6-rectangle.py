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

    def __init__(self, width=0, height=0):
        """init method to initialize in constructor"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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
        """Delete object """
        print("Bye rectangle...")
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1
