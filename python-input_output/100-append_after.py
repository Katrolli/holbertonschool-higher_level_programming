#!/usr/bin/python3
'''append func'''


def append_after(filename="", search_string="", new_string=""):
    '''Search file and add line'''
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string)
    with open(filename, 'w') as file:
        for line in lines:
            file.writelines(line)
