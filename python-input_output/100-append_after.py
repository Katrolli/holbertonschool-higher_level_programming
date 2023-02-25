#!/usr/bin/python3
'''Function that parses file line per line,
adds new_string is search_string is found'''


def append_after(filename="", search_string="", new_string=""):
    '''Search file and add line'''
    with open(filename, 'r') as file:
        lines = file.readlines()
    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
            i += 1
        i += 1
    with open(filename, 'w') as file:
        for line in lines:
            file.writelines(line)
