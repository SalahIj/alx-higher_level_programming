#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = sys.argv[1]
    r_data = get(url)
    if r_data.status_code >= 400:
        print(f"Error code: {r_data.status_code}")
    else:
        print(r_data.text)
