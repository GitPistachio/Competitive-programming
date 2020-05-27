# Project name : SPOJ: CODECODE - Coder Or NonCoder
# Author       : Wojciech Raszka
# Date created : 2019-03-23
# Description  :
# Status       : Accepted (23477201)
# Tags         : R, math, probability theory
# Comment      : O(1)

f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

while (T > 0){
  tokens <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))
  x <- tokens[1]/100.
  y <- tokens[2]/100.

  res <- (1 - x)*(1 - y) + x*y
  write(paste(format(res*100, nsmall=2), "%", sep=""), stdout())
  T = T - 1
}
