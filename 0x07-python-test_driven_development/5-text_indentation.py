#!/usr/bin/python3
"""
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Args:
        Text is string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    ch_s = ['.', ':', '?']
    start_line = True
    for i in text:
        if i == " " and start_line is True:
            continue
        if i in ch_s:
            print(i, end="")
            print('\n')
            start_line = True
        else:
            print(i, end="")
            start_line = False
