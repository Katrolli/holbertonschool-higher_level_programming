#!/usr/bin/python3
"""square module with size"""


class Square:
    '''init function with size 0'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

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
        if self.__size == 0:
            print()
            return
        for new_line in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for space in range(self.position[0]):
                print(' ', end='')
            for j in range(self.__size):
                if j + 1 == self.__size:
                    print("#")
                else:
                    print("#", end='')

    '''getter of position'''
    @property
    def position(self):
        return self.__position

    '''setter of position'''
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
