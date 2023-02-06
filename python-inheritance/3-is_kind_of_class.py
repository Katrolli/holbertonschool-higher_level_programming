#!/usr/bin/python3
'''Module that checks if obj is a class'''


def is_kind_of_class(obj, a_class):
    ''' Function that checks instance'''
    if isinstance(obj, a_class):
        return True
    return False
