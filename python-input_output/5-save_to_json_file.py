#!/usr/bin/python3
'''Json Module'''
import json


def save_to_json_file(my_obj, filename):
    ''' Function that writes to file as json format'''
    my_obj = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as a_file:
        write = a_file.write(my_obj)
    return write
