#!/usr/bin/python3
def uppercase(string):
    uppercase_str = ""
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}".format(uppercase_str))
