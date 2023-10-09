#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for s in my_string:
        if (s != 'c' and s != 'C'):
            string += s
    return (string)
