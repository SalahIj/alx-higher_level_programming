#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = sys.argv[1]
    r_data = get(url)
    r_header = r_data.headers['X-Request-Id']
    print(r_header)
