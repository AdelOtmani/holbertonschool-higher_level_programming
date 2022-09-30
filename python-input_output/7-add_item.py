#!/usr/bin/python3
"""Exercice 7 project holberton Adel Otmani
"""
import sys
import json
from os import path
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = (
        __import__('6-load_from_json_file').load_from_json_file)

if not path.exists("add_item.json"):
    with open("add_item.json", 'a+', encoding="utf-8") as Myfile:
        Myfile.write(json.dumps([]))

myList = load_from_json_file("add_item.json")
myList.extend(sys.argv[1:])
save_to_json_file(myList, "add_item.json")
