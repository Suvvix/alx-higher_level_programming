#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_ord = list(a_dictionary.keys())
    keys_ord.sort()
    for i in keys_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
