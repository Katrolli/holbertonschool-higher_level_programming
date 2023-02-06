#!/usr/bin/python3
'''Module of rectangle class'''


class Rectangle(BaseGeometry):
    ''' Rectangle class'''
    def __init__(self, width, height):
        # self.integer_validator("width", width)
        self.__width = width
        # self.integer_validator("height", height)
        self.__height = height
