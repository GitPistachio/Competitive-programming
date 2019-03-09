# Project name : SPOJ: Insertion sort
# Author       : Wojciech Raszka
# Date created : 2019-??-??
# Description  :
# Status       : Time limit exceeded
# Comment      : Naive method using insertion sort. Time complexity O(n^2)

T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    A = list(map(int, raw_input().split(' ')))

    no_of_swaps = 0
    for i in xrange(1, N):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            no_of_swaps += 1
            j -= 1

    print(no_of_swaps)
