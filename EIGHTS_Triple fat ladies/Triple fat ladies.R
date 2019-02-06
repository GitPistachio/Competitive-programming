# Project name : SPOJ: Triple fat ladies
# Author       : Wojciech Raszka
# Date created : 2019-02-06
# Description  :
# Status       : Accepted (23186394)
# Comment      : 1 -> 192; 2 -> 422 = 192 + (2 - 1) * 250; 3 -> 692 = 192 + (3 - 1) * 250; 4 -> 942 = 192 + (4 - 1) * 250  etc

library(gmp, warn.conflicts=FALSE)

f <- file('stdin', open='r')

t <- as.integer(readLines(f, n=1))

for (i in 1:t){
  k <- as.bigq(readLines(f, n=1))

  eee <- 192 + (k - 1)*250
  write(as.character(eee), stdout())
}
