#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, ) * (2 - len(tuple_a))
    tuple_b += (0, ) * (2 - len(tuple_b))
    r = (map(lambda a, b: a + b, tuple_a, tuple_b))
    return (tuple(r))
