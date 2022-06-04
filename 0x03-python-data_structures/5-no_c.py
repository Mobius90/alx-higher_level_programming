#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(n):None for n in 'c'})
    new_string1 = new_string.translate({ord(n):None for n in 'c'})
    return new_string1
