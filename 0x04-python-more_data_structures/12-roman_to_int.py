#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        num_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ, item = 0, 0
        for i in roman_string:
            if num_roman[i] > item:
                summ += num_roman[i] - item * 2
            else:
                summ += num_roman[i]
            item = num_roman[i]
            return summ
    return 0
