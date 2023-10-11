#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        num1 = 0
        num2 = 0
        num1 = sum(x * y for x, y in my_list)
        num2 = sum(y for x, y in my_list)
        return (num1 / num2)
