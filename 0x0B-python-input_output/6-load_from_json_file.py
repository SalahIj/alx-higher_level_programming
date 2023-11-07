#!/usr/bin/python3
""" The module imported """
import json


def load_from_json_file(filename):
    """ The function defintion """
    with open(filename, 'r', encoding="utf-8") as File:
        Strin = json.load(File)
        return (Strin)
