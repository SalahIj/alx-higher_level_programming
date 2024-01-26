#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    authent = HTTPBasicAuth(username, password)
    r_data = get(url, auth=authent)
    r_js = r_data.json()
    print(r_js['id'])
