#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if (k > i):
            if (i != 8 or k != 9):
                print("{:d}{:d}".format(i, k), end=", ")
            else:
                print("{:d}{:d}".format(i, k))
