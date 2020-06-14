# Project name : CodeChef: ECJAN20I - Psertu in Byteland
# Link         : https://www.codechef.com/problems/ECJAN20I
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-13
# Description  :
# Status       : Accepted (34331477)
# Tags         : python, convex hull, point in convex polygon, points orientation, Andrew's monotone chain convex hull algorithm
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


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n, r = map(int, stdin.readline().split())
    poles = sorted([Point(*map(int, stdin.readline().split())) for _ in range(n)])
    fence = getConvexHull(poles)
    if r >= len(fence):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
