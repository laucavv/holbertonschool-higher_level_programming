#!/usr/bin/python3
"""
    function that returns
    the number of lines of a text file
"""


def number_of_lines(filename=""):
    """funtion """
    with open("my_file_0.txt", mode="r", encoding="utf-8") as my_file:
        num_lines = 0
        for i in my_file:
            num_lines += 1
        return num_lines
