# Project name : SPOJ: CODEM5 - Problem5
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-04
# Description  :
# Status       : Accepted (23568077)
# Tags         : python, dynamic programming, knapsack problem
# Comment      : python 3.5: 0.04 sec

def solve(n, k, weights, solutions):
    if n == -1:
        if k > 0:
            return (0, False)
        else:
            return (0, True)
    elif solutions[n][k] is None:
        if weights[n] > k:
            s = solve(n - 1, k, weights, solutions)
        elif weights[n] < k:
            a1, b1 = solve(n - 1, k, weights, solutions)
            a2, b2 = solve(n - 1, k - weights[n], weights, solutions)
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
    else:
        return solutions[n][k]

    solutions[n][k] = s
    return s

T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    weights = list(map(int, input().split()))
    solutions = [[None for i in range(k + 1)] for j in range(n)]
    min_no_of_obj, is_possible = solve(n - 1, k, weights, solutions)
    if is_possible:
        print(min_no_of_obj)
    else:
        print("impossible")
