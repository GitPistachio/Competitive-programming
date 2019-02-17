# Project name : SPOJ: Sum of digits
# Author       : Wojciech Raszka
# Date created : 2019-02-03
# Description  :
# Status       : Accepted (???)
# Comment      :

library(gmp, warn.conflicts=FALSE)

f <- file('stdin', open='r')

N = readLines(f, n=-1, warn=FALSE)

for (n in N){
  write(as.character(2*as.bigq(n) - 2), stdout())
}
