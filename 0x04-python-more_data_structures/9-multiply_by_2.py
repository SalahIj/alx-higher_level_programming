#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dic = {}
    for k in list(a_dictionary):
        a_dic[k] = a_dictionary.get(k) * 2
    return (a_dic)
