# Project name : SPOJ: FLOG - Find Log
# Author       : Wojciech Raszka
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23373761)
# Comment      :

from math import log

T = int(input())

for t in range(T):
    b, n = map(int, input().split())

    if n <= 1 or b <= 1:
        print('Case ', t + 1, ': Math Error!', sep='')
    else:
        x = log(n, b)
        print('Case ', t + 1, ': %.5f' % x, sep='')
