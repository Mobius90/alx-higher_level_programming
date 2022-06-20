#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for i in my_list:
            if i > x:
                continue
            print("{:d}".format(i), end="")
            y = y + 1
            print("")
    except Exception:
        print("")
    return y
