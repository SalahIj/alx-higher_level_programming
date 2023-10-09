#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenght = len(my_list)
    if (idx >= 0 and idx < lenght):
        my_list[idx] = element
        return (my_list)
    else:
        return (my_list)
