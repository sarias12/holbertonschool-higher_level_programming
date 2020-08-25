#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    r = requests.get(url)
    try:
        list = r.json()
        for idx in range(0, 10):
            sha = list[idx].get('sha')
            name = list[idx].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except IndexError:
        pass
