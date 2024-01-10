#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    x = 0

    for i in uniqlist:
        x += i

    return (x)
