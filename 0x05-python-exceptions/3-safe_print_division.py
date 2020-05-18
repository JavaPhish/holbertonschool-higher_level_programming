#!/usr/bin/python3


def safe_print_division(a, b):
    diff_a = 0
    try:
        diff_a = a / b
    except:
        diff_a = None
    finally:
        print("Inside result: {}".format(diff_a))
        return diff_a
