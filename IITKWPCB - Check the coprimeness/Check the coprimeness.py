# Project name : SPOJ: IITKWPCB - Check the coprimeness
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-16
# Description  :
# Status       : Accepted (23927989)
# Tags         : python, math, coprime
# Comment      :

from sys import stdin, stdout

T = int(stdin.readline())

while T > 0:
    x = int(stdin.readline())
    y = (x + 1)//4

    if x > 2:
        res = 1 + (y - 1)*2
        r = (x + 1) % 4
        if r == 2:
            res += 1
    else:
        res = 1

    stdout.write('%d\n' % res)

    T -= 1
