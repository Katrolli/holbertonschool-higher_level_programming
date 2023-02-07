#!/usr/bin/python3
''' Module that appends text to file'''


def append_write(filename="", text=""):
    ''' Function that appends text to filename'''
    with open(filename, "a", encoding="utf-8") as a_file:
        append = a_file.write(text)
    return append
