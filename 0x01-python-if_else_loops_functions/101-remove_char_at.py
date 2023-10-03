#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for index, i in enumerate(str):
        if (index == n):
            continue
        string += i
    return (string)
