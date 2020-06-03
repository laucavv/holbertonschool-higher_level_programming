#!/usr/bin/python3
"""
    function that returns
    the number of lines of a text file
"""


def number_of_lines(filename=""):
    """funtion """
    with open(filename, encoding="utf-8") as file:
        num_lines = 0
        for i in file:
            num_lines += 1
    file.close()
    return num_lines
