#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for string in sorted(a_dictionary):
        print("{} = {}".format(string, a_dictionary[string]))
