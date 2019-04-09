# Project name : SPOJ: TAP2015H - Hugo s homework
# Author       : Wojciech Raszka
# Date created : 2019-02-20
# Description  :
# Status       : Accepted (23533193)
# Tags         : python, math, right triangle, hypotenuse
# Comment      : P = a*b/2 and a^2 + b^2 = c^2. Solving we have t^2 - t*c^2+4P = 0 where t:= b^2

from math import sqrt

def findLegs(P, c):
    d = c*c*c*c - 16*P*P
    if d < 0:
        return (-1, -1)

    return(sqrt((c*c - sqrt(d))/2), sqrt((c*c + sqrt(d))/2))


T = int(input())

for t in range(T):
    c, P = map(int, input().split())
    a, b = findLegs(P, c)
    if a == -1 or b == -1:
        print(-1)
    else:
        print("{:0.6f} {:0.6f} {:0.6f}".format(a, b, c))
