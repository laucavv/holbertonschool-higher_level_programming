#!/usr/bin/python3
""" inheritance """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle"""
    def __init__(self, width, height):
        """builder"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height
        
    def area(self):
        """Area """
        return self.__width * self.__heigth
    
    def __str__(self):
        "Str"
        return "[Rectangle] {}/{}".format(self.__width, self.__heigth)