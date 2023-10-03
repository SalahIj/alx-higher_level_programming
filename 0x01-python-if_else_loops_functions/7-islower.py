#!/usr/bin/python3
def islower(c):
    for i in range(97, 123, 1):
        if (ord(c) == i):
            return (True)
    else:
        return (False)
