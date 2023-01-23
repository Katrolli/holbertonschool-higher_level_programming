#!/usr/bin/python3
def number_keys(a_dictionary):
    total = 0
    if len(a_dictionary) == 0:
        return 0
    for i, smth in enumerate(a_dictionary):
        total = i
    if total != 0:
        return total + 1
    else:
        return 1
