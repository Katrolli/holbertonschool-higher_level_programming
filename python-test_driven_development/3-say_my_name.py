#!/usr/bin/python3

'''function that prints first and last name as string'''


def say_my_name(first_name, last_name=""):
    '''this is a documented function'''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
