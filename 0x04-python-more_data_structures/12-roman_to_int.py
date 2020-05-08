#!/usr/bin/python3
def roman_to_int(roman_string):
    summ = 0
    if roman_string and type(roman_string) is str:
        num_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        idx = 0
        for idx, item in enumerate(roman_string):
            for key, value in num_roman.items():
                if item == key and idx > 0:
                    if num_roman[roman_string[idx]] > num_roman[roman_string[idx-1]]:
                        summ = summ + value - num_roman[roman_string[idx-1]]
                    else:
                        summ = summ + value
                else:
                    summ = summ + value
    return summ

