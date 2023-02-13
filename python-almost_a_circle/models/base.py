#!/usr/bin/python3
'''Base class module'''


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method that converts to json'''
        string = "[]"
        if list_dictionaries is None:
            return string
        return json.dumps(list_dictionaries)
