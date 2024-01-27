#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r_data = get(url)
    com = r_data.json()
    try:
        j = 0
        while j < 10:
            print('{}: {}'.format(
                com[j].get('sha'),
                com[j].get('commit').get('author').get('name')))
            j = j + 1
    except IndexError:
        pass
