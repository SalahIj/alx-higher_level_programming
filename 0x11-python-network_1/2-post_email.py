#!/usr/bin/python3
""" The necessery imported modules """
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    new_data = urlencode(data)
    new_data = new_data.encode('ascii')
    req = Request(url, new_data, method='POST')
    with urlopen(req) as file_object:
        mail = file_object.read().decode('utf-8')
        print("Your email is: {}".format(mail))
