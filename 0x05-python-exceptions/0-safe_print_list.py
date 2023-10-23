#!/usr/bin/python3

def safe_print_list(my_list=[],x=0):
    a = 0
    for item in my_list[]:
        try:
            print("{}".format(my_list[item]), end=" ")
            x += 1
        except IndexError:
            pass
    print()
    return a

