# Project name : SPOJ: Game store
# Author       : Wojciech Raszka
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23201761)
# Comment      :

N = int(input())

lvl = []

for n in range(N):
    H, E, A = input().split()
    lvl.append((-int(H), int(E), -int(A), n + 1))

lvl.sort()

if N == 1:
    print("Easiest and Hardest is level", 1)
else:
    print("Easiest is level", lvl[0][3])
    print("Hardest is level", lvl[N - 1][3])
