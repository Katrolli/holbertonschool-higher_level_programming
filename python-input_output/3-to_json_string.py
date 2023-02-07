#!/usr/bin/python3
'''Module that prints in json format'''
import json


def to_json_string(my_obj):
    ''' prints the class of the obj and the obj as str'''
    return json.dumps(my_obj)
