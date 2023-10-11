#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        num1 = 0
        num2 = 0
        num1 = sum(x * y for x, y in my_list)
        num2 = sum(y for x, y in my_list)
        return (num1 / num2)
    else:
        return (0)
