#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    num = 0
    x = 0

    for tupl in my_list:
        num += tupl[0] * tupl[1]
        x += tupl[1]
        
        return (num / x)
