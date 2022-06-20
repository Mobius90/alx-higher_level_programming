#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in value:
            print("{:d}".format(i), end="")
        print("")
        return True
    except Exception:
        return False
