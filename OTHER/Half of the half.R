# Project name : SPOJ: STRHH - Half of the half
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       :
# Comment      :

f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

for (t in 1:T){
  line <- readLines(f, n=1)
  n <- nchar(line)/2
  sq <- unlist(strsplit(substr(line, 1, n), ""))
  cat(sq[seq.int(1, n, 2)], file=stdout(), fill=TRUE, sep='')
}
