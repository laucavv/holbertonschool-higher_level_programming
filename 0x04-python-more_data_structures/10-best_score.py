#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        i = 0
        for key, value in a_dictionary.items():
            if i < value:
                i = value
                b = key
        return b
    return None
