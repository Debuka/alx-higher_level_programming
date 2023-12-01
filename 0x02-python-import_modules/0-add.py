#!/usr/bin/python3
#imports add function simple maths
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    outcome = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, outcome))
