# Project name : SPOJ: Fun with Sequences (Act 3)
# Author       : Wojciech Raszka
# Date created : 2019-02-11
# Description  :
# Status       : Accepted (23212628)
# Comment      :

f <- file('stdin', open='r')

n = as.integer(readLines(f, n=1))

S = unlist(strsplit(readLines(f, n=1), ' '))

m = as.integer(readLines(f, n=1))

Q = unlist(strsplit(readLines(f, n=1), ' '))

k = min(n, m)

write(which(S[1:k] == Q[1:k]), stdout())
