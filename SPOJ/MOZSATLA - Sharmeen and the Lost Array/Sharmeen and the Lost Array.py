# Project name : SPOJ: MOZSATLA - Sharmeen and the Lost Array
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-22
# Description  :
# Status       : Accepted (23672782)
# Tags         : python
# Comment      :

T = int(input())

while T > 0:
    n = int(input())
    X = input().split()
    A = [1]*n

    for i in range(n - 2, -1, -1):
        if X[i] == '0':
            A[i] = A[i + 1]
        elif X[i] == '1':
            A[i] = 1
            if A[i + 1] == 1:
                l = i + 1
                A[l] += 1
                while l < n - 1:
                    if X[l] == '0':
                        A[l + 1] += 1
                    elif X[l] == '1' and A[l + 1] <= A[l]:
                        A[l + 1] += 1
                    else:
                        break
                    l += 1
        else:
            A[i] = A[i + 1] + 1

    print(' '.join(map(str, A)))
    T -= 1
