#!/usr/bin/python3
'''Base class module'''
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        '''tst'''
        new_list = []
        new_file = cls.__name__ + ".json"
        if list_objs is not None:
            for el in list_objs:
                new_list.append(el.to_dictionary())
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))
