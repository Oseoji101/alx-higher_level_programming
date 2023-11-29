#!/usr/bin/python3
for i in range(122, 96, -1):
    count = i
    if i % 2 != 0:
        count = count - 32
    print("{:c}".format(count), end="")
