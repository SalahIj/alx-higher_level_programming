#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    Roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    last_num = 0
    T = 0
    for i in reversed(roman_string):
        last_num = Roman_digits[i]
        if (T < last_num * 5):
            T += last_num
        else:
            T -= last_num
    return (T)
