#!/usr/bin/python3
# Function that finds the biggest integer of a list
def max_integer(my_list=[]):
    if len(my_list) == "":
        return (none)

    max_val = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > max_val:
            max_val = my_list[j]
            return (max_val)
