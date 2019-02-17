# Project name : SPOJ: The ball game
# Author       : Wojciech Raszka
# Date created : 2019-02-12
# Description  :
# Status       : Time Limit exceeded
# Comment      : The max probability is when N-1 boxes have exacly one white ball and non black balls. The rest of balls is in the last box.


f = file('stdin', open='r')

T = as.integer(readLines(f, n=1))

for (t in 1:T){
  N = as.integer(readLines(f, n=1))
  p = ((N - 1) + 1/(N + 1))/N
  write(format(round(p, 8), nsmall=8), stdout())
}
