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

    def area(self):
        '''module that returns the area of obj'''
        return self.__width * self.__height

    def display(self):
        '''module that prints height and width'''
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                if j != self.__width - 1:
                    print("#", end="")
            print("#")

    def __str__(self):
        '''Change the represtantion of str'''
        rep = "[Rectangle]"
        rep += " ({})".format(self.id)
        rep += " {}/{}".format(self.__x, self.__y)
        rep += " - "
        rep += "{}/{}".format(self.__width, self.__height)
        return rep

    def update(self, *args, **kwargs):
        '''Update values of obj'''
        ls = []
        for i in self.__dict__.keys():
            ls.append(i)
        if len(args) != 0:
            for i in self.__dict__.keys():
                ls.append(i)
            for i in range(len(args)):
                self.__dict__[ls[i]] = args[i]
        else:
            for key, value in kwargs.item():
                for attr in ls:
                    if key == 'id':
                        self.__dict__[key] = value
                    elif key != 'id' and key in attr:
                        self.__dict[attr] = value
