#!/usr/bin/env python3


def print_last_digit(number):
    if number < 0:
        print("{}".format((number * -1) % 10), end="")
        return (number * -1) % 10

    print("{}".format(number % 10), end="")
    return number % 10