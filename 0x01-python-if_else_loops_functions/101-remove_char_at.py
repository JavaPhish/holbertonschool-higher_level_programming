#!/usr/bin/env python3


def remove_char_at(str, n):
    new_arr = ""

    for i in range(0, len(str)):
        if i is not n:
            new_arr = new_arr + str[i]

    return new_arr
