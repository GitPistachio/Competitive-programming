# Project name : SPOJ: MCOINS - Coins Game
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-27
# Description  :
# Status       : Accepted (23690922)
# Tags         : python, dynamic-programming, game theory
# Comment      :

K, L, m = map(int, raw_input().split())

G = [int(x) for x in raw_input().split()]

N = max(G)
R = [False]*(N + 1)


def setStartingGameResults(R, K, L, N):

    for n in range(1, min(max(K, L), N) + 1):
        if n < 2:
            R[n] = True
        elif n < K:
            R[n] = not R[n - 1]
        elif n < L:
            R[n] = not min(R[n - 1], R[n - K])
        else:
            R[n] = not min(R[n - 1], R[n - K], R[n - L])


def setLateGameResults(R, K, L, N):
    for n in range(max(K, L) + 1, N + 1):
        R[n] = not min(R[n - 1], R[n - K], R[n - L])


setStartingGameResults(R, K, L, N)
setLateGameResults(R, K, L, N)

print ''.join(map(lambda g: 'A' if R[g] else 'B', G))
