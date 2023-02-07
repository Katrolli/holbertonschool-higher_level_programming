#!/usr/bin/python3
''' Module that writes to a file'''


def write_file(filename="", text=""):
    ''' Functiont that writes string to  filename'''
    with open(filename, "w", encoding="utf-8") as a_file:
        write = a_file.write(text)
    return write
