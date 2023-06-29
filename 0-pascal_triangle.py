#!/usr/bin/python3
<<<<<<< HEAD
"""returns a pascal triangle"""


def pascal_triangle(n):
    """
    returns a list of integers in a pascal triangle format
    """

    if n <= 0:
        # return empty list
        return []
    pascal = [[1]]
    if n == 1:
        return pascal

    for i in range(1, n):
        left = -1
        right = 0
        in_pas = []
        for j in range(i + 1):
            num = 0 
            if left > -1:
                num += pascal[i - 1][left]
            if right < i:
                num += pascal[i - 1][right]
            left += 1
            right += 1
            in_pas.append(num)
        pascal.append(in_pas)
    return pascal
=======
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
>>>>>>> c46a1f3487e32d08e94d7a0aa37923ea8f7be2d5
