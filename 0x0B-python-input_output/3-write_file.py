#!/usr/bin/python3
""" function that writes a string to a text file """


def write_file(filename="", text=""):
    """ funtion """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
