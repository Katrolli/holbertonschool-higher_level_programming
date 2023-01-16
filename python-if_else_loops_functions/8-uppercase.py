#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char_new in str:
        if ord(char_new) >= 97 and ord(char_new) <= 122:
            new_str += chr(ord(char_new) - 32)
        else:
            new_str += char_new
    print("{}".format(new_str))
