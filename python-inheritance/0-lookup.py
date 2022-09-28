#!/usr/bin/python3
""" fonction to look up object's attribut"""


def lookup(obj):
    """return list of attributs"""
    att = dir(obj)
    if hasattr(obj, '__class__'):
        return att
