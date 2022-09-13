#!/usr/bin/python3
def max_integer(my_list=[]):
    tmp = my_list[0]
    if my_list == "":
        return (None)
    for i in my_list:
        if i > tmp:
            tmp = i
    return (tmp)
