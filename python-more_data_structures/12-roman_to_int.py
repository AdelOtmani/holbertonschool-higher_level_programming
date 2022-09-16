#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dictionnary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                     'I': 1}
    res = 0
    idx = 0
    while idx < len(roman_string):
        value = a_dictionnary[roman_string[idx]]
        if (
            idx + 1 < len(roman_string)
            and value < a_dictionnary[roman_string[idx + 1]]
        ):
            res -= value
        else:
            res += value
        idx += 1
    return res
