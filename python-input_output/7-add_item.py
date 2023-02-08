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
tmp_list = []

for i in range(len(sys.argv)):
    if i > 0:
        my_list.append(sys.argv[i])
        i += 1
    i += 1
if not os.path.isfile(filename):
    with open(filename, 'w', encoding="utf-8") as a_file:
        save_to_json_file(my_list, file_path)

with open('add_item.json', 'r', encoding="utf-8") as a_file:
    content = json.load(a_file)
    tmp_list = list(content)
    for item in my_list:
        if item not in tmp_list:
            tmp_list.append(item)

save_to_json_file(tmp_list, filename)
new_list = load_from_json_file(filename)
