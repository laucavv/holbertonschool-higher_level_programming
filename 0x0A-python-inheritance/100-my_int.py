#!/usr/bin/python3
""" Class MyInt """


class MyInt(int):
    """ class """

    def __ne__(self, value):
        """ negation to equal """
        return super().__eq__(value)

    def __eq__(self, value):
        """ equal to negation """
        return super().__ne__(value)
