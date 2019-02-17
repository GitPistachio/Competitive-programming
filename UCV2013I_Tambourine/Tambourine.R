# Project name : SPOJ: UCV2013I - Tambourine
# Author       : Wojciech Raszka
# Date created : 2019-02-15
# Description  :
# Status       : Accepted (23238155)
# Comment      : R = r*sin(2*pi/(4*N))

options(digits=15)

f <- file('stdin', open='r')

p <- unlist(strsplit(readLines(f, n=1) , ' '))

r = as.numeric(p[1])
N = as.integer(p[2])

pi = 3.141592653589793238
while (r != 0 || N != 0){
  write(format(round(r/sin(pi/(2*N)), 2), nsmall=2), stdout())
  p <- unlist(strsplit(readLines(f, n=1) , ' '))
  r = as.numeric(p[1])
  N = as.integer(p[2])
}
