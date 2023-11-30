#!/usr/bin/python3

if __name__ == "__main__":
    """print the addition of all args"""
    import sys

    argv = sys.argv
    a = len(argv) - 1
    add = 0
    if a == 0:
        print(add)
    else:
        for i in range(1, len(argv)):
            add += int(argv[i])
        print(add)
