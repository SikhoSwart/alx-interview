#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    """
    lst = []
    if n <= 0:
        return lst
    lst = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(lst[i - 1]) - 1):
            current = lst[i - 1]
            temp.append(lst[i - 1][j] + lst[i - 1][j + 1])
        temp.append(1)
        lst.append(temp)
    return lst
