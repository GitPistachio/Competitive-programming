# Project name : SPOJ: OVGDEL - Good Elements
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-27
# Description  :
# Status       : Accepted (23692744)
# Tags         : python, binary search
# Comment      :

import sys

def isInArray(a, A, l, r):
    while l <= r:
        m = l + (r - l)//2

        if A[m] == a:
            return True
        elif A[m] > a:
            r = m - 1
        else:
            l = m + 1

    return False

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    n = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split()]
    A.sort()

    max_a = A[-1]

    no_of_good_a = 0
    b = None
    for i in range(n):
        a = A[i]
        if a == b:
            no_of_good_a += 1
        elif a > 1:
            b = a
            while a <= max_a:
                if isInArray(a, A, i + 1, n - 1):
                    no_of_good_a += 1
                    break
                a *= A[i]
        else: # a is equal to 1
            if 1 < n and A[1] == 1: #if in sorted array A is 1 then it must by at index 0 and if there is another 1 then all numbers are good
                no_of_good_a = n
            else:
                no_of_good_a = n - 1
            break

    sys.stdout.write("Case %d: %d\n" % (t, no_of_good_a))
