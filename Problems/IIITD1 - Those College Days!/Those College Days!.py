# Project name : SPOJ: INTEST - Enormous Input Test
# Author       : Wojciech Raszka
# Date created : 2019-03-22
# Description  :
# Status       : Accepted (23470705)
# Tags         : python, fast I/O, math, most significant digit, MSD, binary search
# Comment      :


from sys import stdin, stdout

def MSD(n):
    if n < 0:
        n = -n

    m = n
    while (m > 10):
        m = n // 10

    return m

def MSDF(n):
    if n < 0:
        n = -n

    msd = n
    factor = 1
    while (msd >= 10):
        msd = msd // 10
        factor *= 10

    return factor

def solve(n):
    factor = MSDF(n)
    if n < 0:
        x = -2*n
    else:
        x = 0

    return x + factor

T = int(input())

stdout.write('\n'.join(map(lambda x: str(solve(int(x))), stdin)))
