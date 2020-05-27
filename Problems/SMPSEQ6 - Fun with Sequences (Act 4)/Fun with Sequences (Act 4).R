# Project name : SPOJ: SMPSEQ6 - Fun with Sequences (Act 4)
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23291518)
# Comment      :

f <- file('stdin', open='r')

nx <- unlist(strsplit(readLines(f, n=1), ' '))
n = as.integer(nx[1])
x = as.integer(nx[2])

S <- unlist(strsplit(readLines(f, n=1), ' '))
Q <- unlist(strsplit(readLines(f, n=1), ' '))

SQ = c()
for (i in 1:n){
  for (j in max(1, i - x):min(n, i + x)){
      if (S[i] == Q[j]){
          SQ = c(SQ, i)
          break
      }
  }
}

cat(SQ, file=stdout(), fill=TRUE, sep=" ")
