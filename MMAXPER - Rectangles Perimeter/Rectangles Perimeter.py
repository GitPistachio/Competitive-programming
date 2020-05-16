# Project name : SPOJ: MMAXPER - Rectangles Perimeter
# Author       : Wojciech Raszka
# E-mail       : spoj@gitpistachio.site
# Date created : 2020-05-16
# Description  :
# Status       : Accepted (25987878)
# Tags         : python, dynamic programming, rectangle
# Comment      : Only PyPy

from sys import stdin, stdout


class Rect():
    def __init__(self, width, height):
        self.width = width
        self.height = height


def getDim(x):
    w, h = x.split()
    return (int(w), int(h))


def solve(i, side):
    if res[i][side] is None:
        if i > 0:
            if side == 0:
                a = solve(i - 1, 0) + abs(rects[i].height - rects[i - 1].height) + rects[i].width
                b = solve(i - 1, 1) + abs(rects[i].height - rects[i - 1].width) + rects[i].width
                res[i][0] = max(a, b)
            else:
                a = solve(i - 1, 0) + abs(rects[i].width - rects[i - 1].height) + rects[i].height
                b = solve(i - 1, 1) + abs(rects[i].width - rects[i - 1].width) + rects[i].height
                res[i][1] = max(a, b)
        else:
            if side == 0:
                res[0][0] = rects[0].width
            else:
                res[0][1] = rects[0].height
            
        return res[i][side]
    else:
        return res[i][side]
    

if __name__ == '__main__':
    n = int(stdin.readline())
    rects = [Rect(*getDim(x)) for x in stdin]
    res = [[None, None] for _ in range(n)]
    if rects[n -1].width > rects[n -1].height:
        solution = solve(n - 1, 0)
    else:
        solution = solve(n - 1, 1)
    
    stdout.write('%d\n' % solution)