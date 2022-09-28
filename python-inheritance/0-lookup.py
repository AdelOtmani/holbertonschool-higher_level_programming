#!/usr/bin/python3
def lookup(obj):
    att = dir(obj)
    if hasattr(obj, '__class__'):
        return att
