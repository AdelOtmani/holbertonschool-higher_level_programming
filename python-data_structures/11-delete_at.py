#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    new_list.remove(new_list[idx])
    return (new_list)
