#!/usr/bin/python3
""" Requests stuff """


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    email = sys.argv[2]
    url = sys.argv[1]

    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
