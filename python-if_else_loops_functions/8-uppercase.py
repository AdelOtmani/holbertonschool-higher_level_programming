#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            str[i] = str(i + 32)
            i = i + 1
        else:
            i = i + 1
    print("{:c}".format(str))
