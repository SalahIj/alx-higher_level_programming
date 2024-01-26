#!/usr/bin/python3
""" The necessery imported modules """
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    dictionary = {}
    with urlopen(url) as file_object:
        dictionary = dict(file_object.headers)
        serial = dictionary.get("X-Request-Id")
        print(serial)
