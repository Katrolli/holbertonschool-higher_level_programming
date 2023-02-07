#!/usr/bin/python3
'''Json Module'''
import json


def save_to_json_file(my_obj, filename):
    ''' Function that writes to file as json format'''
    with open(filename, 'w', encoding="utf-8") as a_file:
        return json.dump(my_obj, a_file)
