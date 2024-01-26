#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    sys.argv[1] = username
    sys.argv[2] = password
    url = "https://api.github.com/user"
    r_data = get(url, auth=(username, password))
    r_js = r_data.json()
    print(r_js['id'])
