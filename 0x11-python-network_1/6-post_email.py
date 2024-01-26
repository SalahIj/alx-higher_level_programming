#!/usr/bin/python3
""" The necessery importd modules """
import sys
from requests import post


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_mail = {"email": email}
    r = post(url, data=data_mail)
    print(r.text)
