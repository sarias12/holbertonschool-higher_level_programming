#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        character = "None"
    else:
        character = sentence[:1]
    my_tuple = (length, character)
    return my_tuple
