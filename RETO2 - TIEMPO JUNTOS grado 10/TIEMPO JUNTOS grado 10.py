# Project name : SPOJ: RETO2 - TIEMPO JUNTOS grado 10
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-26
# Description  :
# Status       : Accepted (23688932)
# Tags         : python
# Comment      :

L1, R1, L2, R2, k = map(int, input().split())

if R1 < L2:
    print(0)
elif L1 > R2:
    print(0)
else:
    L = max(L1, L2)
    R = min(R1, R2)

    if L <= k <= R:
        print(R - L)
    else:
        print(R - L + 1)
