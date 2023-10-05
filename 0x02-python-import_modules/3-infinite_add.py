#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    lenght = len(sys.argv)
    if (lenght == 1):
        print(0)
    elif (lenght == 2):
        print("{:d}".format(int(sys.argv[1])))
    else:
        sum = 0
        for i in range(1, lenght):
            sum += int(sys.argv[i])
            print("{:d}".format(sum))
