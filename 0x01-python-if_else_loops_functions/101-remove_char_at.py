#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        cp_str = str[:n] + str[n + 1:]
        return cp_str
    else:
        cp_str = str[:]
        return cp_str
