#!/usr/bin/python3
''' Module that reads from file'''


def read_file(filename=""):
    ''' Function that reads from file and prints content'''
    with open(filename, 'r', encoding="utf-8") as a_file:
        read = a_file.read()
        print(read, end="")
