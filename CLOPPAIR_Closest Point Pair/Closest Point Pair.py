# Project name : SPOJ: CLOPPAIR - Closest point problem
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23369275)
# Tags         : python
# Comment      : O(N Log N). Accepted using PYPY.

import sys

class Point:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x)*(self.x - p.x) + (self.y - p.y)*(self.y - p.y))**0.5

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

n = int(raw_input())

points = []
for i in xrange(n):
    x, y = raw_input().split()
    points.append(Point(i, int(x), int(y)))

points.sort(key=lambda x: x.x)

box = {points[0]}

h = sys.float_info.max
j = 0
a = None
b = None
for i in xrange(1, n):
    while j < i and points[i].x - points[j].x > h:
        if points[j] in box:
            box.remove(points[j])
        j += 1
    for p in tuple(box):
        if abs(points[i].y - p.y) < h:
            dist = p.dist(points[i])
            if dist < h:
                h = dist
                a = p.i
                b = points[i].i

    box.add(points[i])

if a > b:
    a, b = b, a

print(str(a) + ' ' + str(b) + ' %.6f' % round(h,6))
