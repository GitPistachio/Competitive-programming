# Project name : CodeChef: KOL1509 - Save The Trees
# Link         : https://www.codechef.com/problems/KOL1509
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-14
# Description  :
# Status       : Accepted (34347611)
# Tags         : python, convex hull, points orientation, Andrew's monotone chain convex hull algorithm, the Shoelace algorithm, area of a simple polygon
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


def doublePolygonArea(polygon_vertices):
    area = 0
    last_vertex = polygon_vertices[-1]
    for vertex in polygon_vertices:
        area += (last_vertex.x + vertex.x)*(vertex.y - last_vertex.y)
        last_vertex = vertex

    return area


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n = int(stdin.readline())
    A = [int(x) for x in stdin.readline().split()]
    min_y = A[n - 1]
    max_y = A[n - 1]
    trees = []
    for i in range(n - 1, 0, -1):
        a = A[i]
        if a < min_y:
            min_y = a
        elif a > max_y:
            max_y = a
        trees.append(Point(A[i - 1], min_y))
        trees.append(Point(A[i - 1], max_y))
    trees = sorted(trees)
    fence = getConvexHull(trees)
    double_area = doublePolygonArea(fence)
    stdout.write(str(double_area) + '\n')
