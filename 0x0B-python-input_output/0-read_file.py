#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
