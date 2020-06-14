# Project name : SPOJ: INOROUT - Inside or outside
# Link         : https://www.spoj.com/problems/INOROUT/
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-13
# Description  :
# Status       : Accepted (26138380)
# Tags         : python, convex polygon, point in convex polygon, points orientation
# Comment      : 

from sys import stdin, stdout


class Point:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return self.__repr__()


def vec(a, b):
    return Point(b.x - a.x, b.y - a.y)


def cross(u, v):
    return u.x*v.y - u.y*v.x


def orient(o, a, b):
    return cross(vec(o, a), vec(o, b))


def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)


def isPointInsideConvexPolygon(p, points):
    side = None
    p1 = points[-1]
    for p2 in points:
        so = sign(orient(p1, p2, p))
        if so != 0:
            if side is None:
                side = so
            elif side != so:
                return False
        p1 = p2

    return True


n, q = map(int, stdin.readline().split())
coordinates = stdin.readline().split()
points = [Point(int(coordinates[i]), int(coordinates[i + 1])) for i in range(0, 2*n, 2)]
for _ in range(q):
    p = Point(*map(int, stdin.readline().split()))
    if isPointInsideConvexPolygon(p, points):
        stdout.write("D\n")
    else:
        stdout.write("F\n")
