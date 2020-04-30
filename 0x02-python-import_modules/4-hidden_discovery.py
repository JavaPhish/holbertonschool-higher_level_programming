#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    for i in dir(hidden_4):
        if "__" != i[0:2]:
            print("{}".format(i))
