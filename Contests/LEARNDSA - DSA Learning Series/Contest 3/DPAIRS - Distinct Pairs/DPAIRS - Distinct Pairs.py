# Project name : CodeChef: DPAIRS - Distinct Pairs
# Link         : https://www.codechef.com/LRNDSA03/problems/DPAIRS
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (35847768)
# Tags         : python
# Comment      :

from sys import stdin, stdout

def printPairs(X, Y):
    if len(X) > 0:
        output = '\n'.join(map(lambda x, y: str(x) + ' ' + str(y), X, Y))
        stdout.write(output + '\n')


n, m = map(int, stdin.readline().split())
A = [int(x) for x in stdin.readline().split()]
B = [int(x) for x in stdin.readline().split()]

min_a = min(A)
min_a_idx = A.index(min_a)
max_b = max(B)
max_b_idx = B.index(max_b)

printPairs([min_a_idx]*m, range(m))
printPairs(range(min_a_idx), [max_b_idx]*min_a_idx)
printPairs(range(min_a_idx + 1, n), [max_b_idx]*(n - min_a_idx - 1))
