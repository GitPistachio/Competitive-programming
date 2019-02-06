# Project name : SPOJ: Sum of digits
# Author       : Wojciech Raszka
# Date created : 2019-02-03
# Description  :
# Status       : Accepted (???)
# Comment      :

library(gmp, warn.conflicts=FALSE)

factorial <- function(n){
    if (n > 1)
        return (n*factorial(n - 1))
    return (as.bigq(1, 1))
}

f <- file('stdin', open='r')

no_of_test_cases <- as.integer(readLines(f , n=1, warn=FALSE))
numbers <- as.integer(readLines(f , n=no_of_test_cases, warn=FALSE))

for (n in numbers){
  write(as.character(factorial(n)), stdout())
}
