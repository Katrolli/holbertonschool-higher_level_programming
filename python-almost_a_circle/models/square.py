#!/usr/bin/python3
'''Module of Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Sqaure class inherits from rect'''
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        error_raise(width=size, height=size, x=x, y=y)
