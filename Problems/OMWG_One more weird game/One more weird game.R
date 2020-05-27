# Project name : SPOJ: OMWG - One more weird game
# Author       : Wojciech Raszka
# Date created : 2019-02-17
# Description  :
# Status       : Accepted (23250636)
# Comment      : You can see on the grid as a grid graph where squares are vertices and neighboring squeres are edges. As it known the nxm grid graph has 2nm - n - m edges.

f <- file('stdin', open='r')

T = as.integer(readLines(f, n=1))

for (t in 1:T){
  nm = unlist(strsplit(readLines(f, n=1), " "))

  n = as.integer(nm[1])
  m = as.integer(nm[2])

  write(2*n*m - n - m, stdout())
}
