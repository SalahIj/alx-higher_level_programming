#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    a = len(sys.argv)
    if (a == 1):
        print("{:d}".format(a - 1), "arguments.")
    elif (a == 2):
        print("{:d}".format(a - 1), "argument:")
        print("1:", sys.argv[1])
    else:
        print("{:d}".format(a - 1), "arguments:")
        for i in range(1, a):
            print("{:d}: {}".format(i, sys.argv[i]))
