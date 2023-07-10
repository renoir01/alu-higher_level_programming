#!/usr/bin/python3

def uppercase(string):
    result = ''
    for char in string:
        ascii_value = ord(char)
        uppercase_char = chr(ascii_value - 32) if 97 <= ascii_value <= 122 else char
        result += uppercase_char
    print("{0:s}\n".format(result), end='')
