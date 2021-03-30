# Project name : SPOJ: MMAXPER - Rectangles Perimeter
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-05-16
# Description  :
# Status       : Accepted (25987978)
# Tags         : python, dynamic programming, rectangle
# Comment      : You take advantage that order of rectangle cannot be changed 

from sys import stdin, stdout


if __name__ == '__main__':
    n = int(stdin.readline())
    x, y = stdin.readline().split()
    last_width = int(x)
    last_height = int(y)
    last_by_width = last_width
    last_by_height = last_height
    for _ in range(n - 1):
        x, y = stdin.readline().split()
        width, height = int(x), int(y)
        a = last_by_width + abs(height - last_height) + width
        b = last_by_height + abs(height - last_width) + width
        c = last_by_width + abs(width - last_height) + height
        d = last_by_height + abs(width - last_width) + height
        last_width = width
        last_height = height
        last_by_width = max(a, b)
        last_by_height = max(c, d)
    
    if last_width >= last_height:
        stdout.write('%d\n' % last_by_width)
    else:
        stdout.write('%d\n' % last_by_height)