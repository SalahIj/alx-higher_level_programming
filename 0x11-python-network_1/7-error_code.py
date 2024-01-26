#!/usr/bin/pyhon3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main":
    url = sys.argv[1]
    r_data = get(url)
    if r_data.status_code >= 400:
        print("Error code: {}".format(r_data.status_code))
    else:
        print(r_data.text)
