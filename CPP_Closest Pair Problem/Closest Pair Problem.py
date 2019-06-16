# Project name : SPOJ: CPP - Closest pair problem
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-02-09
# Description  :
# Status       : Accepted 100 (23199333)
# Tags         : python, point, linear geometry, distance between points
# Comment      :

import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x)*(self.x - p.x) + (self.y - p.y)*(self.y - p.y))**0.5

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

n = int(input())

points = []
for i in range(n):
    x, y = input().split()
    points.append(Point(int(x), int(y)))

points.sort(key=lambda x: x.x)
box = {points[0]}

h = sys.float_info.max
j = 0
for i in range(1, n):
    while j < i and points[i].x - points[j].x > h:
        if points[j] in box:
            box.remove(points[j])
        j += 1
    for p in tuple(box):
        if abs(points[i].y - p.y) < h:
            h = min(h, p.dist(points[i]))
    box.add(points[i])

print('%.6f' % h)
