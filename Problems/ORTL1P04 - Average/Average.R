# Project name : SPOJ: ORTL1P04 - Average
# Author       : Wojciech Raszka
# Date created : 2019-04-02
# Description  :
# Status       : Accepted (23554130)
# Tags         : R
# Comment      : 100 score

f <- file('stdin', open='r')

tokens <- as.integer(unlist(strsplit(readLines(f, n=1), " ")))

m <- mean(tokens)
write(m, stdout())
if (m >= 6){
  write("APROBADO", stdout())
} else {
  write("DESAPROBADO", stdout())
}
