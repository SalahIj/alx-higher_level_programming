#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)
    r = get(url, auth=auth)
    print(r.json().get("id"))
