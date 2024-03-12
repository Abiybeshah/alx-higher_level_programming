#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    las = number % 10
elif number < 0:
    las = number % -10
elif number == 0:
    las = 0

if las < 6 and las != 0:
    note = "and is less than 6 and not 0"
    print("Last digit of {} is {} {}".format(number, las, note))
elif las > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, las))
else:
    print("Last digit of {} is {} and is 0".format(number, las))
