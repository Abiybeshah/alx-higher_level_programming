#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n > 0:
    las = n % 10
elif n < 0:
    las = n % -10
elif n == 0:
    las = 0

if las < 6 and las != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, las))
elif las > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, las))
else:
    print("Last digit of {} is {} and is 0".format(n, las))
