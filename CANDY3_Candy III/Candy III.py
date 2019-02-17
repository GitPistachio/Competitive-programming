# Project name : SPOJ: Candy III
# Author       : Wojciech Raszka
# Date created : 2019-02-07
# Description  :
# Status       : Accepted (23191601)
# Comment      :


T = int(input())

for t in range(T):
    input()
    N = int(input())
    sum_of_candy = sum([int(input()) for i in range(N)])
    if sum_of_candy % N == 0:
        print('YES')
    else:
        print('NO')
