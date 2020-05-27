# Project name : SPOJ: SMPSEQ4 - Fun with Sequences (Act 2)
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23291152)
# Comment      :

n = int(input())
S = input().split()
m = int(input())
Q = input().split()

print(' '.join(filter(lambda s: s in Q, S)))
