#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dire = a_dictionary.copy()
    keys = list(dire.keys())

    for i in keys:
        dire[i] *= 2

    return dire
