# Project name : SPOJ: MUL - Fast Multiplication
# Author       : Wojciech Raszka
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23373544)
# Comment      :

T = int(input())

for t in range(T):
    l1, l2 = map(int, input().split())
    print(l1*l2)
