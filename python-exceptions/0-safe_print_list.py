#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    s = ''
    while c < x:
        try:
            s += str(my_list[c])
            c += 1
        except Exception as e:
            break
    print(s)
    return c
