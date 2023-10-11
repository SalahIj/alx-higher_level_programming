#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        if (a_dictionary.get(i) == value):
            del a_dictionary[i]
    return (a_dictionary)
