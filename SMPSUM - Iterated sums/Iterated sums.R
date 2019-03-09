# Project name : SPOJ: SMPSUM - Iterated sums
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23290219)
# Comment      :

f <- file('stdin', open='r')

l <- unlist(strsplit(readLines(f, n=1), " "))
a <- as.integer(l[1]) - 1
b <- as.integer(l[2])

is <- (b*(b + 1)*(2*b + 1) - a*(a + 1)*(2*a + 1))/6

write(is, stdout())
