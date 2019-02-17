# Project name : SPOJ: Penney game
# Author       : Wojciech Raszka
# Date created : 2019-02-12
# Description  :
# Status       : Accepted (23218953)
# Comment      : 


P = int(input())

for p in range(P):
    a = 0
    b = 0
    c = 0
    N = int(input())
    i = 1
    C = [0]*8
    for l in input():
        a = b
        b = c
        c = 1 if l == 'H' else 0
        if i >= 3:
            C[(a << 2) + (b << 1) + c] += 1

        i += 1
    print(N, ' '.join(map(str, C)), '', sep=' ')
