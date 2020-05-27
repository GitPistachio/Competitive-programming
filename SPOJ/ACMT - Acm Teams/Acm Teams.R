# Project name : SPOJ: ACMT - Acm Teams
# Author       : Wojciech Raszka
# Date created : 2019-03-17
# Description  :
# Status       : Accepted (23440149)
# Comment      : O(n) solution. Maximize f(x,y) = 3x + 3y, where x denotes number of each teams respectively

options(digits=20)

f <- file('stdin', open='r')

T = as.integer(readLines(f, n=1))

while (T > 0){
  tokens = as.integer(unlist(strsplit(readLines(f, n=1), ' ', fixed=TRUE)))
  E = tokens[1]
  N = tokens[2]

  max_no_of_teams = 0
  if (2*E <= N){
    max_no_of_teams = E
  } else if (E >= 2*N) {
    max_no_of_teams = N
  } else {
    max_no_of_teams = max(E %/% 2, N %/% 2, (N + E) %/% 3)
  }

  write(format(max_no_of_teams, scientific=FALSE), stdout())
  T = T - 1
}
