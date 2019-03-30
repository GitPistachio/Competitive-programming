# Project name : SPOJ: SBANK - Sorting Bank Accounts
# Author       : Wojciech Raszka
# Date created : 2019-03-15
# Description  :
# Status       : Accepted (23420647)
# Comment      :

library(plyr)
f <- file('stdin', open='r')

T <- as.integer(readLines(f, n=1))

for (t in 1:T){
  n <- as.integer(readLines(f, n=1))
  bank_accounts <- readLines(f, n=n)
  dt <- count(bank_accounts)
  write.table(dt, file=stdout(), quote=FALSE, row.names=FALSE, col.names=FALSE, sep="")

  if (t < T){
	write("", stdout())
    readLines(f, n=1)
  }
}
