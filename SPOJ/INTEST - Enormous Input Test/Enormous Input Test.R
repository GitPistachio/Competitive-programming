# Project name : SPOJ: INTEST - Enormous Input Test
# Author       : Wojciech Raszka
# Date created : 2019-03-15
# Description  :
# Status       : Accepted (23420587)
# Comment      :

f <- file('stdin', open='r')

p <- unlist(strsplit(readLines(f, n=1) , ' '))

n <- as.integer(p[1])
k <- as.integer(p[2])

write(sum(as.integer(readLines(f, n=n)) %% k == 0), stdout())
