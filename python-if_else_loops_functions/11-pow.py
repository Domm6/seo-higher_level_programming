#!/usr/bin/python3
def pow(a, b):
    num = a
    for i in range(b - 1):
      num *= a
    print(num)
    return num
