#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n > 0:
    l = n % 10
elif n < 0:
    temp = -n
    l = temp % 10
    l = -l
elif n == 0:
    l = 0

if l < 6 and l != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, l))
elif l > 5:
    print("Last digit of {} is {} and is greater than 5"
            .format(n, l))
else:
    print("Last digit of {} is {} and is 0".format(n, l))
