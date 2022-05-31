#!/usr/bin/python3
for i in range(0, 99):
    for j in range(i + 1, 10):
        print("{0}{1}".format(i, j), end=', ')
print("{0:d}".format(i + 1))
