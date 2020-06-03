#!/usr/bin/python3
""" class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class"""

    def __init__(self, size):
        """ builder """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        """ str """
        return "[Square] {}/{}".format(self.__size, self.__size)
