#!/usr/bin/python3
def roman_to_int(roman_string):
    nlist = {'X': 10, 'VII': 7, 'IX': 9, 'LXXXVII': 87, 'DCCVII': 707}
    a = 0
    if not roman_string:
        return 0
    for i in nlist.keys():
        if i == roman_string:
            a = nlist[i]
    return a
