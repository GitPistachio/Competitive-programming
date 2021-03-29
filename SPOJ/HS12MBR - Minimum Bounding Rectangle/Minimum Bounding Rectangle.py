# Project name : SPOJ: HS12MBR - Minimum Bounding Rectangle
# Link         : https://www.spoj.com/problems/HS12MBR/
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23286818)
# Tags         : python,  math, geometry, rectangle, gift wrapping algorithm, minimum bounding rectangle, sliding window technique
# Comment      : 100 points

from functools import reduce

def rectangleCoordinates(c1, c2):
    """Get minimum bounding rectangle for two rectangles.
       Args:
           c1 (tuple): cordinates of left top and right bottom corners of first rectangle
           c1 (tuple): cordinates of left top and right bottom corners of second rectangle
       
       Returns:
           tuple: cordinates of left top and right bottom corners of minimum bounding rectangle

    """
    if c1[3] > c2[3]:
        if c1[2] > c2[2]:
            if c1[1] < c2[1]:
                if c1[0] < c2[0]:
                    return (c1[0], c1[1], c1[2], c1[3])
                else:
                    return (c2[0], c1[1], c1[2], c1[3])
            else:
                if c1[0] < c2[0]:
                    return (c1[0], c2[1], c1[2], c1[3])
                else:
                    return (c2[0], c2[1], c1[2], c1[3])
        else:
            if c1[1] < c2[1]:
                if c1[0] < c2[0]:
                    return (c1[0], c1[1], c2[2], c1[3])
                else:
                    return (c2[0], c1[1], c2[2], c1[3])
            else:
                if c1[0] < c2[0]:
                    return (c1[0], c2[1], c2[2], c1[3])
                else:
                    return (c2[0], c2[1], c2[2], c1[3])
    else:
        if c1[2] > c2[2]:
            if c1[1] < c2[1]:
                if c1[0] < c2[0]:
                    return (c1[0], c1[1], c1[2], c2[3])
                else:
                    return (c2[0], c1[1], c1[2], c2[3])
            else:
                if c1[0] < c2[0]:
                    return (c1[0], c2[1], c1[2], c2[3])
                else:
                    return (c2[0], c2[1], c1[2], c2[3])
        else:
            if c1[1] < c2[1]:
                if c1[0] < c2[0]:
                    return (c1[0], c1[1], c2[2], c2[3])
                else:
                    return (c2[0], c1[1], c2[2], c2[3])
            else:
                if c1[0] < c2[0]:
                    return (c1[0], c2[1], c2[2], c2[3])
                else:
                    return (c2[0], c2[1], c2[2], c2[3])

def getCoordinates(p):
    """Get left top and right bottom corner of minimum bounding rectangle."""
    if p[0] == 'p': # minimum bounding rectangle for point
        return (int(p[1]), int(p[2]), int(p[1]), int(p[2]))
    elif p[0] == 'c': # minimum bounding rectangle for circle
        x = int(p[1])
        y = int(p[2])
        r = int(p[3])
        return (x - r, y - r, x + r, y + r)
    elif p[0] == 'l': # minimum bounding rectangle for line segment
        x1 = int(p[1])
        y1 = int(p[2])
        x2 = int(p[3])
        y2 = int(p[4])
        if y2 > y1:
            if x1 < x2:
                return (x1, y1, x2, y2)
            else:
                return (x2, y1, x1, y2)
        else:
            if x1 < x2:
                return (x1, y2, x2, y1)
            else:
                return (x2, y2, x1, y1)

T = int(input())

for t in range(T):
    n = int(input())
    p = reduce(rectangleCoordinates, [getCoordinates(input().split()) for i in range(n)])
    print(p[0], p[1], p[2], p[3])
    if t + 1 < T:
        input()
