#!/usr/bin/python3
""" The necessery imported modules """
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as file_object:
            print(file_object.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
