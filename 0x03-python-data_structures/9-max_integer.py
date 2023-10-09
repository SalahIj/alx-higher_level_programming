#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    lenght = len(my_list)
    if (lenght < 0):
        return (None)
    else:
        for i in range(lenght):
            if (my_list[i] >= max):
                max = my_list[i]
    return (max)
