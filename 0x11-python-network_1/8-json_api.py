#!/usr/bin/python3
""" Requests stuff """


import requests
import sys

if __name__ == '__main__':

    input = ""
    if len(sys.argv) > 1:
        input = sys.argv[1]

    data = {'q': input}
    ip = 'http://0.0.0.0:5000/search_user'

    r = requests.post(ip, data)

    id = r.json().get('id')
    name = r.json().get('name')

    if (id is not None and name is not None):
        print('[{}] <{}>'.format(id, name))
    else:
        print('No result')
