# Project name : SPOJ: PGR01 - Progressions
# Author       : Wojciech Raszka
# Date created : 2019-03-31
# Description  :
# Status       : Accepted (23537738)
# Tags         : python, integer sequence A124647 (OEIS)
# Comment      : a(n) = (2n + 1)*3^n

T = int(input())

for t in range(T):
    n = int(input()) - 1
    print((2*n + 1)*3**n)
