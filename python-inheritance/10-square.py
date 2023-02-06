#!/usr/bin/python3
'''Importing Rectangle module'''
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    ''' new square class that inherits from rectangle'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}.".format(self.__size, self.__size)