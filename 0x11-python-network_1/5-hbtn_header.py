#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = sys.argv[1]
    r = get(url)
    dictionary = dict(r.headers)
    print(dictionary.get('X-Request-Id'))
