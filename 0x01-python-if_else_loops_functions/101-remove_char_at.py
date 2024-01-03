#!/usr/bin/python3
def remove_char_at(str, n):
    cstr = ""
    for x, c in enumerate(str):
        if x != n:
            cstr += c
    return cstr
