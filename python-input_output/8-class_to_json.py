#!/usr/bin/python3

def class_to_json(obj):
    '''Function that retuns new dict based on obj values'''
    dic = {}
    for key, value in obj.__dict__.items():
        dic[key] = obj.__dict__[key]
    return dic
