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
    """init method to initialize in constructor"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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
