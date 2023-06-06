#!/usr/bin/python3
def pow(a, b):
    i = 1
    pow = 1
    if b > 0:
        while i <= b:
            pow = pow*a
            i += 1
    elif b == 0:
        pow = 1
    else:
        b = b * -1
        while i <= b:
            pow = pow/a
            i += 1
    return pow
