#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    new_list = my_list.copy()
    new_list.sort(reverse=True)
    return (new_list[0])
