#!/usr/bin/python3
'''Json module'''
import json


def load_from_json_file(filename):
    ''' Function that creates object from json file'''
    with open(filename, "r", encoding="utf-8") as a_file:
        read = a_file.read()
    return json.loads(read)
