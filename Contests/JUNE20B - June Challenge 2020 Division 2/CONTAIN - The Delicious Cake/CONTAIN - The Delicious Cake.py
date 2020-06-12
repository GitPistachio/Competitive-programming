# Project name : CodeChef: CONTAIN - The Delicious Cake
# Link         : https://www.codechef.com/JUNE20B/problems/CONTAIN
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-08
# Description  :
# Status       : Unaccepted (???)
# Tags         : python, convex hull, point in convex polygon
# Score        : 0
# Comment      :

from sys import exit, stdin, stdout


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def getConvexHull(points):
    if len(points) <= 1:
        return []

    remaining_points = []
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            if cross(lower[-2], lower[-1], p) != 0:
                remaining_points.append(lower.pop())
            else:
                lower.pop()
        lower.append(p)

    rest = []
    upper = []
    for p in reversed(remaining_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            if cross(upper[-2], upper[-1], p) != 0:
                rest.append(upper.pop())
            else:
                upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def isInsideConvexHull(x, y, points):
    side = None
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        xj, yj = points[(i + 1) % n]

        d = (x - xi)*(yj - yi) - (y - yi)*(xj - xi)
        if d == 0:
            return False

        if side is None:
            side = d > 0
        elif (d > 0) != side:
            return False

    return True


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n, q = map(int, stdin.readline().split())
    points = sorted(set(tuple(map(int, stdin.readline().split())) for _ in range(n)))
    for _ in range(q):
        x, y = map(int, stdin.readline().split())

        remaining_points = points.copy()
        try:
            remaining_points.remove((x, y))
        except Exception:
            pass

        cnt = 0
        while True:
            convex_hull = getConvexHull(remaining_points)

            if len(convex_hull) < 3:
                break

            if not isInsideConvexHull(x, y, convex_hull):
                break

            print(convex_hull)
            cnt += 1

        stdout.write(str(cnt) + '\n')
