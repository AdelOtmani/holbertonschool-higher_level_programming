#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    if my_list is None:
        print("", end="")
    else:
        while i < (len(my_list)):
            r = (len(my_list) - 1) - i
            print("{:d}".format(my_list[r]))
            i = i + 1
