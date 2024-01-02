#!/usr/bin/python3
'''module that is used for working with Pascal's triangle.
'''


def pascal_triangle(x):
    '''Creates a list of lists of integers
    '''
    triangle = []
    if type(x) is not int or x <= 0:
        return triangle
    for a in range(x):
        line = []
        for c in range(a + 1):
            if c == 0 or c == a:
                line.append(1)
            elif a > 0 and c > 0:
                line.append(triangle[a - 1][c - 1] + triangle[a - 1][c])
        triangle.append(line)
    return triangle
