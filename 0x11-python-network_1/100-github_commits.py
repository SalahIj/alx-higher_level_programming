#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    request = get(url)
    commits = request.json()
    try:
        i = 0
        while i < 10:
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
            i += 1
    except IndexError:
        pass
