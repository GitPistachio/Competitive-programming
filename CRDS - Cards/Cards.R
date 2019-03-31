# Project name : SPOJ: CRDS - Cards
# Author       : Wojciech Raszka
# Date created :
# Description  :
# Status       : Accepted (23536964)
# Tags         : R, integer sequence A005449 (OEIS)
# Comment      : a(n) = n*(3*n + 1)/2

options(scipen=999)

f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

#N <- as.integer(readLines(f, n=T))
N <- read.table(f) #faster

An <- N*(3*N + 1)/2

write.table(An %% 1000007, file=stdout(), quote=FALSE, row.names=FALSE, col.names=FALSE, sep=' ')
