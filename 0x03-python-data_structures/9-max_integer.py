#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)
    else:
        max_value = my_list[0]
        for k in range(len(my_list)):
            if my_list[k] > max_value:
                max_value = my_list[k]
        return (max_value)
