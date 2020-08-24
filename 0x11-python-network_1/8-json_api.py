#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        dict = r.json()
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dict['id'], dict['name']))
    except ValueError:
        print("Not a valid JSON")
