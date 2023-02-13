#!/usr/bin/python3
'''Module of Rectangle class'''
from models.base import Base


def error_raise(**kwargs):
    '''Function that handles error raising'''
    for key, value in kwargs.items():
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(key))
        if key in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(key))
        if key in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(key))


class Rectangle(Base):
    '''Rectangle class inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        error_raise(width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        error_raise(width=width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        error_raise(height=height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        error_raise(x=x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        error_raise(y=y)
        self.__y = y
