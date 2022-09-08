#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        s += c

    print("{}".format(s))
