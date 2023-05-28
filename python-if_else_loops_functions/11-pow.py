#!/usr/bin/python3
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = base
        for _ in range(exponent - 1):
            result *= base
        return result
    else:
        result = 1 / base
        for _ in range(-exponent - 1):
            result /= base
        return result
