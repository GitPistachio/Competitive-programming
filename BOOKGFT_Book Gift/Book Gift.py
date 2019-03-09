# Project name : SPOJ: BOOKGFT - Book Gift
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23283389)
# Comment      :

T = int(input())

for t in range(T):
    M, N = map(int, input().split())
    if N % M  == 0:
        print("YES")
    else:
        print("NO")
