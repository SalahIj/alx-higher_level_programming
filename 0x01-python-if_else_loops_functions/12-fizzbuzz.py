#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101, 1):
        if (i % 3 == 0 and i % 5 != 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0 and i % 3 != 0):
            print("Buzz", end=" ")
        elif (i % 3 == 0 and i % 5 == 0):
            print("FizzBuss", end=" ")
        else:
            print("{:d}".format(i), end=" ")
