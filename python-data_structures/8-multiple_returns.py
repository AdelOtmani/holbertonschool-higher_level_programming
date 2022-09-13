#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if sentence == "":
        return ((n, None))
    else:
        m = sentence[0]
        t = (n, m)
        return (t)
