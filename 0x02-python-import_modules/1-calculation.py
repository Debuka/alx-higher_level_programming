#!/usr/bin/python3
"""tthis programs imports function and those some maths,
then prints the result"""
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, div(a, b)))
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))

