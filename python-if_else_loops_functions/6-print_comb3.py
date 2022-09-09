#!/usr/bin/python3
newline = '\n'
for d in range(10):
    for u in range(d + 1, 10):
        print("{}{}".format(d, u), end="")
        if d != 8 and u != 9:
            print(", ", end="")
