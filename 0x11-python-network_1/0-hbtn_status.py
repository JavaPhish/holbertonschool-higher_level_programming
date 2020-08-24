#!/usr/bin/python3
""" Requests stuff """


import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print("Body response:")
        print("    - type: {}".format(type(response.read())))
        print("    - content: {}".format(r))
        print("    - utf8 content: {}".format(r.decode('utf-8')))
