#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        result = a
        for _ in range(b - 1):
            result *= a
        return result
    else:
        result = 1 / a
        for _ in range(-b - 1):
            result /= a
        return '{:.19f}'.format(result)
