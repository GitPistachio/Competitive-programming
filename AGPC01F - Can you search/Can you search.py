# Project name : SPOJ: AGPC01F - Can you search?
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-16
# Description  :
# Status       : Accepted (23644182)
# Tags         : python, sliding window
# Comment      :

def min_(x):
    global min_val

    x = int(x)
    if x < min_val:
        min_val = x

    return min_val

T = int(raw_input())

while T > 0:
    tokens = raw_input().split()
    if len(tokens) < 2:
        continue
    n, q = map(int, tokens)

    min_val = 10**5 + 1
    A = [min_(x) for x in raw_input().split()]
    print '\n'.join(map(lambda x: str(A[int(x) - 1]) , raw_input().split()))

    T -= 1
