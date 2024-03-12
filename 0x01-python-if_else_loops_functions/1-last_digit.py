#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num > 0:
    las = num % 10
elif num < 0:
    temp = -num
    las = temp % 10
    las = -las
elif num == 0:
    las = 0

if las < 6 and las != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, las))
elif las > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, las))
else:
    print("Last digit of {} is {} and is 0".format(num, las))
