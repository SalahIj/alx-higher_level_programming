#!/usr/bin/python3
import sys
from requests import post


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = post(url, params=payload)
    print(r.text)
