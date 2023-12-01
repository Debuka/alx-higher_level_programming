#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

if _ _name_ _ == "_ _main_ _":
    a = 10
    b = 5
    outcome_of_add = add(a, b)
    outcome_of_sub = sub(a, b)
    outcome_of_div = div(a, b)
    outcome_of_mul = mul(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, outcome_of_add))
    print("{:d} - {:d} = {:d}".format(a, b, outcome_of_sub))
    print("{:d} / {:d} = {:d}".format(a, b, outcome_of_div))
    print("{:d} * {:d} = {:d}".format(a, b, outcome_of_mul))

