#!/usr/bin/python3
""" The module imported """
import json


def save_to_json_file(my_obj, filename):
    """ The function definition """
    text = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
