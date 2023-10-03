#!/usr/bin/python3
for k in range(ord('a'), ord('z') + 1):
    if (k == 101 or k == 113):
        continue
    print("{:c}".format(k), end="")
