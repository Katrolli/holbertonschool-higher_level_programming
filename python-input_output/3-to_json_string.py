#!/usr/bin/python3
import json
'''Module that prints in json format'''


def to_json_string(my_obj):
    ''' prints the class of the obj and the obj as str'''
    return json.dumps(my_obj)
