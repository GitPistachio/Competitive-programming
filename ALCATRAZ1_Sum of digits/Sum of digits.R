# Project name : SPOJ: Sum of digits
# Author       : Wojciech Raszka
# Date created : 2019-02-06
# Description  :
# Status       : Time limit exceeded
# Comment      : I think it is imposible to do in R. Reading input takes more time than it is given.

f <- file('stdin', open='r')

T = readLines(f, n=1)

for (t in 1:T){
  n <- readLines(f, n=1)

  write(sum(as.integer(unlist(strsplit(n, split='')))), stdout())
}
