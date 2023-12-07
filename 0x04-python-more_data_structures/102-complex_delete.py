#!/usr/bin/python3
# a function that deletes keys with a specific value in a dict.
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for val_dictionary in list_keys:
        if value == a_dictionary.get(val_dictionary):
            del a_dictionary[val_dictionary]

    return (a_dictionary)
