#!/usr/bin/python3
'''Json module'''
import sys
import json
import os
import os.path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


file_path = os.path.join(os.getcwd(), "add_item.json")
filename = 'add_item.json'
my_list = []

if not os.path.isfile(filename):
    with open(filename, 'w', encoding="utf-8") as a_file:
        a_file.write("")
for i in range(len(sys.argv)):
    if i > 0:
        my_list.append(sys.argv[i])
        i += 1
    i += 1
with open(filename, 'w', encoding="utf-8") as a_file:
    a_file.write("")

save_to_json_file(my_list, file_path)
new_list = load_from_json_file(file_path)
