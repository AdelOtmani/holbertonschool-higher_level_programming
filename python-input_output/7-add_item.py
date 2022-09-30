#!/usr/bin/python3
"""Exercice 7 project holberton Adel Otmani
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    myList = load_from_json_file("add_item.json")
except ValueError:
    myList = []

save_to_json_file(myList + sys.argv[1:], "add_item.json")
