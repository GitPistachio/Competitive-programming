# Project name : SPOJ: G11 - Binario
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-02
# Description  :
# Status       : Accepted (23562331)
# Tags         : python, prefix sum, cumulative sum
# Comment      :

n = int(input())

cumulative_sum = 0
def rollingSum(x):
    x = int(x)
    global cumulative_sum

    cumulative_sum += x
    return cumulative_sum

A = [0]
A.extend([rollingSum(x) for x in input().split()])

Q = int(input())

for q in range(Q):
    i, j = map(int, input().split())
    print(A[j + 1] - A[i])
