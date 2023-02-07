#!/usr/bin/python3
""" Module that inverts comparison operators"""


class MyInt(int):
    ''' Rebel Class '''
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if self.x == other:
            return False

    def __ne__(self, other):
        if self.x == other:
            return True
