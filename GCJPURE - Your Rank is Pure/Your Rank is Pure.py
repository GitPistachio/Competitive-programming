# Project name : SPOJ: GCJPURE - Your Rank is Pure
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-06
# Description  :
# Status       : Accepted (23889417)
# Tags         : python, n-Fibonacci sequence, integer sequence A079500 (OEIS)
# Comment      : Google Code Jam Round 1B 2010, Problem C. Your Rank is Pure

from sys import stdin, stdout

p = 100003
MAX_N = 500
H_MAX_N = MAX_N//2

F = [[1]*(min(MAX_N - i, H_MAX_N) + 1) for i in range(MAX_N + 1)]
L = [1]*(MAX_N + 1)
last_relevant_val = 0
RANK = [3]*(MAX_N + 1)
RANK[2] = 2
RANK[1] = 1
RANK[0] = 0
for i in range(2, MAX_N + 1):
    start = max(2, i - H_MAX_N)
    for n in range(start, i - 1):
        m = i - n
        L[m] += F[n - 1][m]
        if n - m > 0:
        	L[m] -= F[n - m - 1][m]

        L[m] = L[m] % p
        RANK[i] += L[m]
        F[n][m] = L[m]

    RANK[i] += last_relevant_val
    if i - start == H_MAX_N:
        last_relevant_val = (last_relevant_val + L[i - start]) % p

T = int(stdin.readline())

for t in range(1, T + 1):
    n = int(stdin.readline())
    stdout.write("Case #%d: %d\n" % (t, RANK[n - 1] % p))
