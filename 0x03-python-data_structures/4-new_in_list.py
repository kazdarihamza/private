#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx > (len(my_list) - 1) or idx < 0:
            return my_list
    new_list = [x for x in my_list]
    new_list[idx] = element
    return new_list
