#!/usr/bin/python3
"""method for reading a file"""

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
