#!/usr/bin/python3

def max_integer(my_list=[]):
    notValid = my_list is None or len(my_list) == 0
    if notValid:
        return
    maxNum = my_list[0]
    for i in my_list:
        if i > maxNum:
            maxNum = i
    return maxNum
