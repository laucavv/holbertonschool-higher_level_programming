#!/usr/bin/python3
""" create an class called square with size and we validate the input """


class Square:
    """init method to initialize in constructor"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """ getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
