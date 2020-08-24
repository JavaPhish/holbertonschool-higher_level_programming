#!/usr/bin/python3
""" Requests stuff """


import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        r = response.info()
        print(r.get('X-Request-Id'))
