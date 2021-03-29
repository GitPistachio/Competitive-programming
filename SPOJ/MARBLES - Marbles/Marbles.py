# Project name : SPOJ: MARBLES - Marbles
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-04-18
# Description  :
# Status       : Accepted (23196497)
# Tags         : python, combinations without repetition, math, combinatorics
# Comment      : C(n - 1, k - 1)


def combination(n, k):
    if k > n - k:
        k = n - k

    no_of_possibilities = 1

    for i in range(k):
        no_of_possibilities = no_of_possibilities*(n - i)//(i + 1)

    return no_of_possibilities


T = int(input())

while T > 0:
    n, k = map(int, input().split())

    print(combination(n - 1, k - 1))

    T -= 1
