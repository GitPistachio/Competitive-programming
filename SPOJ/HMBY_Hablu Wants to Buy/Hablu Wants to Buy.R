# Project name : SPOJ: HMBY - Hablu Wants to Buy
# Author       : Wojciech Raszka
# Date created : 2019-02-16
# Description  :
# Status       : Accepted (23241231)
# Comment      :

library(gmp, warn.conflicts=FALSE)

f <- file('stdin', open='r')

n <- unlist(strsplit(readLines(f, n=1), ' '))
w = as.bigz(n[6])

sum_of_notes = 2*as.bigz(n[1]) + 4*as.bigz(n[2]) + 8*as.bigz(n[3]) + 16*as.bigz(n[4]) + 32*as.bigz(n[5])

if (w %% 2 == 0 && sum_of_notes >= w){
  write("YES", stdout())
} else{
  write("NO", stdout())
}
