# Project name : SPOJ: Insertion sort
# Author       : Wojciech Raszka
# Date created : 2019-??-??
# Description  :
# Status       : Time limit exceeded
# Comment      : Naive method using insertion sort. Time complexity O(n^2)

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split(' ')))

    no_of_swaps = 0
    for i in range(1, N):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            no_of_swaps += 1
            j -= 1

    print(no_of_swaps)
