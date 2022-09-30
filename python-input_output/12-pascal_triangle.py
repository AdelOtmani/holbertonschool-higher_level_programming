#!/usr/bin/python3
"""Exercice 12 project holberton Adel Otmani
"""


def pascal_triangle(n):
    """12. Pascal's Triangle

    Args:
        n (_type_): object
    """
    if n <= 0:
        return []
    res = []
    l = []
    for i in range(n):
        c = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                c.append(1)
            else:
                c.append(l[j] + l[j - 1])
        l = c
        res.append(c)
    return res
