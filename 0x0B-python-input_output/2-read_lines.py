#!/usr/bin/python3
""" a function that reads n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """ funtion"""
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        num_l = len(lines)

        if nb_lines <= 0 or nb_lines > num_l:
            for line in lines:
                print(line, end="")
        else:
            num_c = 1
            for line in lines:
                print(line, end="")
                num_c += 1
                if num_c > nb_lines:
                    break