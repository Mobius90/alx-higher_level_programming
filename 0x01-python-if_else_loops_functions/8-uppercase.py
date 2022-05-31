failed
#!/usr/bin/python3
from curses.ascii import isdigit


def uppercase(str):
    for i in str:
        if isdigit(i) ==True:
            print("{0}".format(i), end='')
        if ord(i) > 96 and ord(i) < 123:
            i = ord(i) - 32
            print("{:c}".format(i), end='')
uppercase("best 98");