#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pasw = sys.argv[2]
    url = 'https://api.github.com/user'
    value = {'login': user}
    r = requests.get(url, params=value, auth=(user, pasw))
    dict = r.json()
    print("{}".format(dict.get('id')))
