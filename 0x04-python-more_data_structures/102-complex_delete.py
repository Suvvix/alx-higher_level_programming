#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for value in keys:
        if value == a_dictionary.get(value):
            del a_dictionary[value]

    return (a_dictionary)
