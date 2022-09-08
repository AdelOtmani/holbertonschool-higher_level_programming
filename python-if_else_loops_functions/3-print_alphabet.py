#!/usr/bin/python3
for i in range(97, 123):
    if (chr(i) == 'e' or chr(i) == 'q'):
        i = i + 1
    else:
        print("{:c}".format(i), end='')
        i = i + 1
