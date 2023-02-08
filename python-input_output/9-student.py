#!/usr/bin/python3
''' Module of Student class'''


class Student:
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        d = {}
        for key, value in self.__dict__.items():
            d[key] = self.__dict__[key]
        return d
