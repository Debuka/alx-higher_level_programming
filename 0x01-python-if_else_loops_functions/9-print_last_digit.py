#!/usr/bin/python3
#Prints last digits of a number
def print_last_digit(number):
    ls_dt = abs(number) % 10
    print(ls_dt, end="")
    return ls_dt

