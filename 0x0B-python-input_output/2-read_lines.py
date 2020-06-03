#!/usr/bin/python3
"""a function that reads n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """funtion"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            num_c = 0
            if nb_lines <= 0 or nb_lines == num_c:
                print(line, end="")
