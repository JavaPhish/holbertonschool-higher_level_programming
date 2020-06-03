#!/usr/bin/python3
""" Inherets from list """


class MyList(list):
    """ Inherets from list """

    def print_sorted(self):
        """ Prints a list in ascending order """

        print(sorted(self))
