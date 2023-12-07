#!/usr/bin/python3
""" Function that returns a list with it's values
multiplied without using a loop"""
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
