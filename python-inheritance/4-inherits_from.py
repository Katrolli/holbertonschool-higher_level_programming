#!/usr/bin/python3
'''Module that checks if obj has inherited from class'''


def inherits_from(obj, a_class):
    '''if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
