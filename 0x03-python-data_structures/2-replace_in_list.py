#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    notValid = idx < 0 or idx >= len(my_list)
    if notValid:
        return my_list
    my_list[idx] = element
    return my_list
