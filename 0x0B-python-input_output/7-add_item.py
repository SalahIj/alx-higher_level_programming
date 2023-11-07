#!/usr/bin/python3
""" The module imported """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

listarg = list(sys.argv)
try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []

lenght = len(listarg)
if (lenght > 1):
    for i in range(1, lenght):
        data.append(sys.argv[i])
save_to_json_file(data, "add_item.json")
