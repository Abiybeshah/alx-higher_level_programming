#!/usr/bin/python3
if __name__ == "__main__":
from hidden_4 import *
all_n = dir()
for i in range(0, len(all_n)):
    if all_n[i][:2] != " ":
        print("{:s}".format(all_n[i]))
