#!/usr/bin/python3

def safe_print_list(my_list=[],x=0):
a = 0
    for item in my_list[]:
        try:
            if isinstance(item, (int,str,float,bool,set,dict,list,tuple))
                 print(my_list[i], end=" ")
                x += 1
        except IndexError:
            pass
    print()
    return a

