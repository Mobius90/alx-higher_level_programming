#!/usr/bin/python3
def print_last_digit(number):
    if number > -1:
        i = number % 10
        print(f"{i:d}", end='')
        return i
    else:
        i = (number * -1) % 10
        print(f"{i:d}", end='')
        return i
