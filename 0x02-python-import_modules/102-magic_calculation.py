#!/usr/bin/python3

def magic_calculation(a, b):
    try:
        from magic_calculation_102 import add, sub
    except ImportError:
        print("Error: Unable to import necessary functions.")
        return None

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

result = magic_calculation(10, 5)
print("Result:", result)

