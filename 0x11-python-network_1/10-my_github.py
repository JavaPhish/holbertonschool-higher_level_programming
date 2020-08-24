#!/usr/bin/python3
""" Requests stuff """


import requests
import sys

if __name__ == '__main__':

    user = sys.argv[1]
    pas = sys.argv[2]
    data = {'username': user,
            'password': pas}

    url = 'https://api.github.com/user'

    sess = requests.Session()
    sess.auth = (user, pas)

    print(sess.get(url).json().get('id'))
