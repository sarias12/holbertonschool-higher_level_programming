#!/usr/bin/python3
"""Task 6"""


def find_peak(list_of_integers):
    """"Check if it's a peak"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
