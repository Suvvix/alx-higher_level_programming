#!/usr/bin/python3
def no_c(my_string):
    returnal = ""
    for x in my_string:
        if x != "c" and x != "C":
            returnal += x
    return returnal
