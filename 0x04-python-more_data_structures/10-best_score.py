#!/usr/bin/python3


def best_score(a_dictionary):
    best = -1
    if a_dictionary is None:
        return None

    for key in a_dictionary.keys():
        if a_dictionary[key] > best:
            best = a_dictionary[key]

    return best
