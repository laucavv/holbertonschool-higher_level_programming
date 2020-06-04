#!/usr/bin/python3
"""
    function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ funtion """
    with open(filename, mode="w", encoding="utf-8") as file:
        obj_j = json.dumps(my_obj)
        file.write(obj_j)
    return file
