#!/usr/bin/python3
"""
    script that adds all arguments to
    a Python list, and then save them to a file:
"""
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    list_n = load_from_json_file(filename)
except:
    list_n = []

for i in argv[1:]:
    list_n.append(i)

save_to_json_file(list_n, filename)
