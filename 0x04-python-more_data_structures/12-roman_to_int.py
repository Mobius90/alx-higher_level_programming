#!/usr/bin/python3
def roman_to_int(roman_string):
    nlist = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and nlist[roman_string[i]] > nlist[roman_string[i - 1]]:
            a += nlist[roman_string[i]] - 2 * nlist[roman_string[i - 1]]
        else:
            a += nlist[roman_string[i]]
    return a
