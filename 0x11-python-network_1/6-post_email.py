#!/usr/bin/python3
""" Requests stuff """


import requests
import sys

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data)
    print(r.text)
