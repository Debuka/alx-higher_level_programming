#!/usr/bin/python3
#Adds 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    outcome = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (outcome)
