#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            str[i] = chr(ord(i) + 32)
    print("{:c}".format(str))
