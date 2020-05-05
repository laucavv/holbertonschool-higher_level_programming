#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if sentence:
        first_sen = sentence[0]
    else:
        first_sen = None
    tup = (len_sen, first_sen)
    return (tup)
