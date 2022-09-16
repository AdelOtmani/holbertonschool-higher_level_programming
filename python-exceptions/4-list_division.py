#!/usr/bin/python3
from decimal import DivisionByZero
from hashlib import new


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            new_list.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError as e:
            new_list.append(0)
            print("division by 0")
        except IndexError as e:
            new_list.append(0)
            print("out of range")
        except TypeError as e:
            new_list.append(0)
            print("wrong type")
        finally:
            i += 1
    return new_list
