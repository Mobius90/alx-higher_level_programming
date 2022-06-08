#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, j in sorted(a_dictionary.items()):
        print("{0}: {1}".format(i, j))
        
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
