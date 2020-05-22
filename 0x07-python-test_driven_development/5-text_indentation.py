#!/usr/bin/python3
""" Contains one func """


def text_indentation(text):
    """ Prints the given text with double spacing """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    printed = ""

    letter = 0
    while (letter < len(text)):

        if (text[letter] in "." or text[letter] in "?" or text[letter] in ":"):
            printed += text[letter] + "\n\n"
        elif (text[letter] is " "):
            if (printed[-1] is not "\n"):
                printed += " "
        else:
            printed += text[letter]

        letter += 1

    print(printed, end="")
