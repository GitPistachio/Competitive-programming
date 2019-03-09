# Project name : SPOJ: FRNDZND - Friend Zoned
# Author       : Wojciech Raszka
# Date created : 2019-02-20
# Description  :
# Status       :
# Comment      :

f <- file('stdin', open='r')

NQ <- unlist(strsplit(readLines(f, n=1), ' '))
Q <- as.integer(NQ[2])

A <- unlist(strsplit(readLines(f, n=1), ' '))

for(t in 1:Q){
  LR <- unlist(strsplit(readLines(f, n=1), ' '))

  if (LR[1] == LR[2]){
    write(A[as.integer(LR[1])], stdout())
  } else {
    write(0, stdout())
  }
}
