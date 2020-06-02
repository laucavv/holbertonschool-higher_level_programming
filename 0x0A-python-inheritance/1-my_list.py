#!/usr/bin/python3
"""  class MyList that inherits from list """


class MyList(list):
    """ that prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        """prints the list """
        print(sorted(self))
