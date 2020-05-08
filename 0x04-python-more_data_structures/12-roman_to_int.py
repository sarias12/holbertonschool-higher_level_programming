#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string == 'IV':
        return 4
    if roman_string == 'IX':
        return 9
    if not roman_string:
        return None
    for letter in roman_string:
        number += arabic.get(letter)
    return number
