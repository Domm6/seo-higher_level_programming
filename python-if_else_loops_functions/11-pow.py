#!/usr/bin/python3
def pow(a, b):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = a
        for _ in range(b - 1):
            result *= a
        return result
    else:
        result = 1 / a
        for _ in range(-b - 1):
            result /= a
        return result
