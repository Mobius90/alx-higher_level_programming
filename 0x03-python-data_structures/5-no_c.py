#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.translate({ord(n):None for n in 'cC'})
    return my_string
