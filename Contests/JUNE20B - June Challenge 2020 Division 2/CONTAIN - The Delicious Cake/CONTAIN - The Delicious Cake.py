# Project name : CodeChef: CONTAIN - The Delicious Cake
# Link         : https://www.codechef.com/JUNE20B/problems/CONTAIN
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-08
# Description  :
# Status       : Accepted (34442926)
# Tags         : python, convex hull, point in a convex polygon, Andrew's monotone chain algotithm, geometric computation
# Score        : 100
# Comment      :

from sys import exit, stdin, stdout


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

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


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


def isPointStrictlyInsideConvexPolygon(p, points):
    side = None
    p1 = points[-1]
    for p2 in points:
        so = sign(orient(p1, p2, p))
        if so != 0:
            if side is None:
                side = so
            elif side != so:
                return False
        else:
            return False
        p1 = p2

    return True


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n, q = map(int, stdin.readline().split())
    chiefs_points = sorted([Point(*map(int, stdin.readline().split())) for _ in range(n)])
    layers = []
    while True:
        convex_hull = getConvexHull(chiefs_points)
        if len(convex_hull) < 3:
            break
        layers.append(convex_hull)
        for p in convex_hull:
            chiefs_points.remove(p)
        for p in chiefs_points.copy():
            if not isPointStrictlyInsideConvexPolygon(p, convex_hull):
                chiefs_points.remove(p)
    for _ in range(q):
        candle_point = Point(*map(int, stdin.readline().split()))

        cnt = 0
        for layer in layers:
            if isPointStrictlyInsideConvexPolygon(candle_point, layer):
                cnt += 1
            else:
                break

        stdout.write(str(cnt) + '\n')
