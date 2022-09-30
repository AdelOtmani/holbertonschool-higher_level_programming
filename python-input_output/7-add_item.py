#!/usr/bin/python3
""" Exercice 7 projet holberton Adel Otmani.

"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

obj = []
obj = load_from_json_file("add_item.json")
obj.extend(sys.argv[1:])
save_to_json_file(obj, "add_item.json")
