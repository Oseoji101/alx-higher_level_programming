if __name__ == "__main__":
    """print the num and list of arguments."""
    import sys

    argv = sys.argv
    a = len(argv) - 1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("{} argument:".format(a))
        print("{}: {}".format(a, argv[a]))
    else:
        print("{} arguments:".format(a))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
