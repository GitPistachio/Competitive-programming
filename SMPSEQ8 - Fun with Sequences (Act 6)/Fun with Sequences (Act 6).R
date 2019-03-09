# Project name : SPOJ: SMPSEQ8 - Fun with Sequences (Act 6)
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23291876)
# Comment      :

f <- file('stdin', open='r')

n <- as.integer(readLines(f, n=1))
S <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))

m <- as.integer(readLines(f, n=1))
Q <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))

if (sum(S) > sum(Q)){
  cat(S, file=stdout(), fill=TRUE, sep=" ")
} else {
  cat(Q, file=stdout(), fill=TRUE, sep=" ")
}
