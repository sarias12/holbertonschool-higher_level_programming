#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or type(roman_string) != str:
        return None
    for letter in roman_string:
        number += arabic.get(letter)
    if roman_string[-2:] == 'IV' or roman_string[-2:] == 'IX':
        number -= 2
    return number
