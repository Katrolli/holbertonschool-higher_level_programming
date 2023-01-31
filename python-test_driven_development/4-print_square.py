#!/usr/bin/python3

'''function that prints a square of size "size"'''

def print_square(size):
    ''' checking possibile cases'''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            if j + 1 == size:
                print('#')
            else:
                print('#', end="")
