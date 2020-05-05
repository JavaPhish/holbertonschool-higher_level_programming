#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    val1 = 0
    val2 = 0
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if len(tuple_a) > 1:
        val1 = val1 + tuple_a[0]
        val2 = val2 + tuple_a[1]
    elif (len(tuple_a) is 1):
        val1 = val1 + tuple_a[0]
    if (len(tuple_b) > 1):
        val1 = val1 + tuple_b[0]
        val2 = val2 + tuple_b[1]
    elif (len(tuple_b) is 1):
        val1 = val1 + tuple_a[0]

    return (val1, val2)
