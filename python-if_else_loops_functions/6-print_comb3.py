#!/usr/bin/python3
newline = '\n'
for d in range(10):
    for u in range(d + 1, 10):
        print("{}{}".format(d, u), end="")
        if ((d*10) + u) != 89:
            print(", ", end="")
print("")
