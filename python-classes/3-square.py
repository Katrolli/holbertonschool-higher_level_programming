#!/usr/bin/python3
"""square module with size"""


class Square:
    '''init function with size 0'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    '''returning area of square '''
    def area(self):
        return self.__size ** 2
