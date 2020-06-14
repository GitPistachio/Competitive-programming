# Project name : CodeChef: CF224 - Polygon
# Link         : https://www.codechef.com/problems/CF224
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-14
# Description  :
# Status       : Accepted (34348809)
# Tags         : python, convex hull, points orientation, Andrew's monotone chain convex hull algorithm, perimeter of a convex polygon, distance between two points
# Comment      : 

from sys import stdin, stdout
from math import sqrt


class Point:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return self.__repr__()

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True

        return False


def vec(a, b):
    return Point(b.x - a.x, b.y - a.y)


def cross(u, v):
    return u.x*v.y - u.y*v.x


def orient(o, a, b):
    return cross(vec(o, a), vec(o, b))


def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)


def getConvexHull(points):
    lower = []
    for p in points:
        while len(lower) >= 2 and sign(orient(lower[-2], lower[-1], p)) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and sign(orient(upper[-2], upper[-1], p)) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def dist(a, b):
    return sqrt((b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y))


def convexPolygonPerimeter(polygon_vertices):
    if len(polygon_vertices) <= 1:
        return 0

    last_p = polygon_vertices[-1]
    perimeter = 0
    for p in polygon_vertices:
        perimeter += dist(last_p, p)
        last_p = p

    return perimeter


no_of_points = int(stdin.readline())
points = sorted([Point(*map(int, stdin.readline().split())) for _ in range(no_of_points)])
convex_hull = getConvexHull(points)
perimeter = convexPolygonPerimeter(convex_hull)
stdout.write('{:.1f}\n'.format(perimeter))
