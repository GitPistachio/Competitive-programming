# Project name : SPOJ: A very easy problem
# Author       : Wojciech Raszka
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23200675)
# Tags         : R
# Comment      :

library(binaryLogic)

weirdForm <- function(b){
  i <- length(b) - 1
  if (i == 0){
    if (b[1]){
      return ("2(0)")
    } else{
      return ("")
    }
  } else if (i == 1){
    if (b[2]){
      return ("2+2(0)")
    } else {
      return ("2")
    }
  } else {
      l <- paste("2(", weirdForm(as.binary(i)), ")", sep="")
      t <- match(TRUE, tail(b, -1))
      if (!is.na(t)){
        r <- weirdForm(tail(b, -t))
        return (paste(l, "+", r, sep=""))
      } else {
        return (l)
      }


  }
}

N = c(137, 1315, 73, 136, 255, 1384, 16385)

for (n in N){
    write(paste(n, "=", weirdForm(as.binary(n)), sep=""), stdout())
}
