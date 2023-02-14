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
        '''obj saved to json file'''
        ls = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for item in list_objs:
                ls.append(item.to_dictionary())
        with open(file_name, "w", encoding="utf-8") as n_file:
            n_file.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        '''json to obj'''
        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Create new instance'''
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(3, 2)
        elif cls.__name__ == "Square":
            dummy_inst = cls(3)
        dummy_inst.update(**dictionary)
        return dummy_inst
