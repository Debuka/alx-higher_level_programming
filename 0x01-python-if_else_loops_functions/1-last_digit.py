#!/usr/bin/python3
""" program that assigns
number at random each timeit executes"""
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end=" ")
if digit > 5:
    print("and greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and less than 6 and not 0")

