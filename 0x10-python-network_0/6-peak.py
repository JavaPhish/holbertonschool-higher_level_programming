#!/usr/bin/python3
""" Finds the peak of a list """


def find_peak(list_of_integers):
    """ Find the peak """
    highest = None
    for num in list_of_integers:
        if highest is None or num > highest:
            highest = num

    return highest
