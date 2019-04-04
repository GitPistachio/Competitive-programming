# Project name : SPOJ: CODEM5 - Problem5
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-03
# Description  :
# Status       : Accepted (23563568)
# Tags         : python, brute force, knapsack problem
# Comment      : python 3.5: 1.56 sec, pypy 2.6: 0.49


def solve(n, k, weights):
    if n == -1:
        if k > 0:
            s =  (0, False)
        else:
            s = (0, True)
    elif weights[n] > k:
        s = solve(n - 1, k, weights)
    elif weights[n] < k:
        a1, b1 = solve(n - 1, k, weights)
        a2, b2 = solve(n - 1, k - weights[n], weights)
        if b1 and b2:
            s = (min(a1, 1 + a2), True)
        elif b1:
            s = (a1, b1)
        elif b2:
            s = (1 + a2, True)
        else:
            s = (0, False)
    else:
        s = (1, True)
    return s

T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    weights = list(map(int, input().split()))
    min_no_of_obj, is_possible = solve(n - 1, k, weights)
    if is_possible:
        print(min_no_of_obj)
    else:
        print("impossible")
