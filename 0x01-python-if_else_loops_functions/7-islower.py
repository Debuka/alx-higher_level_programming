#!/usr/bin/python3
"""This program checks for lowercase characters"""
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

