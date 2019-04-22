# Project name : SPOJ: MOZGEOL - Jenny the GeoLover
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-21
# Description  :
# Status       : Accepted (23669744)
# Tags         : python, math, geometry, right-angle trinalge
# Comment      :

from math import sin, radians

T = int(input())

for t in range(1, T + 1):
    b, angle = map(float, input().split())

    h = b/sin(radians(angle))
    print("Case ", t,  ": ", '{:6f}'.format(h), sep="")
