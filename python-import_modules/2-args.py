#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = len(sys.argv) - 1

    if av == 0:
        print("0 argument.")
    elif av == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(av))
    for j in range(1, av):
        print("{}: {:s}".format(j + 1, sys.argv[j + 1]))
