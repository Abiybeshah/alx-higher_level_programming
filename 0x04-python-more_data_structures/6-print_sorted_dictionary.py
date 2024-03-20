#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = []
    if a_dictionary:
        for a, b in a_dictionary.items():
            key.append(a)
        key.sort()
        for item in key:
            print("{} : {}".format(items, a_dictionary(items)))
