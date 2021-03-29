# Project name : SPOJ: EASYMRKS - Easy Marks
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 
# Description  :
# Status       : 
# Tags         : python
# Comment      :

import math

T = int(input())

for i in range(1, T + 1):
    N, K = list(map(int, input().split(' ')))
    sum_of_n = sum(map(int, input().split(' ')))
    print('Case ', i,  ': ', math.floor(K*(N + 1) - sum_of_n), sep='')
    T -= 1
