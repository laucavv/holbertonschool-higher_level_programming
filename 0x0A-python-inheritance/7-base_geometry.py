#!/usr/bin/python3
""" Class  BaseGeometry"""


class BaseGeometry:
    """ Public instance method """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            if value is not an integer: raise a TypeError exception,
            with the message <name> must be an integer

            if value is less or equal to 0: raise a ValueError exception
            with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
