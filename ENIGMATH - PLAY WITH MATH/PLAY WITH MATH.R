# Project name : SPOJ: ENIGMATH - PLAY WITH MATH
# Author       : Wojciech Raszka
# Date created :
# Description  :
# Status       : Accepted (23536665)
# Tags         : R, gcd, greatest common divisior, linear Diophantine equation
# Comment      :

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


X <- matrix(0, T, 2)
A <- read.table(f)

d <- apply(A, 1, gcd)
X[, 1] <- A[, 2]/d
X[, 2] <- A[, 1]/d


write.table(trimws(format(X, scientific=FALSE)), file=stdout(), quote=FALSE, row.names=FALSE, col.names=FALSE, sep=' ')
