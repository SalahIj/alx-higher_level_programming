#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import post


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r_data = post(url, data={"q": q})
    try:
        if r_data.headers['content-type'] == "application/json":
            print(f"[{json['id']}] {json['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
