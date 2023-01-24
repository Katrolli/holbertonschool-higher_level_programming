#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    values = list(a_dictionary.values())
    if len(values) == 0:
        return None
    for i, nr in enumerate(values):
        if nr > max:
            max = nr
    key_list = list(a_dictionary.keys())
    position = values.index(max)
    return key_list[position]
