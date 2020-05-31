# Project name : CodeChef: WWALK - Weird Walk
# Link         : https://www.codechef.com/LTIME84B/problems/LOSTWKND
# Try it on    : https://ideone.com/09W6Zg
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-05-30
# Description  :
# Status       : Accepted(33460569)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout


def weirdDistance(n, A, B):
    """Calculate weird distance."""
    werid_dist = 0
    walk_dist_by_a = 0
    walk_dist_by_b = 0

    for i in range(n):
        if walk_dist_by_a == walk_dist_by_b and A[i] == B[i]:
            werid_dist += A[i]

        walk_dist_by_a += A[i]
        walk_dist_by_b += B[i]

    return werid_dist


no_of_test_cases = int(stdin.readline())


for _ in range(no_of_test_cases):
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    weird_distance = weirdDistance(n, A, B)
    stdout.write("{}\n".format(weird_distance))
