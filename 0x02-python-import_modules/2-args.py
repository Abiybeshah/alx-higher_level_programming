#!/usr/bin/python3
if __name__ != "__main__":
    exit()
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    j = 0
    for arg in argv:
        if j != 0:
            print("{:d}: {:s}".format(i, arg))
	    j += 1
