# Project name : SPOJ: ENPRIME - Prime Number
# Author       : Wojciech Raszka
# Date created : 2019-03-25
# Description  :
# Status       : Accepted (23483831)
# Tags         : python, factorial
# Comment      :

from functools import reduce

N = int(input())
if N <= 1:
    print(1)
else:
    print(reduce(lambda x, y: x*y, range(1, N + 1)))
