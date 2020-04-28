#!/usr/bin/python3


def uppercase(str):
    LOUD_STR = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            LOUD_STR = LOUD_STR + chr(ord(i) - 32)
        else:
            LOUD_STR = LOUD_STR + i
    print("{}".format(LOUD_STR))
