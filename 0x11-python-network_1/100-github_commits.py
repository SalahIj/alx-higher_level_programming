#!/usr/bin/python3
""" The necessery imported modules """
import sys
from requests import get


if __name__ == "__main__":
    repo = sys.argv[1]
    malik = sys.argv[2]
    url = f'https://api.github.com/repos/{malik}/{repo}/commits'

    request = get(url)
    commits = request.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
