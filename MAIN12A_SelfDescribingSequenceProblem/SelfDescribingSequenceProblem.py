# Project name : SPOJ: MAIN12A - SelfDescribingSequenceProblem
# Author       : Wojciech Raszka
# Date created : 2019-02-15
# Description  :
# Status       : Accepted (23238763)
# Comment      :


sq = [1]

last = 2
for i in range(6136):
    sq += [last]*sq[i]
    last += 1

T = int(input())

for t in range(T):
    print("Case #", t + 1, ": ", sq[int(input()) - 1], sep="")
