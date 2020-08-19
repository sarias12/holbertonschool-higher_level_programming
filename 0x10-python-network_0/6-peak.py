#!/usr/bin/python3
"""Task 6"""


def find_peak(list_of_integers):
    """"Check if it's a peak"""
    if len(list_of_integers) == 0:
        return None
    lt = list_of_integers
    start = 1
    end = len(lt) - 1
    peak = lt[0]
    while start < end:
        if lt[start] > lt[start - 1] and lt[start] > lt[start + 1]:
            peak = lt[start]
            start += 1
        else:
            start += 1
    return peak
