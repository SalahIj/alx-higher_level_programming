#!/usr/bin/python3
""" The necessery imported modules """
from requests import get

if __name__ == "__main__":
    r = get('https://alx-intranet.hbtn.io/status')
    data = r.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
