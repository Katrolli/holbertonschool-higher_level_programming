#!/usr/bin/python3
''' function that prints formated text'''


def text_indentation(text):
    ''' checking possibile cases'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print('\n')
            while text[i + 1] == ' ':
                # print("blank")
                i += 1
        i += 1
