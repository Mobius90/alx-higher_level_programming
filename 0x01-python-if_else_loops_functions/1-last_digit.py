#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if x > 5:
    print("Last digit of {0} is {1} and is greater that 5".format(number, x))
elif x == 0:
    print("Last digit of {0} is {1} and is 0".format(number, x))
else :
    if x < 0:
        x = x * -1
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, x))
     