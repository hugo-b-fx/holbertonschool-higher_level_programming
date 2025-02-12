#!/usr/bin/python3
"""
python list to a json file
"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    name = "add_item.json"

    try:
        ML = load_from_json_file(name)
    except FileNotFoundError:
        ML = []

    ML.extend(sys.argv[1:])
    save_to_json_file(ML, name)
