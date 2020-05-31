# Project name : SPOJ: BISHOPS - Bishops
# Author       : Wojciech Raszka
# Date created : 2019-02-08
# Description  :
# Status       : Accepted (23195535)
# Comment      :

library(gmp, warn.conflicts=FALSE)

f <- file('stdin', open='r')

N = readLines(f, n=-1, warn=FALSE)

for (n in N){
  if (n == 1)
    write(1, stdout())
  else
    write(as.character(2*as.bigq(n) - 2), stdout())
}
