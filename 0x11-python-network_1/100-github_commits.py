#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"

    r_data = get(url)
    com = r_data.json()
    try:
        i = 0
        while i < 10:
            print(f"{com[i].get('sha')}:
                  {com[i].get('commit').get('author').get('name')}")
            i++
    except IndexError:
        pass
