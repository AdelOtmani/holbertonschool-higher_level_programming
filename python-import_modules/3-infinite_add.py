#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = len(sys.argv) - 1
    r = 0
    for i in range(av):
        r += int(sys.argv[i + 1])
    print("{}".format(r))
