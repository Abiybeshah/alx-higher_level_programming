#!/usr/bin/python3
def no_c(my_string):
    listchar = list(my_string)
        for char in listchar:
            if char == 'c' or char == 'C':
                listchar.remove(char)
                return ("".join(listchar))
