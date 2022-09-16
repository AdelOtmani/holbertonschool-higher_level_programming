#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    i = 0
    s = ''
    while i < x:
        try:
            s += "{:d}".format(my_list[i])
            c += 1
        except IndexError as e:
            print(s, end="")
            raise (e)
        except Exception as e:
            pass
        i += 1
    print(s)
    return c
