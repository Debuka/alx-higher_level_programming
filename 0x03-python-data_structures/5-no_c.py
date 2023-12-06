#!/usr/bin/python3
''' Function that removes all
characters c and C from a string'''
def no_c(my_string):
    nw_list = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(nw_list))

