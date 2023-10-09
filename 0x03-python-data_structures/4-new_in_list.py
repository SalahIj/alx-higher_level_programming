#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return (None)
    lenght = len(my_list)
    my_new_list = []
    if (idx >= 0 and idx < lenght):
        my_new_list = my_list.copy()
        my_new_list[idx] = element
        return (my_new_list)
    else:
        return (my_list)
