#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    tmp = my_list[0]
    for i in my_list:
        if i > tmp:
            tmp = i
    return (tmp)


list = []
max_value = max_integer(list)
print("Max: {}".format(max_value))
