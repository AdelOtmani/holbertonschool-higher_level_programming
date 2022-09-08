#!/usr/bin/python3
newline = '\n'
for i in range(00, 100):
    print("{:02d}".format(i)+f"{', ' if i < 99 else newline}", end="")
    i = i + 1
