#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i < 1:
        print("{} arguments.".format(i))
    elif x == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
        for k in range(i):
            print("{}: {:s}".format(k + 1, argv[k + 1]))
