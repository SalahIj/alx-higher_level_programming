#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r_data = get(url)
    com = r_data.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                com[i].get('sha'),
                com[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
