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

    '''getter of size'''
    @property
    def size(self):
        return self.__size

    '''change size function'''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    '''returning area of square '''
    def area(self):
        return self.__size ** 2

    '''print size of square as #'''
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if j + 1 == self.__size:
                    print("#")
                else:
                    print("#", end='')
        if self.__size == 0:
            print()
