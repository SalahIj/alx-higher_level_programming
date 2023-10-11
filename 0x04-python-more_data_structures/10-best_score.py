#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is not None):
        max_value = 0
        max_key = None
        for i, j in a_dictionary.items():
            if (max_value < j):
                max_key = i
                max_value = j
        return (max_key)
    else:
        return (None)
