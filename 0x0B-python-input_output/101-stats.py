#!/usr/bin/python3
""" The module imported """
from sys import stdin


COD = {'200': 0, '301': 0, '400': 0, '401': 0,
       '403': 0, '404': 0, '405': 0, '500': 0}
size_t = 0
i = 0


def printing_funtion():
    """ The function description:
        is printing function
    """
    print("File size: {}".format(size_t))
    for cle, value in sorted(COD.items()):
        if (value > 0):
            print(f"{cle}: {value}")


try:
    for ls in stdin:
        ls = ls.split()
        if (len(ls) >= 2):
            temoin = i
            if (ls[-2] in COD):
                COD[ls[-2]] += 1
                i += 1
            try:
                size_t += int(ls[-1])
                if (temoin == i):
                    i += 1
            except Exception:
                if (temoin == i):
                    continue
        if (i % 10 == 0):
            printing_funtion()
    printing_funtion()
except KeyboardInterrupt:
    printing_funtion()
