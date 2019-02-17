# Project name : SPOJ: Easy calculation
# Author       : Wojciech Raszka
# Date created : 2019-02-08
# Description  :
# Status       : Accepted (23196497)
# Comment      : I used Newton methos for finding root of f(x) = Ax+Bsin(x) - C for x_0 = C/A due to Ax - B - C <= f(x) <= Ax + B - C => (C-B)/A <= x_0 <= (C+B)/A

from math import sin, cos

def f(x, A, B, C):
    return A*x + B*sin(x) - C

def df(x, A, B, C):
    return A + B*cos(x)

def rootOfFunction(f, m, x, *args):

    e = abs(f(x, *args)/m)
    while e > 0.0000001:
        x = x - f(x, *args)/df(x, *args)
        e = abs(f(x, *args)/m)
    return round(x, 6)


T = int(input())

for t in range(T):
    A, B, C = list(map(int, input().split(' ')))
    m = A + B
    x = C/A
    print(rootOfFunction(f, m, x, A, B, C))
