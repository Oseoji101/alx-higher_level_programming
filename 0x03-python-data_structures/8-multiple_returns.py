#!/usr/bin/python3

def multiple_returns(sentence):

    if len(sentence) == 0:
        result = 0, None
    else:
        result = len(sentence), sentence[0]
    return (result)
