#!/usr/bin/python3
"""
    function that adds 2 integers.a and b must be integers or floats,
    otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer
    Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """ function that adds 2 integers """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
