# Project name : SPOJ: Simple Arithmetics II
# Author       : Wojciech Raszka
# Date created : 2019-02-07
# Description  :
# Status       : Wrong Answer
# Comment      : It is write just for fun. It's only for small numbers and respect order of operations.

f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

for (t in 1:T){
  readLines(f, n=1)
  eq <- readLines(f, n=1)
  eq <- sub('=', '', eq)
  eq <- sub('/', '%/%', eq)
  write(eval(parse(text=eq)), stdout())
}
