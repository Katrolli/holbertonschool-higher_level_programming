#!/usr/bin/python3
'''Module for checking instance'''


def is_same_class(obj, a_class):
    ''' Function that checks if obj is an instance of a class'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
