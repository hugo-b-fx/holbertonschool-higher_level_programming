#!/usr/bin/python3
"""
writes an object to a txt file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
