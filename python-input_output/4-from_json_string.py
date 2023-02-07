#!/usr/bin/python3
''' Json module'''
import json


def from_json_string(my_str):
    '''Function that converts json str to python type'''
    a_type = json.loads(my_str)
    return a_type
