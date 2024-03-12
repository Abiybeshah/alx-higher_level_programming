#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_dig = number % 10
elif number < 0:
    temp = -number
    last_dig = temp % 10
else:
    last_dig = 0

if last_dig < 6:
    print("last digit of {} is {} and is less than 6 and not 0".format(number, last_dig))
elif last_dig > 5:
    print("last digit of {} is {} and is greater than 5".format(number, last_dig))
else:
    print("last digit of {} is {} and is 0".format(number, last_dig))
