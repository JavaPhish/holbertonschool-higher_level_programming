#!/usr/bin/python3
""" Inherets from list """


class MyList(list):
    """ Inherets from list """

    def print_sorted(self):
        """ Prints a list in ascending order """

        newlist = []
        for l_i in self:
            newlist.append(l_i)
        newlist.sort()
        print(newlist)
