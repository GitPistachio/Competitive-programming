# Project name : SPOJ: ENIGMATH - PLAY WITH MATH
# Author       : Wojciech Raszka
# Date created :
# Description  :
# Status       : Accepted (23536766)
# Tags         : R, gcd, greatest common divisior, linear Diophantine equation
# Comment      :

options(scipen=999)

gcd <- function(x){
	while (x[2] != 0){
		t = x[2]
		x[2] = x[1] %% x[2]
		x[1] = t
	}
	return (x[1])
}

f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

A <- read.table(f)

d <- apply(A, 1, gcd)

write.table((A/d)[,2:1], file=stdout(), quote=FALSE, row.names=FALSE, col.names=FALSE, sep=' ')
