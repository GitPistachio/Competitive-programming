# Project name : SPOJ: SMPSEQ3 - Fun with Sequences
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23291137)
# Comment      :

n = int(input())
S = input().split()
m = int(input())
Q = input().split()

print(' '.join(filter(lambda s: not s in Q, S)))
